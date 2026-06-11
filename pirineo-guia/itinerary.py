"""Itinerario 12 días — Pirineo aragonés, catalán y francés."""


def build_days(day_block, gallery, spot):
    days = ""

    days += day_block(
        1, "Ordesa · Huesca", "Parque Nacional de Ordesa y Torla",
        "95", "1 h 45", "8–16", "3–6 h",
        "Jaca <span class=\"arrow\">→</span> Broto <span class=\"arrow\">→</span> Torla <span class=\"arrow\">→</span> Pradera de Ordesa <span class=\"arrow\">→</span> Cola de Caballo",
        "Primer contacto con el Pirineo atlántico: hayas en brote, cascadas con caudal de deshielo y el murmullo del Arazas. Torla es un pueblo de montaña auténtico.",
        gallery("ordesa_pradera", "ordesa_cola", "torla", "ordesa_pradera"),
        "<li>Visitar Broto y sus puentes medievales</li><li>Sendero clásico Ordesa – Cola de Caballo</li><li>Atardecer en Torla con vistas al Mondarruego</li>",
        "<li>8:00 Salida Jaca</li><li>9:30 Pradera de Ordesa</li><li>13:00 Comida</li><li>17:00 Regreso parking</li><li>19:00 Paseo Torla</li>",
        spot("ordesa_pradera", "Pradera de Ordesa", "Pradera amplia flanqueada por paredes de caliza, hayas y el río Arazas.") +
        spot("ordesa_cola", "Cola de Caballo", "Cascada icónica del parque; en primavera el caudal es generoso.") +
        spot("torla", "Torla", "Pueblo de piedra pegado al parque, base perfecta para Ordesa."),
        """<div class="hike-box"><strong>🥾 Ordesa – Cola de Caballo</strong><br>~16 km ida/vuelta · +400 m · 5–6 h. <a href="https://www.ordesa.net/" target="_blank" rel="noopener">ordesa.net →</a></div>""",
        "https://www.google.com/maps/dir/Jaca,+Huesca/Torla,+Huesca/Pradera+de+Ordesa,+Torla",
        ["Jaca, Huesca", "Broto, Huesca", "Torla, Huesca", "Pradera de Ordesa, Torla"],
        "map-day1", "Ordesa",
    )

    days += day_block(
        2, "Sobrarbe", "Aínsa medieval y Sobrarbe",
        "78", "1 h 30", "4–6", "1h 30–2 h",
        "Torla <span class=\"arrow\">→</span> Fiscal <span class=\"arrow\">→</span> Aínsa <span class=\"arrow\">→</span> Mediano <span class=\"arrow\">→</span> Escalona",
        "Pueblo amurallado de película, embalse turquesa entre peñas y valle auténtico del Sobrarbe.",
        gallery("ainsa", "mediano", "ainsa", "torla"),
        "<li>Plaza porticada de Aínsa</li><li>Mirador del embalse de Mediano</li><li>Sendero ribazas de Escalona</li>",
        "<li>9:00 Torla → Aínsa</li><li>10:30 Aínsa a pie</li><li>13:00 Comida en plaza</li><li>15:30 Mediano</li>",
        spot("ainsa", "Aínsa", "Plaza mayor triangular, arcadas de piedra y castillo encima.") +
        spot("mediano", "Embalse de Mediano", "Agua turquesa atrapada entre paredes verticales del Sobrarbe.") +
        spot("torla", "Entorno Sobrarbe", "Sierras calizas y valles verdes entre Ordesa y Aínsa."),
        """<div class="hike-box"><strong>🥾 Ribazas de Escalona</strong><br>~4 km · 1 h 30 · senda fluvial suave.</div>""",
        "https://www.google.com/maps/dir/Torla,+Huesca/A%C3%ADnsa,+Huesca/Embalse+de+Mediano,+Huesca",
        ["Torla, Huesca", "Aínsa, Huesca", "Embalse de Mediano, Huesca"],
        "map-day2", "Sobrarbe",
    )

    days += day_block(
        3, "Benasque", "Valle de Benasque y Estós",
        "72", "1 h 20", "6–10", "2h 30–4 h",
        "Aínsa <span class=\"arrow\">→</span> Campo <span class=\"arrow\">→</span> Benasque <span class=\"arrow\">→</span> Cerler <span class=\"arrow\">→</span> Estós",
        "El Pirineo más alpino: picos nevados, ibones glaciares y pueblos de piedra donde aún suena el aragonés.",
        gallery("benasque", "estos", "benasque", "estos"),
        "<li>Benasque: plaza e iglesia</li><li>Valle de Estós – Espigantosa</li><li>Atardecer en Cerler</li>",
        "<li>8:30 Aínsa</li><li>10:00 Benasque</li><li>11:00 Sendero Estós</li><li>17:00 Regreso</li>",
        spot("estos", "Valle de Estós", "Hayas centenarias, río Fradiñana y paredes de granito.") +
        spot("benasque", "Benasque", "Capital del valle: piedra gris, bares de montañeros y tiendas de senderismo.") +
        spot("estos", "Cascada Espigantosa", "Caída vertical en el bosque con caudal de deshielo en mayo-junio."),
        """<div class="hike-box"><strong>🥾 Estós – Espigantosa</strong><br>~10 km · +350 m · 2h 30–3 h ida.</div>""",
        "https://www.google.com/maps/dir/A%C3%ADnsa,+Huesca/Benasque,+Huesca/Valle+de+Est%C3%B3s,+Huesca",
        ["Aínsa, Huesca", "Benasque, Huesca", "Valle de Estós, Huesca"],
        "map-day3", "Benasque",
    )

    days += day_block(
        4, "Valle de Tena", "Panticosa, ibones y Sallent",
        "65", "1 h 15", "5–8", "2–3 h",
        "Benasque <span class=\"arrow\">→</span> Biescas <span class=\"arrow\">→</span> Panticosa <span class=\"arrow\">→</span> Sallent de Gállego",
        "Aguas termales de montaña, ibones espejo bajo picos nevados y el Gállego bajando con furia de deshielo.",
        gallery("panticosa", "sallent", "panticosa", "benasque"),
        "<li>Baño termal opcional Panticosa</li><li>Ibón de Piedrafita según nieve</li><li>Paseo por Sallent</li>",
        "<li>9:00 Benasque</li><li>10:30 Panticosa</li><li>14:00 Sallent</li>",
        spot("panticosa", "Panticosa", "Balneario histórico: vapor sobre el río Caldarés entre picos.") +
        spot("sallent", "Sallent de Gállego", "Pueblo de pizarra negra auténtico, menos masificado que Formigal.") +
        spot("benasque", "Valle de Tena", "Transición alpina hacia el Gállego y los ibones."),
        """<div class="hike-box"><strong>🥾 Panticosa – Ibón Piedrafita</strong><br>~8 km · +300 m · 2–3 h. Comprobar nieve en <a href="https://www.turismodearagon.com/" target="_blank" rel="noopener">Turismo Aragón</a>.</div>""",
        "https://www.google.com/maps/dir/Benasque,+Huesca/Panticosa,+Huesca/Sallent+de+G%C3%A1llego,+Huesca",
        ["Benasque, Huesca", "Panticosa, Huesca", "Sallent de Gállego, Huesca"],
        "map-day4", "Tena",
    )

    days += day_block(
        5, "Valle de Hecho", "Selva de Oza y Ansó (Navarra)",
        "110", "2 h", "6–9", "2h 30–3 h",
        "Sallent <span class=\"arrow\">→</span> Hecho <span class=\"arrow\">→</span> Selva de Oza <span class=\"arrow\">→</span> Ansó",
        "Pirineo navarro: hayedos, cascadas escondidas y Ansó, uno de los pueblos mejor conservados del Roncal.",
        gallery("hecho", "anso", "hecho", "anso"),
        "<li>Valle de Hecho en coche</li><li>Sendero Selva de Oza</li><li>Ansó: arquitectura tradicional</li>",
        "<li>8:00 Sallent</li><li>10:30 Selva de Oza</li><li>13:30 Ansó</li>",
        spot("hecho", "Valle de Hecho", "Praderas verdes, caseríos de piedra y el río Veral.") +
        spot("anso", "Ansó", "Calles empedradas y casas con lonas de piedra — joya de Navarra.") +
        spot("hecho", "Selva de Oza", "Hayedo atlántico con musgo, helechos y cascadas en gradas."),
        """<div class="hike-box"><strong>🥾 Selva de Oza</strong><br>~6 km · +250 m · 2 h 30. <a href="https://www.turismo.navarra.es/" target="_blank" rel="noopener">Turismo Navarra →</a></div>""",
        "https://www.google.com/maps/dir/Sallent+de+G%C3%A1llego,+Huesca/Hecho,+Navarra/Ans%C3%B3,+Navarra",
        ["Sallent de Gállego, Huesca", "Hecho, Navarra", "Ansó, Navarra"],
        "map-day5", "Hecho",
    )

    days += day_block(
        6, "Pirineo catalán · España", "Val d'Aran, Vielha y Taüll",
        "105", "2 h 15", "3–5", "1–2 h",
        "Ansó <span class=\"arrow\">→</span> Bielsa <span class=\"arrow\">→</span> Vielha <span class=\"arrow\">→</span> Arties <span class=\"arrow\">→</span> Taüll",
        "Entramos en el Val d'Aran, la comarca catalana al norte del Pirineo: aranés en las calles, iglesios románicos del s. XII y vistas a la Maladeta.",
        gallery("vielha", "taull", "vielha", "taull"),
        "<li>Vielha: capital del Aran — mercado y casco</li><li>Arties: pueblo de piedra junto al Garona</li><li>Sant Climent de Taüll (románico UNESCO)</li><li>Opcional: subida al Mirador de Beret</li>",
        "<li>8:00 Ansó</li><li>10:30 Vielha</li><li>12:00 Taüll — iglesia románica</li><li>14:00 Comida en Arties</li><li>17:00 Paseo Vielha</li>",
        spot("vielha", "Vielha · Val d'Aran", "Capital aranesa: el Garona nace aquí y las montañas rodean el valle.") +
        spot("taull", "Sant Climent de Taüll", "Iglesia románica del s. XII con frescos bizantinos — joya del arte catalán.") +
        spot("vielha", "Bossòst", "Pueblo con casas de pizarra y el río pasando bajo el puente de madera."),
        """<div class="hike-box"><strong>🥾 Taüll – Sant Climent</strong><br>~2 km · llano · 45 min. Visita interior con reserva en temporada. <a href="https://www.turismevaldaran.com/" target="_blank" rel="noopener">Turismo Val d'Aran →</a></div>""",
        "https://www.google.com/maps/dir/Ans%C3%B3,+Navarra/Vielha,+Lleida/Ta%C3%BCll,+Lleida",
        ["Ansó, Navarra", "Vielha e Mijaran, Lleida", "Taüll, Lleida"],
        "map-day6", "Val d'Aran",
    )

    days += """
      <div class="section-intro" style="margin:3rem 0 2rem;padding:1.25rem 1.5rem;background:var(--pine-pale);border-radius:var(--radius-sm);border-left:4px solid var(--pine)">
        <strong>🇫🇷 Extensión · 6 días Pirineo francés y catalán</strong><br>
        Del Val d'Aran cruzamos a Francia por Somport. Seis jornadas por Hautes-Pyrénées y la Cerdanya/Catalunya Nord: Lescun, Gaube, Gavarnie, Tourmalet, Puigcerdà, Villefranche y el Canigó.
      </div>
"""

    days += day_block(
        7, "Franco-español · Aspe", "Canfranc, Somport y Lescun",
        "98", "2 h", "5–8", "2–3 h",
        "Vielha <span class=\"arrow\">→</span> Bielsa <span class=\"arrow\">→</span> Canfranc <span class=\"arrow\">→</span> Somport <span class=\"arrow\">→</span> Lescun",
        "Cruzamos la frontera: estación Belle Époque de Canfranc, paso de Somport y Lescun, pueblo auténtico del valle d'Aspe.",
        gallery("canfranc", "lescun", "canfranc", "lescun"),
        "<li>Estación internacional de Canfranc</li><li>Cruce Somport — DNI/pasaporte</li><li>Lescun y valle d'Aspe</li>",
        "<li>8:30 Vielha</li><li>10:00 Canfranc</li><li>11:00 Somport</li><li>12:30 Lescun</li><li>15:00 Sendero</li>",
        spot("canfranc", "Estación de Canfranc", "Palacio ferroviario de 1928 entre montañas — uno de los edificios más fotogénicos de los Pirineos.") +
        spot("lescun", "Lescun", "Pueblo de piedra y madera en el valle d'Aspe, entre los más bonitos de Francia.") +
        spot("lescun", "Valle d'Aspe", "Praderas, Pic d'Anie al fondo y queserías de oveja."),
        """<div class="hike-box"><strong>🥾 Lescun – Cascada d'Arrious</strong><br>~5 km · +200 m · 2 h. <a href="https://www.pyrenees-ariegeoises.com/" target="_blank" rel="noopener">Turismo Ariège →</a></div>""",
        "https://www.google.com/maps/dir/Vielha,+Lleida/Canfranc,+Huesca/Lescun,+France",
        ["Vielha e Mijaran, Lleida", "Canfranc, Huesca", "Lescun, France"],
        "map-day7", "Canfranc",
    )

    days += day_block(
        8, "Valle de Ossau · Francia", "Laruns, Aubisque y Lac de Bious",
        "88", "2 h", "4–6", "1h 30–2 h",
        "Lescun <span class=\"arrow\">→</span> Laruns <span class=\"arrow\">→</span> Col du Soulor <span class=\"arrow\">→</span> Gabas",
        "Carreteras legendarias del Tour de France y el espejo turquesa del Lac de Bious bajo el Pic du Midi de Ossau.",
        gallery("laruns", "bious", "laruns", "bious"),
        "<li>Laruns: arquitectura ossalat</li><li>Col du Soulor y Aubisque</li><li>Lac de Bious-Artigues</li>",
        "<li>8:00 Lescun</li><li>10:00 Laruns</li><li>11:30 Col du Soulor</li><li>15:00 Lac Bious</li>",
        spot("laruns", "Laruns", "Capital del valle de Ossau: casas blancas, queserías y el Gave d'Ossau.") +
        spot("bious", "Lac de Bious-Artigues", "Ibón a 1.725 m reflejando el Pic du Midi de Ossau.") +
        spot("laruns", "Valle de Ossau", "Prados verdes, ovejas y picos calcáreos al fondo."),
        """<div class="hike-box"><strong>🥾 Gabas – Lac Bious</strong><br>~6 km · +150 m · 1 h ida. <a href="https://www.pyrenees-national.fr/" target="_blank" rel="noopener">Parc National →</a></div>""",
        "https://www.google.com/maps/dir/Lescun,+France/Laruns,+France/Gabas,+France",
        ["Lescun, France", "Laruns, France", "Gabas, France"],
        "map-day8", "Ossau",
    )

    days += day_block(
        9, "Cauterets · Francia", "Pont d'Espagne y Lac de Gaube",
        "68", "1 h 25", "4–6", "2–2h 30",
        "Laruns <span class=\"arrow\">→</span> Cauterets <span class=\"arrow\">→</span> Pont d'Espagne <span class=\"arrow\">→</span> Lac de Gaube",
        "Parque Nacional francés: Cauterets termal, Puente de España sobre cascadas y Lac de Gaube a los pies del Vignemale.",
        gallery("cauterets", "pont_espagne", "gaube", "gaube"),
        "<li>Cauterets: pueblo balneario</li><li>Pont d'Espagne</li><li>Lac de Gaube (GR-10)</li>",
        "<li>8:30 Laruns</li><li>10:00 Cauterets</li><li>11:00 Pont d'Espagne</li><li>12:30 Lac de Gaube</li>",
        spot("cauterets", "Cauterets", "Pueblo victoriano entre bosques, olor a azufre suave y calles de madera pintada.") +
        spot("pont_espagne", "Pont d'Espagne", "Puente de piedra sobre cascadas múltiples — puerta al parque nacional.") +
        spot("gaube", "Lac de Gaube", "Lago glaciar turquesa con el Vignemale (3.298 m) de fondo — imprescindible."),
        """<div class="hike-box"><strong>🥾 Pont d'Espagne – Gaube</strong><br>~5 km · +150 m · 2 h. <a href="https://www.cauterets.com/" target="_blank" rel="noopener">cauterets.com →</a></div>""",
        "https://www.google.com/maps/dir/Laruns,+France/Cauterets,+France/Pont+d%27Espagne,+Cauterets",
        ["Laruns, France", "Cauterets, France", "Pont d'Espagne, Cauterets, France"],
        "map-day9", "Gaube",
    )

    days += day_block(
        10, "Gavarnie · UNESCO", "Cirque de Gavarnie y Grande Cascade",
        "42", "1 h", "6–8", "2h 30–3 h",
        "Cauterets <span class=\"arrow\">→</span> Luz-Saint-Sauveur <span class=\"arrow\">→</span> Gavarnie <span class=\"arrow\">→</span> Cirque UNESCO",
        "El coloso de la naturaleza: anfiteatro glaciar de 1.500 m, cascada de 423 m y pueblo de montaña auténtico.",
        gallery("gavarnie", "gavarnie_cascade", "gavarnie", "gavarnie_cascade"),
        "<li>Luz-Saint-Sauveur: fortalezas Vauban</li><li>Sendero al Cirque de Gavarnie</li><li>Grande Cascade — chubasquero</li>",
        "<li>9:00 Cauterets</li><li>10:00 Luz</li><li>10:45 Gavarnie</li><li>11:30 Cirque</li><li>17:00 Regreso</li>",
        spot("gavarnie", "Cirque de Gavarnie", "Anfiteatro glaciar UNESCO de 1.500 m de pared vertical.") +
        spot("gavarnie_cascade", "Grande Cascade", "423 m — la cascada más alta de Francia metropolitana.") +
        spot("gavarnie", "Gavarnie pueblo", "Casas de piedra gris, queserías y burros que suben al cirque."),
        """<div class="hike-box"><strong>🥾 Gavarnie – Cirque</strong><br>~6 km · +200 m · 2h 30–3 h. <a href="https://www.gavarnie.com/" target="_blank" rel="noopener">gavarnie.com →</a></div>""",
        "https://www.google.com/maps/dir/Cauterets,+France/Gavarnie,+France",
        ["Cauterets, France", "Luz-Saint-Sauveur, France", "Gavarnie, France"],
        "map-day10", "Gavarnie",
    )

    days += day_block(
        11, "Tourmalet · Valle d'Aure", "Col du Tourmalet y Lac de Payolle",
        "75", "1 h 45", "3–5", "1–1h 30",
        "Gavarnie <span class=\"arrow\">→</span> Col du Tourmalet <span class=\"arrow\">→</span> Lac de Payolle <span class=\"arrow\">→</span> Arreau",
        "Subimos el mítico Tourmalet (2.115 m) y bajamos al valle d'Aure: lagos de Payolle entre abetos y pueblos de piedra.",
        gallery("tourmalet", "payolle", "tourmalet", "payolle"),
        "<li>Col du Tourmalet — cumbre ciclista</li><li>Lac de Payolle</li><li>Arreau: pueblo del valle d'Aure</li>",
        "<li>8:00 Gavarnie</li><li>9:30 Tourmalet</li><li>10:30 Payolle</li><li>12:00 Arreau — comida</li>",
        spot("tourmalet", "Col du Tourmalet", "Puerto a 2.115 m — el más alto del Tour asfaltado. Vistas 360°.") +
        spot("payolle", "Lac de Payolle", "Lago de montaña rodeado de hayas y abetos a 1.130 m.") +
        spot("payolle", "Valle d'Aure", "Praderas verdes y caseríos de piedra entre pinares."),
        """<div class="hike-box"><strong>🥾 Lac de Payolle</strong><br>~3 km · llano · 1 h rodeando el lago.</div>""",
        "https://www.google.com/maps/dir/Gavarnie,+France/Col+du+Tourmalet/Lac+de+Payolle,+France/Arreau,+France",
        ["Gavarnie, France", "Col du Tourmalet, France", "Lac de Payolle, France", "Arreau, France"],
        "map-day11", "Tourmalet",
    )

    days += day_block(
        12, "Catalunya Nord · Cerdanya", "Puigcerdà, Mont-Louis, Villefranche y Canigó",
        "130", "2 h 45", "4–7", "2–3 h",
        "Arreau <span class=\"arrow\">→</span> Puymorens <span class=\"arrow\">→</span> Puigcerdà <span class=\"arrow\">→</span> Llívia <span class=\"arrow\">→</span> Mont-Louis <span class=\"arrow\">→</span> Villefranche <span class=\"arrow\">→</span> Prades",
        "Cierre en el Pirineo catalán francés: cruzamos la Cerdanya, el enclave de Llívia, la fortaleza Vauban de Mont-Louis, Villefranche-de-Conflent (UNESCO) y las vistas al Canigó.",
        gallery("puigcerda", "llivia", "villefranche", "canigo"),
        "<li>Túnel de Puymorens → Cerdanya</li><li>Puigcerdà y mercado</li><li>Llívia — enclave catalán en Francia</li><li>Mont-Louis: ciudadela Vauban</li><li>Villefranche-de-Conflent (UNESCO)</li><li>Mirador al Canigó desde Prades</li>",
        "<li>8:00 Arreau</li><li>10:00 Puigcerdà</li><li>11:00 Llívia</li><li>12:00 Mont-Louis</li><li>14:00 Villefranche</li><li>16:00 Prades — Canigó</li><li>18:00 Fin del viaje</li>",
        spot("puigcerda", "Puigcerdà", "Capital de la Cerdanya catalana: plaza, lago y ambiente mediterráneo de montaña.") +
        spot("llivia", "Llívia", "Pueblo catalán rodeado de territorio francés — farmacia más antigua de Europa.") +
        spot("villefranche", "Villefranche-de-Conflent", "Villa medieval amurallada UNESCO, tren amarillo del Petit Train y Fort Liberia.") +
        spot("canigo", "Canigó", "Montaña sagrada de Catalunya — vistas desde Prades o sendero a Cortalets (1 día)."),
        """<div class="hike-box"><strong>🥾 Villefranche – Fort Liberia</strong><br>~4 km · +200 m · 1h 30. Teleférico disponible. Alternativa: paseo murallas UNESCO. <a href="https://www.catalunya.com/" target="_blank" rel="noopener">Catalunya Nord →</a></div>""",
        "https://www.google.com/maps/dir/Arreau,+France/Puigcerd%C3%A0,+Spain/Mont-Louis,+France/Villefranche-de-Conflent,+France/Prades,+France",
        ["Arreau, France", "Puigcerdà, Spain", "Llívia, Spain", "Mont-Louis, France", "Villefranche-de-Conflent, France", "Prades, France"],
        "map-day12", "Cerdanya",
    )

    return days
