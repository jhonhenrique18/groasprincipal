"""Category-level editorial content for /productos/<slug> hub pages.

Why a separate module: each of the 9 categories needs to function as a
real SEO hub, not a bare product-grid. Search queries like "especias al
por mayor en Paraguay", "frutos secos importados", "harinas sin gluten
mayorista" land on these category pages — and a page with only a list of
cards has zero content to rank with. This module provides the editorial
intro (250-400 words), category-specific FAQs and structured data hints
that turn each category into a real ranking surface.

Usage from app.py:
    from categories_data import get_category_content
    content = get_category_content(slug)  # may be None if not curated

Each entry maps `category_slug` -> {intro, faq, scientific_terms, ...}.
"""

from __future__ import annotations

CATEGORY_CONTENT: dict[str, dict] = {
    # ════════════════════════════════════════════════════════════════
    "especias-y-condimentos": {
        "h2": "Especias y Condimentos al por Mayor: la columna vertebral de la cocina paraguaya y latinoamericana",
        "intro": """
            <p>El catálogo de <strong>especias y condimentos al por mayor</strong> de Especias del Paraguay reúne las 38 especias más utilizadas en la industria alimentaria, la chacinería, la panificación y la gastronomía profesional del Paraguay y la región. Desde el comino egipcio que define el chimichurri y el asado paraguayo, hasta la canela vietnamita que perfuma panadería y bebidas, pasando por el pimentón dulce que da color natural a embutidos sin tartrazina.</p>
            <p>Importamos directo de los orígenes referentes mundiales: <strong>Egipto</strong> (comino, hibisco), <strong>India</strong> (cúrcuma, pimienta), <strong>Vietnam</strong> (canela, anís estrellado), <strong>Brasil</strong> (clavo, colorífico, paprika), <strong>España</strong> (sal rosa, harinas), sin intermediarios escondidos. Cada lote viene con certificado de origen y análisis bromatológico básico.</p>
            <p>Atendemos a fábricas de chacinas y embutidos, restaurantes y parrilladas, panaderías y chiperías, sazonadores y blends industriales, productos cárnicos pre-condimentados, herboristerías y minimercados saludables. Para producción mensual relevante ofrecemos contratos anuales con precio fijo y entrega programada.</p>
        """,
        "faq": [
            {
                "q": "¿Qué especias son más usadas en la cocina paraguaya?",
                "a": "Las cinco más usadas son comino (asado, chimichurri, locro), pimienta negra (uso universal), pimentón dulce (color natural en chacinas), orégano peruano (asado y pizzería) y ajo granulado o en polvo. Para chipa específicamente, semilla de anís verde es indispensable.",
            },
            {
                "q": "¿Cuál es la diferencia entre comprar especias enteras o molidas?",
                "a": "Las especias enteras (comino en grano, pimienta en grano, canela en rama) conservan aroma 24-36 meses. Las molidas pierden 40-50 % del aroma en 90 días. Para industria con alta rotación, ambos formatos sirven; para uso prolongado o calidad premium, siempre las enteras molidas en planta.",
            },
            {
                "q": "¿Cuál es el pedido mínimo mayorista?",
                "a": "Depende del producto. Para mayoría las cajas de 10 kg o bolsas de 25 kg son el formato estándar. Para volúmenes menores o reventa al por menor también atendemos por consulta directa.",
            },
            {
                "q": "¿Trabajan con factura legal y crédito fiscal?",
                "a": "Sí. Toda venta lleva factura legal con IVA discriminado, apta para crédito fiscal y registro contable.",
            },
            {
                "q": "¿Hacen contratos anuales con precio fijo?",
                "a": "Sí, para clientes con volumen estable. Asegura precio contra fluctuación cambiaria y disponibilidad. Cotización personalizada según volumen mensual estimado.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════
    "hierbas-y-tes": {
        "h2": "Hierbas y Tés al por Mayor: insumos para infusiones, bebidas funcionales y herboristería profesional",
        "intro": """
            <p>El catálogo de <strong>hierbas y tés al por mayor</strong> de Especias del Paraguay reúne 14 botánicos de uso amplio en la industria de infusiones, bebidas funcionales, coctelería de autor, cosmética natural y suplementación nutracéutica. Manzanilla flor entera, hibisco para té rojo y bebidas funcionales, matcha japonés ceremonial, cedrón paraguayo (capim limão) digestivo, melissa relajante, lavanda aromaterapéutica y más.</p>
            <p>Importamos flor entera y hojas seleccionadas — no triturados ni mezclados con tallos — porque sabemos que la diferencia se siente en el aroma, en el rendimiento por kilo y en el color de la infusión. Orígenes referentes: <strong>Argentina y Egipto</strong> para manzanilla, <strong>Egipto y Tailandia</strong> para hibisco, <strong>Japón</strong> para matcha ceremonial, productores regionales del Cono Sur para hierbas tradicionales.</p>
            <p>Atendemos a fábricas de té en bolsitas y a granel, productores de bebidas RTD funcionales (tés helados, kombuchas, aguas saborizadas), bares de coctelería premium, herboristerías y droguerías naturales, cosmética artesanal premium, restaurantes con carta de infusiones de autor y consumidores que buscan calidad gourmet. Cada lote viene con certificado de origen y análisis bromatológico básico.</p>
        """,
        "faq": [
            {
                "q": "¿Qué hierbas son más vendidas en Paraguay?",
                "a": "Manzanilla flor (digestiva, calmante, base de tés en bolsitas), hibisco flor (té rojo, bebidas funcionales), cedrón/capim limão (digestivo paraguayo tradicional), melissa (relajante) y matcha japonés (gama premium para cafeterías de autor).",
            },
            {
                "q": "¿Cómo se prepara correctamente un té de hierbas?",
                "a": "Agua a 90 °C (no en ebullición) durante 5-7 minutos con la tetera tapada. Hervir agua destruye buena parte de los aceites volátiles responsables del aroma. Para cold brew (té frío), 8-12 horas en agua fría a 4 °C.",
            },
            {
                "q": "¿La flor entera rinde más que la triturada?",
                "a": "Sí. La flor entera tiene menos relleno (sin tallo ni polvo) y conserva aceites esenciales en mayor concentración. Una flor entera bien preparada rinde 20-30 % más que la versión triturada por kilo.",
            },
            {
                "q": "¿Tienen hierbas orgánicas certificadas?",
                "a": "Bajo pedido y según volumen, podemos importar versiones orgánicas certificables de los principales productos. Consulte por disponibilidad y costo del adicional según certificadora.",
            },
            {
                "q": "¿Cuál es el pedido mínimo para industria de bebidas?",
                "a": "Para producción RTD (ready-to-drink) trabajamos cajas de 25 kg como mínimo. Para herboristerías y reventa, cajas de 10 kg.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════
    "frutas-deshidratadas": {
        "h2": "Frutas Deshidratadas al por Mayor: insumos para granolas, repostería premium y snacks saludables",
        "intro": """
            <p>El catálogo de <strong>frutas deshidratadas al por mayor</strong> de Especias del Paraguay reúne 11 frutas seleccionadas para industria de granolas y mueslis premium, repostería de fin de año (panettones, pan dulce, fruitcakes), barras energéticas, mix gourmet y snacks saludables. Cranberry americano, damasco turco, uva pasa, dátiles sin hueso, ciruela, kiwi deshidratado, higo seco lérida, piña tropical, cereza glaseada, goji berry y mix de frutas tropicales.</p>
            <p>Importamos de orígenes referentes según fruta: <strong>Estados Unidos</strong> (cranberry, ciruela), <strong>Turquía</strong> (damasco, higo, uva pasa), <strong>Chile/Argentina</strong> (frutas regionales), <strong>Sudeste asiático</strong> (piña tropical, mix), <strong>China</strong> (goji berry). Calidad estable lote a lote, niveles de humedad controlados (importante para conservación), sin agregados de azúcar artificial salvo en presentaciones específicas.</p>
            <p>Atendemos a fábricas de granolas y mueslis premium, panaderías de fin de año, restaurantes y reposterías de autor, almacenes saludables y dietéticas, gimnasios con tienda propia de barras y snacks, heladerías artesanales que usan frutas como decoración o base. Para volúmenes industriales ofrecemos contratos por temporada (especialmente para producción de panettones de Navidad).</p>
        """,
        "faq": [
            {
                "q": "¿Cuál es la diferencia entre fruta deshidratada y fruta confitada?",
                "a": "La deshidratada perdió agua naturalmente (sol o aire seco) sin agregar azúcar; conserva sabor original concentrado. La confitada (cereza glaseada, frutas glace) pasó por jarabe de azúcar — más dulce, mayor vida útil, presentación brillante. Cada una sirve para aplicaciones distintas.",
            },
            {
                "q": "¿Cuánto rinden las frutas deshidratadas en producción industrial?",
                "a": "Aproximadamente 1 kg de fruta deshidratada equivale a 4-6 kg de fruta fresca en sabor concentrado. En granolas, 100 g de fruta deshidratada por kilo de granola es la dosis estándar; en panettones, 200-300 g por kilo de masa.",
            },
            {
                "q": "¿Son aptas para celíacos?",
                "a": "Las frutas naturales son sin gluten. Para certificación apta celíacos en producto industrial requiere análisis de contaminación cruzada en planta procesadora. Algunas marcas premium tienen certificación.",
            },
            {
                "q": "¿Tienen sulfitos o conservantes?",
                "a": "Algunas frutas deshidratadas claras (damasco, manzana, piña) usan dióxido de azufre como conservante natural; otras son completamente sin aditivos. Consulte por la versión específica que necesita — ofrecemos ambas.",
            },
            {
                "q": "¿Cuál es el pedido mínimo?",
                "a": "Caja de 5 kg para reventa premium; caja de 10-25 kg para industria. Para temporada de panettones (octubre-diciembre) ofrecemos contratos por temporada con entrega programada.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════
    "semillas-y-granos": {
        "h2": "Semillas y Granos al por Mayor: superalimentos, sin gluten y panificación funcional",
        "intro": """
            <p>El catálogo de <strong>semillas y granos al por mayor</strong> de Especias del Paraguay reúne 12 productos que son la columna vertebral de la categoría saludable moderna: chía con omega-3 vegetal, quinoa peruana proteína completa, linaza dorada, semilla de anís para chipa paraguaya, garbanzos importados, lentejas rojas, semillas de calabaza y girasol, granola tradicional, avena en copos finos, salvado y trigo sarraceno.</p>
            <p>Importamos de orígenes referentes: <strong>Perú</strong> (quinoa real), <strong>México y Bolivia</strong> (chía premium), <strong>Argentina</strong> (linaza, girasol), <strong>España</strong> (anís verde, garbanzos), <strong>Canadá</strong> (avena premium). Cada producto viene con certificado de origen y análisis bromatológico básico. Para industria sin gluten certificable, ofrecemos análisis de contaminación cruzada bajo pedido.</p>
            <p>Atendemos a fábricas de productos sin gluten certificables, panificadoras industriales y artesanales especializadas en pan funcional y celíaco, chiperías profesionales (anís verde es el insumo crítico), industria de granolas y mueslis premium, almacenes saludables y dietéticas, gimnasios y nutrición deportiva, restaurantes de cocina sana y plant-based. Para volúmenes industriales ofrecemos contratos anuales con precio fijo.</p>
        """,
        "faq": [
            {
                "q": "¿La quinoa, la chía y la linaza son sin gluten naturalmente?",
                "a": "Sí, las tres son naturalmente sin gluten. Para certificación apta celíacos en producto industrial requiere análisis de contaminación cruzada en planta. Para industria que produce línea celíaca, ofrecemos lotes con análisis específico bajo pedido.",
            },
            {
                "q": "¿Cuánto anís lleva un kilo de masa de chipa?",
                "a": "8-10 g de semillas enteras por kilo de masa para chipa común. La semilla va entera, no se muele. Ver nuestra guía completa de Insumos para Chipa Industrial para dosis por variante.",
            },
            {
                "q": "¿La quinoa peruana es realmente mejor que la de otros orígenes?",
                "a": "Perú produce el 50 % de la quinoa mundial y la calidad de la quinoa real peruana es referencia internacional por uniformidad de tamaño, color blanco-marfil estable y bajo contenido de saponinas (ya pre-perlada lista para usar).",
            },
            {
                "q": "¿Cuánto rinde 1 kg de chía en producción de pudín?",
                "a": "Aproximadamente 100 porciones de pudín individual (10 g por porción). En panificación rinde 200 panes funcionales pequeños (5 g por unidad). En geles deportivos, rinde 400 unidades (2,5 g por gel).",
            },
            {
                "q": "¿Cuál es el pedido mínimo?",
                "a": "Bolsa de 5 kg para dietéticas y reventa premium; bolsa de 25 kg para industria. Para fábricas con volumen estable ofrecemos contratos anuales.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════
    "frutos-secos": {
        "h2": "Frutos Secos al por Mayor: insumos premium para repostería, plant-based y aperitivos gourmet",
        "intro": """
            <p>El catálogo de <strong>frutos secos al por mayor</strong> de Especias del Paraguay reúne 11 productos premium que son la base de la categoría gourmet en Paraguay: castaña de cajú W1 cruda y con sal, almendra californiana americana, almendra laminada, nuez mariposa, pistacho con y sin cáscara, castaña de Brasil amazónica, nuez pecán, macadamia y avellana sin cáscara.</p>
            <p>Importamos de los orígenes referentes mundiales: <strong>California (USA)</strong> para almendras, <strong>Vietnam e India</strong> para castaña de cajú, <strong>Chile y Argentina</strong> para nuez mariposa y pecán, <strong>Brasil amazónico</strong> para castaña de Brasil, <strong>Irán y California</strong> para pistacho premium, <strong>Australia</strong> para macadamia. Calidad uniforme lote a lote, sin partidos en presentación premium, niveles de humedad controlados para conservación.</p>
            <p>Atendemos a fábricas de mix gourmet y aperitivos premium, alfajoreras y reposterías de fin de año (la nuez mariposa para coronar alfajores es nuestro #1), heladerías artesanales y pastelerías de autor (pasta de pistacho, macarons, frangipane), industria plant-based (leches vegetales de almendra y cajú, queso vegano, mantequillas), almacenes saludables y gimnasios con tienda propia de snacks. Para producción industrial ofrecemos formatos en cajas de 22,68 kg (50 lbs) con precio competitivo.</p>
        """,
        "faq": [
            {
                "q": "¿Qué significa W1 en castaña de cajú?",
                "a": "W1 es el grado premium internacional para cajú entero: granos enteros sin partir, tamaño grande uniforme, color blanco-marfil sin manchas. La nomenclatura W (whole) seguida de número indica granos por libra; menor número, mayor tamaño.",
            },
            {
                "q": "¿Por qué la nuez mariposa cuesta más que la nuez en cuartos?",
                "a": "Porque exige descascarado manual cuidadoso para preservar las dos mitades enteras unidas (forma de alas de mariposa). Solo el 35-40 % del rendimiento de descascarado sale como mariposa; el resto son mitades sueltas y cuartos.",
            },
            {
                "q": "¿Conviene almendra con piel o pelada (blanqueada)?",
                "a": "Con piel para uso general (mix, granola, leche vegetal). Pelada para repostería fina donde el color blanco importa (macarons, mazapanes, frangipane fina).",
            },
            {
                "q": "¿Cómo se conservan mejor los frutos secos?",
                "a": "Envase hermético, lugar seco y fresco. A temperatura ambiente: 6-9 meses. Refrigerados a 4 °C: 12-18 meses. Congelados: hasta 24 meses. Las nueces (mariposa, pecán) son las más sensibles por el alto omega-3.",
            },
            {
                "q": "¿Cuál es el pedido mínimo para industria?",
                "a": "Caja de 10 kg para reventa premium y reposterías; caja de 22,68 kg (50 lbs) para industria. Para fábricas plant-based con leches vegetales o pastas, ofrecemos cotización por proyecto.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════
    "suplementos-y-superalimentos": {
        "h2": "Suplementos y Superalimentos al por Mayor: la categoría que define la góndola saludable moderna",
        "intro": """
            <p>El catálogo de <strong>suplementos y superalimentos al por mayor</strong> de Especias del Paraguay reúne 9 productos que son los protagonistas de la nutrición funcional contemporánea: spirulina (proteína vegetal completa, hierro), moringa, maca peruana energizante, psyllium (fibra soluble), eritritol y xilitol (edulcorantes naturales), colágeno hidrolizado, creatina monohidratada y guaraná amazónico.</p>
            <p>Importamos de orígenes referentes mundiales: <strong>India y China</strong> para spirulina y moringa de calidad nutracéutica, <strong>Perú</strong> para maca andina auténtica, <strong>Brasil amazónico</strong> para guaraná, <strong>Estados Unidos y Europa</strong> para creatina y colágeno premium, <strong>España</strong> para eritritol y xilitol grado alimentario. Cada lote viene con certificado de origen y análisis bromatológico; para industria nutracéutica regulada, ofrecemos análisis adicional bajo pedido (perfil aminoacídico, metales pesados, perfil de proteína).</p>
            <p>Atendemos a fábricas de suplementos en cápsulas y comprimidos, productores de polvos proteicos vegetales y blends funcionales, gimnasios y tiendas de nutrición deportiva con línea propia, almacenes saludables y dietéticas, industria de bebidas funcionales RTD (golden lattes, batidos verdes, energéticos naturales), barras energéticas y geles deportivos. Para volúmenes industriales ofrecemos cotización por proyecto.</p>
        """,
        "faq": [
            {
                "q": "¿Qué porcentaje de proteína tiene la spirulina?",
                "a": "60-70 % de proteína por peso seco con perfil aminoacídico completo (todos los esenciales). Por eso es el ingrediente preferido en polvos proteicos vegetales y suplementación deportiva plant-based.",
            },
            {
                "q": "¿La maca peruana es realmente energizante?",
                "a": "La maca andina (Lepidium meyenii) tiene tradición de uso en Perú como adaptógeno energizante. Estudios modernos sostienen efectos sobre energía, libido y resistencia, aunque las afirmaciones específicas requieren validación regulatoria según jurisdicción del producto final.",
            },
            {
                "q": "¿El eritritol y el xilitol son seguros como sustitutos del azúcar?",
                "a": "Sí, ambos son aprobados como edulcorantes seguros por FDA, EFSA y autoridades latinoamericanas. El eritritol no eleva glucosa; el xilitol tiene efecto similar pero es tóxico para perros (importante en productos pet-friendly).",
            },
            {
                "q": "¿La creatina monohidratada de ustedes es grado farmacéutico?",
                "a": "La calidad varía por origen. Trabajamos con grado alimentario premium con análisis de pureza disponible. Para industria nutracéutica regulada, podemos cotizar grado farmacéutico con certificación específica bajo pedido.",
            },
            {
                "q": "¿Cuál es el pedido mínimo para fábricas de suplementos?",
                "a": "Bolsa de 1 kg para reventa premium; bolsa de 5 kg para herboristerías y gimnasios; bolsa de 25 kg para fábricas. Cotización por proyecto disponible para volúmenes mayores.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════
    "derivados-de-coco": {
        "h2": "Derivados de Coco al por Mayor: insumos para repostería tropical, keto y plant-based",
        "intro": """
            <p>El catálogo de <strong>derivados de coco al por mayor</strong> de Especias del Paraguay reúne 5 productos esenciales para repostería tropical, dieta keto, plant-based y panificación moderna: leche de coco en polvo, chips de coco tostado, coco rallado fino, azúcar de coco orgánica y coco rallado en copos. Cada uno tiene aplicaciones específicas en industria, gastronomía y consumo doméstico premium.</p>
            <p>Importamos de los principales productores tropicales — <strong>Filipinas</strong>, <strong>Indonesia</strong> y <strong>Sri Lanka</strong> — donde el cocotero es cultivo nativo de calidad referente mundial. Cada lote viene con certificado de origen y análisis bromatológico básico, niveles de humedad y grasa controlados (importante para vida útil y comportamiento en producción).</p>
            <p>Atendemos a panificadoras de productos tropicales (pasteles caribeños, alfajores con coco, galletitas), heladerías artesanales (sorbetes de coco, paletas tropicales), industria sin gluten y keto (la harina de coco es base de la categoría low-carb), reposterías premium con líneas plant-based, almacenes saludables, restaurantes de comida asiática y caribeña, productores de granolas tropicales. Para industria con volumen estable ofrecemos contratos por temporada.</p>
        """,
        "faq": [
            {
                "q": "¿Diferencia entre coco rallado fino y en copos?",
                "a": "El fino tiene granulometría pequeña, ideal para integrar en masas (galletitas, pan tropical, bombones). En copos tiene piezas mayores, ideal para coronar productos y para granolas premium donde la textura visible importa.",
            },
            {
                "q": "¿La leche de coco en polvo es lo mismo que la enlatada?",
                "a": "Es la versión deshidratada de la leche de coco, lista para reconstituir con agua. Más práctica para industria (no requiere refrigeración antes de abrir, vida útil mayor), perfil nutricional similar al líquido original.",
            },
            {
                "q": "¿El azúcar de coco es realmente más saludable que la común?",
                "a": "Tiene índice glicémico ligeramente menor (~54 vs 65 del azúcar refinada) y conserva trazas minerales del cocotero. No es 'sano sin restricción' — sigue siendo azúcar — pero permite posicionamiento clean-label y orgánico.",
            },
            {
                "q": "¿La harina de coco es apta para celíacos?",
                "a": "Sí, naturalmente sin gluten. Para certificación apta celíacos requiere análisis de contaminación cruzada en planta. Es base fundamental de panificación keto y celíaca por su perfil alto en fibra.",
            },
            {
                "q": "¿Cuál es el pedido mínimo?",
                "a": "Bolsa de 5 kg para reventa y reposterías; bolsa de 25 kg para industria. Para temporada de productos tropicales y de fin de año ofrecemos contratos con entrega programada.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════
    "harinas-especiales": {
        "h2": "Harinas Especiales al por Mayor: la base de la repostería sin gluten, keto y panificación premium",
        "intro": """
            <p>El catálogo de <strong>harinas especiales al por mayor</strong> de Especias del Paraguay reúne 9 productos que son insumos críticos para la repostería contemporánea sin gluten, keto, plant-based y panificación premium: harina de almendra Parmex, Regal y Calconut (las tres marcas referentes españolas para macarons y repostería fina), harina de coco para keto, harina de arroz integral, harina de garbanzos, harina de linaza dorada, gelatina sin sabor y goma xantana (espesante natural).</p>
            <p>Importamos de orígenes referentes mundiales: <strong>España</strong> para las harinas de almendra premium (las tres marcas distintas para distintas aplicaciones — Parmex y Calconut fina para macarons, Regal para frangipane), <strong>Filipinas</strong> para harina de coco, <strong>India</strong> para garbanzo y arroz integral, <strong>Argentina y Canadá</strong> para linaza dorada. Cada lote viene con certificado de origen y análisis bromatológico básico.</p>
            <p>Atendemos a reposterías profesionales y panaderías especializadas en macarons franceses (la granulometría fina de las harinas de almendra Parmex es la referencia industrial), fábricas de productos sin gluten certificables para celíacos, panificadoras de pan keto y low-carb, heladerías que usan harinas como base de masas, restaurantes con repostería plant-based y vegana, almacenes saludables y dietéticas con línea premium. Para producción industrial ofrecemos formatos en bolsas de 25 kg con cotización por volumen.</p>
        """,
        "faq": [
            {
                "q": "¿Qué diferencia hay entre las harinas de almendra Parmex, Regal y Calconut?",
                "a": "Las tres son harinas de almendra blanqueada españolas premium. Parmex y Calconut tienen granulometría fina ideal para macarons franceses (donde la textura del biscuit importa críticamente). Regal tiene granulometría ligeramente más gruesa, ideal para frangipane y bizcochuelos. La elección depende de la aplicación final.",
            },
            {
                "q": "¿La harina de almendra es realmente sin gluten certificable?",
                "a": "Naturalmente sí. Para certificación apta celíacos en producto industrial, requiere análisis de contaminación cruzada en la planta procesadora. Las marcas españolas premium suelen tener certificación; las marcas industriales requieren análisis específico por lote.",
            },
            {
                "q": "¿Para qué sirve la goma xantana?",
                "a": "Es un espesante y estabilizante natural, esencial en panificación sin gluten porque sustituye la elasticidad estructural del gluten. Dosis típica: 0,3-0,5 % del peso de la harina. Sin xantana, los panes celíacos quedan desmoronados.",
            },
            {
                "q": "¿Cuánto rinde 1 kg de harina de almendra en macarons?",
                "a": "Aproximadamente 600-800 unidades de macarons (pares de 1,5-2 g cada lado). Para producción industrial es uno de los insumos de mayor costo por unidad, justificable solo si la calidad final lo justifica.",
            },
            {
                "q": "¿Cuál es el pedido mínimo para reposterías?",
                "a": "Bolsa de 5 kg para reposterías y panificadoras especializadas; bolsa de 25 kg para fábricas de macarons y productos sin gluten. Para producción industrial con volumen estable ofrecemos contratos anuales.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════
    "cacao": {
        "h2": "Cacao al por Mayor: insumos premium para repostería, heladería y bebidas chocolatadas industriales",
        "intro": """
            <p>El catálogo de <strong>cacao al por mayor</strong> de Especias del Paraguay reúne los 3 formatos de cacao más usados en industria moderna: cacao alcalino en polvo (también llamado cacao holandés o dutch cocoa, el estándar industrial mundial), cacao en polvo black (versión ultra oscura para color y sabor intenso) y nibs de cacao (granos enteros tostados sin moler, formato premium para repostería gourmet y consumo crudismo).</p>
            <p>Importamos cacao procesado en orígenes referentes — <strong>Costa de Marfil</strong>, <strong>Ghana</strong>, <strong>Brasil</strong> y <strong>Ecuador</strong> son los productores top mundiales del fruto del <em>Theobroma cacao</em>. La alcalinización del cacao, inventada en Holanda en 1828 por van Houten, transforma el cacao natural en el formato industrial moderno: color más oscuro, sabor más suave, dispersión perfecta en líquidos.</p>
            <p>Atendemos a fábricas de panificación industrial (galletitas tipo Oreo, brownies, alfajores rellenos, panettones de chocolate), heladerías artesanales y industriales (helados de chocolate, paletas, cremas), productores de bebidas chocolatadas RTD (leches chocolatadas, polvos solubles tipo "chocolatada"), reposterías premium con coberturas y rellenos de chocolate, fábricas de bombones y trufas, productores de mezclas para batidos proteicos sabor chocolate. Para industria con volumen estable ofrecemos contratos anuales con precio fijo.</p>
        """,
        "faq": [
            {
                "q": "¿Cuál es la diferencia entre cacao alcalino y cacao natural?",
                "a": "El alcalino es tratado con álcali (carbonato de potasio) durante el procesamiento, lo que reduce acidez, oscurece el color, suaviza el sabor y mejora dispersión en líquidos. El natural conserva sabor más complejo y mayor acidez, ideal para panificación con bicarbonato.",
            },
            {
                "q": "¿Por qué se llama cacao holandés?",
                "a": "Porque el proceso de alcalinización fue inventado en Holanda en 1828 por Coenraad van Houten. El nombre 'dutch cocoa' o 'cacao holandés' se mantiene comercialmente hasta hoy como sinónimo internacional.",
            },
            {
                "q": "¿Puedo sustituir cacao alcalino por natural en cualquier receta?",
                "a": "No directamente. Las recetas que usan bicarbonato dependen de la acidez del cacao natural para leudar. Si sustituye por alcalino, debe ajustar agentes leudantes. En recetas con polvo de hornear (no bicarbonato puro), la sustitución es más simple.",
            },
            {
                "q": "¿Qué son los nibs de cacao y cómo se usan?",
                "a": "Son granos de cacao tostados y picados, sin moler ni procesar a manteca. Aportan sabor intenso, textura crujiente y son apreciados en repostería raw, granolas premium, bombones gourmet y consumo directo (snack saludable amargo).",
            },
            {
                "q": "¿Cuál es el pedido mínimo para industria?",
                "a": "Bolsa de 5 kg para reposterías y heladerías artesanales; bolsa de 25 kg para fábricas de panificación, bebidas y heladerías industriales. Para producción con volumen estable ofrecemos contratos anuales con precio fijo.",
            },
        ],
    },
}


def get_category_content(slug: str) -> dict | None:
    """Return editorial content for a category slug or None if not curated."""
    return CATEGORY_CONTENT.get(slug)
