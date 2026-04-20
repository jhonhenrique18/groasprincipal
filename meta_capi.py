"""Meta Conversions API (CAPI) helper.

Sends events to Meta's server-side endpoint with SHA-256 hashing of PII.
Designed as a companion to the Meta Pixel (client-side) for event
deduplication — the same event_id must be used on both sides within a
48h window for Meta to count the event once.

Silent no-op when META_PIXEL_ID or META_CAPI_ACCESS_TOKEN are not set,
so dev environments don't need credentials.
"""
import hashlib
import time

import requests
from flask import current_app


GRAPH_API_VERSION = 'v20.0'
GRAPH_TIMEOUT_SECONDS = 3

HASHABLE_FIELDS = ('em', 'ph', 'fn', 'ln', 'external_id')
PASSTHROUGH_FIELDS = ('client_ip_address', 'client_user_agent', 'fbp', 'fbc')


def sha256_hash(value):
    """Lowercase, strip, SHA-256 hex. Returns None for empty input."""
    if not value:
        return None
    normalized = str(value).strip().lower()
    if not normalized:
        return None
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()


def normalize_phone(phone):
    """Keep only digits for hashing per Meta spec."""
    if not phone:
        return None
    digits = ''.join(c for c in str(phone) if c.isdigit())
    return digits or None


def _build_user_data(user_data):
    out = {}
    for key in HASHABLE_FIELDS:
        raw = user_data.get(key)
        if key == 'ph':
            raw = normalize_phone(raw)
        h = sha256_hash(raw)
        if h:
            out[key] = h
    for key in PASSTHROUGH_FIELDS:
        v = user_data.get(key)
        if v:
            out[key] = v
    return out


def send_capi_event(event_name, event_id, event_source_url, user_data=None, custom_data=None):
    """Fire-and-forget-ish CAPI event. Returns response dict or None.

    Never raises — CAPI failures must not break user-facing flows.
    """
    pixel_id = current_app.config.get('META_PIXEL_ID')
    access_token = current_app.config.get('META_CAPI_ACCESS_TOKEN')
    if not pixel_id or not access_token:
        return None

    event = {
        'event_name': event_name,
        'event_time': int(time.time()),
        'event_id': event_id,
        'event_source_url': event_source_url,
        'action_source': 'website',
        'user_data': _build_user_data(user_data or {}),
    }
    if custom_data:
        event['custom_data'] = custom_data

    payload = {'data': [event]}
    test_code = current_app.config.get('META_TEST_EVENT_CODE')
    if test_code:
        payload['test_event_code'] = test_code

    url = f'https://graph.facebook.com/{GRAPH_API_VERSION}/{pixel_id}/events'
    try:
        resp = requests.post(
            url,
            params={'access_token': access_token},
            json=payload,
            timeout=GRAPH_TIMEOUT_SECONDS,
        )
        return resp.json()
    except Exception as exc:
        current_app.logger.warning('CAPI send failed for %s: %s', event_name, exc)
        return None


def user_data_from_request(req, form=None):
    """Build user_data dict from Flask request + optional form payload."""
    forwarded = req.headers.get('X-Forwarded-For', '')
    client_ip = forwarded.split(',')[0].strip() if forwarded else req.remote_addr
    data = {
        'client_ip_address': client_ip,
        'client_user_agent': req.headers.get('User-Agent'),
        'fbp': req.cookies.get('_fbp'),
        'fbc': req.cookies.get('_fbc'),
        'external_id': req.cookies.get('_ep_eid'),
    }
    if form:
        data['em'] = form.get('email')
        data['ph'] = form.get('phone')
        data['fn'] = form.get('name')
    return data
