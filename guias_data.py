"""Editorial guides — long-form content for SEO domination in Paraguay.

Compatibility note: uses `from __future__ import annotations` so the
modern type-hint syntax (`dict | None`) works on Python 3.9 (local dev)
and 3.12 (Railway prod) without changes.

Each entry maps `guide_slug` -> structured content used by templates/guias/*
to render a magazine-style article. The slug intentionally mirrors the
product slug so internal linking is trivial: `/guias/manzanilla-flor` ->
`/producto/manzanilla-flor`.

Why a Python dict and not a CMS / database table:
- Versioned in git, reviewable in PR (every word change has a diff).
- Editor-friendly: copy edits become commits with attribution.
- No moving parts: a fresh deploy comes up with the latest content
  without a separate seed step.
- Trivially extensible: add a new entry, restart, the route serves it.

Content strategy:
- Each guide targets BOTH consumer queries ("para qué sirve la X",
  "cómo preparar X") AND B2B queries ("X al por mayor", "comprar X
  en Paraguay", "proveedor de X"), so the same URL captures both
  intents and funnels everyone to a WhatsApp lead.
- Word count target: 1100-1500 per guide (Google's content-depth
  signal for competitive Spanish queries in 2026).
- Schema stack: Article + FAQPage + HowTo + BreadcrumbList per page.
- Every guide ends with a B2B CTA — that's the conversion point.

When adding a new guide:
1. The `product_slug` MUST exist in seo_aliases.PRODUCT_ALIASES.
2. Sections accept HTML strings (rendered with |safe in Jinja).
3. FAQ questions become FAQPage schema entries automatically.
4. HowTo is optional; when present, becomes HowTo schema.
5. Related guide slugs become internal links + topic cluster signal.
"""

from __future__ import annotations

GUIDES: dict[str, dict] = {
    # ═════════════════════════════════════════════════════════════════
    # 1. MANZANILLA FLOR
    # ═════════════════════════════════════════════════════════════════
    "manzanilla-flor": {
        "product_slug": "manzanilla-flor",
        "title": "Manzanilla en Flor: la guía completa para industria, gastronomía y consumo familiar en Paraguay",
        "dek": "Una flor pequeña que mueve millones de tazas por año. Cómo elegirla, qué la hace especial y por qué la manzanilla a granel es el insumo que su negocio necesita.",
        "meta_title": "Manzanilla en Flor — Guía Completa | Grãos S.A.",
        "meta_description": "Todo sobre la manzanilla en flor: beneficios, usos, cómo preparar el té perfecto y dónde comprar manzanilla al por mayor en Paraguay con importación directa.",
        "category": "Hierbas y Tés",
        "reading_time": 8,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",  # CSS theme variant
        "intro": """
            <p class="lead">La <strong>manzanilla</strong> es probablemente la hierba más buscada del Paraguay. Aparece en la cocina de la abuela, en la farmacia, en la barra del bar antes de un cocido digestivo y en la línea de producción de bebidas, cosméticos y suplementos. Pero no toda manzanilla es igual.</p>
            <p>En Grãos S.A. importamos <em>Matricaria chamomilla</em> en flor entera —no triturada, no en bolsitas, no mezclada con tallos— porque sabemos que la diferencia se siente en el aroma y se mide en el rendimiento por kilo. Esta guía es para los tres tipos de cliente que llegan acá: la familia que quiere preparar el mejor té de manzanilla en casa, la fábrica que necesita un proveedor estable de manzanilla al por mayor, y el restaurante o herboristería que vive de la calidad del insumo.</p>
            <p>Si solo tiene un minuto: vamos directo a las <a href="#presentaciones">presentaciones disponibles</a> o consulte por WhatsApp. Si tiene ocho, lea todo. Va a entender por qué hay dos décimas de diferencia entre una manzanilla buena y una excelente.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es la manzanilla en flor?",
                "body": """
                    <p>La <strong>manzanilla</strong> (<em>Matricaria chamomilla</em>, también conocida como <em>camomila</em> o <em>chamomile</em>) es una planta de la familia <em>Asteraceae</em>, originaria del sur y este de Europa, hoy cultivada extensamente en Egipto, Argentina, Hungría y la región andina. La parte que se usa para infusión es la <strong>flor entera</strong>: un capítulo amarillo en el centro rodeado de pétalos blancos, secado a baja temperatura para preservar los aceites esenciales.</p>
                    <p>Cuando se habla de "manzanilla flor" en el mercado mayorista paraguayo, se está hablando de la flor entera deshidratada, no de la planta entera molida. La diferencia es enorme: la flor entera concentra <strong>chamazuleno</strong>, <strong>bisabolol</strong> y <strong>flavonoides</strong> en proporciones específicas que dan el aroma dulce-amaderado característico. Cuando ve una manzanilla con tallos verdes mezclados, está viendo un producto inferior.</p>
                    <p>El consumidor paraguayo conoce la manzanilla principalmente como té digestivo después del almuerzo, pero su uso industrial va mucho más allá: cosmética natural, jarabes infantiles, productos de higiene capilar y bebidas funcionales.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Beneficios y propiedades reconocidas",
                "body": """
                    <p>La literatura tradicional y la investigación moderna coinciden en un perfil consistente:</p>
                    <ul>
                        <li><strong>Digestiva:</strong> reduce la sensación de pesadez después de comidas abundantes; uso clásico en Paraguay con el cocido o el guiso.</li>
                        <li><strong>Calmante:</strong> los flavonoides apigenina y luteolina están asociados a un efecto suave de relajación; por eso es la primera elección para tomar antes de dormir.</li>
                        <li><strong>Antiinflamatoria tópica:</strong> el bisabolol se usa en cremas, pomadas y enjuagues para piel sensible o irritaciones leves.</li>
                        <li><strong>Antioxidante:</strong> compuestos polifenólicos que sirven en formulaciones nutracéuticas.</li>
                    </ul>
                    <p>Esto explica por qué la <strong>industria farmacéutica y cosmética</strong> paraguaya y de la región consume volúmenes importantes de manzanilla flor: no es solo un té; es un activo natural con perfil seguro y aceptación cultural masiva.</p>
                    <p class="callout">Aviso: la manzanilla es un alimento, no un medicamento. Cualquier afirmación terapéutica debe ser respaldada por su equipo regulatorio si la va a usar en un producto registrado.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en industria, gastronomía y comercio mayorista",
                "body": """
                    <p>Si usted compra manzanilla al por mayor en Paraguay, probablemente cae en uno de estos perfiles:</p>
                    <ul>
                        <li><strong>Tetera y herboristería:</strong> envasado en bolsitas filtrantes, mezclas tipo "buenas noches" con melissa y cedrón, blends digestivos con menta o anís.</li>
                        <li><strong>Producción de bebidas:</strong> infusiones frías RTD (ready-to-drink), kombuchas saborizadas, bebidas funcionales con relajantes naturales.</li>
                        <li><strong>Cosmética y cuidado personal:</strong> shampoos para cabello rubio, lociones para piel sensible, jabones artesanales premium.</li>
                        <li><strong>Gastronomía premium:</strong> jarabes para coctelería, helados artesanales, postres con notas florales, panificados especiales.</li>
                        <li><strong>Suplementos nutracéuticos:</strong> cápsulas, tinturas, extractos secos.</li>
                    </ul>
                    <p>En todos los casos, la <strong>flor entera</strong> permite trazabilidad visual de calidad —un comprador entrenado puede juzgar el lote a simple vista— y rinde más por kilo que la versión triturada, porque hay menos relleno de tallo y polvo. Para fábricas que dan tickets fiscales y necesitan certificado de origen, Grãos S.A. importa con documentación completa.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo preparar el té de manzanilla perfecto",
                "body": """
                    <p>El error más común es hervir la flor: el agua hirviendo destruye buena parte del aceite esencial y deja un té amargo. La técnica correcta es <strong>infusión a 90 °C, no ebullición</strong>.</p>
                    <ol>
                        <li>Caliente agua filtrada y apague el fuego justo antes del hervor (cuando empiezan las primeras burbujas).</li>
                        <li>Use 1 cucharada sopera (aproximadamente 2 g) de manzanilla flor entera por taza de 200 ml.</li>
                        <li>Vierta el agua sobre la flor en una tetera o jarra de vidrio. Tape para que los aceites volátiles no escapen.</li>
                        <li>Repose 5 a 7 minutos. Más tiempo no significa más sabor; significa más amargor por taninos.</li>
                        <li>Cuele y sirva. Endulzar con miel de monte o azúcar mascabo realza las notas florales.</li>
                    </ol>
                    <p>Para uso industrial en bebidas frías, la práctica es <strong>cold brew</strong>: dejar la flor en agua fría a 4 °C durante 8 a 12 horas. Resultado más claro, menos amargor, perfil aromático más limpio. Excelente para botellas RTD.</p>
                """,
                "howto": {
                    "name": "Cómo preparar té de manzanilla",
                    "total_time": "PT7M",
                    "steps": [
                        {"name": "Calentar agua", "text": "Caliente 200 ml de agua filtrada hasta justo antes del hervor (90 °C)."},
                        {"name": "Medir manzanilla", "text": "Coloque 1 cucharada sopera (2 g) de manzanilla flor entera en la tetera."},
                        {"name": "Verter e infusar", "text": "Vierta el agua sobre la flor, tape la tetera y deje reposar 5 a 7 minutos."},
                        {"name": "Colar y servir", "text": "Cuele en la taza y endulce a gusto con miel o azúcar mascabo."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles para mayoristas",
                "body": """
                    <p>Grãos S.A. trabaja con fábricas, distribuidoras, herboristerías, restaurantes y minimercados en todo el Paraguay. La manzanilla flor entera está disponible en:</p>
                    <ul>
                        <li><strong>Caja institucional 10 kg</strong> — formato más vendido para restaurantes y herboristerías.</li>
                        <li><strong>Caja 20 kg</strong> — para fábricas de té en bolsitas y producción de bebidas.</li>
                        <li><strong>Volúmenes de proyecto</strong> — pallets para industria cosmética y nutracéutica.</li>
                    </ul>
                    <p>Importación directa desde Argentina y Egipto, sin intermediarios, con certificado de origen y análisis bromatológico. Pago por transferencia, factura legal y entrega a todo el país. Si usted necesita un proveedor confiable de <strong>manzanilla al por mayor en Paraguay</strong>, este es el lugar.</p>
                    <p class="cta-inline"><a href="/producto/manzanilla-flor" class="btn-link">Ver ficha del producto →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Qué diferencia hay entre manzanilla en flor y manzanilla común de bolsita?",
                "a": "La manzanilla en flor es la flor entera deshidratada y conserva todos los aceites esenciales y compuestos activos. La manzanilla en bolsita comercial muchas veces es polvo + tallos triturados, con menos aroma, menos rendimiento y mayor amargor. Por eso la flor entera es el formato profesional.",
            },
            {
                "q": "¿La manzanilla pierde efecto si se hierve?",
                "a": "Sí, parcialmente. El agua en ebullición evapora los aceites volátiles responsables del aroma y de buena parte del efecto calmante. La técnica correcta es infusión a 90 °C con la tetera tapada durante 5 a 7 minutos.",
            },
            {
                "q": "¿La manzanilla puede tomarse durante el embarazo?",
                "a": "El consumo ocasional moderado en infusión es ampliamente practicado, pero el consumo diario o en altas dosis durante el embarazo debe ser consultado con el profesional de salud que acompaña a la gestante. Esto vale para cualquier hierba, no solo para la manzanilla.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de manzanilla flor entera?",
                "a": "Aproximadamente 500 tazas de 200 ml usando 2 g por taza. En producción industrial de té en bolsitas, 1 kg rinde alrededor de 1.000 unidades de 1 g. El rendimiento real depende del nivel de infusión deseado por el formulador.",
            },
            {
                "q": "¿Cuál es el origen de la manzanilla que importan?",
                "a": "Grãos S.A. importa principalmente de Argentina y Egipto, los dos orígenes más reconocidos por calidad estable. Cada lote viene con certificado de origen y análisis bromatológico básico.",
            },
            {
                "q": "¿Hacen entregas a todo el Paraguay?",
                "a": "Sí. Despachamos a todo el territorio nacional con factura legal. Para volúmenes mayoristas trabajamos transferencia bancaria y coordinamos logística según destino.",
            },
            {
                "q": "¿Cuál es el pedido mínimo para mayoristas?",
                "a": "El formato más pequeño para mayoristas es la caja institucional de 10 kg. Para volúmenes menores y reventa al por menor también atendemos por consulta directa por WhatsApp.",
            },
        ],
        "related_slugs": ["hibisco-flor", "cedron-capim-limao", "melissa-toronjil", "lavanda-flor"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 2. CANELA EN RAMA 6CM
    # ═════════════════════════════════════════════════════════════════
    "canela-en-rama-6cm": {
        "product_slug": "canela-en-rama-6cm",
        "title": "Canela en Rama: por qué la astilla de 6 cm es el formato preferido por panaderías y fábricas en Paraguay",
        "dek": "Cinnamomum verum, no casia. Aroma dulce y complejo que solo la rama entera entrega. Guía completa para gastronomía, industria y consumo doméstico.",
        "meta_title": "Canela en Rama 6 cm — Guía Mayorista | Grãos S.A.",
        "meta_description": "Todo sobre la canela en rama: variedades, usos, cómo elegirla, cómo preparar y dónde comprar canela al por mayor en Paraguay con importación directa de Vietnam.",
        "category": "Especias y Condimentos",
        "reading_time": 9,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">La <strong>canela en rama</strong> es la especia más universalmente querida del mundo. Está en el chipá guazú de la abuela, en el café latte de la cadena de cafeterías, en la galletita exportada y en la línea de producción de un yogurt funcional. Pero el mercado mayorista paraguayo confunde dos productos muy distintos: la <strong>canela verum</strong> (la fina, de Sri Lanka y Vietnam) y la <strong>canela cassia</strong> (la fuerte, china e indonesia).</p>
            <p>En Grãos S.A. trabajamos canela en rama de 6 cm originaria de <strong>Vietnam</strong>, un origen que combina aroma intenso, color rojizo profundo y precio competitivo. Esta guía explica las diferencias, los usos industriales y los formatos disponibles para revendedores, panaderías, fábricas de bebidas y restaurantes en Paraguay.</p>
            <p>¿Solo quiere comprar? <a href="#presentaciones">Salte a presentaciones</a>. ¿Quiere entender qué está comprando? Siga leyendo.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es la canela en rama y cuáles son las variedades?",
                "body": """
                    <p>La <strong>canela</strong> (<em>Cinnamomum</em>) es la corteza interna seca de árboles del género <em>Cinnamomum</em>. Cuando se enrolla en cilindros, recibe el nombre de <strong>canela en rama</strong>, <strong>canela astilla</strong> o <strong>canela entera</strong>. Existen dos especies principales en el comercio mundial:</p>
                    <ul>
                        <li><strong>Cinnamomum verum (canela de Ceylán o "verdadera"):</strong> color claro, sabor dulce y suave, frágil al tacto. La preferida en repostería europea fina y productos premium.</li>
                        <li><strong>Cinnamomum cassia (canela china, indonesia y vietnamita):</strong> color rojizo más oscuro, sabor más intenso y picante, corteza más rígida. Es la canela dominante en América Latina y en gran parte de la cocina paraguaya.</li>
                    </ul>
                    <p>La canela vietnamita —que es la que Grãos S.A. importa en formato 6 cm— es <em>Cinnamomum cassia</em> seleccionada por su perfil aromático equilibrado: tiene la potencia de la cassia china con un final más dulce, lo que la hace versátil para repostería, bebidas calientes y aplicaciones industriales.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Beneficios y compuestos activos",
                "body": """
                    <p>La canela contiene <strong>cinamaldehído</strong> (60–80 % del aceite esencial), <strong>eugenol</strong>, <strong>cumarina</strong> (presente especialmente en la cassia) y polifenoles. La investigación moderna asocia el consumo moderado de canela con:</p>
                    <ul>
                        <li>Efecto <strong>termogénico</strong> y digestivo suave.</li>
                        <li>Capacidad <strong>antioxidante</strong> alta, comparable a otras especias top como clavo y cúrcuma.</li>
                        <li>Actividad <strong>antimicrobiana</strong> in vitro contra varios patógenos alimentarios; por eso se usa históricamente como conservante natural.</li>
                        <li>Soporte como ingrediente en formulaciones nutracéuticas dirigidas a control glicémico (consulte siempre criterio profesional).</li>
                    </ul>
                    <p class="callout">Importante para fábricas: la cassia tiene mayor contenido de <strong>cumarina</strong> que la verum. Si usted está formulando un producto para consumo diario en altas dosis (suplemento, infantil, dietético registrado), evalúe con su equipo regulatorio si la verum es más apropiada para su categoría.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos para industria, panificación y mayoristas",
                "body": """
                    <p>La canela en rama de 6 cm es el formato más versátil del mercado mayorista. Se puede infusionar entera, romper para infusiones cortas, moler en planta para mantener frescura, o presentar entera en productos premium. Aplicaciones más comunes en Paraguay:</p>
                    <ul>
                        <li><strong>Panificación industrial:</strong> rolls de canela, panettones de fin de año, galletitas, alfajores con relleno especiado.</li>
                        <li><strong>Bebidas calientes y frías:</strong> café latte, chocolate caliente, bebidas mate-canela, kombuchas saborizadas, gaseosas artesanales.</li>
                        <li><strong>Coctelería premium:</strong> jarabes de canela infusionados, palitos para drinks tipo old fashioned, decoración de copas.</li>
                        <li><strong>Postres y helados:</strong> arroz con leche, mazamorra, helados de canela, dulce de leche con notas especiadas.</li>
                        <li><strong>Productos típicos paraguayos:</strong> chipa cuatro quesos con canela, sopa paraguaya saborizada, mbaipy de mandioca dulce.</li>
                        <li><strong>Cosmética y aromaterapia:</strong> jabones especiados, sales de baño, ambientadores naturales.</li>
                    </ul>
                    <p>Para fábricas que necesitan canela en grandes volúmenes con calidad estable lote a lote, la canela vietnamita 6 cm de Grãos S.A. ofrece la combinación más buscada: precio competitivo, perfil aromático fuerte y disponibilidad consistente.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo usar canela en rama: técnicas básicas",
                "body": """
                    <p>La regla de oro: <strong>la canela en rama libera mejor su sabor con calor sostenido y lento</strong>, no con calor agresivo corto. Tres técnicas profesionales:</p>
                    <ol>
                        <li><strong>Infusión líquida (té, chocolate caliente, leche dorada):</strong> 1 rama de 6 cm por cada 500 ml de líquido. Calentar a fuego bajo durante 8 a 10 minutos sin hervir fuerte. Retirar la rama antes de servir.</li>
                        <li><strong>Cocción larga (arroz con leche, mazamorra, compotas):</strong> incorporar la rama desde el inicio del cocción y retirar al final. La canela libera lentamente sin amargar.</li>
                        <li><strong>Infusión en frío (jarabes, cold brew, kombucha):</strong> dejar 2 ramas de 6 cm en 1 litro de líquido a temperatura ambiente durante 24 a 48 horas. Resultado: sabor limpio, sin compuestos amargos del calor.</li>
                    </ol>
                    <p>Tip industrial: si usted muele la canela en planta para incorporar a una fórmula seca (premezcla de panificación, blend de café), hágalo lo más cerca posible de la producción. La canela molida pierde 30–40 % de aroma en 60 días aún en envase cerrado.</p>
                """,
                "howto": {
                    "name": "Cómo preparar leche con canela y miel",
                    "total_time": "PT12M",
                    "steps": [
                        {"name": "Calentar leche", "text": "Caliente 500 ml de leche entera a fuego bajo en una olla."},
                        {"name": "Agregar canela", "text": "Añada 1 rama de canela de 6 cm cuando la leche empiece a entibiar."},
                        {"name": "Infusionar", "text": "Mantenga el fuego mínimo durante 10 minutos sin dejar hervir. Revuelva ocasionalmente."},
                        {"name": "Endulzar y servir", "text": "Retire la rama, incorpore 1 cucharada de miel y sirva caliente."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Grãos S.A. trabaja la canela en rama de 6 cm en formatos pensados para industria, panificación y reventa:</p>
                    <ul>
                        <li><strong>Caja 10 kg</strong> — formato estándar para panaderías, restaurantes y herboristerías.</li>
                        <li><strong>Caja 20 kg</strong> — para fábricas de bebidas, productos típicos y exportación.</li>
                    </ul>
                    <p>Importación directa de Vietnam, sin intermediarios. Cada lote viene con certificado de origen, análisis bromatológico y trazabilidad completa. Si su negocio depende de una <strong>canela al por mayor confiable en Paraguay</strong>, hable con nosotros.</p>
                    <p class="cta-inline"><a href="/producto/canela-en-rama-6cm" class="btn-link">Ver ficha del producto →</a> · <a href="/producto/canela-en-polvo-100-pura" class="btn-link">Canela en polvo →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Qué diferencia hay entre canela de Ceylán y canela cassia?",
                "a": "La canela de Ceylán (Cinnamomum verum) es más clara, suave y dulce; la cassia (Cinnamomum cassia) es más oscura, intensa y picante. La cassia tiene mayor contenido de cumarina y es la dominante en América Latina por sabor y precio.",
            },
            {
                "q": "¿La canela vietnamita es cassia?",
                "a": "Sí, es Cinnamomum cassia originaria de Vietnam. Tiene la potencia de la cassia china pero con un final más dulce y un color rojizo profundo apreciado en repostería.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de canela en rama de 6 cm?",
                "a": "Aproximadamente 165 ramas por kilo. Si la usa para infusión líquida (1 rama por 500 ml), rinde 80 litros de bebida o té de canela.",
            },
            {
                "q": "¿Conviene comprar canela en rama o canela en polvo?",
                "a": "Para mantener aroma y rendimiento, la rama es siempre superior porque la molienda libera aceites volátiles que se pierden con el tiempo. Si necesita polvo, lo ideal es moler en planta lo más cerca posible del momento de uso.",
            },
            {
                "q": "¿La canela ayuda a controlar el azúcar en sangre?",
                "a": "Hay estudios que sugieren que la canela puede tener un efecto modesto en el control glicémico, pero no reemplaza tratamiento médico. Si está formulando un producto con esa indicación, valide con su equipo regulatorio.",
            },
            {
                "q": "¿Qué cuidados tiene el almacenamiento?",
                "a": "Lugar seco, a la sombra, lejos de fuentes de humedad. La canela en rama bien guardada mantiene aroma por 18 a 24 meses. La molida pierde calidad mucho más rápido (60–90 días).",
            },
            {
                "q": "¿Hacen entregas y facturación legal a todo el Paraguay?",
                "a": "Sí. Despachamos a todo el país, emitimos factura legal y trabajamos con transferencia bancaria. Coordinamos logística según volumen y destino.",
            },
        ],
        "related_slugs": ["clavo-de-olor", "anis-estrellado", "nuez-moscada-en-polvo", "cardamomo-en-grano"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 3. CURCUMA EN POLVO
    # ═════════════════════════════════════════════════════════════════
    "curcuma-en-polvo": {
        "product_slug": "curcuma-en-polvo",
        "title": "Cúrcuma en Polvo: el oro amarillo que mueve la industria de suplementos, bebidas y comida natural en Paraguay",
        "dek": "Curcuma longa molida fina, color amarillo intenso, aroma terroso. Por qué la cúrcuma india es el estándar mundial y cómo usarla a escala industrial.",
        "meta_title": "Cúrcuma en Polvo — Guía Mayorista | Grãos S.A.",
        "meta_description": "Cúrcuma en polvo importada de India al por mayor en Paraguay. Beneficios, usos industriales, leche dorada, golden latte, suplementos. Calidad estable lote a lote.",
        "category": "Especias y Condimentos",
        "reading_time": 8,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">La <strong>cúrcuma</strong> dejó de ser una especia exótica para convertirse en el ingrediente estrella de la nueva ola de productos saludables: leche dorada, golden lattes, suplementos antiinflamatorios, blends funcionales para superalimentos y curries instantáneos. Lo que era nicho hace diez años hoy es categoría de góndola.</p>
            <p>En Grãos S.A. importamos <strong>cúrcuma en polvo de India</strong>, el origen mundial por excelencia (también llamada açafrão da terra en portugués o turmeric en inglés). Esta guía es para industria de suplementos, fábricas de bebidas funcionales, restaurantes especializados, herboristerías y consumidores que quieren entender la diferencia entre una cúrcuma estándar y una premium.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es la cúrcuma y por qué India?",
                "body": """
                    <p>La <strong>cúrcuma</strong> (<em>Curcuma longa</em>) es un rizoma de la familia <em>Zingiberaceae</em>, pariente cercano del jengibre. Se cosecha, hierve, seca y muele para obtener el polvo amarillo intenso conocido en el mundo entero. India produce el <strong>80 % de la cúrcuma del planeta</strong>, y los estados de Tamil Nadu, Andhra Pradesh y Maharashtra son los polos productivos más importantes.</p>
                    <p>El compuesto activo principal de la cúrcuma es la <strong>curcumina</strong>, un polifenol responsable del color amarillo y de prácticamente todas las propiedades funcionales atribuidas a la especia. El contenido de curcumina varía típicamente entre 2 % y 5 % del peso total. Una cúrcuma premium tiene contenido cercano al 4 %.</p>
                    <p>Otras formas comerciales que circulan en el mercado: cúrcuma molida común, cúrcuma orgánica certificada, extractos estandarizados (95 % curcumina, usados en suplementos), y cúrcuma fermentada. Grãos S.A. trabaja la versión culinaria estándar de calidad alta, ideal para industria alimentaria y herboristería.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Beneficios y aplicaciones funcionales",
                "body": """
                    <p>La cúrcuma es probablemente la especia con más estudios científicos publicados de la última década. La curcumina está asociada a:</p>
                    <ul>
                        <li><strong>Acción antiinflamatoria</strong> en estudios in vitro y en humanos.</li>
                        <li><strong>Capacidad antioxidante</strong> alta.</li>
                        <li><strong>Soporte digestivo y hepático</strong> en uso tradicional ayurvédico.</li>
                        <li><strong>Efecto colorante natural</strong>: la cúrcuma reemplaza colorantes sintéticos amarillos en alimentos clean-label.</li>
                    </ul>
                    <p>Detalle importante para industria: la curcumina se absorbe mal sola. Los productos funcionales modernos combinan cúrcuma con <strong>pimienta negra (piperina)</strong>, que aumenta la biodisponibilidad hasta 20 veces, y con <strong>grasa</strong> (leche, aceite de coco), porque la curcumina es liposoluble. Por eso la fórmula clásica del golden latte funciona: cúrcuma + pimienta + leche entera.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en industria, suplementos y gastronomía",
                "body": """
                    <p>La cúrcuma en polvo es uno de los ingredientes más versátiles del mercado mayorista. Aplicaciones de mayor demanda en Paraguay:</p>
                    <ul>
                        <li><strong>Suplementos nutracéuticos:</strong> cápsulas con piperina, polvos solubles, gomas masticables, blends antiinflamatorios.</li>
                        <li><strong>Bebidas funcionales:</strong> golden lattes, leches doradas RTD, kombuchas amarillas, bebidas deportivas naturales.</li>
                        <li><strong>Industria de currys y blends:</strong> base de curry indio, masala, mezclas para asado funcional.</li>
                        <li><strong>Repostería saludable y panificación:</strong> panes funcionales, muffins de cúrcuma, galletitas integrales.</li>
                        <li><strong>Colorante natural alimentario:</strong> reemplazo de tartrazina E102 en pastas, fideos, mostazas, pickles, lácteos saborizados.</li>
                        <li><strong>Cosmética natural:</strong> mascarillas faciales, jabones detox, exfoliantes corporales.</li>
                    </ul>
                    <p>Para fábricas con producción mensual significativa, la cúrcuma india de Grãos S.A. ofrece estabilidad de color lote a lote —crítico cuando el amarillo del producto final es parte de la identidad de marca— y precio competitivo en formato granel.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo preparar leche dorada (golden milk) industrial-grade",
                "body": """
                    <p>La <strong>leche dorada</strong> (<em>golden milk</em>) es la receta ancestral ayurvédica que disparó el consumo global de cúrcuma. Adaptada para producción industrial:</p>
                    <ol>
                        <li>Por cada 250 ml de leche entera o vegetal, use 1 cucharadita (3 g) de cúrcuma en polvo.</li>
                        <li>Agregue una pizca (~0,1 g) de pimienta negra molida —la piperina multiplica la absorción hasta 20 veces—.</li>
                        <li>Caliente a fuego bajo entre 60 °C y 70 °C, sin hervir. Incorpore una cucharadita de aceite de coco si quiere reforzar la liposolubilidad.</li>
                        <li>Endulce con 1 cucharadita de miel o jarabe natural una vez fuera del fuego.</li>
                        <li>Opcional: agregue jengibre molido y canela para perfil ayurvédico completo.</li>
                    </ol>
                    <p>Aplicación industrial: el mismo principio se usa en bebidas RTD pasteurizadas. La curcumina debe ser dispersada con un emulsificante natural (lecitina de girasol, goma xantana) para evitar sedimentación.</p>
                """,
                "howto": {
                    "name": "Cómo preparar leche dorada (golden milk)",
                    "total_time": "PT8M",
                    "steps": [
                        {"name": "Medir ingredientes", "text": "Mida 250 ml de leche, 1 cdta de cúrcuma, una pizca de pimienta negra y 1 cdta de aceite de coco."},
                        {"name": "Calentar leche", "text": "Caliente la leche a fuego bajo hasta 60-70 °C sin dejar hervir."},
                        {"name": "Incorporar especias", "text": "Agregue la cúrcuma, la pimienta y el aceite de coco. Mezcle con batidor."},
                        {"name": "Endulzar y servir", "text": "Retire del fuego, agregue 1 cdta de miel y sirva caliente."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles para mayoristas",
                "body": """
                    <p>Grãos S.A. importa cúrcuma en polvo de India en formatos para industria y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 10 kg</strong> — formato estándar para herboristerías y restaurantes.</li>
                        <li><strong>Bolsa 25 kg</strong> — para fábricas de suplementos, bebidas funcionales y currys industriales.</li>
                    </ul>
                    <p>Cada lote viene con certificado de origen, análisis bromatológico y, bajo pedido, certificado de contenido de curcumina. Importación directa, factura legal, entrega a todo el Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/curcuma-en-polvo" class="btn-link">Ver ficha del producto →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿La cúrcuma se absorbe mejor con pimienta negra?",
                "a": "Sí. La piperina de la pimienta negra aumenta la biodisponibilidad de la curcumina hasta 20 veces. Por eso prácticamente todos los suplementos serios de cúrcuma incluyen extracto de pimienta o piperina pura.",
            },
            {
                "q": "¿Qué porcentaje de curcumina tiene la cúrcuma de uso culinario?",
                "a": "Entre 2 % y 5 % según origen y procesamiento. La cúrcuma india premium se ubica cerca del 4 %. Los extractos estandarizados para suplementos llegan al 95 % de curcumina.",
            },
            {
                "q": "¿Sirve para colorear alimentos sin aditivos químicos?",
                "a": "Sí, es uno de los colorantes naturales amarillos más usados en la industria. Reemplaza la tartrazina E102 en pastas, mostazas, fideos, lácteos saborizados y productos clean-label.",
            },
            {
                "q": "¿Tiene contraindicaciones?",
                "a": "El consumo culinario es seguro para la mayoría de las personas. Dosis altas en suplemento (>1 g de curcumina pura por día) deben ser consultadas con profesional de salud, especialmente si se está usando anticoagulantes.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de cúrcuma en polvo en producción de bebidas?",
                "a": "Aproximadamente 330 porciones de golden latte (3 g por 250 ml). En suplementos en cápsula de 500 mg, rinde 2.000 cápsulas.",
            },
            {
                "q": "¿Cómo se conserva mejor la cúrcuma molida?",
                "a": "En envase hermético, lejos de luz directa y humedad. Bien almacenada conserva color y aroma por 12 a 18 meses. Después de eso pierde intensidad gradualmente.",
            },
        ],
        "related_slugs": ["jengibre-en-polvo", "pimienta-negra-en-grano", "moringa-en-polvo", "spirulina-en-polvo"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 4. HIBISCO FLOR
    # ═════════════════════════════════════════════════════════════════
    "hibisco-flor": {
        "product_slug": "hibisco-flor",
        "title": "Hibisco en Flor: la flor de Jamaica que conquistó la coctelería, las bebidas funcionales y los tés helados de Paraguay",
        "dek": "Hibiscus sabdariffa, color rubí profundo, sabor cítrico-floral. Cómo se usa en industria, gastronomía premium y consumo doméstico.",
        "meta_title": "Hibisco Flor (Jamaica) — Guía Mayorista | Grãos S.A.",
        "meta_description": "Hibisco flor importado al por mayor en Paraguay: té de hibisco, flor de jamaica, bebidas funcionales, coctelería. Importación directa con calidad estable.",
        "category": "Hierbas y Tés",
        "reading_time": 8,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "berry",
        "intro": """
            <p class="lead">El <strong>hibisco</strong> —llamado también <strong>flor de jamaica</strong> en gran parte de Latinoamérica— pasó de ser una infusión de abuela a ser el ingrediente estrella de bebidas funcionales, coctelería premium y tés helados artesanales. Su color rubí profundo y su perfil cítrico-floral lo hacen uno de los productos más fotogénicos del mercado, lo que se traduce en demanda constante en redes sociales y góndola.</p>
            <p>En Grãos S.A. importamos hibisco flor entera (<em>Hibiscus sabdariffa</em>) seleccionado por intensidad de color y limpieza visual, listo para industria de bebidas, herboristerías, bares de coctelería y restaurantes que quieren ofrecer infusiones diferenciadas.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es el hibisco y por qué se llama flor de jamaica?",
                "body": """
                    <p>El <strong>hibisco</strong> de uso comestible es <em>Hibiscus sabdariffa</em>, una especie distinta del hibisco ornamental que se ve en jardines. La parte que se consume no es la flor en sí, sino el <strong>cáliz seco</strong> que rodea la flor —tejido carnoso, color rubí, sabor agridulce con notas cítricas y a frutas rojas—.</p>
                    <p>El nombre "<strong>flor de jamaica</strong>" se popularizó en México y Centroamérica por la asociación con el Caribe, aunque hoy buena parte de la producción comercial viene de <strong>Egipto, Sudán, Tailandia y Nigeria</strong>. Es la misma planta, distintos nombres regionales:</p>
                    <ul>
                        <li><strong>Paraguay y Cono Sur:</strong> hibisco, hibisco flor.</li>
                        <li><strong>México:</strong> flor de jamaica, jamaica.</li>
                        <li><strong>Brasil:</strong> hibisco, vinagreira.</li>
                        <li><strong>Inglés/internacional:</strong> hibiscus, roselle.</li>
                    </ul>
                    <p>El cáliz contiene <strong>antocianinas</strong> (responsables del color rubí), <strong>ácidos orgánicos</strong> (cítrico, málico, hibíscico) que dan la acidez refrescante, y <strong>vitamina C</strong>.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Beneficios funcionales del hibisco",
                "body": """
                    <p>El hibisco es uno de los ingredientes botánicos con investigación clínica más sólida para bebidas funcionales. Los hallazgos más reproducidos:</p>
                    <ul>
                        <li><strong>Soporte cardiovascular:</strong> varios estudios asocian el consumo regular de té de hibisco con efecto modesto sobre presión arterial.</li>
                        <li><strong>Capacidad antioxidante</strong> elevada por las antocianinas.</li>
                        <li><strong>Diurético natural</strong> en uso tradicional, lo que lo posiciona en bebidas detox.</li>
                        <li><strong>Aporte de vitamina C</strong> y polifenoles.</li>
                    </ul>
                    <p>Estos atributos lo hacen ideal para etiquetas <strong>"funcional"</strong>, <strong>"natural"</strong> y <strong>"sin aditivos"</strong>, una categoría en pleno crecimiento en góndola paraguaya y de la región.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en industria, coctelería y gastronomía",
                "body": """
                    <p>Por color, sabor y perfil saludable, el hibisco es un ingrediente premiado:</p>
                    <ul>
                        <li><strong>Bebidas RTD funcionales:</strong> tés helados embotellados, kombuchas rosadas, aguas saborizadas naturales.</li>
                        <li><strong>Coctelería de autor:</strong> jarabes infusionados (hibisco-jengibre, hibisco-cardamomo), espumas y reducciones para drinks de firma.</li>
                        <li><strong>Pastelería gourmet:</strong> macarons rosa rubí, glaseados naturales, mermeladas artesanales, cheesecakes con coulis de hibisco.</li>
                        <li><strong>Helados y sorbetes:</strong> sorbete de hibisco-frutilla, paletas artesanales con color natural.</li>
                        <li><strong>Industria nutracéutica:</strong> blends de polvos detox, cápsulas con extracto seco, mezclas para bebidas instantáneas.</li>
                        <li><strong>Cocina paraguaya y latinoamericana:</strong> aguas frescas de jamaica, gelatinas naturales, salsas agridulces para carnes.</li>
                    </ul>
                    <p>Característica clave para industria: el hibisco entrega <strong>color sin colorante artificial</strong>, lo que es crítico en productos clean-label.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo preparar agua y té de hibisco",
                "body": """
                    <p>El hibisco tiene dos modos de preparación dominantes según la temperatura:</p>
                    <ol>
                        <li><strong>Té caliente:</strong> 1 cucharada (5 g) de flor entera por cada 250 ml de agua a 90 °C. Reposo 5 minutos. Color rubí intenso, sabor más concentrado.</li>
                        <li><strong>Agua fresca de jamaica (cold brew):</strong> 30 g de hibisco por 1 litro de agua fría. Reposo 8 a 12 horas en heladera. Endulzar con jugo de jengibre o miel. Sabor más limpio, menos taninoso.</li>
                    </ol>
                    <p>Para coctelería, la técnica preferida es <strong>jarabe infusionado</strong>: 100 g de hibisco + 500 ml de agua + 500 g de azúcar mascabo. Hervor breve, reposo 30 minutos, colado. Conserva 30 días en heladera. Base perfecta para drinks de firma.</p>
                """,
                "howto": {
                    "name": "Cómo preparar agua de jamaica (hibisco frío)",
                    "total_time": "PT8H30M",
                    "steps": [
                        {"name": "Medir hibisco", "text": "Coloque 30 g de hibisco flor entera en una jarra de 1 litro."},
                        {"name": "Agregar agua fría", "text": "Llene la jarra con 1 litro de agua fría filtrada."},
                        {"name": "Refrigerar", "text": "Tape y deje en heladera entre 8 y 12 horas."},
                        {"name": "Colar y endulzar", "text": "Cuele la flor, endulce con miel o azúcar mascabo y sirva con hielo."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Hibisco flor entera importado para industria, reventa y coctelería:</p>
                    <ul>
                        <li><strong>Caja 10 kg</strong> — formato estándar para coctelería, herboristerías y bebidas artesanales.</li>
                        <li><strong>Caja 25 kg</strong> — para fábricas de bebidas RTD y nutracéuticos.</li>
                    </ul>
                    <p>Importación directa de Egipto y Tailandia, calidad estable, certificado de origen y análisis bromatológico.</p>
                    <p class="cta-inline"><a href="/producto/hibisco-flor" class="btn-link">Ver ficha del producto →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Hibisco y flor de jamaica son lo mismo?",
                "a": "Sí. Son nombres distintos para Hibiscus sabdariffa, según la región. En Paraguay y el Cono Sur se llama hibisco; en México y Centroamérica se llama flor de jamaica.",
            },
            {
                "q": "¿El té de hibisco baja la presión?",
                "a": "Hay estudios clínicos que muestran un efecto modesto en personas con presión limítrofe, especialmente con consumo regular. No reemplaza tratamiento médico y debe ser usado como complemento dietario.",
            },
            {
                "q": "¿Por qué algunos hibiscos manchan la lengua y otros no?",
                "a": "Depende de la concentración de antocianinas y del tiempo de infusión. Una infusión muy concentrada o muy larga deja color residual. Reducir tiempo a 5 minutos minimiza el efecto.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de hibisco en producción de bebidas?",
                "a": "Aproximadamente 33 litros de agua de jamaica concentrada (30 g/L) o 200 tazas de té (5 g por taza). En jarabe de coctelería, rinde 5 litros de jarabe terminado.",
            },
            {
                "q": "¿Sirve para colorear bebidas sin colorante artificial?",
                "a": "Sí, es uno de los colorantes naturales rojo-rosa más usados en bebidas funcionales. Estable en pH ácido (jugo de naranja, limón); en pH básico vira hacia tonos azulados.",
            },
            {
                "q": "¿Qué presentaciones manejan?",
                "a": "Cajas de 10 kg para reventa y coctelería, y cajas de 25 kg para fábricas. Volúmenes mayores se cotizan por proyecto.",
            },
        ],
        "related_slugs": ["manzanilla-flor", "lavanda-flor", "cedron-capim-limao", "te-verde-importado"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 5. SPIRULINA EN POLVO
    # ═════════════════════════════════════════════════════════════════
    "spirulina-en-polvo": {
        "product_slug": "spirulina-en-polvo",
        "title": "Spirulina en Polvo: el superalimento que cambió la industria de suplementos y bebidas funcionales",
        "dek": "Arthrospira platensis, 60 % de proteína vegetal, perfil completo de aminoácidos. Por qué la spirulina es la base de la nueva generación de productos saludables en Paraguay.",
        "meta_title": "Spirulina en Polvo — Guía Mayorista | Grãos S.A.",
        "meta_description": "Spirulina en polvo importada al por mayor en Paraguay para industria de suplementos, bebidas funcionales, smoothies y nutracéuticos. Calidad premium, importación directa.",
        "category": "Suplementos y Superalimentos",
        "reading_time": 8,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "green",
        "intro": """
            <p class="lead">La <strong>spirulina</strong> es probablemente el ingrediente nutracéutico más estudiado del último siglo. La FAO la describió como "el alimento del futuro" en los años 70, y hoy es base de cápsulas, polvos solubles, bebidas funcionales, smoothies y barritas en todo el mundo. En Paraguay, la categoría de superalimentos creció más del 40 % los últimos tres años, y la spirulina es la cabeza de góndola.</p>
            <p>En Grãos S.A. importamos <strong>spirulina en polvo (Arthrospira platensis)</strong> de calidad premium, con perfil nutricional alto y estable lote a lote. Esta guía es para fábricas de suplementos, formuladores de bebidas funcionales, herboristerías, gimnasios con línea propia de productos, y consumidores que quieren entender qué están comprando.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es la spirulina exactamente?",
                "body": """
                    <p>La <strong>spirulina</strong> no es una planta ni un alga clásica: es una <strong>cianobacteria fotosintética</strong> (<em>Arthrospira platensis</em>) que crece en aguas alcalinas tropicales y subtropicales. Se cultiva en estanques controlados, se cosecha por filtración, se seca por spray-drying y se muele a polvo verde-azulado intenso, soluble parcialmente en líquidos.</p>
                    <p>Lo que hace única a la spirulina es su perfil nutricional:</p>
                    <ul>
                        <li><strong>60 %–70 % de proteína</strong> con todos los aminoácidos esenciales (incluido lisina, escasa en proteínas vegetales).</li>
                        <li><strong>Hierro biodisponible</strong>: 28 mg por 100 g, una de las fuentes vegetales más densas.</li>
                        <li><strong>Vitamina B12 análoga</strong> y otras del complejo B.</li>
                        <li><strong>Ficocianina</strong>, pigmento azul único con actividad antioxidante.</li>
                        <li><strong>Clorofila</strong>, beta-caroteno, ácido gamma-linolénico (GLA).</li>
                    </ul>
                    <p>Origen comercial dominante: India y China. Hay producción local creciente en Argentina y Brasil, pero los volúmenes industriales siguen siendo asiáticos.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Beneficios y aplicaciones funcionales",
                "body": """
                    <p>El consumo regular de spirulina está asociado a:</p>
                    <ul>
                        <li><strong>Aporte proteico vegetal completo</strong>: ideal para dietas veganas, vegetarianas y deportivas.</li>
                        <li><strong>Soporte de niveles de hierro</strong>, especialmente en perfiles con anemia leve o requerimientos elevados.</li>
                        <li><strong>Capacidad antioxidante alta</strong> por la combinación de ficocianina, beta-caroteno y vitamina E.</li>
                        <li><strong>Apoyo al sistema inmunológico</strong> en uso tradicional y en algunos estudios.</li>
                        <li><strong>Desintoxicación</strong>: capacidad de unirse a metales pesados; uso en protocolos quelantes.</li>
                    </ul>
                    <p>Esto explica su penetración rápida en categorías como <strong>polvos proteicos vegetales</strong>, <strong>fórmulas detox</strong>, <strong>energizantes naturales</strong> y <strong>multivitamínicos clean-label</strong>.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos para industria de suplementos y bebidas funcionales",
                "body": """
                    <p>La spirulina es uno de los ingredientes más versátiles de la industria nutracéutica:</p>
                    <ul>
                        <li><strong>Cápsulas y comprimidos:</strong> el formato más vendido en farmacia y herboristería; dosis típica de 500 mg a 1 g por unidad.</li>
                        <li><strong>Polvos proteicos vegetales:</strong> blends con proteína de arroz, guisante o cáñamo; aporta perfil aminoacídico y color natural.</li>
                        <li><strong>Smoothies y batidos verdes:</strong> en escala industrial (RTD), en barras de jugos y en gimnasios premium.</li>
                        <li><strong>Barritas energéticas y geles deportivos:</strong> aporta proteína, hierro y color verde clean-label.</li>
                        <li><strong>Pastas y panificación funcional:</strong> fideos verdes, panes proteicos, galletitas funcionales.</li>
                        <li><strong>Cosmética natural:</strong> mascarillas detox, jabones de algas, productos antiage por su perfil antioxidante.</li>
                    </ul>
                    <p>Reto técnico para fábricas: la spirulina tiene <strong>sabor marino fuerte</strong>. La formulación moderna lo enmascara con frutas tropicales (mango, piña, banana), cacao o vainilla. El color verde puro también se diluye con cacao en formulaciones marrones.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo usar spirulina en consumo doméstico",
                "body": """
                    <p>La dosis estándar de mantenimiento es <strong>3 a 5 g por día</strong> (1 cucharadita rasa). Tres formas profesionales de incorporarla:</p>
                    <ol>
                        <li><strong>Smoothie verde:</strong> 1 cdta de spirulina + 1 banana + ½ taza de espinaca + 200 ml de leche vegetal + 1 cdta de miel. Procese 60 segundos. Sabor enmascarado por la banana.</li>
                        <li><strong>Shot mañanero:</strong> 1 cdta de spirulina disuelta en jugo de naranja recién exprimido. La vitamina C mejora absorción de hierro.</li>
                        <li><strong>Yogurt funcional:</strong> mezcle 1 cdta de spirulina con 200 g de yogurt natural y 1 cdta de miel. Excelente desayuno proteico.</li>
                    </ol>
                    <p>Importante: la spirulina nunca debe calentarse a más de 70 °C; el calor degrada la ficocianina y reduce el valor nutricional. Se incorpora siempre al final de la preparación.</p>
                """,
                "howto": {
                    "name": "Cómo preparar smoothie verde con spirulina",
                    "total_time": "PT5M",
                    "steps": [
                        {"name": "Reunir ingredientes", "text": "Disponga 1 cdta de spirulina, 1 banana, ½ taza de espinaca, 200 ml de leche vegetal y 1 cdta de miel."},
                        {"name": "Procesar", "text": "Coloque todo en la licuadora y procese durante 60 segundos hasta obtener una mezcla homogénea."},
                        {"name": "Servir frío", "text": "Sirva inmediatamente sin agregar hielo caliente ni cocinar; la spirulina pierde valor con calor alto."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles para industria",
                "body": """
                    <p>Grãos S.A. importa spirulina en polvo para fábricas, herboristerías y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 1 kg</strong> — para herboristerías, gimnasios y reventa premium.</li>
                        <li><strong>Bolsa 5 kg</strong> — para fábricas medianas de cápsulas y polvos proteicos.</li>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial para grandes formuladores y bebidas RTD.</li>
                    </ul>
                    <p>Calidad premium, certificado de origen, análisis bromatológico y, bajo pedido, perfil de proteína y metales pesados. Importación directa, factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/spirulina-en-polvo" class="btn-link">Ver ficha del producto →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿La spirulina es un alga o una bacteria?",
                "a": "Técnicamente es una cianobacteria fotosintética, no un alga verdadera. Comercialmente se la trata como superalimento de origen acuático.",
            },
            {
                "q": "¿La spirulina contiene vitamina B12 real?",
                "a": "Contiene una forma análoga de B12 cuya bioactividad humana es debatida. Veganos estrictos no deben depender solo de spirulina para cubrir B12; se recomienda complementar con suplemento específico.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de spirulina en producción de cápsulas?",
                "a": "Aproximadamente 2.000 cápsulas de 500 mg, o 1.000 comprimidos de 1 g. En polvos proteicos rinde alrededor de 200 porciones de 5 g.",
            },
            {
                "q": "¿Por qué la spirulina huele y sabe a mar?",
                "a": "Por su origen acuático y por compuestos sulfurados naturales. La industria moderna lo enmascara con frutas tropicales o cacao.",
            },
            {
                "q": "¿Es segura para consumo diario?",
                "a": "Sí, en dosis de 3-5 g/día es generalmente bien tolerada. Personas con fenilcetonuria deben evitarla por contenido de fenilalanina.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y oscuro. Bien almacenada conserva calidad por 18-24 meses. Después de abierto el envase, idealmente consumir en 6 meses.",
            },
        ],
        "related_slugs": ["moringa-en-polvo", "maca-peruana-en-polvo", "chia-en-semillas", "guarana-en-polvo"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 6. QUINOA EN GRANO
    # ═════════════════════════════════════════════════════════════════
    "quinoa-en-grano": {
        "product_slug": "quinoa-en-grano",
        "title": "Quinoa en Grano: el grano andino milenario que conquistó la góndola saludable de Paraguay",
        "dek": "Chenopodium quinoa, proteína completa, sin gluten, perfil nutricional inigualable. Por qué la quinoa real peruana es el estándar mundial.",
        "meta_title": "Quinoa en Grano — Guía Mayorista | Grãos S.A.",
        "meta_description": "Quinoa peruana al por mayor en Paraguay para industria saludable, restaurantes, herboristerías y reventa. Importación directa, calidad estable lote a lote.",
        "category": "Semillas y Granos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "earth",
        "intro": """
            <p class="lead">La <strong>quinoa</strong> es uno de los pocos alimentos de origen vegetal que aporta <strong>proteína completa</strong>: contiene los nueve aminoácidos esenciales en proporciones equilibradas, algo raro fuera del reino animal. Sumá a eso que es naturalmente <strong>libre de gluten</strong>, fácil de digerir y de cocción rápida, y entendés por qué la categoría sin TACC se construyó alrededor de este grano.</p>
            <p>En Grãos S.A. importamos <strong>quinoa peruana (Chenopodium quinoa)</strong>, el origen referente mundial. Esta guía es para fábricas de productos sin gluten, restaurantes de cocina sana, gimnasios con menú propio y consumidores que quieren entender qué hace especial a este grano andino.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es la quinoa y por qué Perú es el origen referente?",
                "body": """
                    <p>La <strong>quinoa</strong> (<em>Chenopodium quinoa</em>) no es técnicamente un cereal: es un <strong>pseudocereal</strong>, pariente de la espinaca y la remolacha. Crece a más de 3.000 metros sobre el nivel del mar en los Andes, lo que le da resistencia a sequía, frío y suelos pobres —y un perfil nutricional inusualmente denso—.</p>
                    <p>Existen tres variedades comerciales principales:</p>
                    <ul>
                        <li><strong>Quinoa blanca (real):</strong> la más vendida; sabor neutro, textura suave, ideal para uso general.</li>
                        <li><strong>Quinoa roja:</strong> color rojizo, textura más firme, sabor más intenso, ideal para ensaladas frías.</li>
                        <li><strong>Quinoa negra:</strong> color oscuro, sabor terroso, presentación gourmet.</li>
                    </ul>
                    <p>Perú produce alrededor del 50 % de la quinoa mundial; Bolivia, el segundo origen relevante. Grãos S.A. importa principalmente quinoa blanca real peruana, el estándar de calidad para industria.</p>
                    <p>Detalle técnico: la quinoa contiene <strong>saponinas</strong> en la cáscara que dan sabor amargo si no se eliminan. La quinoa comercial moderna viene <strong>perlada</strong> (saponinas removidas mecánicamente y por lavado), lista para cocinar. Igual recomendamos un enjuague rápido antes del uso.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Por qué la quinoa es el grano premium",
                "body": """
                    <p>Perfil nutricional por 100 g de quinoa cruda:</p>
                    <ul>
                        <li><strong>14 g de proteína completa</strong> (más que la avena, comparable a la carne en perfil aminoacídico).</li>
                        <li><strong>7 g de fibra</strong>: alta densidad para un grano.</li>
                        <li><strong>Sin gluten</strong>: apta celíacos sin contaminación cruzada certificada.</li>
                        <li><strong>Hierro, magnesio, fósforo</strong> en proporciones relevantes.</li>
                        <li><strong>Bajo índice glicémico</strong>: ideal para dietas con control de azúcar.</li>
                        <li><strong>Lisina</strong>, aminoácido limitante en la mayoría de los cereales.</li>
                    </ul>
                    <p>Para industria: la quinoa es un ingrediente <strong>"cuatro estrellas"</strong> —sin gluten, alto en proteína, vegano, integral— que permite ticket alto en góndola y posicionamiento premium.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos para industria, restaurantes y reventa",
                "body": """
                    <p>La quinoa es de los granos más versátiles de la categoría saludable:</p>
                    <ul>
                        <li><strong>Industria sin gluten:</strong> harinas mixtas, panes celíacos, pastas premium, galletitas saludables.</li>
                        <li><strong>Productos para celíacos:</strong> mezcla con harinas de arroz, garbanzo y mandioca para textura y proteína.</li>
                        <li><strong>Restaurantes y cocina saludable:</strong> bowls de quinoa, ensaladas mediterráneas, hamburguesas vegetales, rellenos para vegetales horneados.</li>
                        <li><strong>Bebidas y leches vegetales:</strong> leche de quinoa, blends proteicos, smoothies funcionales.</li>
                        <li><strong>Snacks saludables:</strong> quinoa pop (estilo pochoclo gourmet), barritas, granolas, mueslis premium.</li>
                        <li><strong>Cocina deportiva y gimnasio:</strong> menúes proteicos vegetales, marmitas semanales, alimentación post-entreno.</li>
                    </ul>
                    <p>Para reventa al por menor, la quinoa peruana de Grãos S.A. tiene rotación alta en almacenes saludables, dietéticas y minimercados premium.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo cocinar quinoa: la técnica profesional",
                "body": """
                    <p>El error más común con quinoa es cocinarla como arroz blanco. La proporción y el tiempo son distintos:</p>
                    <ol>
                        <li><strong>Enjuagar</strong>: poner la quinoa en un colador fino y enjuagar bajo agua fría 30 segundos para eliminar saponinas residuales.</li>
                        <li><strong>Tostar (opcional pero recomendado)</strong>: en una olla seca, tostar la quinoa 2 minutos a fuego medio. Saca aroma a frutos secos.</li>
                        <li><strong>Cocinar</strong>: agregar 2 partes de agua o caldo por 1 parte de quinoa. Pizca de sal. Llevar a hervor, bajar a fuego mínimo y tapar.</li>
                        <li><strong>Reposar</strong>: cocinar 12-15 minutos hasta que el agua se absorba. Apagar y dejar reposar tapada 5 minutos más.</li>
                        <li><strong>Aflojar con tenedor</strong>: separar los granos. Listo para usar caliente o fría.</li>
                    </ol>
                    <p>1 taza de quinoa cruda rinde aproximadamente 3 tazas cocinada (rinde más que el arroz blanco).</p>
                """,
                "howto": {
                    "name": "Cómo cocinar quinoa perfecta",
                    "total_time": "PT20M",
                    "steps": [
                        {"name": "Enjuagar", "text": "Coloque 1 taza de quinoa en colador fino y enjuague con agua fría durante 30 segundos."},
                        {"name": "Tostar opcional", "text": "Tueste la quinoa en olla seca 2 minutos a fuego medio para realzar el aroma."},
                        {"name": "Cocinar", "text": "Agregue 2 tazas de agua y una pizca de sal. Lleve a hervor, baje el fuego al mínimo y tape."},
                        {"name": "Reposar", "text": "Cocine 12-15 minutos hasta absorber el agua. Apague y deje reposar tapada 5 minutos."},
                        {"name": "Servir", "text": "Afloje los granos con un tenedor y sirva caliente o use frío en ensaladas."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Quinoa peruana real (blanca) en grano para industria, gastronomía y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 5 kg</strong> — para restaurantes, dietéticas y reventa premium.</li>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial para fábricas y producción.</li>
                    </ul>
                    <p>Importación directa de Perú, libre de gluten certificado bajo pedido, calidad estable lote a lote.</p>
                    <p class="cta-inline"><a href="/producto/quinoa-en-grano" class="btn-link">Ver ficha del producto →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿La quinoa es un cereal?",
                "a": "No. Es un pseudocereal: pariente de la espinaca y la remolacha. Se consume como grano pero su botánica es distinta de los cereales clásicos (trigo, maíz, arroz).",
            },
            {
                "q": "¿La quinoa contiene gluten?",
                "a": "No, es naturalmente sin gluten. Para uso en productos certificados aptos para celíacos se requiere análisis de contaminación cruzada del lote específico.",
            },
            {
                "q": "¿Por qué hay que enjuagarla antes de cocinar?",
                "a": "Para eliminar saponinas residuales —compuestos amargos en la cáscara—. La quinoa moderna viene perlada (saponinas removidas), pero un enjuague rápido garantiza sabor neutro.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de quinoa cruda cocinada?",
                "a": "Aproximadamente 3 kg de quinoa cocida, equivalente a 12-15 porciones de bowl. Rendimiento mayor que el arroz blanco.",
            },
            {
                "q": "¿Es realmente proteína completa?",
                "a": "Sí. Contiene los 9 aminoácidos esenciales en proporciones útiles, incluido lisina, lo que es raro en proteínas vegetales.",
            },
            {
                "q": "¿Conviene quinoa blanca, roja o negra?",
                "a": "Para uso general, blanca (real) por sabor neutro y textura suave. Roja para ensaladas frías por firmeza. Negra para presentación gourmet por color y textura más rústica.",
            },
        ],
        "related_slugs": ["chia-en-semillas", "linaza-dorada", "trigo-sarraceno-mourisco", "harina-de-arroz-integral"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 7. CHÍA EN SEMILLAS
    # ═════════════════════════════════════════════════════════════════
    "chia-en-semillas": {
        "product_slug": "chia-en-semillas",
        "title": "Chía en Semillas: la semilla maya que se volvió superalimento global y pilar de la góndola saludable",
        "dek": "Salvia hispanica, omega-3 vegetal, fibra soluble, proteína completa. Cómo se usa en industria, panificación funcional y consumo doméstico.",
        "meta_title": "Chía en Semillas — Guía Mayorista | Grãos S.A.",
        "meta_description": "Chía en semillas al por mayor en Paraguay para industria, panificación funcional, restaurantes y reventa. Importación directa, calidad premium.",
        "category": "Semillas y Granos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "earth",
        "intro": """
            <p class="lead">La <strong>chía</strong> (<em>Salvia hispanica</em>) era alimento básico de los aztecas y mayas. Hoy es uno de los superalimentos más vendidos del mundo, presente en panes, yogures, geles deportivos, pudines, smoothies y barras energéticas. Su atributo más buscado: la mayor concentración de <strong>omega-3 vegetal</strong> de cualquier semilla, junto con un perfil único de fibra que forma gel al hidratarse.</p>
            <p>En Grãos S.A. importamos chía en semillas con calidad estable y origen confiable. Esta guía es para fábricas de panificación funcional, productos sin gluten, herboristerías, restaurantes saludables y consumidores que quieren aprovechar al máximo la chía.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es la chía y de dónde viene?",
                "body": """
                    <p>La <strong>chía</strong> es la semilla de <em>Salvia hispanica</em>, planta de la familia <em>Lamiaceae</em>, originaria del centro de México y Guatemala. Cultivada desde hace más de 3.500 años por mayas y aztecas como alimento de guerreros y mensajeros por su densidad energética.</p>
                    <p>Hoy los principales orígenes comerciales son México, Bolivia, Paraguay, Argentina y Australia. Hay dos variedades:</p>
                    <ul>
                        <li><strong>Chía negra</strong>: la más común, con cáscara oscura veteada.</li>
                        <li><strong>Chía blanca</strong>: variedad premium, color claro, perfil nutricional similar pero con presentación más limpia en productos donde el color importa.</li>
                    </ul>
                    <p>Perfil nutricional por 100 g:</p>
                    <ul>
                        <li><strong>17 g de proteína</strong> con perfil aminoacídico completo.</li>
                        <li><strong>34 g de fibra</strong> (más que cualquier otra semilla común).</li>
                        <li><strong>17 g de omega-3 (ALA)</strong>, la fuente vegetal más densa.</li>
                        <li>Calcio, hierro, magnesio en cantidades relevantes.</li>
                    </ul>
                """,
            },
            {
                "id": "beneficios",
                "heading": "El gel de chía: por qué es único",
                "body": """
                    <p>El atributo más distintivo de la chía es su capacidad de <strong>formar gel</strong>: 1 cucharada de chía en agua absorbe hasta 12 veces su peso en líquido y forma una textura mucilaginosa única. Eso explica varias propiedades funcionales:</p>
                    <ul>
                        <li><strong>Saciedad prolongada</strong>: el gel ralentiza el vaciado gástrico, favorable para dietas de control de peso.</li>
                        <li><strong>Tránsito intestinal</strong>: la fibra soluble actúa como prebiótico y regulador.</li>
                        <li><strong>Hidratación deportiva</strong>: la chía retiene electrolitos disueltos; usada en geles y bebidas para deportes de resistencia.</li>
                        <li><strong>Sustituto de huevo en repostería vegana</strong>: 1 cda de chía + 3 cdas de agua = "huevo de chía" para masas.</li>
                    </ul>
                    <p>Este perfil hace de la chía un ingrediente "navaja suiza" en la industria saludable: aporta omega-3, fibra, proteína y propiedades funcionales (gelificante, espesante, emulsificante) en un solo ingrediente.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en industria y consumo profesional",
                "body": """
                    <p>La chía es un commodity premium en categorías saludables:</p>
                    <ul>
                        <li><strong>Panificación funcional</strong>: panes con chía, panes sin gluten (la chía aporta estructura), galletitas integrales premium.</li>
                        <li><strong>Yogures, pudines y postres</strong>: chía pudding RTD, yogures funcionales, mousses sin gelatina animal.</li>
                        <li><strong>Bebidas funcionales y deportivas</strong>: aguas de chía con limón, geles para corredores, isotónicos artesanales.</li>
                        <li><strong>Barras energéticas y granolas premium</strong>: combina con frutos secos, frutas deshidratadas y miel.</li>
                        <li><strong>Productos sin gluten</strong>: aporta estructura, omega-3 y posicionamiento clean-label en panes y pastas celíacas.</li>
                        <li><strong>Repostería vegana</strong>: huevo de chía como sustituto natural en bizcochos, panqueques y galletitas.</li>
                    </ul>
                    <p>Para reventa, la chía es uno de los productos más vendidos en dietéticas y minimercados saludables. La rotación es alta y el ticket promedio es bueno.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo preparar pudín de chía y agua de chía",
                "body": """
                    <p>Las dos preparaciones más populares aprovechan la capacidad gelificante de la chía:</p>
                    <ol>
                        <li><strong>Pudín de chía clásico</strong>: 3 cdas de chía + 250 ml de leche vegetal o entera + 1 cdta de miel. Mezclar bien, refrigerar mínimo 4 horas (idealmente toda la noche). Servir frío con frutas frescas.</li>
                        <li><strong>Agua de chía con limón</strong>: 1 cda de chía + 250 ml de agua + jugo de medio limón. Reposar 15 minutos. Bebida hidratante baja en calorías.</li>
                        <li><strong>Huevo de chía (vegano)</strong>: 1 cda de chía + 3 cdas de agua. Reposar 10 minutos. Sustituye 1 huevo en panificación.</li>
                    </ol>
                    <p>La chía siempre debe consumirse hidratada o pre-mojada para mejor digestión y absorción de nutrientes.</p>
                """,
                "howto": {
                    "name": "Cómo preparar pudín de chía",
                    "total_time": "PT4H10M",
                    "steps": [
                        {"name": "Mezclar ingredientes", "text": "Mezcle 3 cdas de chía con 250 ml de leche y 1 cdta de miel en un frasco hermético."},
                        {"name": "Mezclar bien", "text": "Revuelva con cuchara durante 30 segundos para evitar grumos. Vuelva a revolver a los 5 minutos."},
                        {"name": "Refrigerar", "text": "Tape y refrigere mínimo 4 horas o idealmente toda la noche."},
                        {"name": "Servir", "text": "Sirva frío con frutas frescas, frutos secos picados o granola."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Chía en semillas para industria, restaurantes y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 5 kg</strong> — para dietéticas, restaurantes y reventa.</li>
                        <li><strong>Bolsa 25 kg</strong> — para fábricas de panificación, barras y bebidas.</li>
                    </ul>
                    <p>Importación directa, calidad estable, certificado de origen.</p>
                    <p class="cta-inline"><a href="/producto/chia-en-semillas" class="btn-link">Ver ficha del producto →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿La chía blanca es mejor que la negra?",
                "a": "Nutricionalmente son prácticamente equivalentes. La diferencia está en presentación: la blanca es preferida en productos donde el color de la chía no debe contrastar (yogurt blanco, postres claros). La negra es estándar para uso general.",
            },
            {
                "q": "¿Cuánto omega-3 aporta la chía vs el pescado?",
                "a": "La chía tiene 17 g de ALA (omega-3 vegetal) por 100 g; el pescado azul tiene 1-3 g de EPA/DHA por 100 g. Son tipos distintos: el ALA debe ser convertido por el cuerpo en EPA/DHA, conversión limitada (5-10 %). La chía es excelente para no-pesetarianos pero no reemplaza pescado.",
            },
            {
                "q": "¿Hay que moler la chía para mejor absorción?",
                "a": "La chía hidratada (en gel) se digiere y absorbe bien sin moler. La chía seca consumida sin hidratar puede pasar entera por el tubo digestivo. Recomendación: siempre hidratar antes de consumir.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de chía en producción de pudín?",
                "a": "Aproximadamente 100 porciones de pudín individual (10 g por porción). En panificación rinde 200 panes funcionales pequeños (5 g por unidad).",
            },
            {
                "q": "¿La chía tiene gluten?",
                "a": "No. Es naturalmente libre de gluten. Para certificación apta celíacos, requiere análisis de contaminación cruzada por lote.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y oscuro. La chía es estable: bien almacenada conserva calidad por 2-3 años por su contenido natural de antioxidantes.",
            },
        ],
        "related_slugs": ["linaza-dorada", "quinoa-en-grano", "semilla-de-girasol-sin-sal", "spirulina-en-polvo"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 8. CACAO ALCALINO EN POLVO
    # ═════════════════════════════════════════════════════════════════
    "cacao-alcalino-en-polvo": {
        "product_slug": "cacao-alcalino-en-polvo",
        "title": "Cacao Alcalino en Polvo: el cacao holandés que transformó la repostería industrial moderna",
        "dek": "Theobroma cacao tratado con álcali para neutralizar acidez. Color más oscuro, sabor más suave, dispersión perfecta en lácteos. La elección de las grandes panificadoras.",
        "meta_title": "Cacao Alcalino en Polvo — Mayorista | Grãos S.A.",
        "meta_description": "Cacao alcalino en polvo al por mayor en Paraguay: panificación industrial, helados, bebidas chocolatadas, repostería profesional. Calidad importada premium.",
        "category": "Cacao",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">Cuando una galletita comercial tiene ese color marrón profundo casi negro, ese sabor a chocolate maduro sin acidez áspera, y se mezcla con leche sin grumos ni separación... está usando <strong>cacao alcalino</strong>, también llamado <strong>cacao holandés</strong> o <strong>dutch cocoa</strong>. Es el estándar global de la industria moderna de panificación, helados y bebidas chocolatadas.</p>
            <p>En Grãos S.A. importamos cacao alcalino premium, ideal para fábricas, panificadoras industriales, heladerías y reposterías profesionales que necesitan color, sabor y dispersión consistente lote a lote.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es el cacao alcalino y por qué es distinto?",
                "body": """
                    <p>El <strong>cacao alcalino</strong> (también <strong>cacao holandés</strong> o <strong>cacao alcalinizado</strong>) es cacao en polvo natural tratado con una solución alcalina suave (típicamente carbonato de potasio o de sodio) durante el procesamiento. Este tratamiento, inventado en Países Bajos en el siglo XIX por van Houten, neutraliza parte de la acidez natural del cacao y modifica varias propiedades:</p>
                    <ul>
                        <li><strong>Color más oscuro</strong>: pasa del marrón rojizo natural a marrón profundo, casi negro.</li>
                        <li><strong>Sabor más suave</strong>: menos amargor, menos acidez, perfil más redondo de chocolate.</li>
                        <li><strong>Mejor dispersión</strong> en líquidos, especialmente lácteos: no flota ni hace grumos como el cacao natural.</li>
                        <li><strong>pH más alto</strong> (7.0-8.0 vs 5.5-6.0 del natural): cambia cómo reacciona con leudantes en panificación.</li>
                    </ul>
                    <p>Esta combinación lo hace el cacao preferido para industria. El cacao natural se usa más en repostería casera donde se busca sabor más complejo y reacción con bicarbonato.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos para industria, panificación y heladería",
                "body": """
                    <p>El cacao alcalino es el caballo de batalla de la repostería industrial:</p>
                    <ul>
                        <li><strong>Panificación industrial</strong>: galletitas tipo Oreo, brownies, bizcochos chocolatados, panettones de chocolate, alfajores rellenos.</li>
                        <li><strong>Heladería</strong>: helados de chocolate, paletas, cremas heladas. Su color profundo y dispersión perfecta lo hacen insustituible.</li>
                        <li><strong>Bebidas chocolatadas RTD</strong>: leches chocolatadas industriales, polvos solubles tipo "chocolatada para tomar", capuccinos saborizados.</li>
                        <li><strong>Coberturas y rellenos</strong>: ganaches industriales, rellenos de bombones, baños para galletitas.</li>
                        <li><strong>Productos secos solubles</strong>: mezclas para batidos, polvos proteicos sabor chocolate, bebidas instantáneas.</li>
                        <li><strong>Repostería profesional</strong>: tortas multicapas, mousses, postres premium en pastelerías y restaurantes.</li>
                    </ul>
                    <p>Para fábricas con producción mensual significativa, el cacao alcalino de Grãos S.A. ofrece estabilidad de color y sabor lote a lote, fundamental cuando el chocolate es parte de la identidad del producto.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar con cacao alcalino: 3 reglas profesionales",
                "body": """
                    <p>Tres puntos críticos que diferencian el uso del cacao alcalino del natural:</p>
                    <ol>
                        <li><strong>Sustitución directa por cacao natural NO funciona en recetas que dependen del bicarbonato</strong>. El cacao natural es ácido y reacciona con bicarbonato; el alcalino no. Si reemplaza, ajuste el polvo de hornear o use ambos leudantes.</li>
                        <li><strong>Tamizar antes de mezclar</strong>: el cacao alcalino tiene tendencia a apelmazarse. Tamizar dos veces antes de incorporar a masas asegura textura uniforme y color homogéneo.</li>
                        <li><strong>Disolver en líquido caliente para máxima dispersión</strong>: en bebidas, mezclar primero el cacao con un poco de líquido caliente formando una pasta, después incorporar al resto. Evita grumos.</li>
                    </ol>
                    <p>Receta clásica para chocolate caliente industrial: 25 g de cacao alcalino + 200 ml de leche entera + 1 cdta de azúcar mascabo + pizca de sal. Calentar a 80 °C, batir, servir.</p>
                """,
                "howto": {
                    "name": "Cómo preparar chocolate caliente con cacao alcalino",
                    "total_time": "PT8M",
                    "steps": [
                        {"name": "Tamizar cacao", "text": "Tamice 25 g de cacao alcalino para evitar grumos."},
                        {"name": "Hacer pasta", "text": "Mezcle el cacao con 30 ml de leche tibia formando una pasta lisa."},
                        {"name": "Calentar leche", "text": "Caliente 170 ml de leche con 1 cdta de azúcar a 80 °C."},
                        {"name": "Combinar", "text": "Incorpore la pasta de cacao a la leche caliente batiendo hasta homogeneizar."},
                        {"name": "Servir", "text": "Agregue una pizca de sal para realzar el chocolate y sirva caliente."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles para industria",
                "body": """
                    <p>Cacao alcalino en polvo importado para fábricas, heladerías y repostería profesional:</p>
                    <ul>
                        <li><strong>Bolsa 5 kg</strong> — para reposterías, heladerías artesanales y restaurantes.</li>
                        <li><strong>Bolsa 25 kg</strong> — para fábricas de panificación, bebidas y heladerías industriales.</li>
                    </ul>
                    <p>Calidad estable lote a lote, color y dispersión consistentes. Importación directa, factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/cacao-alcalino-en-polvo" class="btn-link">Ver ficha del producto →</a> · <a href="/producto/cacao-en-polvo-black" class="btn-link">Cacao black →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Cuál es la diferencia entre cacao natural y cacao alcalino?",
                "a": "El alcalino es tratado con álcali durante el procesamiento, lo que reduce acidez, oscurece el color, suaviza el sabor y mejora dispersión en líquidos. El natural conserva sabor más complejo y mayor acidez, ideal para panificación con bicarbonato.",
            },
            {
                "q": "¿Por qué se llama cacao holandés?",
                "a": "Porque el proceso de alcalinización fue inventado en Holanda en 1828 por Coenraad van Houten. El nombre 'dutch cocoa' o 'cacao holandés' se mantiene comercialmente hasta hoy.",
            },
            {
                "q": "¿Pierde antioxidantes con la alcalinización?",
                "a": "Sí, parcialmente. Reduce el contenido de flavonoides comparado con cacao natural. Para uso industrial donde sabor y color importan más que perfil antioxidante, sigue siendo la mejor opción.",
            },
            {
                "q": "¿Puedo sustituir cacao alcalino por natural en cualquier receta?",
                "a": "No directamente. Las recetas que usan bicarbonato dependen de la acidez del cacao natural para leudar. Si sustituye por alcalino, debe ajustar agentes leudantes. En recetas que ya usan polvo de hornear (no bicarbonato puro), la sustitución es más simple.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de cacao alcalino en producción?",
                "a": "En bebidas chocolatadas, rinde aproximadamente 40 litros (25 g por 250 ml). En panificación, rinde 50-100 productos según el peso por unidad.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y fresco. Bien guardado conserva calidad 18-24 meses. La humedad es el principal enemigo: forma grumos irreversibles.",
            },
        ],
        "related_slugs": ["cacao-en-polvo-black", "nibs-de-cacao", "harina-de-coco", "azucar-de-coco"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 9. ANIS ESTRELLADO
    # ═════════════════════════════════════════════════════════════════
    "anis-estrellado": {
        "product_slug": "anis-estrellado",
        "title": "Anís Estrellado: la especia con forma de estrella que da carácter a panificación, licorería y cocina paraguaya",
        "dek": "Illicium verum, aroma intenso de anetol, presentación icónica. Cómo se usa en industria, repostería tradicional y bebidas premium.",
        "meta_title": "Anís Estrellado — Guía Mayorista | Grãos S.A.",
        "meta_description": "Anís estrellado al por mayor en Paraguay: panificación, licorería artesanal, infusiones, cocina tradicional. Importación directa de Vietnam, calidad premium.",
        "category": "Especias y Condimentos",
        "reading_time": 6,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">El <strong>anís estrellado</strong> es probablemente la especia más fotogénica del mundo: ocho puntas rojizas que parecen estrellas de mar talladas en madera. Pero más allá de la presentación, es uno de los aromas más distintivos de la repostería tradicional, la licorería artesanal y la cocina festiva paraguaya.</p>
            <p>En Grãos S.A. importamos anís estrellado entero de Vietnam, origen mundial referente, seleccionado por intensidad de aroma y limpieza visual. Esta guía es para panificadoras, fábricas de licores y bitters, restaurantes y consumidores que quieren entender cómo aprovechar esta especia única.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es el anís estrellado?",
                "body": """
                    <p>El <strong>anís estrellado</strong> (<em>Illicium verum</em>, también llamado <strong>badiana</strong> o <strong>star anise</strong>) es el fruto seco de un árbol pequeño originario del sudeste de China y Vietnam. Pese al nombre, no está botánicamente relacionado con el <strong>anís verde</strong> (<em>Pimpinella anisum</em>), pero comparte el compuesto aromático principal: el <strong>anetol</strong>, que da el sabor dulce y licoroso característico.</p>
                    <p>El fruto se cosecha cuando aún está verde, se seca al sol y adquiere el color rojizo profundo y la forma de estrella icónica. Se usa entero (estándar profesional) o molido. La forma entera conserva el aroma mucho más tiempo y permite uso decorativo en platos y bebidas.</p>
                    <p>Origen comercial dominante: Vietnam (60 % de la producción mundial), China (30 %), India y Filipinas.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en industria, licorería y cocina",
                "body": """
                    <p>El anís estrellado es uno de los ingredientes con más versatilidad cruzada (dulce y salado):</p>
                    <ul>
                        <li><strong>Panificación tradicional paraguaya</strong>: chipa cuatro quesos con anís, sopa paraguaya, mbeyú, biscochitos festivos.</li>
                        <li><strong>Repostería europea y latinoamericana</strong>: panettones, panetones, alfajores especiados, galletitas navideñas.</li>
                        <li><strong>Licorería artesanal</strong>: anisados, pastis, ouzo, sambuca, bitters de autor, gin de firma.</li>
                        <li><strong>Cocina asiática</strong>: pho vietnamita, brasas chinas (cinco especias), curries indios, marinados de cerdo.</li>
                        <li><strong>Conservas y curtidos</strong>: pepinillos especiados, frutas en almíbar, mermeladas con notas anisadas.</li>
                        <li><strong>Tisanas y bebidas calientes</strong>: chai latte tradicional, infusiones digestivas, vino caliente especiado.</li>
                    </ul>
                    <p>Para fábricas y restaurantes, el formato entero es siempre superior porque permite infusión limpia (se retira fácil al final) y conserva intensidad durante toda la cocción.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo usar anís estrellado: técnicas profesionales",
                "body": """
                    <p>El anís estrellado libera mejor su aroma con <strong>calor sostenido o infusión prolongada</strong>:</p>
                    <ol>
                        <li><strong>Infusión líquida (chai, vino caliente, jarabes)</strong>: 1 estrella entera por cada 500 ml de líquido. Calor bajo durante 10-15 minutos.</li>
                        <li><strong>Cocción larga (caldos pho, curries, marinados)</strong>: agregar 2-3 estrellas al inicio de la cocción y retirar al final. Aporta profundidad sin amargar.</li>
                        <li><strong>Repostería</strong>: 1-2 estrellas trituradas (no en polvo fino) por cada kilo de masa. Evitar moler en polvo industrial salvo para producción a gran escala.</li>
                        <li><strong>Licorería</strong>: maceración en alcohol neutro durante 2-4 semanas, 5 estrellas por litro. Perfil licoroso clásico.</li>
                    </ol>
                """,
                "howto": {
                    "name": "Cómo preparar chai latte con anís estrellado",
                    "total_time": "PT15M",
                    "steps": [
                        {"name": "Reunir especias", "text": "Disponga 1 anís estrellado, 1 rama de canela 6 cm, 4 vainas de cardamomo, 4 clavos."},
                        {"name": "Infusionar especias", "text": "Caliente 250 ml de agua con las especias durante 8 minutos a fuego bajo."},
                        {"name": "Agregar té y leche", "text": "Añada 1 bolsita de té negro y 250 ml de leche caliente. Reposo 4 minutos."},
                        {"name": "Endulzar y colar", "text": "Endulce con 2 cdtas de azúcar mascabo, cuele las especias y sirva."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Anís estrellado entero importado de Vietnam:</p>
                    <ul>
                        <li><strong>Caja 10 kg</strong> — formato estándar para panificación, restaurantes y licorerías.</li>
                    </ul>
                    <p>Calidad premium, intensidad aromática alta, presentación visual limpia. Certificado de origen, factura legal, entrega a todo el Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/anis-estrellado" class="btn-link">Ver ficha del producto →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Anís estrellado y anís verde son lo mismo?",
                "a": "No. Son plantas distintas (Illicium verum vs Pimpinella anisum) sin relación botánica directa, aunque comparten el compuesto aromático anetol. El estrellado es más intenso y picante; el verde es más dulce y suave.",
            },
            {
                "q": "¿Por qué se llama así si tiene 8 puntas?",
                "a": "Por la forma de estrella del fruto seco. Cada punta es un folículo que contiene una semilla. Es la única especia que se usa por la forma del fruto entero.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de anís estrellado en panificación?",
                "a": "Aproximadamente 500 estrellas por kilo. En producción de panificados especiados, rinde unas 200 unidades grandes (panettones, alfajores festivos) o 1.000 unidades pequeñas.",
            },
            {
                "q": "¿Sirve para hacer licor casero?",
                "a": "Sí, es la base de prácticamente todos los anisados clásicos (pastis, anisette, ouzo). Maceración en alcohol neutro 2-4 semanas con 5 estrellas por litro.",
            },
            {
                "q": "¿Cuál es la diferencia entre anís estrellado vietnamita y chino?",
                "a": "Calidad similar; el vietnamita tiende a tener color más vivo y aroma más limpio por estándares de cosecha y secado. Es el origen preferido por la industria premium.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y oscuro. Entero conserva aroma 24+ meses; molido se degrada rápidamente, perdiendo 40 % de aroma en 3-4 meses.",
            },
        ],
        "related_slugs": ["canela-en-rama-6cm", "clavo-de-olor", "cardamomo-en-grano", "semilla-de-anis"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 10. CLAVO DE OLOR
    # ═════════════════════════════════════════════════════════════════
    "clavo-de-olor": {
        "product_slug": "clavo-de-olor",
        "title": "Clavo de Olor: el botón aromático que define embutidos, vinos calientes y repostería tradicional",
        "dek": "Syzygium aromaticum, eugenol concentrado, intensidad aromática insuperable. Por qué pequeñas cantidades cambian todo en industria y cocina profesional.",
        "meta_title": "Clavo de Olor — Guía Mayorista | Grãos S.A.",
        "meta_description": "Clavo de olor entero al por mayor en Paraguay para industria de embutidos, panificación, vinos calientes, conservas. Importación directa de Brasil.",
        "category": "Especias y Condimentos",
        "reading_time": 6,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">El <strong>clavo de olor</strong> es probablemente la especia con mayor concentración aromática del planeta. Una sola unidad de clavo seco contiene tanto aceite esencial volátil que se puede oler a un metro de distancia. Esto lo hace una de las especias más estratégicas de la industria alimentaria: <strong>se usa poco pero define todo</strong>.</p>
            <p>En Grãos S.A. importamos clavo de olor entero de Brasil, uno de los principales orígenes mundiales junto con Indonesia y Madagascar. Esta guía es para industria de embutidos, panificadoras, fábricas de licorería, productores de conservas, y restaurantes profesionales.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es el clavo de olor?",
                "body": """
                    <p>El <strong>clavo de olor</strong> (<em>Syzygium aromaticum</em>, también <strong>cravo da Índia</strong> en portugués o <strong>cloves</strong> en inglés) es el botón floral seco de un árbol perenne nativo de las Islas Molucas (Indonesia). Hoy se cultiva comercialmente en Indonesia, Madagascar, Brasil, Tanzania y Sri Lanka.</p>
                    <p>Lo que lo hace único es la concentración de <strong>eugenol</strong>, compuesto aromático que constituye 70-90 % del aceite esencial. El eugenol explica el aroma intenso, el sabor picante-dulce característico y la actividad antimicrobiana natural.</p>
                    <p>Se vende en dos formatos:</p>
                    <ul>
                        <li><strong>Entero</strong>: estándar profesional. Conserva intensidad durante años.</li>
                        <li><strong>Molido</strong>: práctico para industria con producción a gran escala, pero pierde aroma rápido (60-90 días).</li>
                    </ul>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos para industria, embutidos y panificación",
                "body": """
                    <p>El clavo es estratégico en muchas categorías:</p>
                    <ul>
                        <li><strong>Industria de embutidos</strong>: jamones especiados, salames italianos, mortadelas, chacinas tradicionales paraguayas. Mejora sabor y aporta capacidad antimicrobiana natural (conservante secundario).</li>
                        <li><strong>Conservas y curtidos</strong>: pepinillos en vinagre, frutas en almíbar, chutneys, mermeladas especiadas.</li>
                        <li><strong>Panificación tradicional</strong>: panettones, hot cross buns, pan de jengibre, alfajores festivos, biscochitos navideños.</li>
                        <li><strong>Vinos calientes y bebidas festivas</strong>: glühwein, vino caliente paraguayo, sidra especiada, chai masala.</li>
                        <li><strong>Licorería artesanal</strong>: bitters de autor, gin de firma, vermut artesanal, licores especiados.</li>
                        <li><strong>Cocina latinoamericana</strong>: mole mexicano, escabeches argentinos, locro especiado, asados tradicionales.</li>
                        <li><strong>Cocina asiática</strong>: cinco especias chino, biryani indio, pho vietnamita, garam masala.</li>
                    </ul>
                    <p>Característica industrial clave: el clavo tiene <strong>capacidad antimicrobiana natural</strong> reconocida. Por eso aparece en chacinas, conservas y embutidos curados desde hace siglos: mejora el perfil aromático y extiende vida útil natural.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo usar clavo: dosis y técnicas",
                "body": """
                    <p>La regla de oro: <strong>poco va lejos</strong>. Un exceso de clavo arruina cualquier preparación con un sabor medicinal-quemado. Dosis profesionales:</p>
                    <ul>
                        <li><strong>Vino caliente / glühwein</strong>: 6-8 clavos enteros por litro de vino tinto.</li>
                        <li><strong>Embutidos artesanales</strong>: 0,3-0,5 g de clavo molido por kilo de carne (entre 6-10 unidades enteras molidas).</li>
                        <li><strong>Panificación festiva</strong>: 0,5-1 g de clavo molido por kilo de masa.</li>
                        <li><strong>Conservas dulces</strong>: 4-6 clavos enteros por litro de almíbar.</li>
                        <li><strong>Curtidos</strong>: 8-12 clavos enteros por litro de salmuera.</li>
                    </ul>
                    <p>Tip profesional: para vino caliente o jarabes, los clavos enteros se retiran antes de servir. En embutidos y panificación, se prefiere clavo recién molido para máxima dispersión aromática.</p>
                """,
                "howto": {
                    "name": "Cómo preparar vino caliente con clavo",
                    "total_time": "PT20M",
                    "steps": [
                        {"name": "Reunir especias", "text": "Disponga 6 clavos, 2 ramas de canela, 1 anís estrellado, cáscara de naranja, 2 cdas de azúcar."},
                        {"name": "Calentar vino", "text": "Caliente 1 litro de vino tinto a fuego mínimo en olla, sin dejar hervir."},
                        {"name": "Infusionar", "text": "Agregue las especias y la cáscara de naranja. Mantenga 15 minutos a 70-80 °C."},
                        {"name": "Endulzar y servir", "text": "Incorpore el azúcar, retire las especias y sirva caliente en taza precalentada."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Clavo de olor entero importado de Brasil:</p>
                    <ul>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial para fábricas de embutidos, panificación y conservas.</li>
                    </ul>
                    <p>Calidad premium, alta concentración de eugenol, certificado de origen. Importación directa, factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/clavo-de-olor" class="btn-link">Ver ficha del producto →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Por qué el clavo es tan intenso comparado con otras especias?",
                "a": "Por su altísima concentración de eugenol (70-90 % del aceite esencial). El clavo tiene aproximadamente 3-4 veces más aceite esencial que la canela y 6-8 veces más que la pimienta negra.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de clavo en producción industrial?",
                "a": "Depende de la categoría: en embutidos rinde 2.000-3.000 kg de carne especiada (0,3-0,5 g/kg). En vino caliente, 200 litros (5 g por litro). En panificación, 1.000-2.000 productos festivos.",
            },
            {
                "q": "¿Cuál es la diferencia entre clavo brasileño y de Madagascar?",
                "a": "El brasileño tiende a tener color más oscuro y eugenol más alto; el de Madagascar es más balanceado y delicado. Ambos son premium; la elección depende de la aplicación específica.",
            },
            {
                "q": "¿Tiene propiedades medicinales reconocidas?",
                "a": "El eugenol tiene actividad antimicrobiana, antioxidante y analgésica documentada. En odontología se usa históricamente como anestésico tópico. Para uso en alimentos rige el principio dietético, no farmacológico.",
            },
            {
                "q": "¿Conviene comprar entero o molido?",
                "a": "Para industria con producción a gran escala donde la rotación es rápida, ambos formatos sirven. Para uso prolongado o conservación, siempre entero: conserva aroma años, mientras que molido pierde 40 % en 90 días.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y oscuro. Entero estable 3-5 años; molido idealmente consumido en 90 días desde apertura.",
            },
        ],
        "related_slugs": ["canela-en-rama-6cm", "anis-estrellado", "nuez-moscada-entera", "cardamomo-en-grano"],
    },
}


def get_guide(slug: str) -> dict | None:
    """Return the guide dict for a slug or None if not curated."""
    return GUIDES.get(slug)


def list_guides() -> list[dict]:
    """Return a summary list of all guides — used by the index page.

    The summary includes only the metadata needed for cards: title, dek,
    slug, product_slug, category, reading_time. The full body is loaded
    only on the detail page to keep the index render light.
    """
    return [
        {
            "slug": slug,
            "product_slug": g["product_slug"],
            "title": g["title"],
            "dek": g["dek"],
            "category": g["category"],
            "reading_time": g["reading_time"],
            "published": g["published"],
            "hero_treatment": g.get("hero_treatment", "warm"),
        }
        for slug, g in GUIDES.items()
    ]
