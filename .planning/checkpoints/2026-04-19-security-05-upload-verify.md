# Checkpoint - Security 05: Upload verify image

Date: 2026-04-19
Owner: Claude (Opus 4.7)
Phase: Security basics (item 5 de 7)

## Why this exists

Vuln V5: `save_image()` validava so a extensao do arquivo e tinha um
`except` que, se Pillow falhasse, salvava o arquivo original como-is
na pasta de uploads. Atacante com admin podia renomear qualquer binario
para `.jpg` e o fallback salvava como-is.

## What was done

### `app.py::save_image`

Antes:
```python
try:
    img = PILImage.open(file)
    # ... process
except Exception:
    # Fallback: save original file as-is if Pillow fails  ← INSECURE
    file.save(filepath)
```

Depois:
```python
try:
    img = PILImage.open(file)
    img.load()  # forca decode, falha em fake/corrupt
    # ... process
except Exception:
    app.logger.warning('save_image: rejected upload %r', file.filename)
    return ''
```

Diferencas:
- `img.load()` forca o decode (vs `open()` que e lazy). Falha em
  pseudo-imagens (arquivos com extensao de imagem mas conteudo invalido).
- No falha, funcao retorna `''` sem escrever nada. Nao ha mais fallback
  de "salva o arquivo original".
- Log de warning com o filename que foi rejeitado para auditoria.

Decisao: usei `img.load()` em vez de `Image.verify()` porque verify tem
semantica estranha com file handles (fecha o fp, requer reopen). load()
e mais simples e mais seguro.

## Testing

4 cenarios smoke-testados com Pillow real instalado:

1. ELF binary renomeado pra `.jpg` → rejeitado, nada escrito no disco
2. PNG real 200x200 → processado pra WebP (main + -sm thumbnail)
3. `.exe` → rejeitado pelo whitelist de extensoes
4. PNG com header invalido / bytes truncados → rejeitado

## Trade-offs

- Imagens corrompidas mas parcialmente validas (ex: EXIF quebrado,
  metadata corrompida mas pixels OK) podem ser aceitas. Aceitavel —
  o navegador lida ou descarta, sem risco de exec.
- Payload malicioso embutido em EXIF de imagem real (ex: polyglot PNG+ZIP):
  Pillow re-encoda para WebP, o que descarta EXIF e o payload sobrevive
  somente dentro dos pixels visiveis (impossivel de executar no browser).

## Next step

Avanca pro item 6 (XSS fix no modal de produto).
