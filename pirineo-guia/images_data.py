"""Imágenes reales por sitio — URLs verificadas vía Wikipedia/Commons API."""

# url: miniatura 960px; full: alta resolución para lightbox
SITES = {
    "ordesa_pradera": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Circo_cotatuero.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Circo_cotatuero.jpg",
        "cap": "Parque Nacional de Ordesa y Monte Perdido",
    },
    "ordesa_cola": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Cascada_Cola_de_Caballo_de_Ordesa_entre_monta%C3%B1as.jpg/960px-Cascada_Cola_de_Caballo_de_Ordesa_entre_monta%C3%B1as.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Cascada_Cola_de_Caballo_de_Ordesa_entre_monta%C3%B1as.jpg",
        "cap": "Cascada de la Cola de Caballo, Ordesa",
    },
    "torla": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Iglesia_de_San_Salvador%2C_Torla%2C_Huesca%2C_Espa%C3%B1a%2C_2015-01-07%2C_DD_02.JPG/960px-Iglesia_de_San_Salvador%2C_Torla%2C_Huesca%2C_Espa%C3%B1a%2C_2015-01-07%2C_DD_02.JPG",
        "full": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Iglesia_de_San_Salvador%2C_Torla%2C_Huesca%2C_Espa%C3%B1a%2C_2015-01-07%2C_DD_02.JPG",
        "cap": "Torla, Huesca",
    },
    "ainsa": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Ainsa_m1.jpg/960px-Ainsa_m1.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Ainsa_m1.jpg",
        "cap": "Plaza Mayor de Aínsa",
    },
    "mediano": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Embalse_de_Mediano.jpg/960px-Embalse_de_Mediano.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/8/82/Embalse_de_Mediano.jpg",
        "cap": "Embalse de Mediano, Sobrarbe",
    },
    "benasque": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Benasque_desde_Los_Tres_Barrancos_01.jpg/960px-Benasque_desde_Los_Tres_Barrancos_01.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/1/17/Benasque_desde_Los_Tres_Barrancos_01.jpg",
        "cap": "Benasque, valle de Benasque",
    },
    "estos": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Valle_de_Est%C3%B3s02.JPG/960px-Valle_de_Est%C3%B3s02.JPG",
        "full": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Valle_de_Est%C3%B3s02.JPG",
        "cap": "Valle de Estós",
    },
    "panticosa": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Balneario_de_Panticosa_%281%29.jpg/960px-Balneario_de_Panticosa_%281%29.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Balneario_de_Panticosa_%281%29.jpg",
        "cap": "Balneario de Panticosa",
    },
    "sallent": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Casa_d%27a_Villa_de_Sallent_de_Galligo.jpg/960px-Casa_d%27a_Villa_de_Sallent_de_Galligo.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Casa_d%27a_Villa_de_Sallent_de_Galligo.jpg",
        "cap": "Sallent de Gállego",
    },
    "hecho": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Val_d%27Echo._R%C3%ADo_Arag%C3%B3n_Subord%C3%A1n.jpg/960px-Val_d%27Echo._R%C3%ADo_Arag%C3%B3n_Subord%C3%A1n.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Val_d%27Echo._R%C3%ADo_Arag%C3%B3n_Subord%C3%A1n.jpg",
        "cap": "Valle de Hecho",
    },
    "anso": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Ans%C3%B3_2012.JPG/960px-Ans%C3%B3_2012.JPG",
        "full": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Ans%C3%B3_2012.JPG",
        "cap": "Ansó, Navarra",
    },
    "vielha": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/VIELHA_-_VAL_D%27ARAN_-_IB-377.JPG/960px-VIELHA_-_VAL_D%27ARAN_-_IB-377.JPG",
        "full": "https://upload.wikimedia.org/wikipedia/commons/a/ac/VIELHA_-_VAL_D%27ARAN_-_IB-377.JPG",
        "cap": "Vielha · Val d'Aran",
    },
    "taull": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/%28Barcelona%29_Frescos_of_Sant_Climent_de_Ta%C3%BCll.jpg/960px-%28Barcelona%29_Frescos_of_Sant_Climent_de_Ta%C3%BCll.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/7/71/%28Barcelona%29_Frescos_of_Sant_Climent_de_Ta%C3%BCll.jpg",
        "cap": "Sant Climent de Taüll (románico catalán)",
    },
    "canfranc": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Canfranc_Estaci%C3%B3n._Puerta_de_acceso.jpg/960px-Canfranc_Estaci%C3%B3n._Puerta_de_acceso.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Canfranc_Estaci%C3%B3n._Puerta_de_acceso.jpg",
        "cap": "Estación internacional de Canfranc",
    },
    "lescun": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/LescunVueVersPasDAzuns.jpg/960px-LescunVueVersPasDAzuns.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/4/46/LescunVueVersPasDAzuns.jpg",
        "cap": "Lescun, valle d'Aspe",
    },
    "laruns": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/La_mairie_de_Laruns.jpg/960px-La_mairie_de_Laruns.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/3/3c/La_mairie_de_Laruns.jpg",
        "cap": "Laruns, valle de Ossau",
    },
    "bious": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Lac_de_Bious-Artigues_%281%29.jpg/960px-Lac_de_Bious-Artigues_%281%29.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Lac_de_Bious-Artigues_%281%29.jpg",
        "cap": "Lac de Bious-Artigues",
    },
    "cauterets": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Cauterets_65_H%C3%B4tel_de_ville_Vue_SE_2014.jpg/960px-Cauterets_65_H%C3%B4tel_de_ville_Vue_SE_2014.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/9/94/Cauterets_65_H%C3%B4tel_de_ville_Vue_SE_2014.jpg",
        "cap": "Cauterets",
    },
    "pont_espagne": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Pont_espagne.jpg/960px-Pont_espagne.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Pont_espagne.jpg",
        "cap": "Pont d'Espagne",
    },
    "gaube": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Lago_de_Gaube.JPG/960px-Lago_de_Gaube.JPG",
        "full": "https://upload.wikimedia.org/wikipedia/commons/2/20/Lago_de_Gaube.JPG",
        "cap": "Lac de Gaube y Vignemale",
    },
    "gavarnie": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Gavarnie_recti_small_Wikimedia_Commons.jpg/960px-Gavarnie_recti_small_Wikimedia_Commons.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Gavarnie_recti_small_Wikimedia_Commons.jpg",
        "cap": "Cirque de Gavarnie",
    },
    "gavarnie_cascade": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/.00_2831_Grande_Cascade_de_Gavarnie_-_Pyrinees_%28Frankreich%29.jpg/960px-.00_2831_Grande_Cascade_de_Gavarnie_-_Pyrinees_%28Frankreich%29.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/2/2b/.00_2831_Grande_Cascade_de_Gavarnie_-_Pyrinees_%28Frankreich%29.jpg",
        "cap": "Grande Cascade de Gavarnie",
    },
    "tourmalet": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Col_tourmalet_01.jpg/960px-Col_tourmalet_01.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Col_tourmalet_01.jpg",
        "cap": "Col du Tourmalet",
    },
    "payolle": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Payolle_Lac.jpg/960px-Payolle_Lac.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Payolle_Lac.jpg",
        "cap": "Lac de Payolle",
    },
    "puigcerda": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Plaza_Dion%C3%ADs_Puig.jpg/960px-Plaza_Dion%C3%ADs_Puig.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Plaza_Dion%C3%ADs_Puig.jpg",
        "cap": "Puigcerdà, Cerdanya catalana",
    },
    "llivia": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Ll%C3%ADvia_-_1911.jpg/960px-Ll%C3%ADvia_-_1911.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/4/47/Ll%C3%ADvia_-_1911.jpg",
        "cap": "Llívia, enclave catalán en Francia",
    },
    "montlouis": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Mont-Louis_-_53319720163.jpg/960px-Mont-Louis_-_53319720163.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Mont-Louis_-_53319720163.jpg",
        "cap": "Mont-Louis, fortaleza Vauban",
    },
    "villefranche": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Villefranche-de-Conflent_-_Town_hall_01.jpg/960px-Villefranche-de-Conflent_-_Town_hall_01.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/d/db/Villefranche-de-Conflent_-_Town_hall_01.jpg",
        "cap": "Villefranche-de-Conflent (UNESCO)",
    },
    "canigo": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/35/Canig%C3%B3.jpeg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/3/35/Canig%C3%B3.jpeg",
        "cap": "Canigó desde Prades",
    },
    "jaca": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Jaca_-_Ciudadela_24.jpg/960px-Jaca_-_Ciudadela_24.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/6/60/Jaca_-_Ciudadela_24.jpg",
        "cap": "Ciudadela de Jaca",
    },
}
