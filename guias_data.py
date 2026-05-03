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
        "meta_title": "Manzanilla en Flor — Guía Completa | Especias del Paraguay",
        "meta_description": "Todo sobre la manzanilla en flor: beneficios, usos, cómo preparar el té perfecto y dónde comprar manzanilla al por mayor en Paraguay con importación directa.",
        "category": "Hierbas y Tés",
        "reading_time": 8,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",  # CSS theme variant
        "intro": """
            <p class="lead">La <strong>manzanilla</strong> es probablemente la hierba más buscada del Paraguay. Aparece en la cocina de la abuela, en la farmacia, en la barra del bar antes de un cocido digestivo y en la línea de producción de bebidas, cosméticos y suplementos. Pero no toda manzanilla es igual.</p>
            <p>En Especias del Paraguay importamos <em>Matricaria chamomilla</em> en flor entera —no triturada, no en bolsitas, no mezclada con tallos— porque sabemos que la diferencia se siente en el aroma y se mide en el rendimiento por kilo. Esta guía es para los tres tipos de cliente que llegan acá: la familia que quiere preparar el mejor té de manzanilla en casa, la fábrica que necesita un proveedor estable de manzanilla al por mayor, y el restaurante o herboristería que vive de la calidad del insumo.</p>
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
                    <p>En todos los casos, la <strong>flor entera</strong> permite trazabilidad visual de calidad —un comprador entrenado puede juzgar el lote a simple vista— y rinde más por kilo que la versión triturada, porque hay menos relleno de tallo y polvo. Para fábricas que dan tickets fiscales y necesitan certificado de origen, Especias del Paraguay importa con documentación completa.</p>
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
                    <p>Especias del Paraguay trabaja con fábricas, distribuidoras, herboristerías, restaurantes y minimercados en todo el Paraguay. La manzanilla flor entera está disponible en:</p>
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
                "a": "Especias del Paraguay importa principalmente de Argentina y Egipto, los dos orígenes más reconocidos por calidad estable. Cada lote viene con certificado de origen y análisis bromatológico básico.",
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
        "meta_title": "Canela en Rama 6 cm — Guía Mayorista | Especias del Paraguay",
        "meta_description": "Todo sobre la canela en rama: variedades, usos, cómo elegirla, cómo preparar y dónde comprar canela al por mayor en Paraguay con importación directa de Vietnam.",
        "category": "Especias y Condimentos",
        "reading_time": 9,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">La <strong>canela en rama</strong> es la especia más universalmente querida del mundo. Está en el chipá guazú de la abuela, en el café latte de la cadena de cafeterías, en la galletita exportada y en la línea de producción de un yogurt funcional. Pero el mercado mayorista paraguayo confunde dos productos muy distintos: la <strong>canela verum</strong> (la fina, de Sri Lanka y Vietnam) y la <strong>canela cassia</strong> (la fuerte, china e indonesia).</p>
            <p>En Especias del Paraguay trabajamos canela en rama de 6 cm originaria de <strong>Vietnam</strong>, un origen que combina aroma intenso, color rojizo profundo y precio competitivo. Esta guía explica las diferencias, los usos industriales y los formatos disponibles para revendedores, panaderías, fábricas de bebidas y restaurantes en Paraguay.</p>
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
                    <p>La canela vietnamita —que es la que Especias del Paraguay importa en formato 6 cm— es <em>Cinnamomum cassia</em> seleccionada por su perfil aromático equilibrado: tiene la potencia de la cassia china con un final más dulce, lo que la hace versátil para repostería, bebidas calientes y aplicaciones industriales.</p>
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
                    <p>Para fábricas que necesitan canela en grandes volúmenes con calidad estable lote a lote, la canela vietnamita 6 cm de Especias del Paraguay ofrece la combinación más buscada: precio competitivo, perfil aromático fuerte y disponibilidad consistente.</p>
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
                    <p>Especias del Paraguay trabaja la canela en rama de 6 cm en formatos pensados para industria, panificación y reventa:</p>
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
        "meta_title": "Cúrcuma en Polvo — Guía Mayorista | Especias del Paraguay",
        "meta_description": "Cúrcuma en polvo importada de India al por mayor en Paraguay. Beneficios, usos industriales, leche dorada, golden latte, suplementos. Calidad estable lote a lote.",
        "category": "Especias y Condimentos",
        "reading_time": 8,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">La <strong>cúrcuma</strong> dejó de ser una especia exótica para convertirse en el ingrediente estrella de la nueva ola de productos saludables: leche dorada, golden lattes, suplementos antiinflamatorios, blends funcionales para superalimentos y curries instantáneos. Lo que era nicho hace diez años hoy es categoría de góndola.</p>
            <p>En Especias del Paraguay importamos <strong>cúrcuma en polvo de India</strong>, el origen mundial por excelencia (también llamada açafrão da terra en portugués o turmeric en inglés). Esta guía es para industria de suplementos, fábricas de bebidas funcionales, restaurantes especializados, herboristerías y consumidores que quieren entender la diferencia entre una cúrcuma estándar y una premium.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es la cúrcuma y por qué India?",
                "body": """
                    <p>La <strong>cúrcuma</strong> (<em>Curcuma longa</em>) es un rizoma de la familia <em>Zingiberaceae</em>, pariente cercano del jengibre. Se cosecha, hierve, seca y muele para obtener el polvo amarillo intenso conocido en el mundo entero. India produce el <strong>80 % de la cúrcuma del planeta</strong>, y los estados de Tamil Nadu, Andhra Pradesh y Maharashtra son los polos productivos más importantes.</p>
                    <p>El compuesto activo principal de la cúrcuma es la <strong>curcumina</strong>, un polifenol responsable del color amarillo y de prácticamente todas las propiedades funcionales atribuidas a la especia. El contenido de curcumina varía típicamente entre 2 % y 5 % del peso total. Una cúrcuma premium tiene contenido cercano al 4 %.</p>
                    <p>Otras formas comerciales que circulan en el mercado: cúrcuma molida común, cúrcuma orgánica certificada, extractos estandarizados (95 % curcumina, usados en suplementos), y cúrcuma fermentada. Especias del Paraguay trabaja la versión culinaria estándar de calidad alta, ideal para industria alimentaria y herboristería.</p>
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
                    <p>Para fábricas con producción mensual significativa, la cúrcuma india de Especias del Paraguay ofrece estabilidad de color lote a lote —crítico cuando el amarillo del producto final es parte de la identidad de marca— y precio competitivo en formato granel.</p>
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
                    <p>Especias del Paraguay importa cúrcuma en polvo de India en formatos para industria y reventa:</p>
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
        "meta_title": "Hibisco Flor (Jamaica) — Guía Mayorista | Especias del Paraguay",
        "meta_description": "Hibisco flor importado al por mayor en Paraguay: té de hibisco, flor de jamaica, bebidas funcionales, coctelería. Importación directa con calidad estable.",
        "category": "Hierbas y Tés",
        "reading_time": 8,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "berry",
        "intro": """
            <p class="lead">El <strong>hibisco</strong> —llamado también <strong>flor de jamaica</strong> en gran parte de Latinoamérica— pasó de ser una infusión de abuela a ser el ingrediente estrella de bebidas funcionales, coctelería premium y tés helados artesanales. Su color rubí profundo y su perfil cítrico-floral lo hacen uno de los productos más fotogénicos del mercado, lo que se traduce en demanda constante en redes sociales y góndola.</p>
            <p>En Especias del Paraguay importamos hibisco flor entera (<em>Hibiscus sabdariffa</em>) seleccionado por intensidad de color y limpieza visual, listo para industria de bebidas, herboristerías, bares de coctelería y restaurantes que quieren ofrecer infusiones diferenciadas.</p>
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
        "meta_title": "Spirulina en Polvo — Guía Mayorista | Especias del Paraguay",
        "meta_description": "Spirulina en polvo importada al por mayor en Paraguay para industria de suplementos, bebidas funcionales, smoothies y nutracéuticos. Calidad premium, importación directa.",
        "category": "Suplementos y Superalimentos",
        "reading_time": 8,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "green",
        "intro": """
            <p class="lead">La <strong>spirulina</strong> es probablemente el ingrediente nutracéutico más estudiado del último siglo. La FAO la describió como "el alimento del futuro" en los años 70, y hoy es base de cápsulas, polvos solubles, bebidas funcionales, smoothies y barritas en todo el mundo. En Paraguay, la categoría de superalimentos creció más del 40 % los últimos tres años, y la spirulina es la cabeza de góndola.</p>
            <p>En Especias del Paraguay importamos <strong>spirulina en polvo (Arthrospira platensis)</strong> de calidad premium, con perfil nutricional alto y estable lote a lote. Esta guía es para fábricas de suplementos, formuladores de bebidas funcionales, herboristerías, gimnasios con línea propia de productos, y consumidores que quieren entender qué están comprando.</p>
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
                    <p>Especias del Paraguay importa spirulina en polvo para fábricas, herboristerías y reventa:</p>
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
        "meta_title": "Quinoa en Grano — Guía Mayorista | Especias del Paraguay",
        "meta_description": "Quinoa peruana al por mayor en Paraguay para industria saludable, restaurantes, herboristerías y reventa. Importación directa, calidad estable lote a lote.",
        "category": "Semillas y Granos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "earth",
        "intro": """
            <p class="lead">La <strong>quinoa</strong> es uno de los pocos alimentos de origen vegetal que aporta <strong>proteína completa</strong>: contiene los nueve aminoácidos esenciales en proporciones equilibradas, algo raro fuera del reino animal. Sumá a eso que es naturalmente <strong>libre de gluten</strong>, fácil de digerir y de cocción rápida, y entendés por qué la categoría sin TACC se construyó alrededor de este grano.</p>
            <p>En Especias del Paraguay importamos <strong>quinoa peruana (Chenopodium quinoa)</strong>, el origen referente mundial. Esta guía es para fábricas de productos sin gluten, restaurantes de cocina sana, gimnasios con menú propio y consumidores que quieren entender qué hace especial a este grano andino.</p>
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
                    <p>Perú produce alrededor del 50 % de la quinoa mundial; Bolivia, el segundo origen relevante. Especias del Paraguay importa principalmente quinoa blanca real peruana, el estándar de calidad para industria.</p>
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
                    <p>Para reventa al por menor, la quinoa peruana de Especias del Paraguay tiene rotación alta en almacenes saludables, dietéticas y minimercados premium.</p>
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
        "meta_title": "Chía en Semillas — Guía Mayorista | Especias del Paraguay",
        "meta_description": "Chía en semillas al por mayor en Paraguay para industria, panificación funcional, restaurantes y reventa. Importación directa, calidad premium.",
        "category": "Semillas y Granos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "earth",
        "intro": """
            <p class="lead">La <strong>chía</strong> (<em>Salvia hispanica</em>) era alimento básico de los aztecas y mayas. Hoy es uno de los superalimentos más vendidos del mundo, presente en panes, yogures, geles deportivos, pudines, smoothies y barras energéticas. Su atributo más buscado: la mayor concentración de <strong>omega-3 vegetal</strong> de cualquier semilla, junto con un perfil único de fibra que forma gel al hidratarse.</p>
            <p>En Especias del Paraguay importamos chía en semillas con calidad estable y origen confiable. Esta guía es para fábricas de panificación funcional, productos sin gluten, herboristerías, restaurantes saludables y consumidores que quieren aprovechar al máximo la chía.</p>
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
        "meta_title": "Cacao Alcalino en Polvo — Mayorista | Especias del Paraguay",
        "meta_description": "Cacao alcalino en polvo al por mayor en Paraguay: panificación industrial, helados, bebidas chocolatadas, repostería profesional. Calidad importada premium.",
        "category": "Cacao",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">Cuando una galletita comercial tiene ese color marrón profundo casi negro, ese sabor a chocolate maduro sin acidez áspera, y se mezcla con leche sin grumos ni separación... está usando <strong>cacao alcalino</strong>, también llamado <strong>cacao holandés</strong> o <strong>dutch cocoa</strong>. Es el estándar global de la industria moderna de panificación, helados y bebidas chocolatadas.</p>
            <p>En Especias del Paraguay importamos cacao alcalino premium, ideal para fábricas, panificadoras industriales, heladerías y reposterías profesionales que necesitan color, sabor y dispersión consistente lote a lote.</p>
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
                    <p>Para fábricas con producción mensual significativa, el cacao alcalino de Especias del Paraguay ofrece estabilidad de color y sabor lote a lote, fundamental cuando el chocolate es parte de la identidad del producto.</p>
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
        "meta_title": "Anís Estrellado — Guía Mayorista | Especias del Paraguay",
        "meta_description": "Anís estrellado al por mayor en Paraguay: panificación, licorería artesanal, infusiones, cocina tradicional. Importación directa de Vietnam, calidad premium.",
        "category": "Especias y Condimentos",
        "reading_time": 6,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">El <strong>anís estrellado</strong> es probablemente la especia más fotogénica del mundo: ocho puntas rojizas que parecen estrellas de mar talladas en madera. Pero más allá de la presentación, es uno de los aromas más distintivos de la repostería tradicional, la licorería artesanal y la cocina festiva paraguaya.</p>
            <p>En Especias del Paraguay importamos anís estrellado entero de Vietnam, origen mundial referente, seleccionado por intensidad de aroma y limpieza visual. Esta guía es para panificadoras, fábricas de licores y bitters, restaurantes y consumidores que quieren entender cómo aprovechar esta especia única.</p>
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
        "meta_title": "Clavo de Olor — Guía Mayorista | Especias del Paraguay",
        "meta_description": "Clavo de olor entero al por mayor en Paraguay para industria de embutidos, panificación, vinos calientes, conservas. Importación directa de Brasil.",
        "category": "Especias y Condimentos",
        "reading_time": 6,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">El <strong>clavo de olor</strong> es probablemente la especia con mayor concentración aromática del planeta. Una sola unidad de clavo seco contiene tanto aceite esencial volátil que se puede oler a un metro de distancia. Esto lo hace una de las especias más estratégicas de la industria alimentaria: <strong>se usa poco pero define todo</strong>.</p>
            <p>En Especias del Paraguay importamos clavo de olor entero de Brasil, uno de los principales orígenes mundiales junto con Indonesia y Madagascar. Esta guía es para industria de embutidos, panificadoras, fábricas de licorería, productores de conservas, y restaurantes profesionales.</p>
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

    # ═════════════════════════════════════════════════════════════════
    # 11. COMINO EN GRANO  (cocina paraguaya: chimichurri, asado, locro)
    # ═════════════════════════════════════════════════════════════════
    "comino-en-grano": {
        "product_slug": "comino-en-grano",
        "title": "Comino en Grano: el sabor profundo del asado, el chimichurri y el locro paraguayo",
        "dek": "Cuminum cyminum entero, aroma intenso que solo el grano sin moler conserva. La especia que define la cocina latinoamericana y paraguaya en su versión más auténtica.",
        "meta_title": "Comino en Grano — Guía Mayorista | Especias del Paraguay",
        "meta_description": "Comino en grano al por mayor en Paraguay para industria, asado, chimichurri y embutidos. Importación directa de Egipto. Aroma intenso, calidad estable.",
        "category": "Especias y Condimentos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">Si hay una especia que define la cocina paraguaya y latinoamericana, es el <strong>comino</strong>. Está en el chimichurri del asado del domingo, en el locro de fiesta patria, en el caldo de gallina del invierno, en los embutidos artesanales y en los guisos de carne con mandioca. Pero la mayoría del mercado vende comino molido viejo. La diferencia está en el grano entero.</p>
            <p>En Especias del Paraguay importamos <strong>comino en grano (Cuminum cyminum)</strong> de Egipto, el origen referente mundial, seleccionado por intensidad aromática alta y limpieza visual. Esta guía es para parrilladas, fábricas de chacinas, panificadoras industriales, restaurantes y consumidores que entienden que la diferencia entre un asado bueno y uno excelente está en el comino que usás.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es el comino en grano?",
                "body": """
                    <p>El <strong>comino</strong> (<em>Cuminum cyminum</em>, también <strong>cumin</strong> en inglés o <strong>cominho</strong> en portugués) es la semilla seca de una planta de la familia <em>Apiaceae</em>, parientes de la zanahoria y el perejil. Originaria del Mediterráneo oriental, hoy se cultiva intensivamente en Egipto, India, Irán, Turquía y Siria.</p>
                    <p>El comino en grano es la forma de presentación más profesional. La semilla entera concentra los aceites esenciales —<strong>cuminaldehído</strong> y <strong>p-cimeno</strong>— en proporciones específicas que se liberan cuando el grano se tuesta o se cocina. Comparado con el comino molido, el grano entero conserva su perfil aromático durante 24 a 36 meses; el molido pierde 40-50 % de aroma en 90 días.</p>
                    <p>Origen comercial dominante para Latinoamérica: <strong>Egipto</strong>, por consistencia de tamaño, color y limpieza. Es el comino que vas a encontrar en cualquier carnicería seria del Paraguay.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Beneficios y propiedades",
                "body": """
                    <p>El comino tiene un perfil documentado en uso tradicional y moderno:</p>
                    <ul>
                        <li><strong>Digestivo</strong>: estimula la producción de jugos gástricos. Por eso se usa en cocido digestivo y se agrega a guisos pesados.</li>
                        <li><strong>Carminativo</strong>: reduce gases intestinales. Combina perfecto con legumbres (porotos, lentejas, garbanzos).</li>
                        <li><strong>Aporte de hierro</strong>: una porción de comino tiene cantidades relevantes para industria nutracéutica.</li>
                        <li><strong>Antimicrobiano natural</strong>: contribuye a la conservación de embutidos y chacinas tradicionales.</li>
                        <li><strong>Antioxidante</strong>: capacidad alta por contenido de polifenoles.</li>
                    </ul>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en la cocina paraguaya, asado y industria",
                "body": """
                    <p>El comino en grano es protagonista en categorías que mueven volumen serio en el Paraguay:</p>
                    <ul>
                        <li><strong>Asado y parrilla</strong>: chimichurri tradicional, salmuera para ojo de bife, marinados para vacío y matambre, sal especiada para parrilladas.</li>
                        <li><strong>Industria de chacinas y embutidos</strong>: chorizos paraguayos, salames, morcillas, longanizas. El comino aporta sabor y conservación natural.</li>
                        <li><strong>Cocina paraguaya tradicional</strong>: locro patrio, bori bori, jopará, caldo de gallina campesino, sopa de poroto con mandioca, guisos de carne con verdura.</li>
                        <li><strong>Cocina latinoamericana</strong>: tacos mexicanos, frijoles refritos, picadillo cubano, sazonador de res argentino.</li>
                        <li><strong>Cocina india y árabe</strong>: garam masala, baharat, falafel, kebabs, lentejas a la india.</li>
                        <li><strong>Industria de sazonadores</strong>: blends "para asado", "para carne", "para guiso", mezclas tipo barbecue.</li>
                    </ul>
                    <p>Para fábricas de tempero y chacinas con producción mensual relevante, el comino egipcio en grano de Especias del Paraguay ofrece estabilidad lote a lote y la posibilidad de moler en planta lo más cerca posible de la producción para máximo aroma.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo usar comino en grano: técnicas profesionales",
                "body": """
                    <p>La regla número uno: <strong>tostar el grano antes de moler</strong>. Una sartén seca a fuego medio durante 60-90 segundos transforma el comino completamente, liberando aromas que el grano frío no entrega. Esta es la diferencia entre un chimichurri amateur y uno profesional.</p>
                    <ol>
                        <li><strong>Chimichurri tradicional</strong>: 1 cda de comino tostado y molido por cada 250 ml de aceite. Reposo 24 hs antes de servir.</li>
                        <li><strong>Salmuera de asado</strong>: 1 cda por litro de agua + sal gruesa + ajo machacado + orégano. Pintar la carne durante la cocción.</li>
                        <li><strong>Locro y guisos</strong>: 1 cdta por kilo de carne, agregada en el sofrito inicial junto con cebolla y ajo.</li>
                        <li><strong>Chacinas artesanales</strong>: 0,4-0,6 g por kilo de masa de chorizo o salame.</li>
                        <li><strong>Cocina india</strong>: tostado en ghee al inicio del curry para liberar todos los aromas.</li>
                    </ol>
                """,
                "howto": {
                    "name": "Cómo preparar chimichurri paraguayo",
                    "total_time": "PT24H10M",
                    "steps": [
                        {"name": "Tostar comino", "text": "Tueste 1 cucharada de comino en grano en sartén seca a fuego medio durante 60-90 segundos hasta que libere aroma."},
                        {"name": "Moler grueso", "text": "Muela el comino tostado en mortero o molinillo, dejando textura gruesa, no fina."},
                        {"name": "Mezclar ingredientes", "text": "Combine el comino molido con 250 ml de aceite, 4 cdas de vinagre, 4 dientes de ajo picados, 2 cdas de perejil, 1 cda de orégano, sal y ají molido."},
                        {"name": "Reposar 24 hs", "text": "Tape y reserve en la heladera mínimo 24 horas para que los sabores se integren antes de servir."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Comino en grano egipcio para industria, restaurantes y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial para fábricas de tempero, chacinas y panificación.</li>
                    </ul>
                    <p>Importación directa de Egipto, certificado de origen, calidad estable lote a lote, factura legal y entrega a todo el Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/comino-en-grano" class="btn-link">Ver ficha del producto →</a> · <a href="/producto/comino-en-polvo" class="btn-link">Comino en polvo →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Conviene comprar comino en grano o molido?",
                "a": "Para máxima calidad, siempre en grano. El molido pierde 40-50 % del aroma en 90 días por evaporación de aceites volátiles. El grano entero conserva el perfil hasta 36 meses. Las parrillas profesionales muelen el grano momentos antes de usar.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de comino en grano en producción?",
                "a": "Aproximadamente 1.000 cdas. En chimichurri rinde 1.000 porciones de salsa (250 ml por unidad). En chacinas rinde 1.500-2.500 kg de masa de embutido (0,4-0,6 g por kg).",
            },
            {
                "q": "¿Por qué el comino egipcio es referente?",
                "a": "Por consistencia de tamaño de grano, color marrón claro uniforme, limpieza (poco resto de tallo) y intensidad aromática alta. Es el origen preferido por la industria latinoamericana de chacinas y temperos.",
            },
            {
                "q": "¿El comino y la alcaravea son lo mismo?",
                "a": "No. La alcaravea (Carum carvi) es una semilla parecida visualmente pero con sabor más anisado y dulce. El comino verdadero (Cuminum cyminum) tiene perfil terroso y ahumado.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y oscuro. Bien guardado conserva calidad por 24-36 meses en grano. Después de moler, idealmente consumir en 90 días.",
            },
            {
                "q": "¿Se puede usar en repostería?",
                "a": "Sí, en panes especiados (pan árabe, pan de centeno alemán, pan de comino judío) y en algunos quesos europeos curados. En Paraguay se usa principalmente en aplicaciones saladas.",
            },
        ],
        "related_slugs": ["comino-en-polvo", "pimienta-negra-en-grano", "oregano-peruano", "ajo-granulado"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 12. COMINO EN POLVO
    # ═════════════════════════════════════════════════════════════════
    "comino-en-polvo": {
        "product_slug": "comino-en-polvo",
        "title": "Comino en Polvo: el caballo de batalla de las chacinas, embutidos y temperos industriales",
        "dek": "Cuminum cyminum molido fino para integración rápida en masas, marinados y blends. Cuando el volumen importa más que la frescura del grano.",
        "meta_title": "Comino en Polvo — Guía Mayorista | Especias del Paraguay",
        "meta_description": "Comino en polvo al por mayor en Paraguay para fábricas de chacinas, temperos, sazonadores y panificación. Importación directa de Egipto.",
        "category": "Especias y Condimentos",
        "reading_time": 6,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">Cuando una fábrica de chacinas produce 500 kg de chorizo paraguayo por turno, no puede tostar y moler el comino al momento. Necesita <strong>comino en polvo</strong> consistente, dispersión homogénea y precio competitivo. La industria de tempero, embutidos, panificación industrial y sazonadores comerciales corre con comino molido.</p>
            <p>En Especias del Paraguay importamos comino en polvo egipcio de molienda industrial, ideal para fábricas que necesitan integración rápida en masas, marinados líquidos, mezclas secas y blends instantáneos.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "Comino molido vs comino en grano: cuándo usar cada uno",
                "body": """
                    <p>El <strong>comino en polvo</strong> es <em>Cuminum cyminum</em> molido a granulometría fina (típicamente 60-80 mesh). La industria lo prefiere sobre el grano por tres razones:</p>
                    <ul>
                        <li><strong>Dispersión homogénea</strong>: en una masa de embutido o un marinado, el polvo se distribuye uniformemente sin "puntos calientes" de sabor.</li>
                        <li><strong>Cálculo de dosis preciso</strong>: en producción industrial, gramos de polvo es más práctico que cucharadas de grano molido en planta.</li>
                        <li><strong>Velocidad de proceso</strong>: no requiere tostado ni molienda en línea; va directo al mezclador.</li>
                    </ul>
                    <p>El trade-off es la pérdida aromática más rápida: el polvo bien envasado conserva calidad por 6-12 meses; el grano por 24-36. Para industria con rotación alta, el polvo funciona perfectamente. Para restaurantes y parrillas que valoran el aroma intenso, mejor el grano.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos para industria, chacinas y panificación",
                "body": """
                    <p>El comino en polvo es protagonista en categorías que mueven volumen serio:</p>
                    <ul>
                        <li><strong>Chacinas y embutidos industriales</strong>: chorizo paraguayo, salame italiano, mortadela, hamburguesas, panchos premium. Dosis típica 0,4-0,6 g por kilo de carne.</li>
                        <li><strong>Sazonadores y temperos</strong>: blends "para asado", "para carne", "para pollo", "para guiso". El comino es el componente más reconocible del perfil paraguayo.</li>
                        <li><strong>Productos cárnicos congelados</strong>: hamburguesas, albóndigas, milanesas pre-condimentadas, empanadas industriales.</li>
                        <li><strong>Cocina mexicana industrial</strong>: tacos al pastor, picadillo, frijoles refritos enlatados, salsas de molcajete.</li>
                        <li><strong>Snacks salados</strong>: chips de yuca con tempero paraguayo, garbanzos tostados con especias, semillas saladas.</li>
                        <li><strong>Pre-mezclas para hogar</strong>: sazonadores en sobre, kits de empanada, kits de chimichurri instantáneo.</li>
                    </ul>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar comino en polvo en producción",
                "body": """
                    <p>Tres reglas profesionales para industria:</p>
                    <ol>
                        <li><strong>Hidratación previa</strong>: en marinados líquidos, mezclar el comino con un poco de aceite o agua tibia 5 minutos antes de incorporar. Mejora la dispersión y libera aceites residuales.</li>
                        <li><strong>Incorporación al inicio</strong>: en cocción larga (guisos, salsas), incorporar el comino temprano para que se integre. Su sabor se redondea con el calor sostenido.</li>
                        <li><strong>Almacenamiento crítico</strong>: el comino en polvo es sensible a humedad y luz. Bolsa o tambor cerrado herméticamente, lugar seco a 20-25 °C, sin contacto con olores fuertes.</li>
                    </ol>
                    <p>Para chacinas: el comino en polvo se incorpora directamente a la masa picada junto con sal nitrificante, ajo, pimentón y demás especias. Mezclar 5 minutos en mezcladora industrial garantiza distribución uniforme.</p>
                """,
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Comino en polvo egipcio para industria de chacinas, temperos y panificación:</p>
                    <ul>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial estándar para fábricas.</li>
                    </ul>
                    <p>Importación directa, certificado de origen, granulometría consistente. Factura legal y entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/comino-en-polvo" class="btn-link">Ver ficha del producto →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Cuánto rinde 1 kg de comino en polvo en chacinas?",
                "a": "Aproximadamente 2.000 kg de masa de embutido (0,5 g por kilo). En sazonadores en blend, rinde 100-200 kg de mezcla terminada según la receta.",
            },
            {
                "q": "¿Qué granulometría tiene el comino en polvo industrial?",
                "a": "Típicamente 60-80 mesh, equivalente a polvo medio que se integra rápido en masas líquidas y secas sin formar grumos.",
            },
            {
                "q": "¿Cuánto tiempo conserva su aroma?",
                "a": "Bien envasado y almacenado, 6-12 meses. Después pierde intensidad gradualmente. Para almacenamiento prolongado, prefiera el grano y muela en planta.",
            },
            {
                "q": "¿Sirve para uso doméstico o solo industrial?",
                "a": "Sirve para ambos. La granulometría industrial funciona perfectamente en cocina doméstica para guisos, marinados y temperos rápidos.",
            },
            {
                "q": "¿Se puede mezclar con otras especias en blend?",
                "a": "Sí. El comino combina perfectamente con orégano, ajo en polvo, paprika y pimienta para sazonadores tipo paraguayo o argentino.",
            },
            {
                "q": "¿Tiene certificado de origen y análisis bromatológico?",
                "a": "Sí. Cada lote viene con certificado de origen Egipto y análisis bromatológico básico. Bajo pedido se puede solicitar análisis microbiológico adicional.",
            },
        ],
        "related_slugs": ["comino-en-grano", "ajo-en-polvo", "paprika-dulce", "pimienta-del-reino-en-polvo"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 13. PIMIENTA DEL REINO EN POLVO
    # ═════════════════════════════════════════════════════════════════
    "pimienta-del-reino-en-polvo": {
        "product_slug": "pimienta-del-reino-en-polvo",
        "title": "Pimienta del Reino en Polvo: la especia más vendida del mundo, lista para línea de producción",
        "dek": "Piper nigrum molida fina, dispersión homogénea, perfil pungente equilibrado. La pimienta de uso industrial que llega a millones de mesas.",
        "meta_title": "Pimienta del Reino en Polvo | Especias del Paraguay",
        "meta_description": "Pimienta del reino en polvo al por mayor en Paraguay para industria de chacinas, embutidos, sazonadores y panificación. Importación directa.",
        "category": "Especias y Condimentos",
        "reading_time": 6,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "earth",
        "intro": """
            <p class="lead">La <strong>pimienta del reino</strong> es la especia más comercializada del planeta. Aparece en prácticamente todo platillo salado occidental, en mayonesa industrial, en mostazas, en milanesas pre-armadas, en chacinas, en aderezos para ensalada y en sazonadores universales. La versión en polvo es el formato dominante en industria por dispersión y velocidad de proceso.</p>
            <p>En Especias del Paraguay importamos <strong>pimienta del reino en polvo (Piper nigrum)</strong> de origen Brasil y Vietnam, los dos polos productivos referentes, con perfil pungente equilibrado ideal para fábricas de tempero, embutidos y productos cárnicos.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es la pimienta del reino?",
                "body": """
                    <p>La <strong>pimienta del reino</strong> (<em>Piper nigrum</em>, <strong>black pepper</strong> en inglés, <strong>pimenta do reino</strong> en portugués) es el fruto seco de una liana tropical originaria de la costa de Malabar (India). Hoy se cultiva en Vietnam (productor #1 mundial), Brasil, Indonesia, India y Sri Lanka.</p>
                    <p>Existen cuatro tipos comerciales según el momento de cosecha y procesamiento:</p>
                    <ul>
                        <li><strong>Pimienta negra</strong>: cosechada verde y secada al sol. Es la más pungente y aromática, la dominante en industria.</li>
                        <li><strong>Pimienta blanca</strong>: madura y descascarada. Sabor más suave, menos pungente, color claro para platos blancos.</li>
                        <li><strong>Pimienta verde</strong>: inmadura y conservada en salmuera o liofilizada. Sabor fresco y herbal.</li>
                        <li><strong>Pimienta roja (rosa de Schinus es una falsificación, no es Piper nigrum)</strong>: madurada al rojo, rara y costosa.</li>
                    </ul>
                    <p>La "pimienta del reino" comercial paraguaya es <strong>pimienta negra molida</strong>, el formato industrial estándar.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en industria, chacinas y cocina profesional",
                "body": """
                    <p>La pimienta del reino en polvo es ingrediente universal en categorías saladas:</p>
                    <ul>
                        <li><strong>Industria de chacinas y embutidos</strong>: prácticamente todos los embutidos del mundo llevan pimienta. Dosis típica 1,5-3 g por kilo de masa.</li>
                        <li><strong>Productos cárnicos pre-condimentados</strong>: hamburguesas, milanesas, panchos, salchichas, fiambres.</li>
                        <li><strong>Sazonadores y mezclas</strong>: cualquier blend salado lleva pimienta como base. Sazonadores universales, mezclas para asado, condimentos italianos.</li>
                        <li><strong>Aderezos y salsas industriales</strong>: mayonesa premium, mostaza, vinagretas embotelladas, aderezo César, salsas BBQ.</li>
                        <li><strong>Panificación salada</strong>: focaccia, panes saborizados, grissini, palitos salados, galletitas de queso.</li>
                        <li><strong>Cocina paraguaya</strong>: milanesa con pimienta y ajo, tortilla paraguaya, arroz con pollo, sopa paraguaya tradicional.</li>
                    </ul>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar pimienta del reino en polvo",
                "body": """
                    <p>Reglas profesionales:</p>
                    <ol>
                        <li><strong>Incorporación al final en cocciones cortas</strong>: en preparaciones rápidas (saltados, frituras), agregar la pimienta al final preserva el aroma volátil. El calor prolongado destruye notas pungentes.</li>
                        <li><strong>Incorporación al inicio en cocciones largas</strong>: en guisos, brasados y caldos largos, incorporar al inicio permite que el sabor se integre profundamente.</li>
                        <li><strong>Conservación crítica</strong>: la pimienta molida pierde aroma rápido. Envase hermético, sin luz, sin humedad. Idealmente consumir en 6-9 meses desde apertura.</li>
                        <li><strong>Dosis industriales típicas</strong>: chacinas 1,5-3 g/kg de carne, hamburguesas 2-3 g/kg, sazonadores 5-15 % del blend, mostazas y aderezos 0,5-1 % de la fórmula.</li>
                    </ol>
                """,
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Pimienta del reino en polvo importada para industria, chacinas y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial para fábricas.</li>
                    </ul>
                    <p>Importación directa de Brasil/Vietnam, certificado de origen, granulometría industrial. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/pimienta-del-reino-en-polvo" class="btn-link">Ver ficha del producto →</a> · <a href="/producto/pimienta-negra-en-grano" class="btn-link">Pimienta en grano →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Diferencia entre pimienta negra molida y pimienta del reino?",
                "a": "Son la misma especia. Pimienta del reino, pimienta negra y black pepper son sinónimos comerciales. Vienen del mismo fruto (Piper nigrum) cosechado verde y secado al sol.",
            },
            {
                "q": "¿La pimienta blanca es mejor que la negra?",
                "a": "Diferente, no mejor. La blanca es más suave y se usa en salsas claras donde el color de la negra distrae. La negra es más pungente y aromática, dominante en industria.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de pimienta en polvo en chacinas?",
                "a": "Aproximadamente 400-700 kg de masa de embutido (1,5-3 g por kilo). En sazonadores rinde 7-20 kg de blend terminado.",
            },
            {
                "q": "¿Por qué la pimienta molida pierde aroma rápido?",
                "a": "Por evaporación de piperina y aceites volátiles. La superficie expuesta del polvo es mucho mayor que la del grano. Para máximo aroma, el grano molido en planta es superior; el polvo industrial gana en velocidad de proceso.",
            },
            {
                "q": "¿Tiene aplicaciones medicinales?",
                "a": "La piperina aumenta la biodisponibilidad de la curcumina (en formulaciones funcionales con cúrcuma). Por eso muchos suplementos de cúrcuma incluyen extracto de pimienta negra.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco a 20-25 °C, lejos de fuentes de luz y olores fuertes. Bien guardada conserva aroma 6-12 meses.",
            },
        ],
        "related_slugs": ["pimienta-negra-en-grano", "comino-en-polvo", "ajo-en-polvo", "sal-rosa-del-himalaya-fino"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 14. SEMILLA DE ANÍS  (★ KILLER PRODUCT for chipa paraguaya)
    # ═════════════════════════════════════════════════════════════════
    "semilla-de-anis": {
        "product_slug": "semilla-de-anis",
        "title": "Semilla de Anís: el ingrediente que define la chipa paraguaya y la repostería tradicional",
        "dek": "Pimpinella anisum, anís verde, la semilla pequeña que da carácter al pan más amado del Paraguay. Sin ella, no es chipa.",
        "meta_title": "Semilla de Anís para Chipa — Mayorista | Especias del Paraguay",
        "meta_description": "Semilla de anís al por mayor en Paraguay para chiperías, panificadoras, repostería tradicional y licorería. El ingrediente clave de la chipa paraguaya.",
        "category": "Semillas y Granos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">Si pidieras a una abuela paraguaya la lista de ingredientes para una <strong>chipa</strong> de verdad, te diría almidón de mandioca, queso paraguay, huevos, leche, manteca, sal y —el detalle que hace toda la diferencia— <strong>anís en semilla</strong>. Sin esa semilla pequeña verde-marrón perfumando la masa, no es chipa: es otra cosa.</p>
            <p>En Especias del Paraguay importamos <strong>semilla de anís (Pimpinella anisum)</strong>, también llamado <strong>anís verde</strong>, seleccionada por intensidad aromática y limpieza. Esta guía es para chiperías, panificadoras industriales, fábricas de productos típicos paraguayos, repostería tradicional, licorería artesanal y consumidores que respetan la receta original.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es la semilla de anís?",
                "body": """
                    <p>La <strong>semilla de anís</strong> (<em>Pimpinella anisum</em>, también <strong>anís verde</strong> o <strong>anise seeds</strong> en inglés) es la semilla seca de una planta herbácea de la familia <em>Apiaceae</em>, parientes del comino, hinojo y eneldo. Originaria del Mediterráneo oriental, hoy se cultiva en España, Egipto, Turquía, Siria e Irán.</p>
                    <p>Atención al nombre: el <strong>anís verde</strong> (Pimpinella anisum, semilla pequeña) es <em>distinto</em> del <strong>anís estrellado</strong> (Illicium verum, fruto en forma de estrella). Comparten el aroma a <strong>anetol</strong> pero son plantas no relacionadas. La chipa paraguaya usa exclusivamente el anís verde en semilla.</p>
                    <p>El compuesto activo principal es el <strong>anetol</strong> (90 % del aceite esencial), responsable del aroma dulce-licoroso característico que define la chipa, los biscochitos festivos y la cocina sefardí mediterránea.</p>
                """,
            },
            {
                "id": "chipa",
                "heading": "El anís y la chipa paraguaya: una historia de 400 años",
                "body": """
                    <p>La <strong>chipa</strong> paraguaya nace en las reducciones jesuíticas del siglo XVII, cuando los guaraníes adoptaron el almidón de mandioca como sustituto del trigo y los jesuitas trajeron quesos, huevos y especias del Mediterráneo. El anís en semilla llegó por esa ruta y nunca más salió de la receta.</p>
                    <p>Las cinco variantes principales que llevan anís:</p>
                    <ul>
                        <li><strong>Chipa común</strong> (chipa argolla, la del bus de larga distancia): masa amarilla, queso paraguay, almidón, anís en cantidad notable.</li>
                        <li><strong>Chipa cuatro quesos</strong>: versión premium con mayor cantidad de queso. Anís más sutil pero presente.</li>
                        <li><strong>Chipa kavure</strong>: variante alargada cocida en horno de barro. Anís bien marcado.</li>
                        <li><strong>Chipa so'o</strong>: rellena de carne. Anís suaviza el sabor.</li>
                        <li><strong>Chipa avatí</strong>: hecha con harina de maíz. El anís aporta dulzor herbal.</li>
                    </ul>
                    <p>Otras aplicaciones paraguayas: <strong>biscochitos festivos</strong> (Navidad, Año Nuevo), <strong>panettone paraguayo</strong>, <strong>mbeyú dulce</strong>, <strong>panificados de Semana Santa</strong>.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos para chiperías, panificación y licorería",
                "body": """
                    <p>El anís en semilla es protagonista en categorías que pesan en el Paraguay:</p>
                    <ul>
                        <li><strong>Chiperías industriales y artesanales</strong>: producción diaria de chipa común y variantes premium. Dosis típica 5-10 g de anís por kilo de masa.</li>
                        <li><strong>Panificación tradicional</strong>: panettones de fin de año, panes especiados de fiestas, alfajores festivos, biscochitos navideños.</li>
                        <li><strong>Repostería europea</strong>: bizcochos italianos (pizzelle, anginetti), galletitas griegas (koulourakia), pasteles sefardíes.</li>
                        <li><strong>Licorería artesanal</strong>: sambuca, anisette, ouzo casero, gin de firma con notas anisadas, licor de anís paraguayo.</li>
                        <li><strong>Tisanas digestivas</strong>: infusión sola o con hinojo. Excelente para sobremesa.</li>
                        <li><strong>Industria de yogures y lácteos saborizados</strong>: yogures con miel y anís, helados artesanales, dulce de leche premium.</li>
                    </ul>
                    <p>Para chiperías con producción mensual relevante, la semilla de anís de Especias del Paraguay ofrece consistencia lote a lote — esencial cuando el sabor de tu chipa es parte de la identidad de tu marca.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo usar semilla de anís: técnicas profesionales",
                "body": """
                    <p>Técnicas según la aplicación:</p>
                    <ol>
                        <li><strong>Para chipa</strong>: 8-10 g de semillas enteras por kilo de masa de chipa, incorporadas durante el amasado. NO moler — la semilla entera es parte de la textura clásica.</li>
                        <li><strong>Para repostería europea</strong>: triturar grueso en mortero antes de incorporar a masas finas. Aporta aroma sin la textura crujiente.</li>
                        <li><strong>Para infusión</strong>: 1 cdta de semillas enteras por taza, 5 minutos en agua a 90 °C.</li>
                        <li><strong>Para licorería</strong>: maceración 4-6 semanas, 30 g de semillas por litro de alcohol neutro 40-60 % v/v.</li>
                    </ol>
                """,
                "howto": {
                    "name": "Cómo amasar chipa paraguaya con anís",
                    "total_time": "PT1H30M",
                    "steps": [
                        {"name": "Reunir ingredientes", "text": "Disponga 1 kg de almidón de mandioca, 500 g de queso paraguay rallado, 4 huevos, 200 ml de leche, 200 g de manteca, 1 cda (8 g) de semillas de anís y sal."},
                        {"name": "Mezclar secos", "text": "En un bol grande mezcle el almidón, el queso rallado, las semillas de anís y la sal. Las semillas enteras quedan en la masa, no se muelen."},
                        {"name": "Incorporar húmedos", "text": "Agregue la manteca derretida tibia, los huevos batidos y la leche tibia. Amase hasta obtener una masa homogénea pero no pegajosa."},
                        {"name": "Formar y hornear", "text": "Forme las chipas (argolla o bastón). Hornee 18-22 minutos a 220 °C hasta dorar. Servir tibia."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Semilla de anís verde para chiperías, panificadoras y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial para producción de chipa y panificados festivos.</li>
                    </ul>
                    <p>Importación directa, certificado de origen, calidad estable lote a lote. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/semilla-de-anis" class="btn-link">Ver ficha del producto →</a> · <a href="/producto/anis-estrellado" class="btn-link">Anís estrellado →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Anís verde y anís estrellado son lo mismo?",
                "a": "No. El anís verde (Pimpinella anisum, semilla pequeña) es el de la chipa. El anís estrellado (Illicium verum, fruto en forma de estrella) es de cocina asiática. Comparten aroma a anetol pero son plantas distintas y no son intercambiables sin ajustar la receta.",
            },
            {
                "q": "¿Cuánto anís lleva 1 kg de masa de chipa?",
                "a": "8-10 g (aproximadamente 1 cucharada sopera) de semillas enteras por kilo de masa. Más cantidad satura el sabor y menos lo deja imperceptible.",
            },
            {
                "q": "¿Hay que moler el anís para chipa?",
                "a": "No. Para chipa tradicional la semilla va entera, contribuyendo a la textura característica. En repostería fina se puede triturar grueso.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de anís en producción de chipa?",
                "a": "Aproximadamente 100-125 kg de masa de chipa terminada (8-10 g por kilo). Para una chipería que produce 50 kg de masa por turno, 1 kg de anís cubre 10 turnos.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y oscuro. La semilla entera conserva aroma 24-30 meses. Bolsa cerrada en cámara seca es ideal para chiperías.",
            },
            {
                "q": "¿Puede usarse en infusión digestiva?",
                "a": "Sí, ampliamente. La infusión de anís verde es uno de los digestivos tradicionales más antiguos del Mediterráneo. Combina perfecto con manzanilla y melissa para una sobremesa relajante.",
            },
        ],
        "related_slugs": ["anis-estrellado", "hinojo", "cardamomo-en-grano", "manzanilla-flor"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 15. CASTAÑA DE CAJÚ W1 CRUDA
    # ═════════════════════════════════════════════════════════════════
    "castana-de-caju-w1-cruda": {
        "product_slug": "castana-de-caju-w1-cruda",
        "title": "Castaña de Cajú W1 Cruda: la calidad premium para aperitivos, repostería y leches vegetales",
        "dek": "Anacardium occidentale, calidad W1 (granos enteros tamaño grande), cruda y sin sal. La base más versátil para industria de snacks, panificación y plant-based.",
        "meta_title": "Castaña de Cajú W1 Cruda — Mayorista | Especias del Paraguay",
        "meta_description": "Castaña de cajú W1 cruda al por mayor en Paraguay para industria de aperitivos, repostería, leches vegetales y mix gourmet. Calidad premium importada.",
        "category": "Frutos Secos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">La <strong>castaña de cajú</strong> (también llamada <em>castanha de caju</em> en portugués o <em>cashew</em> en inglés) es uno de los frutos secos más versátiles del mundo: aperitivo gourmet, base de leches vegetales, ingrediente premium en repostería, materia prima para mantequillas, snack saludable. Pero la calidad varía mucho según el grado.</p>
            <p>En Especias del Paraguay importamos <strong>Cajú W1 Cruda</strong>, el grado premium que combina granos enteros, tamaño grande uniforme y procesamiento sin tostar ni salar. Esta guía es para fábricas de snacks, repostería profesional, productores plant-based, almacenes saludables y consumidores que valoran calidad.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué significa W1 y por qué importa?",
                "body": """
                    <p>La <strong>castaña de cajú</strong> (<em>Anacardium occidentale</em>) se clasifica internacionalmente por <strong>tamaño y entereza del grano</strong>. La nomenclatura mundial usa "W" (whole, entera) seguido de un número que indica granos por libra. Cuanto MENOR el número, MÁS GRANDE el grano:</p>
                    <ul>
                        <li><strong>W180</strong>: 180 granos por libra → granos extra grandes (ultra-premium).</li>
                        <li><strong>W210</strong>: 210 granos por libra → granos grandes (premium gourmet).</li>
                        <li><strong>W240 / W320</strong>: granos medianos (estándar comercial).</li>
                        <li><strong>W450</strong>: granos pequeños (industrial, repostería).</li>
                    </ul>
                    <p>El grado <strong>W1</strong> es la mejor selección dentro de su rango: granos enteros sin partir, tamaño uniforme, color blanco-marfil sin manchas, humedad controlada. Es la castaña que vas a encontrar en mix de frutos secos premium y aperitivos gourmet.</p>
                    <p>Origen comercial dominante: Vietnam (productor #1 mundial), India, Brasil y Costa de Marfil.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Beneficios y perfil nutricional",
                "body": """
                    <p>Por 100 g de castaña de cajú cruda:</p>
                    <ul>
                        <li><strong>553 kcal</strong>: alta densidad energética, ideal para barras y aperitivos saciantes.</li>
                        <li><strong>18 g de proteína vegetal</strong> con perfil aminoacídico bueno.</li>
                        <li><strong>44 g de grasas</strong> mayoritariamente monoinsaturadas (las "grasas buenas" del corazón).</li>
                        <li><strong>Magnesio</strong>, <strong>fósforo</strong>, <strong>cobre</strong> en cantidades relevantes.</li>
                        <li><strong>Triptófano</strong>: precursor de serotonina, asociado a bienestar.</li>
                        <li><strong>Bajo en sodio</strong> en versión cruda (a diferencia de la salada).</li>
                    </ul>
                    <p>Por su perfil graso-proteico, la castaña de cajú es uno de los frutos secos más usados en alimentación deportiva, dietas plant-based y productos clean-label.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en industria, repostería y plant-based",
                "body": """
                    <p>La castaña de cajú W1 cruda es uno de los frutos secos más versátiles:</p>
                    <ul>
                        <li><strong>Aperitivos premium y mix gourmet</strong>: tostada en planta, salada light, mezcla con almendras, pasas y arándanos para mix tipo "trail".</li>
                        <li><strong>Industria plant-based</strong>: leche de cajú, queso vegano (cashew cheese), nata vegana, mayonesa plant-based. La cremosidad del cajú es insuperable.</li>
                        <li><strong>Mantequilla de cajú (cashew butter)</strong>: alternativa premium a la mantequilla de maní, más suave y dulce.</li>
                        <li><strong>Repostería premium</strong>: trufas, cheesecakes raw, brownies fit, barras energéticas, pasteles veganos.</li>
                        <li><strong>Cocina indiana y asiática</strong>: pollo al cajú, curries cremosos, pasta de cajú para korma.</li>
                        <li><strong>Granolas y mueslis</strong>: blends premium con avena, cajú picado, frutas deshidratadas.</li>
                    </ul>
                    <p>Para producción de leches vegetales: la receta básica es 1 taza de cajú cruda + 4 tazas de agua filtrada → remojar 4-8 horas → procesar y colar. Resultado: 1 litro de leche cremosa sin necesidad de filtración fina (a diferencia de la leche de almendra que requiere bolsa filtrante).</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar castaña de cajú cruda",
                "body": """
                    <p>Tres técnicas profesionales según uso:</p>
                    <ol>
                        <li><strong>Tostado</strong>: horno a 160 °C durante 8-10 minutos, removiendo a la mitad. Color dorado claro. Tostar más oscuro amarga.</li>
                        <li><strong>Activado (raw, plant-based)</strong>: remojo en agua filtrada 4-8 horas. Reduce los antinutrientes (ácido fítico) y mejora digestibilidad.</li>
                        <li><strong>Pasta de cajú industrial</strong>: tostar suave + procesar 5-8 minutos en procesador potente con pizca de sal hasta obtener pasta cremosa. Sin agregados, conserva 3-6 meses refrigerada.</li>
                    </ol>
                """,
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Castaña de cajú W1 cruda para industria, reventa y aperitivos:</p>
                    <ul>
                        <li><strong>Caja 10 kg</strong> — formato estándar para tostadores y reventa premium.</li>
                        <li><strong>Caja 22,68 kg (50 lbs)</strong> — formato industrial para fábricas de snacks y plant-based.</li>
                    </ul>
                    <p>Importación directa, certificado de origen, calidad W1 garantizada. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/castana-de-caju-w1-cruda" class="btn-link">Ver ficha del producto →</a> · <a href="/producto/castana-de-caju-con-sal-w1" class="btn-link">Cajú con sal →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Por qué la castaña de cajú es siempre 'cruda' aunque ya esté procesada?",
                "a": "Porque viene del fruto entero del cajú, donde la castaña está envuelta en una cáscara con líquido cáustico (urushiol). Toda castaña comercial pasa por descascarado y tratamiento térmico mínimo para retirar el cáustico, pero se vende como 'cruda' porque NO fue tostada gastronómicamente. Sigue cruda en el sentido culinario.",
            },
            {
                "q": "¿La cajú cruda es segura comer así?",
                "a": "Sí. La cajú comercial vendida 'cruda' ya pasó por el proceso obligatorio de descascarado seguro. No hay riesgo de urushiol. Es segura para comer directa del paquete.",
            },
            {
                "q": "¿Conviene W1 o W2 para industria?",
                "a": "W1 para aperitivos premium y plant-based donde la entereza importa. W2/W4 partidos para repostería, mantequillas y aplicaciones donde el grano se va a procesar igual. La elección depende de la aplicación final.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de cajú en leche vegetal?",
                "a": "Aproximadamente 4 litros de leche de cajú (1 taza ≈ 130 g rinde 1 litro). Es el fruto seco más eficiente para leches vegetales por el rendimiento sin necesidad de colar.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y fresco. A 20 °C dura 6 meses; refrigerada a 4 °C dura 12 meses; congelada hasta 24 meses. La grasa rancia es el principal enemigo.",
            },
            {
                "q": "¿Tiene certificado de calidad?",
                "a": "Sí. Cada lote viene con certificado de origen, granulometría W1 garantizada y análisis bromatológico básico. Bajo pedido se puede solicitar análisis adicional.",
            },
        ],
        "related_slugs": ["almendra-americana", "nuez-mariposa", "pistacho-sin-cascara", "macadamia"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 16. ALMENDRA AMERICANA
    # ═════════════════════════════════════════════════════════════════
    "almendra-americana": {
        "product_slug": "almendra-americana",
        "title": "Almendra Americana: el fruto seco rey de la repostería premium y las leches vegetales",
        "dek": "Prunus dulcis californiana, grano grande uniforme, sabor limpio. La almendra que define el estándar mundial para industria saludable.",
        "meta_title": "Almendra Americana — Mayorista | Especias del Paraguay",
        "meta_description": "Almendra americana cruda al por mayor en Paraguay para repostería, panificación premium, leches vegetales y mix gourmet. Origen California, calidad estable.",
        "category": "Frutos Secos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">La <strong>almendra americana</strong> es el estándar global del fruto seco premium. California produce <strong>el 80 % de las almendras del mundo</strong>, y la consistencia de tamaño, color y sabor de la almendra californiana es lo que la repostería profesional, las leches vegetales industriales y los productos sin gluten necesitan: previsibilidad lote a lote.</p>
            <p>En Especias del Paraguay importamos <strong>almendra americana cruda (Prunus dulcis)</strong> origen California, ideal para fábricas de panificación premium, leche de almendras, plant-based, mix de frutos secos y reventa.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Por qué California es el origen referente?",
                "body": """
                    <p>La <strong>almendra</strong> (<em>Prunus dulcis</em>, también <strong>almond</strong> en inglés o <strong>amêndoa</strong> en portugués) es la semilla de un árbol pariente del durazno. California Central Valley combina suelos volcánicos, agua de irrigación, clima mediterráneo y polinización masiva por abejas, dando un volumen y una calidad que ningún otro origen iguala.</p>
                    <p>La almendra californiana se clasifica por:</p>
                    <ul>
                        <li><strong>Variedad</strong>: Nonpareil (premium gourmet), Carmel, Mission, Independence.</li>
                        <li><strong>Tamaño</strong>: 16-18, 18-20, 20-22, 23-25 (almendras por gramo).</li>
                        <li><strong>Estado</strong>: con piel (natural), sin piel (blanqueada), laminada, en harina, en cubitos.</li>
                    </ul>
                    <p>La almendra que importamos es <strong>natural cruda con piel</strong>, formato más versátil para industria.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Perfil nutricional",
                "body": """
                    <p>Por 100 g de almendra cruda:</p>
                    <ul>
                        <li><strong>576 kcal</strong>, alta densidad energética.</li>
                        <li><strong>21 g de proteína</strong>, una de las más altas entre frutos secos.</li>
                        <li><strong>50 g de grasas</strong> mayoritariamente monoinsaturadas (perfil cardiovascular favorable).</li>
                        <li><strong>12 g de fibra</strong>: la más alta entre frutos secos comunes.</li>
                        <li><strong>Vitamina E</strong> (alfa-tocoferol): la almendra es la mejor fuente vegetal natural.</li>
                        <li><strong>Magnesio, calcio, hierro</strong> en cantidades relevantes.</li>
                    </ul>
                    <p>Esto explica su penetración en categorías como "snack saludable", "leche vegetal funcional" y "panificación sin gluten".</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en industria y gastronomía",
                "body": """
                    <p>La almendra americana es protagonista en muchas categorías:</p>
                    <ul>
                        <li><strong>Repostería premium</strong>: macarons, frangipane, pasteles franceses (paris-brest, dacquoise), turrones de Navidad, mazapanes, almond croissants.</li>
                        <li><strong>Leches vegetales</strong>: leche de almendras (RTD y polvo), bebidas barista para cafeterías especiales.</li>
                        <li><strong>Plant-based y vegano</strong>: queso vegano, mantequilla de almendras, nata vegetal.</li>
                        <li><strong>Snacks gourmet</strong>: almendras tostadas con sal del Himalaya, almendras con miel, mix premium con cajú y arándanos.</li>
                        <li><strong>Panificación funcional</strong>: panes de almendra, galletitas low-carb, productos keto.</li>
                        <li><strong>Cocina paraguaya y latinoamericana</strong>: postres especiados con almendra laminada, alfajores premium con relleno de almendra, helado de almendra.</li>
                        <li><strong>Industria de cereales y barras</strong>: granolas premium, barras energéticas, mueslis, cereal mix gourmet.</li>
                    </ul>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar almendra cruda",
                "body": """
                    <p>Cuatro técnicas según aplicación:</p>
                    <ol>
                        <li><strong>Tostado</strong>: 170 °C durante 10-12 minutos, removiendo a la mitad. Aroma se intensifica notablemente.</li>
                        <li><strong>Blanqueado (sin piel)</strong>: hervir 60 segundos, escurrir y pelar a mano. Para macarons y pasteles donde el color blanco importa.</li>
                        <li><strong>Activado (raw)</strong>: remojo en agua filtrada 8-12 horas. Mejor digestibilidad para crudismo y plant-based.</li>
                        <li><strong>Leche de almendras</strong>: 1 taza activada + 4 tazas de agua → procesar 1 minuto → colar con bolsa filtrante. Rinde 1 litro.</li>
                    </ol>
                """,
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Almendra americana cruda con piel para industria y reventa:</p>
                    <ul>
                        <li><strong>Caja 10 kg</strong> — formato estándar para reposterías, panificadoras y reventa premium.</li>
                        <li><strong>Caja 22,68 kg (50 lbs)</strong> — formato industrial.</li>
                    </ul>
                    <p>Importación directa California, certificado de origen, calidad estable lote a lote. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/almendra-americana" class="btn-link">Ver ficha del producto →</a> · <a href="/producto/almendra-laminada" class="btn-link">Almendra laminada →</a> · <a href="/producto/harina-de-almendra-parmex" class="btn-link">Harina de almendra →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Cuál es la diferencia entre almendra americana y almendra europea (española)?",
                "a": "La californiana tiene tamaño y color más uniforme (cultivo intensivo), perfil de sabor más suave. La almendra Marcona española es más dulce, redonda y costosa, usada en aplicaciones gourmet específicas. Para industria, la americana ofrece mejor relación precio/calidad/disponibilidad.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de almendra en leche vegetal?",
                "a": "Aproximadamente 4 litros de leche de almendras (1 taza ≈ 140 g rinde 1 litro). El residuo de la pulpa (okara de almendra) puede usarse en panificación.",
            },
            {
                "q": "¿Conviene almendra con piel o pelada?",
                "a": "Con piel para uso general (mix, granola, leche). Pelada para repostería fina donde el color blanco importa (macarons, mazapanes). Pelar requiere blanquear, lo que agrega proceso pero da resultado profesional.",
            },
            {
                "q": "¿Es segura para personas con alergia al maní?",
                "a": "La almendra es un fruto seco, NO un legume como el maní. Las alergias son distintas. Pero hay personas con alergia cruzada — debe ser declarado en etiqueta de productos industriales.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y fresco. A 20 °C dura 9-12 meses; refrigerada a 4 °C dura 18 meses; congelada hasta 24 meses. La grasa monoinsaturada es relativamente estable.",
            },
            {
                "q": "¿Es apta para celíacos?",
                "a": "La almendra natural es naturalmente sin gluten. Para certificación apta celíacos en producto industrial, requiere análisis de contaminación cruzada en la planta procesadora.",
            },
        ],
        "related_slugs": ["castana-de-caju-w1-cruda", "harina-de-almendra-parmex", "nuez-mariposa", "almendra-laminada"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 17. NUEZ MARIPOSA
    # ═════════════════════════════════════════════════════════════════
    "nuez-mariposa": {
        "product_slug": "nuez-mariposa",
        "title": "Nuez Mariposa: el corte premium para alfajores, panificación de fiesta y postres de autor",
        "dek": "Juglans regia, mariposa = mitad entera con forma de alas. La presentación visual más apreciada en repostería profesional.",
        "meta_title": "Nuez Mariposa — Mayorista | Especias del Paraguay",
        "meta_description": "Nuez mariposa al por mayor en Paraguay para alfajores, panificación premium, postres y repostería de autor. Origen Chile/Argentina, corte mariposa entero.",
        "category": "Frutos Secos",
        "reading_time": 6,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "earth",
        "intro": """
            <p class="lead">Cuando una pastelería profesional necesita decorar la cobertura de un alfajor, coronar un brownie premium o presentar un pan dulce navideño, no usa nuez picada cualquiera. Usa <strong>nuez mariposa</strong>: la mitad entera de la nuez, con su forma característica de alas de mariposa, color marrón claro y aspecto premium.</p>
            <p>En Especias del Paraguay importamos <strong>nuez mariposa (Juglans regia)</strong> de Chile y Argentina, los orígenes referentes del Cono Sur, seleccionada por entereza, color claro y limpieza. Esta guía es para reposterías, alfajoreras industriales, panificadoras de fin de año y restaurantes premium.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué significa mariposa en el corte de nuez?",
                "body": """
                    <p>La <strong>nuez común</strong> (<em>Juglans regia</em>, también <strong>walnut</strong> en inglés o <strong>noz</strong> en portugués) tiene una estructura interna de cuatro lóbulos separados por una membrana. Cuando se descascara con cuidado, se puede extraer la nuez en dos mitades enteras unidas — esa es la <strong>mariposa</strong>.</p>
                    <p>Clasificación comercial:</p>
                    <ul>
                        <li><strong>Mariposa entera</strong>: dos mitades unidas, la presentación premium.</li>
                        <li><strong>Mitades</strong>: una mitad entera (segunda calidad).</li>
                        <li><strong>Cuartos</strong>: ¼ del grano, aceptable para repostería que las pica.</li>
                        <li><strong>Granulado</strong>: trozos pequeños, uso industrial en mezclas.</li>
                    </ul>
                    <p>La mariposa cuesta más por kilo porque exige descascarado manual cuidadoso. Cada kilo de nuez con cáscara rinde aproximadamente 350-400 g de mariposas y 100-200 g de mitades + cuartos.</p>
                    <p>Origen Cono Sur: Chile (Valle del Aconcagua, Curicó) y Argentina (San Juan, Mendoza, Catamarca). Variedades dominantes: Chandler, Serr, Howard, Sunland.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Perfil nutricional",
                "body": """
                    <p>Por 100 g de nuez:</p>
                    <ul>
                        <li><strong>654 kcal</strong>: la nuez más calórica entre frutos secos comunes.</li>
                        <li><strong>15 g de proteína</strong>.</li>
                        <li><strong>65 g de grasas</strong>, con perfil único:</li>
                        <li><strong>9 g de omega-3 ALA</strong>: la nuez es la fuente más densa de omega-3 entre frutos secos.</li>
                        <li><strong>Antioxidantes polifenólicos</strong>: capacidad antioxidante alta.</li>
                        <li><strong>Magnesio, fósforo, manganeso</strong>.</li>
                    </ul>
                    <p>El perfil omega-3 hace de la nuez un ingrediente preferido en productos "saludables", "para el corazón" y plant-based.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en repostería, panificación y gastronomía",
                "body": """
                    <p>La mariposa es la presentación favorita de la repostería profesional:</p>
                    <ul>
                        <li><strong>Alfajores premium</strong>: la mariposa entera coronando el alfajor de chocolate o glaseado es marca registrada. Industria del alfajor argentino y paraguayo la usa intensivamente.</li>
                        <li><strong>Panificación de fiestas</strong>: pan dulce navideño, panettone tradicional, stollen alemán, christmas cake.</li>
                        <li><strong>Postres de autor</strong>: brownies con mariposa coronando, tarta de nuez, baklava, baba de nuez.</li>
                        <li><strong>Bombonería</strong>: bombones con relleno de praliné, garrapiñadas premium, turrones blandos.</li>
                        <li><strong>Cocina latina festiva</strong>: rosca de pascua, biscochuelos navideños, dulce de nuez en almíbar.</li>
                        <li><strong>Granolas y mueslis premium</strong>: blends gourmet con avena, nuez mariposa, dátiles y arándanos.</li>
                        <li><strong>Cocina mediterránea y árabe</strong>: ensalada Waldorf, baklava, muhammara (pasta de nuez y pimiento), tabule especial.</li>
                    </ul>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar nuez mariposa",
                "body": """
                    <p>La nuez es delicada — sus aceites se oxidan más rápido que los de otros frutos secos. Reglas profesionales:</p>
                    <ol>
                        <li><strong>Tostado suave</strong>: 160 °C durante 6-8 minutos. Más tiempo o más temperatura amarga rápidamente.</li>
                        <li><strong>Decoración</strong>: para coronar productos terminados (alfajores, brownies), usar la mariposa cruda — el calor del horno la termina de tostar levemente y conserva forma.</li>
                        <li><strong>Picado para mezclas</strong>: trozos de 5-8 mm para granolas y panes; menores de 3 mm para masas finas.</li>
                        <li><strong>Conservación crítica</strong>: refrigerar siempre que sea posible. La grasa de nuez es la más sensible a oxidación entre frutos secos.</li>
                    </ol>
                """,
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Nuez mariposa Chile/Argentina para industria, alfajoreras y repostería:</p>
                    <ul>
                        <li><strong>Caja 10 kg</strong> — formato estándar para alfajoreras y reposterías.</li>
                    </ul>
                    <p>Importación directa, certificado de origen, calidad mariposa entera garantizada. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/nuez-mariposa" class="btn-link">Ver ficha del producto →</a> · <a href="/producto/nuez-pecan" class="btn-link">Nuez pecán →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Por qué la nuez mariposa cuesta más que la nuez en cuartos?",
                "a": "Porque exige descascarado manual cuidadoso para preservar la forma entera de las dos mitades unidas. Solo el 35-40 % del rendimiento de descascarado sale como mariposa; el resto son mitades sueltas y cuartos.",
            },
            {
                "q": "¿Conviene mariposa entera o cuartos para mi alfajor?",
                "a": "Mariposa entera para coronar visualmente (presentación premium). Cuartos o granulado si la nuez se va a triturar o esconder en relleno. La diferencia de costo justifica el uso solo donde la apariencia importa.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de nuez mariposa en alfajores?",
                "a": "Aproximadamente 250-330 alfajores premium (3-4 g por unidad para coronar la cobertura). En granola rinde 25 kg de granola terminada (4 % del peso).",
            },
            {
                "q": "¿Por qué la nuez tiene aroma diferente cuando es vieja?",
                "a": "Por oxidación de las grasas omega-3, que son las más sensibles. Una nuez vieja huele a aceite rancio y tiene sabor amargo persistente. Por eso la conservación refrigerada es importante.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Refrigerada (4 °C) en envase hermético: 12 meses. A temperatura ambiente: 6 meses máximo. Congelada: hasta 24 meses sin pérdida de calidad. Para industria con rotación rápida, ambiente controlado funciona.",
            },
            {
                "q": "¿Es apta para celíacos?",
                "a": "La nuez natural es naturalmente sin gluten. Certificación apta celíacos en producto industrial requiere análisis de contaminación cruzada en planta.",
            },
        ],
        "related_slugs": ["almendra-americana", "nuez-pecan", "castana-de-caju-w1-cruda", "pistacho-sin-cascara"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 18. PISTACHO SIN CÁSCARA
    # ═════════════════════════════════════════════════════════════════
    "pistacho-sin-cascara": {
        "product_slug": "pistacho-sin-cascara",
        "title": "Pistacho sin Cáscara: el verde que conquistó la pastelería de autor y los helados premium",
        "dek": "Pistacia vera pelado, listo para procesar. La nueva estrella de la heladería artesanal, los macarons franceses y la decoración gourmet.",
        "meta_title": "Pistacho sin Cáscara — Mayorista | Especias del Paraguay",
        "meta_description": "Pistacho sin cáscara al por mayor en Paraguay para heladería, pastelería de autor, macarons y decoración gourmet. Origen Irán/USA premium.",
        "category": "Frutos Secos",
        "reading_time": 6,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "green",
        "intro": """
            <p class="lead">Hace 10 años el <strong>pistacho</strong> era nicho. Hoy es el fruto seco más fashion del mundo: pasta de pistacho italiana, helado artesanal verde-natural, macarons franceses, croissants premium, tiramisú de pistacho, gelato saborizado. La categoría explotó y la demanda no para de crecer.</p>
            <p>En Especias del Paraguay importamos <strong>pistacho sin cáscara (Pistacia vera)</strong>, la presentación industrial que llega lista para procesar. Esta guía es para heladerías artesanales, pastelerías de autor, fábricas de pasta de pistacho y reposterías premium.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué hace al pistacho tan especial?",
                "body": """
                    <p>El <strong>pistacho</strong> (<em>Pistacia vera</em>, <strong>pistachio</strong> en inglés) es una de las semillas más antiguas cultivadas, originaria de Irán y Asia Central, presente en la dieta humana hace más de 9.000 años. Hoy se cultiva intensivamente en Irán, Estados Unidos (California), Turquía, Siria y Grecia.</p>
                    <p>Lo que lo hace único:</p>
                    <ul>
                        <li><strong>Color verde natural</strong>: clorofila preservada gracias al cosecho temprano. El pistacho de Bronte (Sicilia) es el más verde y costoso del mundo.</li>
                        <li><strong>Sabor distintivo</strong>: dulce, mantecoso, con notas resinosas únicas, imposible de reemplazar.</li>
                        <li><strong>Versatilidad cromática</strong>: el verde natural sin colorante es premium signal en repostería clean-label.</li>
                        <li><strong>Pasta cremosa industrial</strong>: el pistacho procesado da una pasta verde brillante que es la base de prácticamente toda la repostería premium contemporánea.</li>
                    </ul>
                    <p>Origen comercial dominante: Irán (productor histórico) y California (productor moderno mayoritario). Cada origen tiene perfil de sabor sutilmente distinto.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en heladería, pastelería y gastronomía",
                "body": """
                    <p>El pistacho explotó en categorías de gama alta:</p>
                    <ul>
                        <li><strong>Heladería artesanal</strong>: gelato de pistacho es el sabor "test de calidad" de cualquier heladería de autor. La pasta italiana de pistacho de Bronte es la referencia mundial.</li>
                        <li><strong>Pastelería francesa e italiana</strong>: macarons de pistacho, financiers, croissants rellenos, mille-feuille de pistacho, cannoli sicilianos.</li>
                        <li><strong>Crema y pasta de pistacho</strong>: insumo industrial premium, base para tortas, helados, bombones y pastas para untar gourmet.</li>
                        <li><strong>Decoración premium</strong>: pistacho picado coronando bombones, cubriendo trufas, en bordes de tortas, sobre helados.</li>
                        <li><strong>Cocina mediterránea y árabe</strong>: baklava, kunafa, kibbeh con pistacho, ensaladas mediterráneas premium.</li>
                        <li><strong>Bombonería de autor</strong>: trufas con pasta de pistacho, bombones rellenos, chocolates premium.</li>
                    </ul>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar pistacho industrial",
                "body": """
                    <p>El pistacho es delicado — el calor agresivo destruye su color verde natural. Reglas profesionales:</p>
                    <ol>
                        <li><strong>Tostado SUAVE</strong>: 140 °C durante 6-8 minutos máximo. Sobrepasar destruye la clorofila y el pistacho vira a marrón. Para heladería, muchos formuladores no tuestan: usan crudo.</li>
                        <li><strong>Pasta de pistacho industrial</strong>: pistacho crudo + procesador potente 8-12 minutos hasta obtener pasta cremosa. Sin azúcar, sin grasa adicional. Conserva 6 meses refrigerada.</li>
                        <li><strong>Repelado</strong>: para color verde más intenso, blanquear 60 segundos en agua hirviendo y pelar la membrana fina. Trabajo manual costoso pero da pistacho ultra-verde.</li>
                        <li><strong>Decoración</strong>: picado fino o entero crudo, NUNCA agregar al horno por más de 5 minutos para preservar color.</li>
                    </ol>
                """,
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Pistacho sin cáscara para heladería, pastelería y reventa:</p>
                    <ul>
                        <li><strong>Caja 10 kg</strong> — formato estándar para heladerías y reposterías.</li>
                    </ul>
                    <p>Importación directa, certificado de origen, calidad estable. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/pistacho-sin-cascara" class="btn-link">Ver ficha del producto →</a> · <a href="/producto/pistacho-con-cascara" class="btn-link">Pistacho con cáscara →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Por qué el pistacho es tan caro?",
                "a": "Cosecho selectivo, descascarado mecánico cuidadoso, rendimiento bajo (1 árbol da 6-9 kg en años buenos), demanda global en alza acelerada y preferencia por orígenes específicos (Bronte siciliano cuesta 5x el californiano).",
            },
            {
                "q": "¿Cuánto rinde 1 kg de pistacho en pasta industrial?",
                "a": "Aproximadamente 950 g de pasta cremosa (mínima pérdida en proceso). Esa pasta rinde 25-50 litros de helado de pistacho premium o 800-1000 macarons.",
            },
            {
                "q": "¿Conviene pistacho con o sin cáscara para heladería?",
                "a": "Sin cáscara, sin duda. Procesar pistachos con cáscara en escala industrial es inviable. La cáscara se compra para snacks salados, no para procesado.",
            },
            {
                "q": "¿Por qué algunos pistachos son más verdes que otros?",
                "a": "El verde depende de variedad (Bronte siciliano es ultra-verde), cosecha temprana (mantiene clorofila), y procesamiento gentil (calor agresivo destruye el color). Los pistachos californianos tienden al verde-amarillo, los iraníes al verde más intenso.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Refrigerado (4 °C) o congelado para preservar color y sabor. A temperatura ambiente dura 4-6 meses; refrigerado 12 meses; congelado 24 meses.",
            },
            {
                "q": "¿Tiene certificado de origen?",
                "a": "Sí. Cada lote viene con certificado de origen y análisis bromatológico básico. Bajo pedido se puede solicitar análisis de aflatoxinas (regulación importante para industria).",
            },
        ],
        "related_slugs": ["almendra-americana", "castana-de-caju-w1-cruda", "macadamia", "nuez-mariposa"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 19. HARINA DE ALMENDRA PARMEX
    # ═════════════════════════════════════════════════════════════════
    "harina-de-almendra-parmex": {
        "product_slug": "harina-de-almendra-parmex",
        "title": "Harina de Almendra: la base sin gluten que conquistó la repostería contemporánea",
        "dek": "Prunus dulcis molida fina, sin gluten certificable, alta en proteína. La harina que define macarons franceses, dietas keto y pasteles premium sin TACC.",
        "meta_title": "Harina de Almendra Parmex — Mayorista | Especias del Paraguay",
        "meta_description": "Harina de almendra Parmex al por mayor en Paraguay para repostería sin gluten, macarons, dietas keto, panificación premium. Importación directa España.",
        "category": "Harinas Especiales",
        "reading_time": 6,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">La <strong>harina de almendra</strong> es la base secreta de prácticamente toda la repostería contemporánea premium: macarons franceses, financiers, frangipane, pasteles low-carb, recetas keto, panes celíacos certificados, bombones rellenos. Sin gluten naturalmente, alta en proteína, perfil graso saludable.</p>
            <p>En Especias del Paraguay importamos <strong>harina de almendra Parmex</strong>, marca española referente en la industria de repostería profesional. Esta guía es para reposterías, panificadoras especializadas, fábricas de productos sin gluten y dietas funcionales.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es harina de almendra y cómo se hace?",
                "body": """
                    <p>La <strong>harina de almendra</strong> (<em>almond flour</em> en inglés, <em>farinha de amêndoa</em> en portugués) es <strong>almendra cruda blanqueada (sin piel) molida a polvo fino</strong>. Hay dos categorías comerciales:</p>
                    <ul>
                        <li><strong>Harina de almendra blanqueada (sin piel)</strong>: color blanco-marfil, textura más fina, ideal para macarons y repostería fina.</li>
                        <li><strong>Almond meal (con piel)</strong>: color marrón claro con motas, textura más rústica, ideal para panes integrales y galletitas.</li>
                    </ul>
                    <p>La harina Parmex es el primer formato: <strong>almendra blanqueada de origen España molida fina</strong>, granulometría consistente, perfil estable lote a lote — crítico para repostería profesional donde la receta no perdona variaciones.</p>
                    <p>Por 100 g: 21 g de proteína, 50 g de grasas saludables, 12 g de fibra, sin gluten. Es el "polvo proteico" natural de la repostería premium.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en repostería, panificación y dietas funcionales",
                "body": """
                    <p>La harina de almendra es protagonista en categorías premium:</p>
                    <ul>
                        <li><strong>Macarons franceses</strong>: la base ineludible. Sin harina de almendra fina y blanqueada, no hay macaron de calidad. Granulometría es crítica — la Parmex está dimensionada para esa aplicación.</li>
                        <li><strong>Repostería sin gluten certificable</strong>: tortas, galletitas, brownies, magdalenas, pasteles para celíacos.</li>
                        <li><strong>Frangipane y rellenos</strong>: la crema de almendra que va dentro de croissants, galettes, pithiviers y tartas finas.</li>
                        <li><strong>Dietas keto y low-carb</strong>: panes keto, galletitas low-carb, pizzas low-carb, productos premium para nutrición especializada.</li>
                        <li><strong>Bombonería</strong>: trufas con base de almendra molida, bombones con relleno tipo praliné suave.</li>
                        <li><strong>Pastelería italiana</strong>: torta caprese, pasta frolla con almendras, biscotti.</li>
                        <li><strong>Productos para bebés</strong>: papillas naturales, bizcochos sin gluten para introducción alimentaria.</li>
                    </ul>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar harina de almendra: técnica de macaron",
                "body": """
                    <p>El macaron francés es la prueba definitiva de calidad de una harina de almendra. Técnica industrial:</p>
                    <ol>
                        <li><strong>Tamizar dos veces</strong>: harina de almendra + azúcar impalpable juntos, dos pasadas en tamiz fino. Sin esto, los macarons tienen superficie áspera.</li>
                        <li><strong>Macaronage controlado</strong>: incorporar la mezcla seca al merengue italiano con espátula, movimientos envolventes contados (40-50 movimientos). Sobre-mezclar arruina el macaron.</li>
                        <li><strong>Reposo crítico</strong>: 30-45 minutos a temperatura ambiente para formar la "piel" antes de hornear. Sin reposo, no hay pie (la base característica del macaron).</li>
                        <li><strong>Horneado</strong>: 150 °C convector durante 13-15 minutos. Bandeja doble para evitar dorar la base.</li>
                    </ol>
                    <p>Para repostería casera y panes celíacos, la harina de almendra puede sustituir entre 25 % y 50 % de la harina de trigo en muchas recetas, agregando proteína y reduciendo carbohidratos sin sacrificar textura.</p>
                """,
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Harina de almendra Parmex blanqueada para industria y repostería:</p>
                    <ul>
                        <li><strong>Bolsa 5 kg</strong> — formato estándar para reposterías y panificadoras especializadas.</li>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial para fábricas de macarons y productos sin gluten.</li>
                    </ul>
                    <p>Importación directa España, marca Parmex, calidad estable lote a lote. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/harina-de-almendra-parmex" class="btn-link">Parmex →</a> · <a href="/producto/harina-de-almendra-regal" class="btn-link">Regal →</a> · <a href="/producto/harina-de-almendra-calconut" class="btn-link">Calconut →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Diferencia entre harina de almendra Parmex, Regal y Calconut?",
                "a": "Las tres son harinas de almendra blanqueada españolas premium. Parmex y Calconut tienen perfil similar de granulometría fina ideal para macarons. Regal tiene granulometría ligeramente más gruesa, ideal para frangipane y bizcochuelos. La elección depende de la aplicación final.",
            },
            {
                "q": "¿La harina de almendra es sin gluten?",
                "a": "Naturalmente sí. Para certificación apta celíacos en producto industrial, requiere análisis de contaminación cruzada en la planta procesadora. Las marcas españolas premium suelen tener certificación.",
            },
            {
                "q": "¿Puedo sustituir 100 % la harina de trigo por harina de almendra?",
                "a": "En general no, salvo recetas específicas (macarons, financiers, frangipane). En la mayoría de recetas, sustituir 100 % cambia textura porque la almendra no tiene gluten ni almidón estructurante. Ideal mezclar con harinas sin gluten (arroz, mandioca) para productos celíacos.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de harina de almendra en macarons?",
                "a": "Aproximadamente 600-800 unidades de macarons (pares de 1,5-2 g cada lado). Para producción industrial es uno de los insumos de mayor costo por unidad.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y fresco. La grasa de almendra puede oxidar si está expuesta al calor. Refrigerada dura 12-18 meses; a temperatura ambiente 6-9 meses.",
            },
            {
                "q": "¿Sirve para dietas keto?",
                "a": "Sí, es uno de los ingredientes clave de la repostería keto. Bajo en carbohidratos (principalmente fibra), alto en proteína y grasas saludables. Se usa para panes keto, pizzas low-carb y postres sin azúcar.",
            },
        ],
        "related_slugs": ["almendra-americana", "harina-de-coco", "harina-de-arroz-integral", "almendra-laminada"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 20. CURRY
    # ═════════════════════════════════════════════════════════════════
    "curry": {
        "product_slug": "curry",
        "title": "Curry en Polvo: el blend indio que transformó la cocina internacional moderna",
        "dek": "Cúrcuma, comino, cilantro, jengibre, pimienta y cardamomo en proporciones secretas. La mezcla que define la cocina de fusión contemporánea.",
        "meta_title": "Curry en Polvo — Mayorista | Especias del Paraguay",
        "meta_description": "Curry en polvo al por mayor en Paraguay para industria de sazonadores, restaurantes asiáticos, cocina de fusión y blends premium. Importación directa.",
        "category": "Especias y Condimentos",
        "reading_time": 6,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">El <strong>curry</strong> no es una especia: es una receta. Es la mezcla compleja de cúrcuma, comino, cilantro, jengibre, pimienta, cardamomo y otras 8-12 especias menores, en proporciones que cada masala-master indio guarda como secreto familiar. La versión comercializada como "curry en polvo" llegó al mundo occidental vía colonia británica en el siglo XIX y nunca se fue.</p>
            <p>En Especias del Paraguay importamos <strong>curry en polvo</strong> con perfil equilibrado, ideal para industria de sazonadores, restaurantes especializados, blends de fusión y cocina internacional moderna.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué hay realmente dentro del curry?",
                "body": """
                    <p>El <strong>curry</strong> en polvo comercial es un blend de 8 a 15 especias. La fórmula varía por origen pero los ingredientes constantes son:</p>
                    <ul>
                        <li><strong>Cúrcuma</strong> (20-30 %): aporta el color amarillo característico y profundidad.</li>
                        <li><strong>Cilantro en polvo</strong> (15-25 %): base aromática, sabor cítrico-floral.</li>
                        <li><strong>Comino</strong> (10-15 %): cuerpo y sabor terroso.</li>
                        <li><strong>Fenogreco</strong> (5-10 %): el sabor curry distintivo más reconocible.</li>
                        <li><strong>Jengibre</strong> (5-8 %): picor cálido.</li>
                        <li><strong>Pimienta negra</strong> (3-5 %): pungencia.</li>
                        <li><strong>Cardamomo</strong> (2-4 %): notas dulces.</li>
                        <li><strong>Clavo, canela, mostaza</strong> (porcentajes menores).</li>
                    </ul>
                    <p>Variantes regionales: <strong>curry suave</strong> (sin chili), <strong>curry picante / madras</strong> (con chili rojo), <strong>curry verde tailandés</strong> (con cilantro fresco, hierbabuena, chile verde — pasta no en polvo), <strong>curry japonés</strong> (más dulce, tipo S&B).</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en industria, restaurantes y cocina de fusión",
                "body": """
                    <p>El curry tiene aplicaciones que van mucho más allá de la cocina india:</p>
                    <ul>
                        <li><strong>Restaurantes indios y asiáticos</strong>: base de chicken tikka masala, butter chicken, palak paneer, vindaloo, korma, biryani, dahl.</li>
                        <li><strong>Industria de sazonadores</strong>: blends de fusión, sazonadores "curry style" para pollo y verduras, mezclas premium para cocina internacional en supermercado.</li>
                        <li><strong>Salsas y aderezos industriales</strong>: salsa curry para pollo, mayonesa de curry, dips, mostaza curry.</li>
                        <li><strong>Snacks saborizados</strong>: papas curry, garbanzos tostados curry, mix de frutos secos saborizados, chips premium.</li>
                        <li><strong>Cocina de fusión paraguaya</strong>: pollo al curry con coco, salteados de verduras, arroces saborizados, marinados creativos.</li>
                        <li><strong>Cocina vegana y plant-based</strong>: lentejas al curry, garbanzos masala, currys de coco con verduras, salsas para tofu.</li>
                        <li><strong>Industria de productos cárnicos premium</strong>: hamburguesas curry, salchichas saborizadas, pollo marinado.</li>
                    </ul>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo usar curry en polvo: técnicas profesionales",
                "body": """
                    <p>Reglas clave para sacar todo el sabor:</p>
                    <ol>
                        <li><strong>Tostado en grasa</strong>: tostar el curry en aceite o ghee a fuego medio durante 60-90 segundos antes de incorporar otros ingredientes. Esto activa los aceites esenciales y elimina el sabor "crudo" que tiene el polvo sin tostar.</li>
                        <li><strong>Combinación con leche de coco</strong>: el grupo lipídico de la leche de coco potencia los compuestos liposolubles del curry (curcumina especialmente). Por eso los currys tradicionales llevan coco.</li>
                        <li><strong>Marinados</strong>: 3-5 % de curry sobre el peso de la proteína, mezclado con yogurt natural. Reposo 4-12 horas. Excelente para pollo, cordero y tofu.</li>
                        <li><strong>Dosis industriales</strong>: salsas 1-3 % del peso, marinados 3-5 %, sazonadores en blend hasta 30 %.</li>
                    </ol>
                """,
                "howto": {
                    "name": "Cómo preparar pollo al curry con coco",
                    "total_time": "PT45M",
                    "steps": [
                        {"name": "Tostar especias", "text": "Caliente 2 cdas de aceite en sartén honda. Agregue 2 cdas de curry en polvo y tueste 60 segundos a fuego medio."},
                        {"name": "Sofreír cebolla y ajo", "text": "Incorpore 1 cebolla picada y 3 dientes de ajo. Sofreír 5 minutos hasta dorar."},
                        {"name": "Incorporar pollo", "text": "Agregue 600 g de pollo en cubos. Selle 5 minutos hasta dorar."},
                        {"name": "Cocción con coco", "text": "Vierta 400 ml de leche de coco. Cocine a fuego bajo durante 25 minutos hasta espesar. Sazone con sal."},
                        {"name": "Servir", "text": "Sirva con arroz basmati o jazmín y cilantro fresco picado."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Curry en polvo para industria, restaurantes y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial para fábricas de sazonadores y restaurantes especializados.</li>
                    </ul>
                    <p>Importación directa, blend equilibrado, certificado de origen. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/curry" class="btn-link">Ver ficha del producto →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Curry y garam masala son lo mismo?",
                "a": "No exactamente. El curry comercial es un blend con cúrcuma como ingrediente principal (color amarillo). El garam masala es un blend más aromático sin cúrcuma, usado al final de la cocción para perfumar. Recetas auténticas indias usan los dos en momentos distintos.",
            },
            {
                "q": "¿Curry suave o picante para industria paraguaya?",
                "a": "Curry suave para mercado masivo (paladar local prefiere intensidad moderada). Curry picante para restaurantes especializados y cocina de autor. La mayoría de la industria paraguaya pide la versión suave.",
            },
            {
                "q": "¿Puedo hacer mi propio curry custom?",
                "a": "Sí, y es lo que hacen muchas cocinas de autor. Mezcla base: 30 % cúrcuma + 25 % cilantro + 15 % comino + 10 % fenogreco + 10 % jengibre + 5 % pimienta + 5 % cardamomo + cantidades menores de clavo/canela. Ajustar a gusto.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de curry en producción?",
                "a": "Aproximadamente 33-100 kg de salsa curry industrial (1-3 % del peso). En sazonadores rinde 3-10 kg de blend terminado.",
            },
            {
                "q": "¿Por qué algunos currys son más oscuros que otros?",
                "a": "Por la proporción de comino tostado, fenogreco y especias oscuras (clavo, canela). Currys tipo madras y británicos son más oscuros. Currys tipo japonés (S&B) son más amarillos por mayor proporción de cúrcuma.",
            },
            {
                "q": "¿Tiene contraindicaciones?",
                "a": "El curry contiene compuestos activos (cúrcuma, jengibre, fenogreco) que pueden interactuar con anticoagulantes en dosis muy altas. En consumo culinario normal es seguro. Para suplementos basados en cúrcuma o fenogreco, consultar profesional de salud.",
            },
        ],
        "related_slugs": ["curcuma-en-polvo", "comino-en-polvo", "jengibre-en-polvo", "cilantro-en-polvo"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 21. PAPRIKA / PIMENTÓN DULCE
    # ═════════════════════════════════════════════════════════════════
    "paprika-dulce": {
        "product_slug": "paprika-dulce",
        "title": "Pimentón Dulce (Paprika): el rojo natural que define chacinas, asado y cocina española en Paraguay",
        "dek": "Capsicum annuum molido fino, color rojo intenso sin colorante artificial. La especia que pinta los chorizos, los chimichurris y los guisos del Mediterráneo.",
        "meta_title": "Pimentón Dulce / Paprika — Mayorista | Especias del Paraguay",
        "meta_description": "Pimentón dulce (paprika) al por mayor en Paraguay para industria de chacinas, embutidos, asado, sazonadores y cocina española. Color rojo natural sin aditivos.",
        "category": "Especias y Condimentos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">Cuando un chorizo paraguayo tiene ese rojo profundo y apetitoso, no es colorante artificial: es <strong>pimentón dulce</strong>, también llamado <strong>paprika</strong>. La misma especia que pinta el goulash húngaro, la paella valenciana, el chimichurri rojo argentino, las patatas a la brava españolas y prácticamente toda la chacinería del mundo. Sin pimentón, no hay rojo natural.</p>
            <p>En Especias del Paraguay importamos <strong>pimentón dulce (Capsicum annuum)</strong> de molienda fina, color rojo intenso estable y aroma equilibrado, ideal para fábricas de embutidos, sazonadores, restaurantes españoles y cocina paraguaya tradicional.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es el pimentón dulce y de dónde viene?",
                "body": """
                    <p>El <strong>pimentón dulce</strong> (también <strong>paprika</strong>, <strong>pimentón rojo</strong> o <strong>sweet paprika</strong>) es el polvo seco del fruto maduro del <em>Capsicum annuum</em>, un pariente cercano del morrón rojo. Los pimientos se cultivan, secan al sol o ahumados, se descartan semillas y nervaduras (donde está la capsaicina picante), y se muelen a polvo fino rojo intenso.</p>
                    <p>Tres orígenes referentes mundiales:</p>
                    <ul>
                        <li><strong>España (La Vera, Murcia)</strong>: el pimentón dulce español es la referencia gourmet. La Vera produce además el ahumado.</li>
                        <li><strong>Hungría (Szeged, Kalocsa)</strong>: la paprika húngara, símbolo nacional, base del goulash y la cocina centroeuropea.</li>
                        <li><strong>China y Perú</strong>: orígenes industriales mayoritarios para el mercado global.</li>
                    </ul>
                    <p>La diferencia entre <strong>dulce</strong>, <strong>picante</strong> y <strong>ahumado</strong> está en la variedad de pimiento y el procesamiento. El dulce es el más vendido por aplicación universal y paladar amplio.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Por qué la industria ama el pimentón dulce",
                "body": """
                    <p>Más allá del sabor, el pimentón dulce es un <strong>colorante natural concentrado</strong>:</p>
                    <ul>
                        <li><strong>Capsantina y capsorubina</strong>: pigmentos naturales rojo-anaranjados estables al calor moderado, ideales para industria.</li>
                        <li><strong>Beta-caroteno (provitamina A)</strong>: contribuye al color y aporta nutricional.</li>
                        <li><strong>Vitamina E</strong>: actúa como antioxidante natural en formulaciones grasas.</li>
                        <li><strong>Capsaicina baja</strong>: en variedad dulce el picor es prácticamente nulo, lo que permite usar dosis altas para color sin agregar pungencia.</li>
                        <li><strong>Reemplazo clean-label de colorantes E160c y similares</strong>: cumple la función de colorante en chacinas y productos cárnicos, sin necesidad de aditivos sintéticos.</li>
                    </ul>
                    <p>Esto explica por qué prácticamente todo embutido del mundo lleva pimentón: aporta color, sabor y conservante natural en un solo ingrediente.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en chacinas, asado y cocina paraguaya",
                "body": """
                    <p>El pimentón es protagonista en categorías que mueven volumen serio en el Paraguay:</p>
                    <ul>
                        <li><strong>Industria de chacinas y embutidos</strong>: chorizo paraguayo, salame italiano, mortadela, chorizo colorado argentino, longaniza, butifarra, sobrasada española. Dosis típica 5-15 g por kilo de carne.</li>
                        <li><strong>Asado y parrilla</strong>: salmuera para vacío y matambre, rub seco para costillas, marinado de pollo asado, chimichurri rojo (variante con pimentón).</li>
                        <li><strong>Cocina paraguaya tradicional</strong>: bori bori coloreado, locro patrio, sopa paraguaya con toque de paprika, pollo guisado.</li>
                        <li><strong>Cocina española</strong>: paella valenciana, patatas a la brava, gazpacho, pulpo a la gallega, arroz negro, callos a la madrileña.</li>
                        <li><strong>Cocina húngara y centroeuropea</strong>: goulash tradicional, pörkölt, langos, pollo paprikash, salchichas de Frankfurt.</li>
                        <li><strong>Sazonadores y temperos</strong>: blends "para asado", "para pollo", mezclas tipo cajún, BBQ rubs, sazonadores universales.</li>
                        <li><strong>Snacks saborizados</strong>: papas fritas con paprika, chips, palomitas saborizadas, tortillas premium.</li>
                        <li><strong>Salsas industriales</strong>: salsa española, mayonesa de paprika, aderezos rojos, mostazas saborizadas.</li>
                    </ul>
                    <p>Para fábricas de chacinas con producción mensual relevante, el pimentón dulce de Especias del Paraguay ofrece estabilidad de color lote a lote — crítico cuando el rojo del producto final es parte de la identidad de marca.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar pimentón dulce: técnicas profesionales",
                "body": """
                    <p>Tres reglas críticas:</p>
                    <ol>
                        <li><strong>NUNCA quemar el pimentón</strong>: a más de 160 °C el pimentón se carameliza rápido y desarrolla amargor agresivo permanente. Esta es la razón #1 de paellas y guisos arruinados. Incorporar SIEMPRE con la sartén fuera del fuego o líquido recién agregado.</li>
                        <li><strong>Activar en grasa, NO en agua</strong>: el pimentón es liposoluble. Mezclarlo primero con aceite tibio o manteca derretida libera todo su perfil aromático y de color. En agua sola queda apagado.</li>
                        <li><strong>Almacenamiento crítico</strong>: el pimentón es la especia que más rápido pierde color y aroma con luz. Envase oscuro hermético, lugar fresco. Bien guardado conserva calidad 12-18 meses; mal guardado pierde 50 % de color en 6 meses.</li>
                    </ol>
                    <p>Dosis industriales típicas:</p>
                    <ul>
                        <li>Chacinas: 5-15 g por kilo de masa (15 g da color rojo profundo).</li>
                        <li>Salmuera de asado: 1 cda por litro + sal + ajo.</li>
                        <li>Sazonadores: 10-30 % del blend total para mezclas "rojas".</li>
                        <li>Paella: 1 cdta por 4 personas, agregada con la sartén templada.</li>
                    </ul>
                """,
                "howto": {
                    "name": "Cómo preparar marinado para pollo asado con pimentón",
                    "total_time": "PT4H10M",
                    "steps": [
                        {"name": "Mezclar especias", "text": "En un bol mezcle 2 cdas de pimentón dulce, 1 cda de comino, 1 cda de ajo en polvo, 1 cda de orégano y 1 cdta de sal."},
                        {"name": "Activar en aceite", "text": "Agregue 100 ml de aceite de oliva tibio (no caliente) y mezcle hasta formar una pasta roja brillante."},
                        {"name": "Marinar pollo", "text": "Aplique la pasta sobre 1 kg de pollo (presa entera o trozos) frotando bien. Reposo en heladera 4 horas mínimo."},
                        {"name": "Asar", "text": "Hornee a 180 °C durante 45-60 minutos hasta que la piel quede crujiente y el interior cocido. Servir con limón."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Pimentón dulce en polvo para industria de chacinas, restaurantes y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial para fábricas de embutidos y sazonadores.</li>
                    </ul>
                    <p>Importación directa, color estable, certificado de origen. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/paprika-dulce" class="btn-link">Pimentón dulce →</a> · <a href="/producto/paprika-ahumada" class="btn-link">Ahumada →</a> · <a href="/producto/paprika-picante" class="btn-link">Picante →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Pimentón dulce, paprika y pimentón rojo son lo mismo?",
                "a": "Sí, son sinónimos comerciales del mismo producto: Capsicum annuum molido sin picante. 'Paprika' viene del húngaro y se popularizó internacionalmente; 'pimentón dulce' es el nombre español original; 'pimentón rojo' es nombre genérico latinoamericano. En el Paraguay se usan los tres indistintamente.",
            },
            {
                "q": "¿Qué diferencia hay entre dulce, picante y ahumado?",
                "a": "Dulce: variedad sin capsaicina, color y aroma sin picor. Picante: variedad con capsaicina, agrega calor además de color. Ahumado (pimentón de La Vera): pimientos secados al humo de roble, aporta sabor ahumado característico imposible de replicar.",
            },
            {
                "q": "¿Por qué el pimentón se quema tan fácil?",
                "a": "Por su contenido alto de azúcares naturales y carotenoides que caramelizan rápido a temperaturas mayores de 160 °C. La regla industrial es siempre incorporar fuera del fuego o con líquido ya añadido.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de pimentón en chacinas?",
                "a": "Aproximadamente 100-200 kg de masa de embutido (5-15 g por kilo según intensidad de color deseada). Para chorizo paraguayo tradicional, dosis típica es 8-10 g/kg.",
            },
            {
                "q": "¿Sirve como colorante natural certificable?",
                "a": "Sí. La oleorresina de pimentón es ampliamente usada como colorante natural en industria alimentaria, reemplazando colorantes sintéticos en productos clean-label, kosher y orgánicos certificables (depende de la certificadora específica).",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase opaco hermético, lugar fresco lejos de luz directa. La luz UV es el principal enemigo: degrada los carotenoides y blanquea el rojo. Bien guardado conserva calidad por 12-18 meses; mal guardado pierde 50 % de color en 6 meses.",
            },
        ],
        "related_slugs": ["paprika-ahumada", "paprika-picante", "comino-en-polvo", "ajo-granulado"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 22. PILLAR A — INSUMOS PARA CHIPA INDUSTRIAL
    # ═════════════════════════════════════════════════════════════════
    "insumos-chipa-paraguaya": {
        "product_slug": "semilla-de-anis",
        "title": "Insumos para Chipa Industrial: la lista completa que toda chipería profesional necesita",
        "dek": "Anís, sal correcta, especias secundarias, presentaciones por volumen y costos por kilo. La guía operativa que toda chipería paraguaya quisiera tener antes de empezar.",
        "meta_title": "Insumos para Chipa Industrial — Guía Completa | Especias del Paraguay",
        "meta_description": "Lista completa de insumos para chipa industrial en Paraguay: anís, sal, especias, dosis profesionales, costos por kilo y dónde comprar al por mayor.",
        "category": "Hierbas y Tés",
        "reading_time": 11,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">Abrir una <strong>chipería</strong> en Paraguay parece simple hasta que llega el momento de comprar insumos. ¿Cuánto anís lleva un kilo de masa? ¿Qué sal usar? ¿Hay diferencia entre el queso paraguay de Concepción y el de Misiones? ¿Cuál es el rendimiento real por kilo? Estas preguntas separan a una chipería que vende rentable de una que cierra en seis meses.</p>
            <p>Esta guía consolida lo que aprendimos atendiendo a más de cien chiperías paraguayas: <strong>la lista completa de insumos</strong>, las dosis profesionales por kilo de masa, los rendimientos por insumo, los costos relativos y dónde se compra cada cosa. Para chiperías nuevas, para fábricas industriales y para cualquier panificadora que quiera incorporar chipa al portfolio.</p>
        """,
        "sections": [
            {
                "id": "que-es-chipa",
                "heading": "La chipa paraguaya y sus 5 variantes principales",
                "body": """
                    <p>Antes de comprar nada, hay que entender qué se va a producir. La <strong>chipa</strong> no es un producto único: es una familia de panificados de almidón de mandioca y queso paraguay, con cinco variantes principales que cada chipería decide cuál(es) trabajar:</p>
                    <ul>
                        <li><strong>Chipa común (chipa argolla)</strong>: la versión más vendida. Forma de argolla, masa amarilla por el queso, anís bien marcado. Es la chipa del bus de larga distancia y del desayuno paraguayo.</li>
                        <li><strong>Chipa cuatro quesos</strong>: versión premium con mayor cantidad de queso (paraguay + parmesano + mozzarella + ricotta). Anís más sutil pero presente. Margen mayor, menor volumen.</li>
                        <li><strong>Chipa kavure</strong>: variante alargada (forma de bastón), tradicional cocida en horno de barro. Anís bien marcado. Producto cultural fuerte en zonas rurales.</li>
                        <li><strong>Chipa so'o</strong>: rellena de carne picada con cebolla. Volumen menor, ticket más alto. El anís suaviza el sabor.</li>
                        <li><strong>Chipa avatí (chipa de maíz)</strong>: hecha con harina de maíz (no almidón de mandioca), color amarillo intenso, dulce-salada. Anís aporta dulzor herbal característico.</li>
                    </ul>
                    <p>Una chipería profesional típica trabaja la común y una o dos variantes premium. La elección define la cadena de insumos.</p>
                """,
            },
            {
                "id": "anis",
                "heading": "Insumo crítico #1: Anís en semilla (la pieza no negociable)",
                "body": """
                    <p>Si solo pudiéramos darte un consejo: <strong>no escatimes en anís</strong>. Es el insumo que define el sabor de la chipa, y la diferencia entre uno bueno y uno mediocre se siente desde el primer mordisco.</p>
                    <p><strong>Especificación profesional:</strong></p>
                    <ul>
                        <li><strong>Variedad</strong>: anís verde (<em>Pimpinella anisum</em>), NO anís estrellado. Son plantas distintas y no son intercambiables.</li>
                        <li><strong>Origen recomendado</strong>: España, Egipto o Turquía. Calidad estable, perfil aromático limpio.</li>
                        <li><strong>Formato</strong>: semilla entera, NO molida. La semilla entera conserva aroma 24-30 meses; el polvo pierde 50 % en 90 días.</li>
                        <li><strong>Dosis profesional</strong>: 8-10 g por kilo de masa de chipa común. Para cuatro quesos, 5-7 g (más sutil). Para avatí, 10-12 g (dulzor herbal pronunciado).</li>
                    </ul>
                    <p><strong>Cálculo operativo</strong>: una chipería que produce 50 kg de masa por turno consume 400-500 g de anís por turno → 8-10 kg al mes con 22 días operativos. Una caja de 10 kg cubre el mes completo.</p>
                    <p><a href="/guias/semilla-de-anis">Guía completa de semilla de anís →</a></p>
                """,
            },
            {
                "id": "sal",
                "heading": "Insumo crítico #2: La sal correcta",
                "body": """
                    <p>La elección de la sal define dos cosas: <strong>perfil de sabor</strong> y <strong>posicionamiento del producto</strong>.</p>
                    <ul>
                        <li><strong>Sal común fina</strong>: la más usada en chiperías de barrio. Funcional, económica.</li>
                        <li><strong>Sal rosa del Himalaya fina</strong>: la opción premium para chipa cuatro quesos y productos diferenciados. Aporta minerales (potasio, magnesio) y permite posicionamiento "natural" o "gourmet". Cuesta ~3x la común pero el ticket de la chipa premium absorbe.</li>
                        <li><strong>Sal marina fina</strong>: alternativa intermedia, perfil más limpio que la común.</li>
                    </ul>
                    <p><strong>Dosis profesional</strong>: 12-15 g de sal por kilo de masa. Más sal mata el sabor del queso paraguay; menos deja la chipa insulsa.</p>
                    <p><a href="/guias/sal-rosa-del-himalaya-fino">Guía sal rosa del Himalaya →</a></p>
                """,
            },
            {
                "id": "especias-secundarias",
                "heading": "Insumos #3: Especias secundarias que diferencian",
                "body": """
                    <p>Una chipa estándar lleva almidón, queso, anís y sal. Una chipa <strong>diferenciada</strong> incorpora especias secundarias que el resto del mercado no usa:</p>
                    <ul>
                        <li><strong>Comino en grano molido en planta</strong>: 1-2 g/kg, aporta profundidad y cuerpo. Muy usado en chipa de Concepción.</li>
                        <li><strong>Orégano peruano</strong>: 1 g/kg en chipa cuatro quesos para perfil mediterráneo. Diferenciador de gama alta.</li>
                        <li><strong>Pimienta negra molida fina</strong>: 0,5 g/kg en chipa so'o (relleno de carne). Aporta calor sutil sin picar.</li>
                        <li><strong>Colorífico (urucum)</strong>: 1-2 g/kg en chipa avatí para color amarillo intenso natural sin tartrazina.</li>
                    </ul>
                    <p>Estas especias <strong>no son obligatorias</strong>, pero permiten construir una línea Premium con mayor margen y diferenciación contra la chipería del barrio.</p>
                """,
            },
            {
                "id": "no-importamos",
                "heading": "Insumos que NO importamos (pero hay que conseguir)",
                "body": """
                    <p>Para honestidad operativa, esto es lo que toda chipería necesita y que NO compra de Especias del Paraguay (porque no es nuestro core):</p>
                    <ul>
                        <li><strong>Almidón de mandioca</strong>: 40-50 % del peso de la masa. Compra local en proveedores de almidón paraguayo (Concepción, Caaguazú).</li>
                        <li><strong>Queso paraguay</strong>: 25-35 % del peso. Compra directa de queserías (San Pedro, Misiones, Caaguazú son los polos productivos).</li>
                        <li><strong>Manteca o grasa de cerdo</strong>: 8-12 %. Frigoríficos locales.</li>
                        <li><strong>Huevos y leche</strong>: distribución local.</li>
                    </ul>
                    <p>Lo que NOSOTROS te aseguramos: anís, sal rosa, especias secundarias y el catálogo completo si querés expandir a otros panificados (panettones, biscochitos festivos, mbeyú dulce).</p>
                """,
            },
            {
                "id": "lista-compras",
                "heading": "Lista de compras anual para chipería estándar (50 kg/día)",
                "body": """
                    <p>Para una chipería que produce 50 kg de masa por turno, 22 días al mes (~13 toneladas de masa al año):</p>
                    <ul>
                        <li><strong>Anís en semilla</strong>: ~125 kg/año → 12-13 cajas de 10 kg (recomendamos formato 25 kg para volumen).</li>
                        <li><strong>Sal rosa fina (premium) o común</strong>: ~190 kg/año.</li>
                        <li><strong>Comino en grano (si trabajás línea diferenciada)</strong>: ~25 kg/año.</li>
                        <li><strong>Orégano peruano (línea premium)</strong>: ~12 kg/año.</li>
                        <li><strong>Colorífico (chipa avatí)</strong>: ~25 kg/año si avatí es producto regular.</li>
                    </ul>
                    <p>Total inversión anual en especias y sal premium: <strong>aproximadamente 3-5 % del costo total de insumos</strong> (el grueso es queso y almidón). Pero ese 3-5 % es lo que define la calidad percibida del producto final.</p>
                """,
            },
            {
                "id": "presentaciones",
                "heading": "Cómo armar tu cadena con Especias del Paraguay",
                "body": """
                    <p>Trabajamos con chiperías de todos los tamaños:</p>
                    <ul>
                        <li><strong>Chipería de barrio (10-30 kg/día)</strong>: cajas de 10 kg de anís, kg de sal premium en bolsa.</li>
                        <li><strong>Chipería industrial (50-200 kg/día)</strong>: bolsas 25 kg, contrato anual con precio fijo, entrega programada.</li>
                        <li><strong>Fábrica de chipa congelada (200+ kg/día)</strong>: pallets, logística dedicada, cotización por proyecto.</li>
                    </ul>
                    <p>Importación directa de cada origen, certificado de origen y análisis bromatológico, factura legal, entrega a todo el Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/semilla-de-anis" class="btn-link">Ver anís →</a> · <a href="/producto/sal-rosa-del-himalaya-fino" class="btn-link">Sal rosa →</a> · <a href="/producto/comino-en-grano" class="btn-link">Comino →</a> · <a href="/producto/oregano-peruano" class="btn-link">Orégano →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Cuánto anís lleva un kilo de masa de chipa?",
                "a": "8-10 g de semillas enteras por kilo de masa para chipa común. 5-7 g para chipa cuatro quesos (más sutil). 10-12 g para chipa avatí. La semilla va entera, NO se muele.",
            },
            {
                "q": "¿Qué pasa si uso anís estrellado en lugar de anís verde?",
                "a": "El sabor cambia totalmente. Son plantas distintas (Pimpinella anisum vs Illicium verum). El anís estrellado tiene perfil más licoroso y picante; en chipa queda un sabor extraño. La receta tradicional usa anís verde en semilla.",
            },
            {
                "q": "¿Vale la pena la sal rosa para chipa?",
                "a": "Para chipa común no hace mucha diferencia. Para chipa cuatro quesos o líneas premium, sí — permite posicionamiento 'natural' y aporta minerales reales. La diferencia de costo (3x sal común) se absorbe fácil en el ticket premium.",
            },
            {
                "q": "¿Cómo conservar el anís en la chipería?",
                "a": "Bolsa cerrada, lugar seco, lejos de luz directa, lejos del horno. La semilla entera conserva aroma 24-30 meses bien guardada. Una vez abierta una bolsa de 25 kg, idealmente consumir en 6-8 meses.",
            },
            {
                "q": "¿Cuál es el pedido mínimo para una chipería nueva?",
                "a": "Atendemos cualquier volumen. Para una chipería que está empezando, una caja de 10 kg de anís + bolsa de sal premium cubre el primer mes con margen. Cuando crezca el volumen, pasamos a formatos más grandes con mejor precio por kilo.",
            },
            {
                "q": "¿Hacen contratos anuales con precio fijo?",
                "a": "Sí, para chiperías industriales con volumen estable. Asegura precio contra fluctuación de tipo de cambio y disponibilidad. Cotización personalizada según volumen mensual estimado.",
            },
        ],
        "related_slugs": ["semilla-de-anis", "sal-rosa-del-himalaya-fino", "comino-en-grano", "oregano-peruano"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 23. PILLAR B — 7 ESPECIAS DEL ASADO PARAGUAYO
    # ═════════════════════════════════════════════════════════════════
    "especias-asado-paraguayo": {
        "product_slug": "comino-en-grano",
        "title": "Las 7 Especias Imprescindibles del Asado Paraguayo: la guía del parrillero profesional",
        "dek": "Sal, comino, ajo, pimentón, orégano, pimienta y romero. La combinación que separa una parrillada amateur de una asado de autor. Dosis, técnicas y orden de aplicación.",
        "meta_title": "7 Especias del Asado Paraguayo — Guía Profesional | Especias del Paraguay",
        "meta_description": "Las 7 especias imprescindibles del asado paraguayo: sal, comino, ajo, pimentón, orégano, pimienta y romero. Dosis profesionales, técnicas y dónde comprar al por mayor.",
        "category": "Especias y Condimentos",
        "reading_time": 10,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">El <strong>asado paraguayo</strong> es una institución cultural. Domingo de familia, año nuevo, primera comunión, jubilación: todo se celebra alrededor del fuego, la parrilla y la carne. Pero la diferencia entre un asado memorable y uno que se olvida no está en la carne — está en las <strong>especias</strong>.</p>
            <p>Esta guía consolida el conocimiento de parrilleros profesionales y carnicerías serias del Paraguay. Las <strong>siete especias imprescindibles</strong>, la dosis profesional de cada una, el orden correcto de aplicación, el chimichurri perfecto y el botiquín completo de la parrilla. Para parrilladas comerciales, restaurantes, casas de carne, y todo paraguayo que quiera cocinar como un profesional.</p>
        """,
        "sections": [
            {
                "id": "que-define",
                "heading": "¿Qué define un asado paraguayo profesional?",
                "body": """
                    <p>Tres elementos:</p>
                    <ul>
                        <li><strong>Cortes correctos</strong>: vacío, asado de tira, costilla, matambre, mollejas, chinchulines, chorizo.</li>
                        <li><strong>Fuego controlado</strong>: brasas (no llama directa), distancia adecuada de la parrilla, paciencia.</li>
                        <li><strong>Especias bien aplicadas</strong>: en el momento correcto, en la cantidad correcta, en la combinación correcta.</li>
                    </ul>
                    <p>Las primeras dos las aprende cualquier asador con práctica. La tercera es donde casi todos fallan, y es donde se pierde la diferencia entre lo amateur y lo profesional.</p>
                """,
            },
            {
                "id": "las-7",
                "heading": "Las 7 especias imprescindibles, en orden de importancia",
                "body": """
                    <ol>
                        <li><strong>Sal gruesa o sal rosa del Himalaya en grano</strong>. La especia más importante. Se aplica antes de poner la carne al fuego (para vacío y costillas) o al final (para mollejas y achuras). Dosis: una cucharada sopera por kilo de carne. La sal rosa del Himalaya en gruesa aporta minerales y un sabor más limpio que la sal común.</li>
                        <li><strong>Comino en grano molido en mortero</strong>. La segunda en importancia para perfil paraguayo/argentino. Se incorpora en el chimichurri o se espolvorea levemente sobre cortes magros como matambre y vacío. Dosis: 1 cucharadita por kilo. Tostar el grano antes de moler multiplica el aroma.</li>
                        <li><strong>Ajo (granulado o en polvo)</strong>. Indispensable en chimichurri, salmuera y sazonadores. Granulado mantiene textura; el polvo se integra mejor en líquidos. Dosis: 1 cucharada por kilo de carne en marinados.</li>
                        <li><strong>Pimentón dulce (paprika)</strong>. Aporta color rojo apetitoso y dulzor natural. Indispensable en chimichurri rojo, salmueras de costilla y rubs secos. Dosis: 1 cucharada sopera por kilo. NUNCA quemar — incorporar fuera del fuego.</li>
                        <li><strong>Orégano peruano</strong>. Más aromático que el orégano común. Va en chimichurri, salmuera y especialmente en chorizo casero. Dosis: 1 cucharadita sopera por kilo.</li>
                        <li><strong>Pimienta negra en grano molida fresco</strong>. Aporta pungencia. Va al final de la cocción o en el chimichurri. Moler en el momento es esencial — el polvo viejo pierde aroma. Dosis: 1 cucharadita por kilo.</li>
                        <li><strong>Romero seco</strong>. Opcional pero diferenciador. Va en cortes grasos como costilla y cerdo. Aporta aroma resinoso premium. Dosis: 1/2 cucharadita por kilo.</li>
                    </ol>
                """,
            },
            {
                "id": "chimichurri",
                "heading": "El chimichurri perfecto: 3 versiones profesionales",
                "body": """
                    <p>El chimichurri es el examen final del parrillero. Tres versiones según el estilo:</p>
                    <p><strong>Chimichurri clásico paraguayo (sin pimienta picante):</strong></p>
                    <ul>
                        <li>250 ml aceite de oliva o girasol</li>
                        <li>4 cdas vinagre de vino tinto</li>
                        <li>4 dientes de ajo bien picados</li>
                        <li>2 cdas perejil fresco picado</li>
                        <li>1 cda orégano seco</li>
                        <li>1 cda comino tostado y molido grueso</li>
                        <li>1 cdta pimentón dulce</li>
                        <li>Sal y pimienta a gusto</li>
                    </ul>
                    <p>Mezclar todo, reposar 24 hs en heladera antes de servir. Vida útil: 2 semanas refrigerado.</p>
                    <p><strong>Chimichurri picante (estilo argentino):</strong> agregar 1-2 cdtas de ají molido picante al clásico. Aporta calor sin perder el perfil.</p>
                    <p><strong>Chimichurri rojo (con pimentón):</strong> aumentar el pimentón dulce a 2 cdas + 1 cdta de pimentón ahumado. Color profundo, sabor más intenso.</p>
                    <p><a href="/guias/comino-en-grano">Guía completa de comino →</a></p>
                """,
            },
            {
                "id": "salmuera",
                "heading": "Salmuera tradicional: el secreto de la parrilla profesional",
                "body": """
                    <p>La <strong>salmuera</strong> (agua salada saborizada que se pinta sobre la carne durante la cocción) es lo que diferencia el asado de un parrillero serio:</p>
                    <ol>
                        <li>1 litro de agua tibia</li>
                        <li>2 cucharadas soperas de sal gruesa</li>
                        <li>4 dientes de ajo machacados</li>
                        <li>1 cda de orégano peruano</li>
                        <li>1 cda de pimentón dulce</li>
                        <li>1/2 cda de comino tostado</li>
                        <li>Hojas de laurel (opcional)</li>
                    </ol>
                    <p>Hervir todo 5 minutos, dejar enfriar, colar. Pintar la carne con un manojo de orégano fresco o pincel cada 15-20 minutos durante la cocción. Resultado: carne jugosa, sabor profundo, costra perfecta.</p>
                """,
            },
            {
                "id": "kit",
                "heading": "El botiquín completo de la parrilla profesional",
                "body": """
                    <p>Para un parrillero comercial o un fanático del asado, este es el kit completo de Especias del Paraguay:</p>
                    <ul>
                        <li><strong>Sal rosa gruesa</strong> — bolsa 5 kg, sal de cocción y de mesa</li>
                        <li><strong>Comino en grano</strong> — bolsa 1 kg, moler en mortero al momento</li>
                        <li><strong>Ajo granulado</strong> — kg, base de salmuera y chimichurri</li>
                        <li><strong>Pimentón dulce</strong> — kg, color y sabor</li>
                        <li><strong>Pimentón ahumado</strong> — 500 g, opcional para chimichurri rojo premium</li>
                        <li><strong>Orégano peruano</strong> — kg, salmuera y chimichurri</li>
                        <li><strong>Pimienta negra en grano</strong> — 500 g, moler al momento</li>
                        <li><strong>Romero seco</strong> — 500 g, cortes grasos y cerdo</li>
                        <li><strong>Laurel</strong> — 250 g, salmueras largas</li>
                    </ul>
                    <p>Total kit profesional: <strong>aproximadamente 9-10 kg de especias</strong> que duran 6-12 meses para una parrilla activa. Para parrilladas comerciales con turnos diarios, escalar a formatos de 10 y 25 kg.</p>
                """,
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones para parrilladas comerciales",
                "body": """
                    <p>Trabajamos con parrilladas, restaurantes y casas de carne en todo el Paraguay:</p>
                    <ul>
                        <li><strong>Parrillada de barrio</strong>: cajas de 10 kg de cada especia base.</li>
                        <li><strong>Restaurante con asado en menú</strong>: bolsas de 25 kg, kit profesional armado a medida.</li>
                        <li><strong>Casa de carne con producción de chimichurri</strong>: contrato mensual con entrega programada.</li>
                    </ul>
                    <p>Importación directa, calidad estable lote a lote, factura legal. Entrega Asunción y todo el país.</p>
                    <p class="cta-inline"><a href="/producto/comino-en-grano" class="btn-link">Comino →</a> · <a href="/producto/paprika-dulce" class="btn-link">Pimentón →</a> · <a href="/producto/oregano-peruano" class="btn-link">Orégano →</a> · <a href="/producto/sal-rosa-del-himalaya-grueso" class="btn-link">Sal rosa →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Cuándo aplico la sal: antes o durante el asado?",
                "a": "Para cortes magros (vacío, matambre): antes, mínimo 30 minutos para que penetre. Para cortes grasos (costilla, asado de tira): durante o después, así no se reseca. Para mollejas y achuras: al final, sobre la carne caliente.",
            },
            {
                "q": "¿Por qué tostar el comino antes de molerlo?",
                "a": "Porque el calor seco activa los aceites esenciales y libera aromas que el grano frío no entrega. Sartén seca, fuego medio, 60-90 segundos hasta que el comino libere fragancia. Diferencia abismal vs comino molido sin tostar.",
            },
            {
                "q": "¿Sal rosa o sal común para asado?",
                "a": "Para parrillada de día a día, sal común gruesa funciona bien. Para parrilla profesional o restaurante, sal rosa del Himalaya gruesa aporta minerales reales y permite posicionamiento premium. La diferencia de costo se justifica con el ticket más alto.",
            },
            {
                "q": "¿Cuánto chimichurri por kilo de carne?",
                "a": "100-150 ml de chimichurri por kilo de carne para acompañar a la mesa. Para marinado pre-cocción, 50 ml por kilo aplicado 2-4 horas antes.",
            },
            {
                "q": "¿Cómo conservar el chimichurri por más tiempo?",
                "a": "Frasco de vidrio limpio, refrigerado, cubrir con una capa de aceite encima del nivel del chimichurri (impide oxidación). Conservación: 2-3 semanas. Si se forma capa blanca encima (oxidación menor), removerla y mezclar — el chimichurri sigue bueno.",
            },
            {
                "q": "¿Vale la pena el romero o es opcional?",
                "a": "Depende del corte. Para costilla con grasa, cerdo y cordero, el romero es diferenciador real (aporta nota resinosa que corta la grasa). Para cortes magros como vacío y matambre, no aporta tanto. Es opcional pero quien lo usa rara vez vuelve atrás.",
            },
        ],
        "related_slugs": ["comino-en-grano", "paprika-dulce", "oregano-peruano", "sal-rosa-del-himalaya-grueso"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 24. COLORÍFICO (COLORAU) — el rojo del locro y la sopa paraguaya
    # ═════════════════════════════════════════════════════════════════
    "colorifico-colorau": {
        "product_slug": "colorifico-colorau",
        "title": "Colorífico (Colorau): el rojo natural que pinta el locro, la sopa paraguaya y los chorizos",
        "dek": "Bixa orellana molida con cereal, color amarillo-rojizo intenso. El colorante natural más usado en cocina paraguaya y brasileña, sustituto perfecto de tartrazina en chacinas.",
        "meta_title": "Colorífico (Colorau) — Mayorista | Especias del Paraguay",
        "meta_description": "Colorífico (colorau) al por mayor en Paraguay para industria de chacinas, locro, sopa paraguaya, chorizos y productos típicos. Color natural sin colorantes artificiales.",
        "category": "Especias y Condimentos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">Cuando una <strong>sopa paraguaya</strong> tiene ese color amarillo dorado intenso, cuando un <strong>locro patrio</strong> luce rojo apetitoso, cuando un chorizo brasileño-paraguayo tiene ese color rojizo cálido — no es tartrazina, no es Eritrosina, no es colorante artificial. Es <strong>colorífico</strong>, también llamado <strong>colorau</strong>: urucum (achiote) molido con harina de maíz o mandioca, el colorante natural más usado en la cocina paraguaya y brasileña.</p>
            <p>En Especias del Paraguay importamos <strong>colorífico</strong> de origen brasileño, calidad estable, color rojo-anaranjado intenso, ideal para industria de chacinas, productos típicos paraguayos, restaurantes regionales y consumo familiar.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es el colorífico exactamente?",
                "body": """
                    <p>El <strong>colorífico</strong> (también <strong>colorau</strong> en portugués brasileño) es una mezcla industrial de:</p>
                    <ul>
                        <li><strong>Urucum / achiote molido</strong> (<em>Bixa orellana</em>): semillas rojas que aportan el color y un sabor muy suave.</li>
                        <li><strong>Harina de maíz o mandioca</strong>: vehículo neutro que diluye el urucum a una concentración manejable.</li>
                        <li><strong>Sal</strong>: en algunas formulaciones, aporta sabor y conservación.</li>
                    </ul>
                    <p>El producto puro (urucum solo molido) es muy concentrado y caro. El colorífico es la versión "industrial" que cualquier cocina paraguaya o brasileña puede usar directo, sin diluir.</p>
                    <p>Origen comercial dominante: <strong>Brasil</strong>. La cocina brasileña adoptó el colorau como ingrediente básico hace siglos vía culinária baiana, y exporta el formato comercial al resto de Sudamérica. En Paraguay es ingrediente esencial de la cocina típica.</p>
                """,
            },
            {
                "id": "usos-py",
                "heading": "Usos en cocina paraguaya tradicional",
                "body": """
                    <p>El colorífico es protagonista de la cocina típica paraguaya en aplicaciones donde el color define el producto:</p>
                    <ul>
                        <li><strong>Sopa paraguaya</strong>: aporta el amarillo-dorado intenso característico. Aplicado al sofrito de cebolla con manteca antes de incorporar la harina de maíz.</li>
                        <li><strong>Locro patrio</strong>: el rojo-naranja del locro de fiestas patrias viene del colorífico aplicado al maíz blanco en cocción.</li>
                        <li><strong>Mbeyú colorado</strong>: variante visual con color intenso para presentación.</li>
                        <li><strong>Chipa avatí (de maíz)</strong>: refuerza el amarillo natural de la harina de maíz.</li>
                        <li><strong>Bori bori coloreado</strong>: aporta cuerpo visual al caldo.</li>
                        <li><strong>Pollo paraguayo guisado</strong>: la base del color del pollo dominical.</li>
                        <li><strong>Arroz a la valenciana</strong>: variante paraguaya con colorífico.</li>
                    </ul>
                    <p>Para industria de chacinas: chorizo paraguayo y brasileño, salame, mortadela. Aporta color natural sin tartrazina.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos industriales: alternativa natural a colorantes sintéticos",
                "body": """
                    <p>El gran valor industrial del colorífico es funcionar como <strong>colorante natural certificable</strong>:</p>
                    <ul>
                        <li><strong>Chacinas y embutidos</strong>: chorizo paraguayo, salame brasileño, mortadela, longaniza. Reemplaza tartrazina E102 y rojo Allura E129.</li>
                        <li><strong>Productos cárnicos pre-condimentados</strong>: hamburguesas, milanesas pre-armadas, panchos premium.</li>
                        <li><strong>Mantecas saborizadas</strong>: manteca de colorífico para untar y cocinar, popular en cocina nordestina brasileña.</li>
                        <li><strong>Snacks salados</strong>: pochoclo saborizado, papas fritas industriales, palitos.</li>
                        <li><strong>Quesos amarillos</strong>: queso colonial, queso paraguay industrial, queso amarillo en barra. Reemplaza colorante anatto químico.</li>
                        <li><strong>Pastas y fideos</strong>: pastas amarillas, fideos al huevo industrial, ñoquis caseros.</li>
                    </ul>
                    <p>Argumento clean-label fuerte: el consumidor paraguayo y brasileño está cada vez más atento a "sin colorantes artificiales", y el colorífico permite ese posicionamiento sin sacrificar el rojo apetitoso.</p>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar colorífico: técnicas profesionales",
                "body": """
                    <p>Tres reglas:</p>
                    <ol>
                        <li><strong>Activar en grasa, NO en agua</strong>: el urucum es liposoluble. Mezclarlo primero con manteca derretida o aceite tibio libera todo el color. En agua sola queda apagado.</li>
                        <li><strong>NO sobrepasar 160 °C</strong>: como el pimentón, el urucum se carameliza con calor agresivo y desarrolla amargor. Incorporar fuera del fuego o con líquido recién agregado.</li>
                        <li><strong>Dosis típicas</strong>: sopa paraguaya 5 g por kilo de masa; chorizo 3-5 g por kilo de carne; arroz colorido 2 cdas por kilo de arroz; manteca de colorífico 30 g por kilo de manteca.</li>
                    </ol>
                """,
                "howto": {
                    "name": "Cómo preparar manteca de colorífico (base brasileña)",
                    "total_time": "PT15M",
                    "steps": [
                        {"name": "Derretir manteca", "text": "Derrita 250 g de manteca a fuego mínimo en una olla. NO hervir."},
                        {"name": "Agregar colorífico", "text": "Incorpore 2 cucharadas (15 g) de colorífico. Revuelva 2 minutos hasta integrar el color."},
                        {"name": "Filtrar (opcional)", "text": "Si quiere textura más limpia, cuele la manteca por un colador fino para retirar el residuo del cereal del colorífico."},
                        {"name": "Conservar", "text": "Guarde en frasco hermético en heladera. Conserva 30 días refrigerada. Excelente para untar pan, saborizar arroz y guisos."},
                    ],
                },
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Colorífico (colorau) brasileño para industria, restaurantes y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 25 kg</strong> — formato industrial para fábricas de chacinas, productos típicos y pastas.</li>
                    </ul>
                    <p>Importación directa, color estable, certificado de origen. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/colorifico-colorau" class="btn-link">Colorífico →</a> · <a href="/producto/semilla-de-achiote-urucum" class="btn-link">Semilla de achiote →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Diferencia entre colorífico y achiote/urucum puro?",
                "a": "El colorífico es urucum molido MEZCLADO con harina (vehículo) — concentración menor, fácil de usar directo. El achiote/urucum puro es solo la semilla molida — mucho más concentrado y caro. Para uso industrial general, colorífico funciona perfecto.",
            },
            {
                "q": "¿Sirve como colorante natural certificable?",
                "a": "Sí. La oleorresina de annatto (extraída del urucum) es ampliamente aceptada como colorante natural en alimentos. Puede declararse como 'colorante natural' o 'extracto de urucum' en etiqueta.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de colorífico en sopa paraguaya?",
                "a": "Aproximadamente 200 kg de masa de sopa paraguaya (5 g por kilo). Para una panadería que produce 50 kg de sopa por día, 1 kg de colorífico cubre 4 días.",
            },
            {
                "q": "¿Por qué se usa harina de maíz/mandioca como base?",
                "a": "Porque el urucum puro es muy intenso y se vuelve difícil de dosificar. La harina diluye el color a una concentración 'usable' directo en cocina, sin necesidad de pesar gramos exactos.",
            },
            {
                "q": "¿Tiene sabor o solo color?",
                "a": "Sabor muy sutil, ligeramente terroso, casi imperceptible. Por eso es tan versátil: aporta color sin alterar el perfil de sabor del plato.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético, lugar seco y oscuro. Bien guardado conserva color e intensidad por 12-18 meses. La luz directa es el principal enemigo del urucum (degrada los pigmentos).",
            },
        ],
        "related_slugs": ["semilla-de-achiote-urucum", "paprika-dulce", "comino-en-polvo", "pimienta-del-reino-en-polvo"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 25. SAL ROSA DEL HIMALAYA FINO
    # ═════════════════════════════════════════════════════════════════
    "sal-rosa-del-himalaya-fino": {
        "product_slug": "sal-rosa-del-himalaya-fino",
        "title": "Sal Rosa del Himalaya: la sal mineral que conquistó la cocina premium y los gimnasios saludables",
        "dek": "84 minerales, color rosado natural, perfil más limpio que la sal común. El upgrade de marca más simple para restaurantes, dietéticas y consumo gourmet en Paraguay.",
        "meta_title": "Sal Rosa del Himalaya Fino — Mayorista | Especias del Paraguay",
        "meta_description": "Sal rosa del Himalaya fina al por mayor en Paraguay para restaurantes premium, dietéticas, gimnasios, spa y reventa gourmet. Calidad 100% natural.",
        "category": "Especias y Condimentos",
        "reading_time": 7,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">Hace 10 años la <strong>sal rosa del Himalaya</strong> era exotismo de spa de hotel cinco estrellas. Hoy es la sal de mesa de cualquier dietética seria, de restaurantes paraguayos premium, de gimnasios con tienda propia, de consumidores conscientes que pagan más por color, minerales y un upgrade simple sobre la sal industrial.</p>
            <p>En Especias del Paraguay importamos <strong>sal rosa del Himalaya fina</strong> de Pakistán, origen 100 % auténtico de las minas de Khewra, calidad alimentaria, color rosado natural intenso. Para restaurantes, dietéticas, almacenes saludables, spas, gimnasios y reventa al por menor.</p>
        """,
        "sections": [
            {
                "id": "que-es",
                "heading": "¿Qué es la sal rosa del Himalaya y por qué es rosada?",
                "body": """
                    <p>La <strong>sal rosa del Himalaya</strong> (también <strong>pink himalayan salt</strong> o <strong>sal rosada</strong>) es <strong>halita</strong> (cloruro de sodio mineral) extraída de las minas de Khewra en Pakistán, en la cordillera de la Sal — formaciones geológicas de hace 250 millones de años cuando un mar antiguo se evaporó y dejó depósitos minerales protegidos por la formación del Himalaya.</p>
                    <p>El color rosado viene de <strong>óxido de hierro y trazas de minerales</strong>: hierro, calcio, potasio, magnesio, zinc, cobre, manganeso. La intensidad del rosa varía por lote — de rosa pálido a rosa profundo — y NO es indicador de calidad, sino de la veta específica de la mina.</p>
                    <p>A diferencia de la sal común industrial (que es 99,9 % cloruro de sodio puro, blanqueada y refinada con anti-aglomerantes), la sal rosa del Himalaya conserva su composición mineral natural. Por eso el sabor es ligeramente diferente: más limpio, menos "salobre agresivo", con cuerpo.</p>
                """,
            },
            {
                "id": "beneficios",
                "heading": "Beneficios y por qué la industria saludable la elige",
                "body": """
                    <p>Atributos que la industria valora:</p>
                    <ul>
                        <li><strong>84 minerales traza</strong>: aporte real (aunque en cantidades mínimas) de calcio, potasio, magnesio.</li>
                        <li><strong>Sin anti-aglomerantes ni blanqueadores</strong>: la sal industrial común lleva yodo añadido, ferrocianuro de sodio, dióxido de silicio. La sal rosa NO necesita aditivos porque la mineralidad natural impide el apelmazado.</li>
                        <li><strong>Color rosado distintivo</strong>: comunica visualmente "natural" y "premium" sin necesidad de etiquetado complejo.</li>
                        <li><strong>Perfil de sabor más limpio</strong>: el cloruro de sodio puro tiene un dejo metálico/agresivo; la sal rosa tiene cuerpo redondo. Los chefs lo notan inmediatamente.</li>
                        <li><strong>Posicionamiento clean-label, keto, paleo, "real food"</strong>: encaja en todas las dietas modernas que rechazan procesados.</li>
                    </ul>
                    <p>Aviso técnico: las afirmaciones de "84 minerales que curan X" son marketing exagerado. Las cantidades de minerales traza son reales pero pequeñas — no reemplazan suplementación. La sal rosa es <strong>sal de calidad superior</strong>, no medicamento.</p>
                """,
            },
            {
                "id": "usos-industria",
                "heading": "Usos en restaurantes, dietéticas y reventa premium",
                "body": """
                    <p>Aplicaciones que mueven volumen en Paraguay:</p>
                    <ul>
                        <li><strong>Restaurantes premium y gastronomía gourmet</strong>: sal de mesa en saleros, sazonadores en cocina, presentación de platos finos. Diferenciador inmediato vs el restaurante de la esquina.</li>
                        <li><strong>Asado y parrilla profesional</strong>: cortes premium (vacío, ojo de bife, costilla) terminados con escama de sal rosa. Perfil más limpio que sal gruesa común.</li>
                        <li><strong>Dietéticas y almacenes saludables</strong>: sal de mesa rebrandeada, kits de cocina saludable, productos sin sodio añadido + sal rosa al gusto.</li>
                        <li><strong>Gimnasios y nutrición deportiva</strong>: alternativa "limpia" a sal común, recomendada en dietas keto y paleo.</li>
                        <li><strong>Spa y bienestar</strong>: sal de baño, exfoliantes corporales, lámparas de sal (decorativas, no consumibles).</li>
                        <li><strong>Industria de productos saludables</strong>: granolas saladas, snacks "naturales", productos con etiqueta clean.</li>
                        <li><strong>Cocina paraguaya tradicional con upgrade</strong>: chipa cuatro quesos premium, sopa paraguaya gourmet, asado de restaurante.</li>
                    </ul>
                """,
            },
            {
                "id": "como-preparar",
                "heading": "Cómo trabajar sal rosa: fina vs gruesa",
                "body": """
                    <p>Dos formatos, dos aplicaciones:</p>
                    <ul>
                        <li><strong>Sal rosa fina</strong>: sal de mesa, salero, sazonado en cocina, masas (panificación, chipa premium), sazonadores y blends. Reemplaza directamente la sal común fina sin ajustar dosis.</li>
                        <li><strong>Sal rosa gruesa</strong>: cocción larga (asado, brasado), sal terminadora sobre platos emplatados (foie gras, chocolate negro, tomate rojo), salmuera. Aporta crunch visual y de textura.</li>
                    </ul>
                    <p>Equivalencia: 1 g de sal rosa = 1 g de sal común en peso. NO hay diferencia significativa en concentración de cloruro de sodio. La diferencia está en perfil de sabor y minerales traza, no en poder salador.</p>
                    <p>Tip profesional: para presentación premium en restaurantes, usar la sal rosa GRUESA como sal terminadora visible. La fina queda invisible una vez disuelta, perdiendo el efecto comunicacional. La gruesa se ve.</p>
                """,
            },
            {
                "id": "presentaciones",
                "heading": "Presentaciones disponibles",
                "body": """
                    <p>Sal rosa del Himalaya importada de Pakistán para industria, restaurantes y reventa:</p>
                    <ul>
                        <li><strong>Bolsa 5 kg fina</strong> — formato dietéticas y reventa premium.</li>
                        <li><strong>Bolsa 25 kg fina</strong> — formato industrial para panificadoras y restaurantes.</li>
                        <li><strong>Bolsa 25 kg gruesa</strong> — para parrilladas y producción de sal terminadora.</li>
                    </ul>
                    <p>Importación directa, calidad alimentaria certificada, color natural. Factura legal, entrega Paraguay.</p>
                    <p class="cta-inline"><a href="/producto/sal-rosa-del-himalaya-fino" class="btn-link">Fina →</a> · <a href="/producto/sal-rosa-del-himalaya-grueso" class="btn-link">Gruesa →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿La sal rosa es realmente más saludable que la común?",
                "a": "Es 'menos procesada' y conserva minerales traza, pero NO es un superalimento. El aporte mineral por porción es pequeño. El verdadero beneficio es: ausencia de aditivos industriales (anti-aglomerantes, blanqueadores), perfil de sabor más limpio, y posicionamiento clean-label.",
            },
            {
                "q": "¿Por qué algunos lotes son más rosados que otros?",
                "a": "Por la veta específica de la mina. La intensidad del rosa varía naturalmente y NO indica diferencia de calidad. Algunos lotes son rosa pálido, otros rosa profundo — todos son auténticos.",
            },
            {
                "q": "¿Tiene yodo?",
                "a": "No naturalmente. La sal común industrial es yodada por requisito sanitario para prevenir bocio. La sal rosa NO está yodada por ser mineral natural. Si la sal rosa es la única que se consume, considerar fuente alternativa de yodo (mariscos, algas, sal yodada en algún producto).",
            },
            {
                "q": "¿Equivalencia de dosis vs sal común?",
                "a": "1:1 en peso. La sal rosa no es 'menos salada' ni 'más salada' que la común. Sustitución directa en cualquier receta.",
            },
            {
                "q": "¿Cuál es el origen real?",
                "a": "Pakistán, minas de Khewra en la cordillera de la Sal. Es prácticamente la única fuente comercial mundial. Cualquier sal rosa del Himalaya 100% auténtica viene de allí. Los certificados de origen lo confirman.",
            },
            {
                "q": "¿Cómo se conserva mejor?",
                "a": "Envase hermético en lugar seco. La sal rosa NO necesita refrigeración. Conserva calidad indefinidamente si se mantiene seca. La humedad la apelmaza pero no la daña — basta secarla y desmenuzar.",
            },
        ],
        "related_slugs": ["sal-rosa-del-himalaya-grueso", "comino-en-grano", "paprika-dulce", "pimienta-negra-en-grano"],
    },

    # ═════════════════════════════════════════════════════════════════
    # 26. PILLAR C — CÓMO ELEGIR IMPORTADOR DE ESPECIAS (institutional B2B)
    # ═════════════════════════════════════════════════════════════════
    "como-elegir-importador-especias-paraguay": {
        "product_slug": "curcuma-en-polvo",
        "title": "Cómo Elegir un Importador de Especias al Por Mayor en Paraguay: 10 criterios profesionales",
        "dek": "Origen real, certificados, estabilidad lote a lote, soporte técnico, banderas rojas. La guía que todo comprador B2B paraguayo quisiera tener antes de firmar el primer contrato.",
        "meta_title": "Cómo Elegir Importador de Especias en Paraguay | Guía B2B",
        "meta_description": "Guía profesional para elegir importador mayorista de especias en Paraguay: 10 criterios técnicos, banderas rojas, cómo comparar proveedores y armar tu cadena.",
        "category": "Especias y Condimentos",
        "reading_time": 9,
        "published": "2026-05-03",
        "updated": "2026-05-03",
        "hero_treatment": "warm",
        "intro": """
            <p class="lead">Elegir mal a un <strong>importador de especias</strong> cuesta dinero. Cuesta lotes inconsistentes que arruinan tu producción, cuesta entregas tardías que cierran tu fábrica un día, cuesta pagar 30 % de más en margen perdido por intermediarios. Y cuesta confianza: una vez que tu cliente final detecta variación en el sabor de tu chipa, tu chorizo o tu producto cárnico, recuperar esa confianza es muy difícil.</p>
            <p>Esta guía consolida lo que aprendimos del lado del proveedor — y lo que escuchamos repetidamente de compradores que se cambiaron a Especias del Paraguay después de malas experiencias. <strong>Diez criterios profesionales</strong> para evaluar a cualquier importador mayorista, banderas rojas que indican un mal proveedor, y cómo armar una cadena de suministro que aguante el crecimiento de tu negocio.</p>
        """,
        "sections": [
            {
                "id": "por-que",
                "heading": "Por qué la elección del importador define tu margen",
                "body": """
                    <p>La diferencia operativa entre un buen y un mal importador suele ser:</p>
                    <ul>
                        <li><strong>5-15 % de variación en precio</strong> entre el mejor y el peor del mercado para el mismo producto.</li>
                        <li><strong>20-40 % de variación en calidad percibida</strong> que tu cliente final puede notar en el producto terminado.</li>
                        <li><strong>2-5 días de tolerancia</strong> en entregas — un mal proveedor puede parar tu producción si llega tarde.</li>
                        <li><strong>Asistencia técnica</strong>: un buen importador te ayuda a mejorar tu fórmula; un malo solo te factura.</li>
                    </ul>
                    <p>Para una panadería que mueve 50 kg de masa por día con margen del 30 %, una variación del 10 % en costo de insumos es 3 % de margen. Para una fábrica industrial que mueve toneladas, ese 3 % es la diferencia entre ganar y perder.</p>
                """,
            },
            {
                "id": "10-criterios",
                "heading": "Los 10 criterios para evaluar un importador",
                "body": """
                    <ol>
                        <li><strong>Origen real (no intermediarios escondidos)</strong>: ¿el importador tiene relación directa con el productor en origen, o compra a un mayorista que compra a otro? Cada eslabón agrega 8-15 % al precio. Pregunte explícitamente: "¿usted importa directo o pasa por intermediario?"</li>
                        <li><strong>Certificados de origen y bromatológicos</strong>: ¿cada lote viene con documentación? ¿análisis bromatológico básico? Para industria regulada (chacinas, suplementos, productos cárnicos), esta documentación NO es opcional.</li>
                        <li><strong>Estabilidad lote a lote</strong>: ¿el color, sabor y aroma del comino que compraste hace 6 meses es igual al de hoy? Un buen importador trabaja con orígenes consistentes; un malo cambia de origen según el precio del momento.</li>
                        <li><strong>Capacidad de volumen real</strong>: ¿pueden atender el crecimiento de tu negocio? Una chipería que pasa de 50 a 200 kg/día no puede esperar que su proveedor "vea si puede conseguir más". El proveedor serio anticipa.</li>
                        <li><strong>Logística y entrega confiable</strong>: ¿entrega en tiempo? ¿factura legal? ¿cobertura nacional? Para producción en serie, retraso = pérdida directa.</li>
                        <li><strong>Términos de pago razonables</strong>: ¿transferencia? ¿factura legal con IVA? ¿plazo para clientes regulares? Un proveedor que solo acepta efectivo sin factura es un riesgo regulatorio importante.</li>
                        <li><strong>Profundidad de catálogo</strong>: ¿una sola compra cubre 80 % de tu necesidad o tenés que armar 5 proveedores? Centralizar reduce costo logístico, simplifica administración, mejora poder de negociación.</li>
                        <li><strong>Soporte técnico real</strong>: ¿el importador entiende de producto o solo factura? Un importador profesional sabe qué dosis recomendar, cómo conservar, qué origen elegir según tu aplicación.</li>
                        <li><strong>Precio en relación al servicio</strong>: el más barato del mercado generalmente sacrifica calidad o documentación o ambas. Si el precio parece demasiado bueno, casi siempre lo es.</li>
                        <li><strong>Reputación verificable</strong>: ¿quiénes son los clientes existentes? Una panadería seria, una chacinera reconocida, un restaurante de marca? La cartera del importador es su currículum.</li>
                    </ol>
                """,
            },
            {
                "id": "banderas-rojas",
                "heading": "Banderas rojas: cómo detectar un mal proveedor",
                "body": """
                    <p>Atención a estas señales — todas son experiencias reales de clientes que se cambiaron a nosotros:</p>
                    <ul>
                        <li><strong>"Solo trabajamos efectivo, sin factura"</strong>: el ahorro de IVA es marginal vs el riesgo regulatorio. Si tenés problema con SET o sanitaria, no podés justificar el origen.</li>
                        <li><strong>El precio cambia cada semana sin justificación</strong>: dependencia de cambio de moneda extrema o intermediación en cascada.</li>
                        <li><strong>"El próximo lote tiene otra variedad/origen pero te queda igual"</strong>: cambio silencioso de producto que tu cliente final va a notar.</li>
                        <li><strong>No tienen documentación de origen disponible</strong>: imposible para industria regulada o exportación.</li>
                        <li><strong>Entregas dependientes del humor del momento</strong>: "te aviso cuando llegue el contenedor". Sin previsibilidad, no podés planificar producción.</li>
                        <li><strong>Cero conocimiento técnico del producto</strong>: si preguntás "¿qué porcentaje de curcumina tiene esta cúrcuma?" y la respuesta es "no sé", el proveedor no puede ayudarte cuando algo salga mal.</li>
                        <li><strong>Catálogo extremadamente limitado</strong>: te obliga a armar 5 proveedores en paralelo, multiplicando costos administrativos.</li>
                        <li><strong>Cero presencia digital, cero referencias</strong>: hoy un proveedor B2B serio tiene catálogo accesible, datos de contacto reales, clientes que pueden referenciarlo.</li>
                    </ul>
                """,
            },
            {
                "id": "como-cumplimos",
                "heading": "Cómo Especias del Paraguay cumple cada criterio",
                "body": """
                    <p>Para ser concretos:</p>
                    <ul>
                        <li><strong>Origen directo</strong>: importamos de Egipto (comino, hibisco), India (cúrcuma), Vietnam (canela, anís estrellado), Brasil (clavo, colorífico, paprika), España (sal rosa, harinas), Pakistán (sal himalaya), California (almendras), Chile/Argentina (nueces). Cada origen es relación directa, no intermediarios.</li>
                        <li><strong>Documentación completa</strong>: certificado de origen y análisis bromatológico básico en cada lote. Bajo pedido, análisis adicional (microbiológico, perfil de pigmentos, contenido de curcumina, metales pesados).</li>
                        <li><strong>Estabilidad lote a lote</strong>: trabajamos con productores fijos por origen, no rotamos según precio del mercado.</li>
                        <li><strong>Capacidad escalable</strong>: desde caja de 10 kg para chipería de barrio hasta pallets para fábrica industrial.</li>
                        <li><strong>Logística nacional</strong>: entrega Asunción y todo el Paraguay, factura legal, transferencia bancaria.</li>
                        <li><strong>Catálogo profundo</strong>: 112 productos en 9 categorías cubre el 90 % de la necesidad de cualquier panadería, chipería, parrillada o industria de chacinas.</li>
                        <li><strong>Soporte técnico real</strong>: dosis recomendadas, técnicas profesionales, ajuste de fórmulas. Las guías que estás leyendo son parte de ese soporte.</li>
                        <li><strong>Reputación verificable</strong>: trabajamos con chiperías, parrilladas, restaurantes, fábricas y distribuidoras paraguayas. Referencias bajo pedido.</li>
                    </ul>
                """,
            },
            {
                "id": "como-empezar",
                "heading": "Cómo empezar a trabajar con nosotros",
                "body": """
                    <p>Tres pasos:</p>
                    <ol>
                        <li><strong>Contactanos por WhatsApp</strong> con tu necesidad concreta: tipo de producto, volumen mensual estimado, ubicación. Te respondemos con cotización en 24-48 hs.</li>
                        <li><strong>Pedido inicial pequeño</strong>: para conocernos, sugerimos un primer pedido razonable (caja o bolsa) que te permita validar calidad antes de comprometer volumen.</li>
                        <li><strong>Contrato anual con precio fijo</strong>: una vez validada la relación, ofrecemos contratos anuales con precio fijo y entrega programada para clientes con volumen estable. Asegura previsibilidad de costo y disponibilidad.</li>
                    </ol>
                    <p class="cta-inline"><a href="/contacto" class="btn-link">Contacto →</a> · <a href="/productos" class="btn-link">Catálogo completo →</a></p>
                """,
            },
        ],
        "faq": [
            {
                "q": "¿Cuál es el pedido mínimo para empezar?",
                "a": "Atendemos cualquier volumen serio. Para reventa al por menor el formato más pequeño es la caja de 10 kg en la mayoría de los productos. Para volúmenes menores (consumidor final, restaurantes pequeños), recomendamos consultar disponibilidad directa.",
            },
            {
                "q": "¿Trabajan con factura legal y crédito fiscal IVA?",
                "a": "Sí. Toda venta lleva factura legal con IVA discriminado. Apta para crédito fiscal y registro contable. Sin factura no operamos — es nuestra forma de proteger al cliente y cumplir regulación.",
            },
            {
                "q": "¿Aceptan pagos en cuotas?",
                "a": "Para clientes regulares con volumen estable, podemos negociar plazo (30-60 días). Pedido inicial siempre es contado. Las condiciones de plazo se evalúan caso a caso según historial.",
            },
            {
                "q": "¿Hacen entrega a interior del país?",
                "a": "Sí. Despachamos a todo el Paraguay. Logística según destino y volumen — Asunción y Gran Asunción con entrega propia, interior con coordinación de transporte.",
            },
            {
                "q": "¿Pueden conseguir productos que no están en su catálogo?",
                "a": "Para volúmenes interesantes, sí. Si tenés necesidad de un producto específico no listado, contactanos: importamos directo de 16 países y podemos evaluar agregarlo al catálogo.",
            },
            {
                "q": "¿Manejan productos orgánicos certificados?",
                "a": "Algunos productos del catálogo tienen versiones orgánicas certificables bajo pedido (cúrcuma, especias asiáticas). Para clientes que necesitan certificación específica, consultar disponibilidad y costo del adicional.",
            },
            {
                "q": "¿Cómo manejan la fluctuación del tipo de cambio?",
                "a": "Para clientes con contrato anual, fijamos precio en guaraníes con cláusula de ajuste según variación cambiaria mayor a 5 %. Para pedidos puntuales, cotización al cambio del día. Esto protege ambas partes ante movimientos de mercado.",
            },
        ],
        "related_slugs": ["insumos-chipa-paraguaya", "especias-asado-paraguayo", "manzanilla-flor", "curcuma-en-polvo"],
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
