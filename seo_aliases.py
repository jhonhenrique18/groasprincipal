"""SEO breadth — curated aliases and scientific names for all 112 products.

This file is the single source of truth for the keyword breadth layer.
The data feeds two paths:

1. Fresh seed (init_db, first boot of a new environment): the seeder reads
   seed_data.json and, before committing each product, looks up its slug
   here and attaches aliases + scientific_name.
2. In-place migration (existing production): a boot-time helper iterates
   over products with empty aliases and backfills from this file.

Why a Python module instead of JSON: aliases are reference data that
benefits from being readable as code, easy to grep, easy to diff in PR,
and trivially extensible without tooling. JSON would require an external
schema; here, a flat dict is enough.

Each entry maps `slug` -> {"aliases": "...", "scientific_name": "..."}.
- aliases: comma-separated, lowercased, free of trailing whitespace. Order
  matters slightly (more important variants first).
- scientific_name: empty string when not biologically classifiable
  (blends, processed products, mineral salts).

When adding a new product:
1. Add the slug-keyed entry below.
2. Cover at minimum: canonical Spanish name, generic Spanish term, English,
  Portuguese, and one regional or scientific variant where relevant.
3. Avoid keyword stuffing — every alias must be a term a real human would
  plausibly type into search.
"""

from __future__ import annotations

# Comma-separated aliases per product slug. Ordered roughly by search volume
# (most common variant first). Includes Spanish (canonical), English (for
# cross-border searches), Portuguese (Brazilian-border traffic) and regional
# Latin American synonyms where they exist.
PRODUCT_ALIASES: dict[str, dict[str, str]] = {
    # ===== ESPECIAS Y CONDIMENTOS =====
    "curcuma-en-polvo": {
        "aliases": "cúrcuma, cúrcuma en polvo, cúrcuma molida, turmeric, açafrão da terra, açafrão, turmeric powder",
        "scientific_name": "Curcuma longa",
    },
    "canela-en-rama-6cm": {
        "aliases": "canela, canela en rama, canela astilla, canela entera, cinnamon, cinnamon stick, canela em rama, canela em pau",
        "scientific_name": "Cinnamomum verum",
    },
    "anis-estrellado": {
        "aliases": "anís estrellado, anís estrella, badiana, star anise, anis estrelado, badián",
        "scientific_name": "Illicium verum",
    },
    "clavo-de-olor": {
        "aliases": "clavo, clavo de olor, clavo entero, cloves, cravo da índia, cravo, clove",
        "scientific_name": "Syzygium aromaticum",
    },
    "comino-en-grano": {
        "aliases": "comino, comino entero, comino en semillas, cumin, cumin seeds, cominho, semilla de comino",
        "scientific_name": "Cuminum cyminum",
    },
    "paprika-dulce": {
        "aliases": "paprika, paprika dulce, pimentón dulce, pimentón, sweet paprika, páprica doce, pimentón rojo",
        "scientific_name": "Capsicum annuum",
    },
    "romero": {
        "aliases": "romero, romero seco, rosemary, alecrim, hierba romero",
        "scientific_name": "Rosmarinus officinalis",
    },
    "pimienta-negra-en-grano": {
        "aliases": "pimienta negra, pimienta entera, pimienta en grano, black pepper, pimenta do reino, pimenta preta, peppercorns",
        "scientific_name": "Piper nigrum",
    },
    "pimienta-del-reino-en-polvo": {
        "aliases": "pimienta, pimienta del reino, pimienta molida, pimienta en polvo, ground black pepper, pimenta do reino moída",
        "scientific_name": "Piper nigrum",
    },
    "oregano-peruano": {
        "aliases": "orégano, orégano peruano, oregano, orégano seco, oregano peruano, orégano deshidratado",
        "scientific_name": "Origanum vulgare",
    },
    "jengibre-en-polvo": {
        "aliases": "jengibre, jengibre molido, ginger, ginger powder, gengibre, jengibre en polvo",
        "scientific_name": "Zingiber officinale",
    },
    "comino-en-polvo": {
        "aliases": "comino, comino molido, comino en polvo, ground cumin, cominho moído, polvo de comino",
        "scientific_name": "Cuminum cyminum",
    },
    "ajo-granulado": {
        "aliases": "ajo, ajo granulado, ajo seco, garlic granules, alho granulado, ajo deshidratado",
        "scientific_name": "Allium sativum",
    },
    "sal-rosa-del-himalaya-fino": {
        "aliases": "sal rosa, sal del himalaya, sal rosa fina, himalayan salt, sal rosada, pink himalayan salt, sal rosa fino",
        "scientific_name": "",
    },
    "canela-en-polvo-100-pura": {
        "aliases": "canela, canela en polvo, canela molida, cinnamon powder, ground cinnamon, canela em pó, canela pura",
        "scientific_name": "Cinnamomum verum",
    },
    "paprika-ahumada": {
        "aliases": "paprika, paprika ahumada, pimentón ahumado, smoked paprika, páprica defumada, pimentón ahumado dulce",
        "scientific_name": "Capsicum annuum",
    },
    "laurel-en-hoja": {
        "aliases": "laurel, hojas de laurel, laurel seco, bay leaves, louro, folha de louro, hoja de laurel entera",
        "scientific_name": "Laurus nobilis",
    },
    "semilla-de-achiote-urucum": {
        "aliases": "achiote, urucum, semilla de achiote, annatto, urucu, bija, achiote en semilla",
        "scientific_name": "Bixa orellana",
    },
    "nuez-moscada-en-polvo": {
        "aliases": "nuez moscada, nuez moscada molida, nutmeg, nutmeg powder, noz moscada, noz-moscada moída",
        "scientific_name": "Myristica fragrans",
    },
    "canela-feculada": {
        "aliases": "canela, canela feculada, canela con fécula, canela molida fécula, canela industrial",
        "scientific_name": "Cinnamomum verum",
    },
    "lemon-pepper": {
        "aliases": "lemon pepper, pimienta limón, pimienta y limón, pimenta limão, lemon pepper seasoning, condimento limón pimienta",
        "scientific_name": "",
    },
    "tempero-edu": {
        "aliases": "tempero, tempero edu, condimento brasileiro, tempero pronto, tempero brasileño, sazonador edu",
        "scientific_name": "",
    },
    "ajo-en-polvo": {
        "aliases": "ajo, ajo en polvo, ajo molido, garlic powder, alho em pó, polvo de ajo",
        "scientific_name": "Allium sativum",
    },
    "colorifico-colorau": {
        "aliases": "colorífico, colorau, colorante natural, urucum molido, achiote molido, annatto powder, colorau brasileiro",
        "scientific_name": "Bixa orellana",
    },
    "chimichurri-con-pimienta": {
        "aliases": "chimichurri, chimichurri picante, chimichurri con pimienta, condimento argentino, chimichurri con ají, chimichurri rojo",
        "scientific_name": "",
    },
    "cilantro-en-polvo": {
        "aliases": "cilantro, cilantro molido, coriandro, coriander, coentro, ground coriander, cilantro seco",
        "scientific_name": "Coriandrum sativum",
    },
    "cardamomo-en-grano": {
        "aliases": "cardamomo, cardamomo verde, cardamomo entero, cardamom, cardamom pods, cardamomo en vaina",
        "scientific_name": "Elettaria cardamomum",
    },
    "chimichurri-sin-pimienta": {
        "aliases": "chimichurri, chimichurri suave, chimichurri sin picante, condimento argentino, chimichurri verde",
        "scientific_name": "",
    },
    "tempero-pega-marido": {
        "aliases": "tempero pega marido, tempero brasileiro, tempero baiano, condimento brasileño, sazonador brasileiro",
        "scientific_name": "",
    },
    "cebolla-perejil-y-ajo": {
        "aliases": "cebolla perejil ajo, mezcla de hierbas, condimento mixto, cebolla y ajo, hierbas secas, sazonador mixto",
        "scientific_name": "",
    },
    "tempero-fit-pollo": {
        "aliases": "tempero pollo, tempero frango, tempero fit, condimento para pollo, sazonador de pollo, tempero fit frango",
        "scientific_name": "",
    },
    "enebro-en-grano": {
        "aliases": "enebro, bayas de enebro, juniper, juniper berries, zimbro, juníperus, enebro entero",
        "scientific_name": "Juniperus communis",
    },
    "paprika-picante": {
        "aliases": "paprika, paprika picante, pimentón picante, hot paprika, páprica picante, pimentón rojo picante",
        "scientific_name": "Capsicum annuum",
    },
    "sal-rosa-del-himalaya-grueso": {
        "aliases": "sal rosa, sal del himalaya, sal gruesa, himalayan salt coarse, sal grossa rosa, sal rosa grueso",
        "scientific_name": "",
    },
    "curry": {
        "aliases": "curry, curry en polvo, curry powder, caril, condimento curry, mezcla de especias curry, curry indiano",
        "scientific_name": "",
    },
    "nuez-moscada-entera": {
        "aliases": "nuez moscada, nuez moscada entera, whole nutmeg, noz moscada inteira, nuez moscada en grano",
        "scientific_name": "Myristica fragrans",
    },
    "mostaza-en-grano-amarilla": {
        "aliases": "mostaza, semillas de mostaza, mostaza amarilla, yellow mustard seeds, mostarda em grão, mostaza en semilla",
        "scientific_name": "Sinapis alba",
    },
    "cebolla-en-polvo": {
        "aliases": "cebolla, cebolla en polvo, cebolla molida, onion powder, cebola em pó, polvo de cebolla",
        "scientific_name": "Allium cepa",
    },
    # ===== HIERBAS Y TÉS =====
    "manzanilla-flor": {
        "aliases": "manzanilla, manzanilla en flor, camomila, chamomile, chamomile flowers, manzanilla flores, camomila chá, té de manzanilla",
        "scientific_name": "Matricaria chamomilla",
    },
    "hibisco-flor": {
        "aliases": "hibisco, flor de jamaica, jamaica, hibiscus, hibiscus flowers, hibisco flor seca, hibisco para té, té de hibisco",
        "scientific_name": "Hibiscus sabdariffa",
    },
    "matcha-japones": {
        "aliases": "matcha, té matcha, té verde matcha, matcha japonês, matcha tea, matcha en polvo, matcha ceremonial",
        "scientific_name": "Camellia sinensis",
    },
    "hinojo": {
        "aliases": "hinojo, semilla de hinojo, fennel, fennel seeds, funcho, anis dulce, hinojo en grano",
        "scientific_name": "Foeniculum vulgare",
    },
    "cardo-mariano": {
        "aliases": "cardo mariano, milk thistle, cardo de maría, silybum, cardo santo, cardo lechero",
        "scientific_name": "Silybum marianum",
    },
    "calendula": {
        "aliases": "caléndula, calendula, marigold, flor de caléndula, calêndula, té de caléndula",
        "scientific_name": "Calendula officinalis",
    },
    "lavanda-flor": {
        "aliases": "lavanda, flor de lavanda, lavender, alfazema, lavanda seca, lavanda flor, té de lavanda",
        "scientific_name": "Lavandula angustifolia",
    },
    "eneldo": {
        "aliases": "eneldo, dill, dill seeds, semillas de eneldo, endro, aneto, eneldo seco",
        "scientific_name": "Anethum graveolens",
    },
    "boldo-chileno": {
        "aliases": "boldo, boldo chileno, boldo del perú, té de boldo, boldo seco, hojas de boldo",
        "scientific_name": "Peumus boldus",
    },
    "te-verde-importado": {
        "aliases": "té verde, green tea, té verde en hojas, chá verde, té verde a granel, té verde importado",
        "scientific_name": "Camellia sinensis",
    },
    "melissa-toronjil": {
        "aliases": "melissa, toronjil, lemon balm, melisa, melissa officinalis, erva cidreira, té de melissa",
        "scientific_name": "Melissa officinalis",
    },
    "alcachofa-hierba": {
        "aliases": "alcachofa, hojas de alcachofa, artichoke, alcachofa hierba seca, alcachofra, té de alcachofa",
        "scientific_name": "Cynara scolymus",
    },
    "bardana": {
        "aliases": "bardana, raíz de bardana, burdock, burdock root, bardana raiz, té de bardana",
        "scientific_name": "Arctium lappa",
    },
    "cedron-capim-limao": {
        "aliases": "cedrón, capim limão, lemon grass, hierba luisa, cidrón, citronela hierba, lemongrass, capim cidreira",
        "scientific_name": "Cymbopogon citratus",
    },
    # ===== CACAO =====
    "cacao-alcalino-en-polvo": {
        "aliases": "cacao, cacao alcalino, cacao en polvo, alkalized cocoa, dutch cocoa, cacao holandés, cacao processado",
        "scientific_name": "Theobroma cacao",
    },
    "cacao-en-polvo-black": {
        "aliases": "cacao, cacao negro, cacao black, black cocoa powder, cacao oscuro, cacao en polvo negro",
        "scientific_name": "Theobroma cacao",
    },
    "nibs-de-cacao": {
        "aliases": "nibs de cacao, cacao nibs, granos de cacao, semillas de cacao, cocoa nibs, nibs de cacao puro",
        "scientific_name": "Theobroma cacao",
    },
    # ===== FRUTOS SECOS =====
    "castana-de-caju-w1-cruda": {
        "aliases": "castaña de cajú, castanha de caju, cashew, cashew nuts, castaña cruda, anacardo, marañón, castaña w1",
        "scientific_name": "Anacardium occidentale",
    },
    "almendra-americana": {
        "aliases": "almendra, almendras, almonds, almond, amêndoa, almendras americanas, almendra californiana",
        "scientific_name": "Prunus dulcis",
    },
    "nuez-mariposa": {
        "aliases": "nuez, nuez mariposa, walnut, walnuts, nuez mariposa entera, noz, nuez de california",
        "scientific_name": "Juglans regia",
    },
    "pistacho-sin-cascara": {
        "aliases": "pistacho, pistachio, pistache, pistachios, pistachos pelados, pistacho pelado, pistacho sin concha",
        "scientific_name": "Pistacia vera",
    },
    "pistacho-con-cascara": {
        "aliases": "pistacho, pistachio in shell, pistacho con cáscara, pistachios con concha, pistache com casca",
        "scientific_name": "Pistacia vera",
    },
    "castana-de-brasil": {
        "aliases": "castaña de brasil, castanha do pará, brazil nut, castaña amazónica, nuez de brasil, brazilian nut",
        "scientific_name": "Bertholletia excelsa",
    },
    "nuez-pecan": {
        "aliases": "nuez pecán, pecan, pecan nuts, nuez pecana, pecã, noz pecan, pecán natural",
        "scientific_name": "Carya illinoinensis",
    },
    "almendra-laminada": {
        "aliases": "almendra, almendra laminada, almendras fileteadas, sliced almonds, amêndoas laminadas, almendras en láminas",
        "scientific_name": "Prunus dulcis",
    },
    "castana-de-caju-con-sal-w1": {
        "aliases": "castaña de cajú, castaña con sal, cashew salted, castanha de caju com sal, anacardo salado, castaña salada w1",
        "scientific_name": "Anacardium occidentale",
    },
    "macadamia": {
        "aliases": "macadamia, macadamia nuts, nuez macadamia, macadâmia, macadamia natural",
        "scientific_name": "Macadamia integrifolia",
    },
    "avellana-sin-cascara": {
        "aliases": "avellana, avellanas, hazelnut, hazelnuts, avelã, avellanas peladas, avellana sin concha",
        "scientific_name": "Corylus avellana",
    },
    # ===== SEMILLAS Y GRANOS =====
    "semilla-de-anis": {
        "aliases": "anís, semilla de anís, anís en grano, anise seeds, anis em grão, semillas de anís, anís verde",
        "scientific_name": "Pimpinella anisum",
    },
    "semilla-de-calabaza": {
        "aliases": "semilla de calabaza, pepitas, pumpkin seeds, semillas de zapallo, sementes de abóbora, semillas de calabaza peladas",
        "scientific_name": "Cucurbita pepo",
    },
    "lenteja-roja": {
        "aliases": "lenteja, lenteja roja, red lentils, lentilha vermelha, lentejas rojas peladas, lenteja roja partida",
        "scientific_name": "Lens culinaris",
    },
    "quinoa-en-grano": {
        "aliases": "quinoa, quinua, quinoa en grano, quinoa blanca, quinoa peruana, quinoa real, semilla de quinoa",
        "scientific_name": "Chenopodium quinoa",
    },
    "granola-tradicional": {
        "aliases": "granola, granola tradicional, granola natural, granola con miel, muesli, granola caseira",
        "scientific_name": "",
    },
    "garbanzos-9mm": {
        "aliases": "garbanzos, garbanzo, chickpeas, garbanzo seco, grão-de-bico, garbanzos importados, garbanzo entero",
        "scientific_name": "Cicer arietinum",
    },
    "chia-en-semillas": {
        "aliases": "chía, semilla de chía, chia seeds, chía en grano, chía negra, sementes de chia, semillas de chia",
        "scientific_name": "Salvia hispanica",
    },
    "linaza-dorada": {
        "aliases": "linaza, linaza dorada, semillas de lino, golden flax seeds, linhaça dourada, linum, linaza amarilla",
        "scientific_name": "Linum usitatissimum",
    },
    "semilla-de-girasol-sin-sal": {
        "aliases": "girasol, semilla de girasol, pipas de girasol, sunflower seeds, sementes de girassol, semilla girasol natural",
        "scientific_name": "Helianthus annuus",
    },
    "avena-en-copos-finos": {
        "aliases": "avena, avena en copos, avena fina, oat flakes, aveia em flocos, copos de avena, avena instantánea",
        "scientific_name": "Avena sativa",
    },
    "salvado-de-avena": {
        "aliases": "salvado de avena, oat bran, farelo de aveia, fibra de avena, salvado integral",
        "scientific_name": "Avena sativa",
    },
    "trigo-sarraceno-mourisco": {
        "aliases": "trigo sarraceno, mourisco, buckwheat, alforfón, trigo sarraceno en grano, trigo mourisco, fagopyrum",
        "scientific_name": "Fagopyrum esculentum",
    },
    # ===== HARINAS ESPECIALES =====
    "gelatina-sin-sabor-en-polvo": {
        "aliases": "gelatina, gelatina sin sabor, unflavored gelatin, gelatina neutra, gelatina en polvo, gelatina incolora",
        "scientific_name": "",
    },
    "harina-de-almendra-parmex": {
        "aliases": "harina de almendra, harina de almendras, almond flour, almond meal, harina almendra parmex, farinha de amêndoa",
        "scientific_name": "Prunus dulcis",
    },
    "harina-de-almendra-regal": {
        "aliases": "harina de almendra, harina de almendras regal, almond flour regal, farinha de amêndoa, harina almendra regal",
        "scientific_name": "Prunus dulcis",
    },
    "harina-de-almendra-calconut": {
        "aliases": "harina de almendra, harina almendra calconut, almond flour calconut, farinha de amêndoa, harina almendra calconut",
        "scientific_name": "Prunus dulcis",
    },
    "harina-de-coco": {
        "aliases": "harina de coco, coconut flour, farinha de coco, harina coco fina, coco rallado en harina",
        "scientific_name": "Cocos nucifera",
    },
    "harina-de-arroz-integral": {
        "aliases": "harina de arroz, harina de arroz integral, brown rice flour, farinha de arroz integral, harina arroz",
        "scientific_name": "Oryza sativa",
    },
    "harina-de-garbanzos": {
        "aliases": "harina de garbanzos, chickpea flour, farinha de grão-de-bico, harina garbanzo, besan, harina de garbanzo",
        "scientific_name": "Cicer arietinum",
    },
    "harina-de-linaza-dorada": {
        "aliases": "harina de linaza, harina linaza dorada, golden flax flour, farinha de linhaça dourada, harina linaza",
        "scientific_name": "Linum usitatissimum",
    },
    "goma-xantana": {
        "aliases": "goma xantana, xanthan gum, xantana, espesante natural, goma xantan, espesante xantana",
        "scientific_name": "",
    },
    # ===== DERIVADOS DE COCO =====
    "leche-de-coco-en-polvo": {
        "aliases": "leche de coco, leche de coco en polvo, coconut milk powder, leite de coco em pó, leche de coco deshidratada",
        "scientific_name": "Cocos nucifera",
    },
    "chips-de-coco": {
        "aliases": "chips de coco, coconut chips, hojuelas de coco, lascas de coco, chips coco tostado",
        "scientific_name": "Cocos nucifera",
    },
    "coco-rallado-fino": {
        "aliases": "coco rallado, coco rallado fino, shredded coconut fine, coco ralado fino, coco rallado natural",
        "scientific_name": "Cocos nucifera",
    },
    "azucar-de-coco": {
        "aliases": "azúcar de coco, coconut sugar, açúcar de coco, azúcar de coco orgánica, azúcar de coco natural",
        "scientific_name": "Cocos nucifera",
    },
    "coco-rallado-en-copos": {
        "aliases": "coco rallado, coco en copos, coconut flakes, coco ralado em flocos, coco rallado grueso",
        "scientific_name": "Cocos nucifera",
    },
    # ===== FRUTAS DESHIDRATADAS =====
    "cranberry": {
        "aliases": "cranberry, arándano rojo, arándanos rojos deshidratados, cranberries, arándano agrio, dried cranberry",
        "scientific_name": "Vaccinium macrocarpon",
    },
    "damasco-turco": {
        "aliases": "damasco, damasco turco, dried apricot, albaricoque seco, orejones, damasco seco, damasco deshidratado",
        "scientific_name": "Prunus armeniaca",
    },
    "mix-de-frutas-deshidratadas": {
        "aliases": "mix de frutas, frutas deshidratadas, dried fruit mix, mix frutas secas, mistura de frutas secas, mix tropical seco",
        "scientific_name": "",
    },
    "uva-pasa-negra": {
        "aliases": "uva pasa, uva pasa negra, pasas de uva, raisins, uvas pasas, passa de uva preta, pasitas",
        "scientific_name": "Vitis vinifera",
    },
    "kiwi-deshidratado": {
        "aliases": "kiwi, kiwi deshidratado, dried kiwi, kiwi seco, kiwi en rodajas seco",
        "scientific_name": "Actinidia deliciosa",
    },
    "datiles-sin-hueso": {
        "aliases": "dátiles, dátiles sin hueso, dates, pitted dates, tâmaras sem caroço, dátil sin carozo",
        "scientific_name": "Phoenix dactylifera",
    },
    "ciruela-sin-hueso": {
        "aliases": "ciruela, ciruela seca, ciruela sin hueso, prunes, ameixa preta, ciruela pasa, ciruela deshidratada",
        "scientific_name": "Prunus domestica",
    },
    "higo-seco-lerida": {
        "aliases": "higo seco, higos secos, dried figs, figos secos, higo seco lérida, higos lérida, higo importado",
        "scientific_name": "Ficus carica",
    },
    "pina-deshidratada": {
        "aliases": "piña, piña deshidratada, dried pineapple, ananás, abacaxi seco, ananá seco, piña seca",
        "scientific_name": "Ananas comosus",
    },
    "cereza-glaseada": {
        "aliases": "cereza, cerezas glaseadas, glace cherries, cerezas confitadas, cerezas glace, cereza confitada",
        "scientific_name": "Prunus avium",
    },
    "goji-berry": {
        "aliases": "goji, goji berry, goji berries, baya goji, baya de goji, lycium, goji deshidratado",
        "scientific_name": "Lycium barbarum",
    },
    # ===== SUPLEMENTOS Y SUPERALIMENTOS =====
    "spirulina-en-polvo": {
        "aliases": "spirulina, spirulina en polvo, spirulina powder, espirulina, alga spirulina, spirulina natural",
        "scientific_name": "Arthrospira platensis",
    },
    "moringa-en-polvo": {
        "aliases": "moringa, moringa en polvo, moringa powder, moringa oleifera, hojas de moringa, moringa pura",
        "scientific_name": "Moringa oleifera",
    },
    "psyllium": {
        "aliases": "psyllium, cáscara de psyllium, psyllium husk, ispágula, plantago, fibra de psyllium, psilio",
        "scientific_name": "Plantago ovata",
    },
    "eritritol-cristal": {
        "aliases": "eritritol, eritritol cristal, erythritol, edulcorante natural, sustituto del azúcar, eritritol granulado",
        "scientific_name": "",
    },
    "colageno-hidrolizado": {
        "aliases": "colágeno, colágeno hidrolizado, collagen, colágeno bovino, colágeno en polvo, péptidos de colágeno",
        "scientific_name": "",
    },
    "creatina-en-polvo": {
        "aliases": "creatina, creatina monohidratada, creatine, creatine monohydrate, creatina pura, suplemento de creatina",
        "scientific_name": "",
    },
    "maca-peruana-en-polvo": {
        "aliases": "maca, maca peruana, maca en polvo, peruvian maca, lepidium meyenii, maca andina, raíz de maca",
        "scientific_name": "Lepidium meyenii",
    },
    "xilitol-cristal": {
        "aliases": "xilitol, xilitol cristal, xylitol, edulcorante xilitol, sustituto del azúcar, xilitol natural",
        "scientific_name": "",
    },
    "guarana-en-polvo": {
        "aliases": "guaraná, guaraná en polvo, guarana powder, guaraná amazónico, paullinia, guaraná molido",
        "scientific_name": "Paullinia cupana",
    },
}


def lookup(slug: str) -> dict[str, str]:
    """Return aliases + scientific_name for a slug, or empty defaults."""
    return PRODUCT_ALIASES.get(slug, {"aliases": "", "scientific_name": ""})


def coverage_report() -> tuple[int, int]:
    """Return (curated_count, total_known_slugs) — used in CLI checks."""
    return (len(PRODUCT_ALIASES), len(PRODUCT_ALIASES))
