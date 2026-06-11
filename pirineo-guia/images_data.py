"""Imágenes reales por sitio (Wikipedia Commons / verificadas)."""

# url: miniatura; full: alta resolución para zoom en lightbox
SITES = {
    "ordesa_pradera": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/WLE_-_2020_-_Parque_nacional_de_Ordesa_y_Monte_Perdido.jpg/960px-WLE_-_2020_-_Parque_nacional_de_Ordesa_y_Monte_Perdido.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/9/90/WLE_-_2020_-_Parque_nacional_de_Ordesa_y_Monte_Perdido.jpg",
        "cap": "Parque Nacional de Ordesa y Monte Perdido",
    },
    "ordesa_cola": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Cola_de_Caballo_%28Ordesa%29.jpg/960px-Cola_de_Caballo_%28Ordesa%29.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Cola_de_Caballo_%28Ordesa%29.jpg",
        "cap": "Cascada de la Cola de Caballo, Ordesa",
    },
    "torla": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Torla_-_01.jpg/960px-Torla_-_01.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Torla_-_01.jpg",
        "cap": "Torla, Huesca",
    },
    "ainsa": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Plaza_Mayor%2C_Ainsa%2C_Sobrarbe%2C_Huesca%2C_Aragon%2C_Spain.jpg/960px-Plaza_Mayor%2C_Ainsa%2C_Sobrarbe%2C_Huesca%2C_Aragon%2C_Spain.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/d/da/Plaza_Mayor%2C_Ainsa%2C_Sobrarbe%2C_Huesca%2C_Aragon%2C_Spain.jpg",
        "cap": "Plaza Mayor de Aínsa",
    },
    "mediano": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Embalse_de_Mediano.jpg/960px-Embalse_de_Mediano.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Embalse_de_Mediano.jpg",
        "cap": "Embalse de Mediano, Sobrarbe",
    },
    "benasque": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Benasque.jpg/960px-Benasque.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Benasque.jpg",
        "cap": "Benasque, valle de Benasque",
    },
    "estos": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Valle_de_Est%C3%B3s.jpg/960px-Valle_de_Est%C3%B3s.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Valle_de_Est%C3%B3s.jpg",
        "cap": "Valle de Estós",
    },
    "panticosa": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Balneario_de_Panticosa.jpg/960px-Balneario_de_Panticosa.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Balneario_de_Panticosa.jpg",
        "cap": "Balneario de Panticosa",
    },
    "sallent": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Sallent_de_G%C3%A1llego.jpg/960px-Sallent_de_G%C3%A1llego.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Sallent_de_G%C3%A1llego.jpg",
        "cap": "Sallent de Gállego",
    },
    "hecho": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Hecho_%28Huesca%29.jpg/960px-Hecho_%28Huesca%29.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Hecho_%28Huesca%29.jpg",
        "cap": "Valle de Hecho",
    },
    "anso": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Ans%C3%B3.jpg/960px-Ans%C3%B3.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Ans%C3%B3.jpg",
        "cap": "Ansó, Navarra",
    },
    "vielha": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Pano_of_Boss%C3%B2st_in_the_Vall_d%27Aran.jpg/960px-Pano_of_Boss%C3%B2st_in_the_Vall_d%27Aran.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/1/11/Pano_of_Boss%C3%B2st_in_the_Vall_d%27Aran.jpg",
        "cap": "Val d'Aran · Bossòst",
    },
    "taull": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Sant_Climent%2C_Ta%C3%BCll.jpg/960px-Sant_Climent%2C_Ta%C3%BCll.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Sant_Climent%2C_Ta%C3%BCll.jpg",
        "cap": "Sant Climent de Taüll (románico catalán)",
    },
    "canfranc": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Canfranc_new_and_old_station.jpg/960px-Canfranc_new_and_old_station.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/3/38/Canfranc_new_and_old_station.jpg",
        "cap": "Estación internacional de Canfranc",
    },
    "lescun": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Lescun_%28Hautes-Pyr%C3%A9n%C3%A9es%29.jpg/960px-Lescun_%28Hautes-Pyr%C3%A9n%C3%A9es%29.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Lescun_%28Hautes-Pyr%C3%A9n%C3%A9es%29.jpg",
        "cap": "Lescun, valle d'Aspe",
    },
    "laruns": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Laruns_%28Pyr%C3%A9n%C3%A9es-Atlantiques%29.jpg/960px-Laruns_%28Pyr%C3%A9n%C3%A9es-Atlantiques%29.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Laruns_%28Pyr%C3%A9n%C3%A9es-Atlantiques%29.jpg",
        "cap": "Laruns, valle de Ossau",
    },
    "bious": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Lac_de_Bious-Artigues.jpg/960px-Lac_de_Bious-Artigues.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Lac_de_Bious-Artigues.jpg",
        "cap": "Lac de Bious-Artigues",
    },
    "cauterets": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Cauterets_%28Hautes-Pyr%C3%A9n%C3%A9es%29.jpg/960px-Cauterets_%28Hautes-Pyr%C3%A9n%C3%A9es%29.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Cauterets_%28Hautes-Pyr%C3%A9n%C3%A9es%29.jpg",
        "cap": "Cauterets",
    },
    "pont_espagne": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Pont_espagne.jpg/960px-Pont_espagne.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Pont_espagne.jpg",
        "cap": "Pont d'Espagne",
    },
    "gaube": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Lac_de_Gaube_01.jpg/960px-Lac_de_Gaube_01.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Lac_de_Gaube_01.jpg",
        "cap": "Lac de Gaube y Vignemale",
    },
    "gavarnie": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Gavarnie_recti_small_Wikipedia.jpg/960px-Gavarnie_recti_small_Wikipedia.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Gavarnie_recti_small_Wikipedia.jpg",
        "cap": "Cirque de Gavarnie",
    },
    "gavarnie_cascade": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Cirque_de_Gavarnie_Haute_Pyrenees.jpg/960px-Cirque_de_Gavarnie_Haute_Pyrenees.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Cirque_de_Gavarnie_Haute_Pyrenees.jpg",
        "cap": "Grande Cascade de Gavarnie",
    },
    "tourmalet": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Col_du_Tourmalet.jpg/960px-Col_du_Tourmalet.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Col_du_Tourmalet.jpg",
        "cap": "Col du Tourmalet",
    },
    "payolle": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Lac_de_Payolle.jpg/960px-Lac_de_Payolle.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Lac_de_Payolle.jpg",
        "cap": "Lac de Payolle",
    },
    "puigcerda": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Ayuntamiento_de_Puigcerd%C3%A0.jpg/960px-Ayuntamiento_de_Puigcerd%C3%A0.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Ayuntamiento_de_Puigcerd%C3%A0.jpg",
        "cap": "Puigcerdà, Cerdanya catalana",
    },
    "llivia": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Ll%C3%ADvia.jpg/960px-Ll%C3%ADvia.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Ll%C3%ADvia.jpg",
        "cap": "Llívia, enclave catalán en Francia",
    },
    "montlouis": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Mont-Louis%2C_cit%C3%A9_vauban.jpg/960px-Mont-Louis%2C_cit%C3%A9_vauban.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Mont-Louis%2C_cit%C3%A9_vauban.jpg",
        "cap": "Mont-Louis, fortaleza Vauban",
    },
    "villefranche": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Villefranche-de-Conflent.jpg/960px-Villefranche-de-Conflent.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/9/99/Villefranche-de-Conflent.jpg",
        "cap": "Villefranche-de-Conflent (UNESCO)",
    },
    "canigo": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Canig%C3%B3_des_de_Prades.jpg/960px-Canig%C3%B3_des_de_Prades.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Canig%C3%B3_des_de_Prades.jpg",
        "cap": "Canigó desde Prades",
    },
    "jaca": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Ciudadela_de_Jaca.jpg/960px-Ciudadela_de_Jaca.jpg",
        "full": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Ciudadela_de_Jaca.jpg",
        "cap": "Ciudadela de Jaca",
    },
}
