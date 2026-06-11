#!/usr/bin/env python3
"""Genera index.html de la guía del Pirineo."""
import re
from pathlib import Path

BASE = Path(__file__).parent
ROOT = BASE.parent

IMG = {
    "hero": "photo-1519681393784-d120267933ba",
    "m1": "photo-1470071459604-3b5ec3a7fe05",
    "m2": "photo-1469474968028-56623f02e42e",
    "m3": "photo-1441974231531-c6227db76b6e",
    "m4": "photo-1506905925346-21bda4d32df4",
    "m5": "photo-1551632811-561732d1e306",
    "m6": "photo-1472214103451-9374bd1c798e",
    "m7": "photo-1439853949127-fa647821eba0",
    "m8": "photo-1518495973542-4542c06a5843",
    "m9": "photo-1682687220063-4742bd7fd538",
    "m10": "photo-1544551763-46a013bb70d5",
    "m11": "photo-1566073771259-6a8506099945",
    "m12": "photo-1520250497591-112f2f40a3f4",
    "m13": "photo-1464822759023-fed622ff2c3b",
    "m14": "photo-1519904981063-b0cf448d479e",
    "m15": "photo-1528360983277-13d401cdc186",
    "m16": "photo-1493246507139-91e8fad9978e",
    "m17": "photo-1475924156734-496f6cac6ec1",
}


def u(key, w=800):
    return f"https://images.unsplash.com/{IMG[key]}?w={w}&q=80"


def gallery(*keys):
    return "".join(
        f'<img src="{u(k)}" alt="" loading="lazy">' for k in keys
    )


def spot(img, title, desc):
    return f"""<li class="spot-item">
                  <div class="spot-img" style="background-image:url('{u(img)}')" role="img" aria-label="{title}"></div>
                  <div class="spot-body"><strong>{title}</strong><span class="spot-desc">{desc}</span></div>
                </li>"""


def day_block(num, zone, title, drive_km, drive_time, hike_km, hike_time, route_text, teaser, gallery_html, activities, schedule, spots_html, hike_html, gmaps_url, map_id, day_key_label):
    return f"""
      <article class="day-card" id="dia-{num}">
        <div class="day-header">
          <div>
            <p class="day-num">Día {num} · {zone}</p>
            <h3 class="day-title">{title}</h3>
          </div>
          <div class="day-meta">
            <span>🚗 {drive_km} km · {drive_time}</span>
            <span>🥾 {hike_km} km · {hike_time}</span>
          </div>
        </div>
        <div class="day-body">
          <div class="route-bar">{route_text}</div>
          <div class="day-stats">
            <div class="stat"><span class="stat-value">{drive_km}</span><span class="stat-label">Km en coche</span></div>
            <div class="stat"><span class="stat-value">{drive_time}</span><span class="stat-label">Conducción</span></div>
            <div class="stat"><span class="stat-value">{hike_km}</span><span class="stat-label">Km a pie</span></div>
            <div class="stat"><span class="stat-value">{hike_time}</span><span class="stat-label">Senderismo</span></div>
          </div>
          <p class="day-teaser">{teaser}</p>
          <div class="day-gallery">{gallery_html}</div>
          {hike_html}
          <div class="day-details">
            <div class="day-detail"><h4>Actividades</h4><ul>{activities}</ul></div>
            <div class="day-detail"><h4>Horario sugerido</h4><ul>{schedule}</ul></div>
            <div class="day-detail day-detail--spots"><h4>Qué verás</h4><ul class="spot-list">{spots_html}</ul></div>
          </div>
          <div class="map-wrap">
            <div id="{map_id}" class="leaflet-map" role="img" aria-label="Mapa día {num} {day_key_label}"></div>
            <p class="map-caption">🗺️ Mapa interactivo offline · Toca los marcadores</p>
          </div>
          <a class="btn-map" href="{gmaps_url}" target="_blank" rel="noopener">📍 Ver ruta en Google Maps</a>
        </div>
      </article>"""


def main():
    menorca = (ROOT / "docs/index.html").read_text(encoding="utf-8")
    leaflet_m = re.search(
        r"<script>\n/\* Leaflet 1\.9\.4.*?</script>\n",
        menorca,
        re.DOTALL,
    )
    leaflet_block = leaflet_m.group(0) if leaflet_m else ""
    maps_js = (BASE / "maps-init.js").read_text(encoding="utf-8")

    days = ""
    days += day_block(
        1, "Ordesa · Huesca", "Parque Nacional de Ordesa y Torla",
        "95", "1 h 45", "8–16", "3–6 h", 
        "Jaca <span class=\"arrow\">→</span> Broto <span class=\"arrow\">→</span> Torla <span class=\"arrow\">→</span> Pradera de Ordesa <span class=\"arrow\">→</span> (sendero) Cola de Caballo",
        "Primer contacto con el Pirineo atlántico: hayas en brote, cascadas con caudal de deshielo y el murmullo del Arazas. Torla es un pueblo de montaña auténtico, sin postureo alpino.",
        gallery("m1", "m2", "m4", "m3"),
        "<li>Visitar la iglesia y calles de Broto</li><li>Sendero clásico por Ordesa hasta Cola de Caballo (o Cascada de la Cola de Caballo viewpoint)</li><li>Atardecer en Torla con vistas al Mondarruego</li>",
        "<li>8:00 Salida desde Jaca</li><li>9:30 Pradera de Ordesa — inicio sendero</li><li>13:00 Comida (mochila o restaurante en Torla)</li><li>17:00 Regreso al parking</li><li>19:00 Paseo por Torla</li>",
        spot("m1", "Pradera de Ordesa", "Pradera amplia flanqueada por paredes de caliza: olor a hayas mojadas, rebuzno de burros de carga y el río Arazas rompiendo el silencio.") +
        spot("m2", "Cascada de la Cola de Caballo", "Caída de agua en forma de cola blanca sobre roca gris. En primavera el caudal es generoso; lleva impermeable para la bruma.") +
        spot("m4", "Torla", "Pueblo de piedra y pizarra pegado al parque. Panadería temprano, casas con balcones de madera y el tejado del Pirineo encima."),
        """<div class="hike-box"><strong>🥾 Ruta a pie · Ordesa – Cola de Caballo</strong><br>
        Desde Pradera de Ordesa: ~8 km ida (16 km ida/vuelta) · desnivel ~400 m · 3 h ida / 5–6 h total.
        Terreno: senda ancha al inicio, rodero en tramos finales. <a href="https://www.ordesa.net/" target="_blank" rel="noopener">Info Parque Ordesa →</a></div>""",
        "https://www.google.com/maps/dir/Jaca,+Huesca/Torla,+Huesca/Pradera+de+Ordesa,+Torla",
        "map-day1", "Ordesa",
    )

    days += day_block(
        2, "Sobrarbe", "Aínsa medieval y Sobrarbe",
        "78", "1 h 30", "4–6", "1h 30–2 h",
        "Torla <span class=\"arrow\">→</span> Fiscal <span class=\"arrow\">→</span> Aínsa <span class=\"arrow\">→</span> Embalse de Mediano <span class=\"arrow\">→</span> Escalona",
        "De la montaña alta al Sobrarbe: un pueblo amurallado de película, un embalse turquesa entre peñas y un valle donde el tiempo parece detenerse.",
        gallery("m7", "m8", "m6", "m5"),
        "<li>Pasear la plaza porticada de Aínsa (uno de los pueblos más bonitos de España)</li><li>Mirador del embalse de Mediano</li><li>Sendero corto por el barranco de San Martín o ribazas de Escalona</li>",
        "<li>9:00 Traslado Torla → Aínsa</li><li>10:30 Aínsa a pie (1 h mínimo)</li><li>13:00 Comida en plaza</li><li>15:30 Mediano y Escalona</li><li>18:00 Regreso a Aínsa</li>",
        spot("m7", "Aínsa", "Plaza mayor con forma de triángulo, arcadas de piedra y el castillo0 encima. Olor a leña por la tarde y las sierras del Sobrarbe al fondo.") +
        spot("m8", "Embalse de Mediano", "Agua turquesa atrapada entre paredes verticales. El pueblo sumergido asoma en sequía; en primavera el contraste verde-agua es brutal.") +
        spot("m6", "Escalona", "Valle estrecho con casas de piedra, huertos y silencio. Menos visitado que Aínsa; auténtico Sobrarbe."),
        """<div class="hike-box"><strong>🥾 Ruta a pie · Ribazas de Escalona</strong><br>
        ~4 km ida/vuelta · desnivel suave · 1 h 30. Senda junto al río, ideal con niños. Alternativa: subida al mirador de Mediano (2 h).</div>""",
        "https://www.google.com/maps/dir/Torla,+Huesca/A%C3%ADnsa,+Huesca/Embalse+de+Mediano,+Huesca",
        "map-day2", "Sobrarbe",
    )

    days += day_block(
        3, "Benasque", "Valle de Benasque y Estós",
        "72", "1 h 20", "6–10", "2h 30–4 h",
        "Aínsa <span class=\"arrow\">→</span> Campo <span class=\"arrow\">→</span> Benasque <span class=\"arrow\">→</span> Cerler <span class=\"arrow\">→</span> Valle de Estós",
        "El Pirineo más alpino: picos nevados de fondo, ibones glaciares al alcance de una mañana y pueblos de piedra donde aún suena el aragonés.",
        gallery("m4", "m9", "m10", "m11"),
        "<li>Benasque: café en la plaza y visita a la iglesia</li><li>Subida al valle de Estós (Cascada de la Espigantosa o ibón de Batisiere según tiempo)</li><li>Atardecer en Cerler con vistas al Aneto</li>",
        "<li>8:30 Salida Aínsa</li><li>10:00 Benasque</li><li>11:00 Inicio sendero Estós</li><li>14:30 Comida en el valle</li><li>17:00 Regreso parking</li>",
        spot("m9", "Valle de Estós", "Hayas centenarias, río Fradiñana y paredes de granito. Olor a resina de pino y aire limpio de ibón.") +
        spot("m10", "Cascada de la Espigantosa", "Caída vertical en el bosque: en mayo-junio el agua baja con fuerza del deshielo. El sendero es pedregoso pero accesible.") +
        spot("m11", "Benasque", "Capital del valle: casas de piedra gris, bares de montañeros y tiendas de senderismo. Base perfecta para rutas."),
        """<div class="hike-box"><strong>🥾 Ruta a pie · Estós – Espigantosa</strong><br>
        ~5 km ida (10 km total) · +350 m · 2 h 30–3 h ida. <a href="https://es.wikiloc.com/wikiloc/map.do?q=valle+estos" target="_blank" rel="noopener">Tracks Wikiloc →</a></div>""",
        "https://www.google.com/maps/dir/A%C3%ADnsa,+Huesca/Benasque,+Huesca/Valle+de+Est%C3%B3s,+Huesca",
        "map-day3", "Benasque",
    )

    days += day_block(
        4, "Valle de Tena", "Panticosa, ibones y Sallent",
        "65", "1 h 15", "5–8", "2–3 h",
        "Benasque <span class=\"arrow\">→</span> Biescas <span class=\"arrow\">→</span> Panticosa <span class=\"arrow\">→</span> Ibón de Piedrafita <span class=\"arrow\">→</span> Sallent de Gállego",
        "Aguas termales de montaña, ibones espejo bajo picos todavía nevados y el río Gállego bajando con furia de deshielo.",
        gallery("m12", "m5", "m3", "m2"),
        "<li>Baño termal opcional en Panticosa (reserva)</li><li>Ruta corta a ibón de Piedrafita o Bachimaña según nieve</li><li>Sallent de Gállego: pueblo pirenaico auténtico</li>",
        "<li>9:00 Traslado desde Benasque</li><li>10:30 Panticosa / ibones</li><li>14:00 Comida en Sallent</li><li>16:00 Paseo ribagorzano</li>",
        spot("m12", "Panticosa", "Balneario histórico en el valle: vapor sobre el río Caldarés, montañas alrededor y olor a azufre suave.") +
        spot("m5", "Ibón de Piedrafita", "Laguna de alta montaña reflejando picos. En primavera puede haber nieve en tramos finales — crampones ligeros si hay hielo.") +
        spot("m3", "Sallent de Gállego", "Casas de pizarra negra, fuentes y el murmullo del Gállego. Menos masificado que Formigal; auténtico."),
        """<div class="hike-box"><strong>🥾 Ruta a pie · Panticosa – Ibón Piedrafita</strong><br>
        ~4 km ida · +300 m · 1 h 30 ida. Comprobar estado del sendero en <a href="https://www.turismodearagon.com/" target="_blank" rel="noopener">Turismo Aragón</a>.</div>""",
        "https://www.google.com/maps/dir/Benasque,+Huesca/Panticosa,+Huesca/Sallent+de+G%C3%A1llego,+Huesca",
        "map-day4", "Tena",
    )

    days += day_block(
        5, "Valle de Hecho", "Selva de Oza y Ansó (Navarra)",
        "110", "2 h", "6–9", "2h 30–3 h",
        "Sallent <span class=\"arrow\">→</span> Hecho <span class=\"arrow\">→</span> Selva de Oza <span class=\"arrow\">→</span> Ansó <span class=\"arrow\">→</span> Foces de Lescún",
        "Cruzamos al Pirineo navarro: hayedos en floración tardía, cascadas escondidas y Ansó, uno de los pueblos mejor conservados del valle de Roncal.",
        gallery("m6", "m7", "m1", "m8"),
        "<li>Conducir el valle de Hecho (curvas pero espectacular)</li><li>Sendero por la Selva de Oza hasta cascadas</li><li>Ansó: arquitectura tradicional y museo del traje</li>",
        "<li>8:00 Salida Sallent (día largo en coche)</li><li>10:30 Selva de Oza</li><li>13:30 Ansó y comida</li><li>16:00 Foces de Lescún (mirador corto)</li>",
        spot("m6", "Valle de Hecho", "Praderas verdes, caseríos de piedra y el río Veral. Sensación de fin del mundo — en el mejor sentido.") +
        spot("m1", "Selva de Oza", "Hayedo atlántico con musgo, helechos y cascadas en gradas. Olor a tierra húmeda y canto de pájaros.") +
        spot("m7", "Ansó", "Calles empedradas, casas con lonas de piedra y balcones de madera. Uno de los pueblos más bonitos de Navarra."),
        """<div class="hike-box"><strong>🥾 Ruta a pie · Selva de Oza – Cascadas</strong><br>
        ~6 km ida/vuelta · +250 m · 2 h 30. Parque Natural de los Valles Occidentales. <a href="https://www.turismo.navarra.es/" target="_blank" rel="noopener">Turismo Navarra →</a></div>""",
        "https://www.google.com/maps/dir/Sallent+de+G%C3%A1llego,+Huesca/Hecho,+Navarra/Ans%C3%B3,+Navarra",
        "map-day5", "Hecho",
    )

    days += day_block(
        6, "Jaca y Río Aragón", "Historia y despedida pirenaica",
        "85", "1 h 45", "3–5", "1–2 h",
        "Ansó <span class=\"arrow\">→</span> Jaca <span class=\"arrow\">→</span> Santa Cruz de la Serós <span class=\"arrow\">→</span> San Juan de la Peña <span class=\"arrow\">→</span> (salida)",
        "Último día más relajado: románico del s. XI, monasterio entre rocas y la ciudadela de Jaca — cierre perfecto antes de bajar a Zaragoza.",
        gallery("m11", "m12", "m4", "m2"),
        "<li>Santa Cruz de la Serós: iglesia románica</li><li>Monasterio viejo de San Juan de la Peña (entre rocas)</li><li>Ciudadela de Jaca y paseo por el río Aragón</li>",
        "<li>9:00 Traslado Ansó → Jaca</li><li>10:30 San Juan de la Peña</li><li>13:00 Comida en Jaca</li><li>15:00 Ciudadela</li><li>17:00 Fin del viaje</li>",
        spot("m11", "San Juan de la Peña", "Monasterio medieval encajado bajo un peñasco enorme. Olor a piedra fría, musgo y eco de siglos.") +
        spot("m12", "Santa Cruz de la Serós", "Iglesia románica en un valle tranquilo: luz filtrada, columnas sencillas y silencio absoluto.") +
        spot("m4", "Jaca", "Ciudadela pentagonal, calles con sabor a montaña y tapas en el casco. Despedida animada tras días de silencio."),
        """<div class="hike-box"><strong>🥾 Ruta a pie · Bosque de la Pardina (opcional)</strong><br>
        ~3 km · llano · 1 h. Bosque de hayas junto al río Aragón, ideal si sobra energía antes de marchar.</div>""",
        "https://www.google.com/maps/dir/Ans%C3%B3,+Navarra/San+Juan+de+la+Pe%C3%B1a,+Huesca/Jaca,+Huesca",
        "map-day6", "Jaca",
    )

    days += """
      <div class="section-intro" style="margin:3rem 0 2rem;padding:1.25rem 1.5rem;background:var(--pine-pale);border-radius:var(--radius-sm);border-left:4px solid var(--pine)">
        <strong>🇫🇷 Extensión · 5 días en el Pirineo francés</strong><br>
        A partir del día 7 cruzamos a Francia por Somport. Lescun, Ossau, Cauterets, Gavarnie (UNESCO) y el Tourmalet — regreso a España por Portalet y Bielsa.
      </div>
"""

    days += day_block(
        7, "Franco-español · Aspe", "Canfranc, Somport y Lescun",
        "92", "1 h 50", "5–8", "2–3 h",
        "Jaca <span class=\"arrow\">→</span> Canfranc (estación) <span class=\"arrow\">→</span> Somport <span class=\"arrow\">→</span> Lescun",
        "Cruzamos la frontera por el histórico paso de Somport: la estación Belle Époque de Canfranc, praderas del valle d'Aspe y Lescun, uno de los pueblos más bonitos del Pirineo francés — sin multitudes de agosto.",
        gallery("m13", "m14", "m6", "m7"),
        "<li>Visitar la estación internacional de Canfranc (exterior y museo)</li><li>Cruzar Somport hacia Francia — lleva DNI/pasaporte</li><li>Paseo por Lescun y mirador del valle d'Aspe</li><li>Sendero al Chemin de la Mâture o Cascada d'Arrious (según tiempo)</li>",
        "<li>8:30 Salida Jaca</li><li>9:30 Canfranc — fotos estación</li><li>10:30 Cruce frontera Somport</li><li>12:00 Lescun y comida</li><li>15:00 Sendero valle d'Aspe</li><li>18:00 Paseo nocturno por el pueblo</li>",
        spot("m13", "Estación de Canfranc", "Palacio ferroviario de 1928 entre montañas: cristaleras, bóvedas de piedra y silencio fronterizo. Uno de los edificios más fotogénicos de los Pirineos.") +
        spot("m14", "Paso de Somport", "Frontera natural a 1.640 m: praderas, venta de quesos de oveja y el primer cartel en francés. Sensación de cruce de mundo en 5 minutos.") +
        spot("m6", "Lescun", "Pueblo de casas de piedra y madera en el valle d'Aspe. Panadería con olor a mantequilla, iglesia del s. XII y vistas al Pic d'Anie."),
        """<div class="hike-box"><strong>🥾 Ruta a pie · Lescun – Cascada d'Arrious</strong><br>
        ~5 km ida/vuelta · +200 m · 2 h. Bosque y cascada en el valle d'Aspe. Alternativa corta: paseo por el Chemin de la Mâture (mirador). <a href="https://www.pyrenees-ariegeoises.com/" target="_blank" rel="noopener">Turismo Ariège →</a></div>""",
        "https://www.google.com/maps/dir/Jaca,+Huesca/Canfranc,+Huesca/Lescun,+France",
        "map-day7", "Canfranc",
    )

    days += day_block(
        8, "Valle de Ossau · Francia", "Laruns, Aubisque y Lac de Bious",
        "88", "2 h", "4–6", "1h 30–2 h",
        "Lescun <span class=\"arrow\">→</span> Accous <span class=\"arrow\">→</span> Laruns <span class=\"arrow\">→</span> Col du Soulor <span class=\"arrow\">→</span> Gabas",
        "Día de carreteras de montaña legendarias — Col du Soulor y Aubisque — y el valle de Ossau: prados verdes, ovejas y el espejo turquesa del Lac de Bious-Artigues bajo el Pic du Midi.",
        gallery("m15", "m16", "m5", "m3"),
        "<li>Carretera panorámica por Accous y valle d'Aspe</li><li>Laruns: mercado y arquitectura ossalat</li><li>Subida al Col du Soulor (miradores)</li><li>Sendero al Lac de Bious-Artigues desde Gabas</li>",
        "<li>8:00 Salida Lescun</li><li>10:00 Laruns — café y paseo</li><li>11:30 Col du Soulor (paradas foto)</li><li>13:00 Comida en Gabas</li><li>15:00 Lac de Bious-Artigues</li>",
        spot("m15", "Laruns", "Capital del valle de Ossau: casas blancas con contraventanas rojas, queserías artesanales y el murmullo del Gave d'Ossau. Auténtico Pirineo francés.") +
        spot("m16", "Col du Soulor", "Puerto a 1.474 m con curvas de postal y vistas al valle. Uno de los pasos más bonitos del Tour de France — conduce hacia el Aubisque.") +
        spot("m5", "Lac de Bious-Artigues", "Ibón de montaña a 1.725 m reflejando el Pic du Midi de Ossau. Praderas con flores en junio y silencio absoluto salvo el viento."),
        """<div class="hike-box"><strong>🥾 Ruta a pie · Gabas – Lac de Bious-Artigues</strong><br>
        ~3 km ida (6 km total) · +150 m · 1 h ida. Senda ancha y señalizada desde el parking de Gabas. <a href="https://www.pyrenees-national.fr/" target="_blank" rel="noopener">Parc National des Pyrénées →</a></div>""",
        "https://www.google.com/maps/dir/Lescun,+France/Laruns,+France/Gabas,+France",
        "map-day8", "Ossau",
    )

    days += day_block(
        9, "Cauterets · Francia", "Pont d'Espagne y Lac de Gaube",
        "68", "1 h 25", "4–6", "2–2h 30",
        "Laruns <span class=\"arrow\">→</span> Argelès-Gazost <span class=\"arrow\">→</span> Cauterets <span class=\"arrow\">→</span> Pont d'Espagne <span class=\"arrow\">→</span> Lac de Gaube",
        "El corazón del Parque Nacional francés: pueblo termal de Cauterets, el Puente de España sobre cascadas y el Lac de Gaube — lago glaciar a los pies del Vignemale, el pico más alto del Pirineo francés.",
        gallery("m17", "m9", "m10", "m2"),
        "<li>Cauterets: calles victorianas y termas (baño opcional)</li><li>Teleférico o sendero al Pont d'Espagne</li><li>Ruta al Lac de Gaube por el GR-10</li><li>Atardecer con vistas al Vignemale (3.298 m)</li>",
        "<li>8:30 Salida Laruns</li><li>10:00 Cauterets — paseo pueblo</li><li>11:00 Pont d'Espagne</li><li>12:30 Lac de Gaube — picnic</li><li>16:00 Regreso a Cauterets</li>",
        spot("m17", "Cauterets", "Pueblo balneario del s. XIX entre bosques: fachadas de madera pintada, olor a azufre suave y ambiente de montaña elegante sin ser pretencioso.") +
        spot("m9", "Pont d'Espagne", "Puente de piedra sobre cascadas múltiples: bruma, musgo y rugido del agua de deshielo. Puerta de entrada al corazón del parque nacional.") +
        spot("m10", "Lac de Gaube", "Lago glaciar turquesa a 1.725 m con el Vignemale de fondo. Uno de los paisajes más espectaculares de todo el Pirineo — imprescindible."),
        """<div class="hike-box"><strong>🥾 Ruta a pie · Pont d'Espagne – Lac de Gaube</strong><br>
        ~2,5 km ida (5 km total) · +150 m · 45 min ida / 2 h total. Senda GR-10 bien marcada. Teleférico disponible hasta mitad de ruta. <a href="https://www.cauterets.com/" target="_blank" rel="noopener">cauterets.com →</a></div>""",
        "https://www.google.com/maps/dir/Laruns,+France/Cauterets,+France/Pont+d%27Espagne,+Cauterets",
        "map-day9", "Gaube",
    )

    days += day_block(
        10, "Gavarnie · UNESCO", "Cirque de Gavarnie y Grande Cascade",
        "42", "1 h", "6–8", "2h 30–3 h",
        "Cauterets <span class=\"arrow\">→</span> Luz-Saint-Sauveur <span class=\"arrow\">→</span> Gavarnie <span class=\"arrow\">→</span> Cirque de Gavarnie",
        "Víctor Hugo lo llamó «el coloso de la naturaleza»: un anfiteatro de paredes de 1.500 m, la cascada más alta de Francia (423 m) y un pueblo de montaña donde el tiempo se mide en mulas y queso de oveja.",
        gallery("m1", "m4", "m11", "m8"),
        "<li>Luz-Saint-Sauveur: fortalezas Vauban y puentes históricos</li><li>Gavarnie: iglesia románica y artesanía local</li><li>Sendero al Cirque de Gavarnie (UNESCO)</li><li>Grande Cascade de Gavarnie — lleva chubasquero</li>",
        "<li>9:00 Salida Cauterets</li><li>10:00 Luz — parada café</li><li>10:45 Gavarnie</li><li>11:30 Inicio sendero cirque</li><li>14:00 Grande Cascade — comida mochila</li><li>17:00 Regreso pueblo</li>",
        spot("m1", "Cirque de Gavarnie", "Anfiteatro glaciar de 1.500 m de pared vertical. Eco de cascadas, silencio de roca y la sensación de estar dentro de una catedral natural.") +
        spot("m4", "Grande Cascade", "423 m de caída libre — la cascada más alta de Francia metropolitana. En primavera el caudal es máximo; la bruma moja a 100 m de distancia.") +
        spot("m11", "Gavarnie", "Pueblo a 1.400 m con casas de piedra gris, queserías y burros que suben al cirque. Auténtico, aunque con turismo — evita agosto si puedes."),
        """<div class="hike-box"><strong>🥾 Ruta a pie · Gavarnie – Cirque – Grande Cascade</strong><br>
        ~6 km ida/vuelta · +200 m · 2 h 30–3 h. Senda ancha sin dificultad técnica. Patrimonio UNESCO. <a href="https://www.gavarnie.com/" target="_blank" rel="noopener">gavarnie.com →</a></div>""",
        "https://www.google.com/maps/dir/Cauterets,+France/Luz-Saint-Sauveur,+France/Gavarnie,+France",
        "map-day10", "Gavarnie",
    )

    days += day_block(
        11, "Tourmalet · Regreso", "Col du Tourmalet, Payolle y Bielsa",
        "118", "2 h 30", "3–5", "1–1h 30",
        "Gavarnie <span class=\"arrow\">→</span> Col du Tourmalet <span class=\"arrow\">→</span> Lac de Payolle <span class=\"arrow\">→</span> Arreau <span class=\"arrow\">→</span> Portalet <span class=\"arrow\">→</span> Bielsa",
        "Último día épico: subimos el mítico Tourmalet (2.115 m), lagos de Payolle entre abetos y regresamos a España por el puerto de Portalet — cierre perfecto cruzando de nuevo la frontera.",
        gallery("m12", "m5", "m6", "m3"),
        "<li>Col du Tourmalet — cumbre del mito ciclista</li><li>Lac de Payolle: paseo ribereño entre pinos</li><li>Arreau: pueblo del valle d'Aure</li><li>Regreso a España por Portalet → valle de Bielsa</li>",
        "<li>8:00 Salida Gavarnie</li><li>9:30 Col du Tourmalet (foto cumbre)</li><li>10:30 Lac de Payolle</li><li>12:00 Arreau — comida</li><li>14:30 Portalet → Bielsa</li><li>16:30 Fin del viaje</li>",
        spot("m12", "Col du Tourmalet", "Puerto a 2.115 m, el más alto del Tour de France asfaltado. Vistas 360° sobre valles y picos — puede haber nieve en junio, lleva chaqueta.") +
        spot("m5", "Lac de Payolle", "Lago de montaña rodeado de hayas y abetos a 1.130 m. Praderas verdes, silencio y el reflejo del Pic du Midi de Bigorre en días claros.") +
        spot("m6", "Bielsa · Parque de Bielsa", "Regreso al Pirineo aragonés: casco medieval, túnel de Bielsa-Fabrega hacia Francia y la puerta al Parque de Ordesa por el otro lado. Despedida pirenaica.") ,
        """<div class="hike-box"><strong>🥾 Ruta a pie · Lac de Payolle (paseo)</strong><br>
        ~3 km ida/vuelta · llano · 1 h. Rodeo del lago entre bosque. Ideal para estirar piernas tras el Tourmalet. Comprobar estado del Portalet en <a href="https://www.turismodearagon.com/" target="_blank" rel="noopener">Turismo Aragón</a>.</div>""",
        "https://www.google.com/maps/dir/Gavarnie,+France/Col+du+Tourmalet/Lac+de+Payolle,+France/Bielsa,+Huesca",
        "map-day11", "Tourmalet",
    )

    hero_url = u("hero", 1920)
    img = {k: u(k) for k in IMG if k != "hero"}

    html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="theme-color" content="#2d5a3d">
  <title>Pirineo · Guía 11 Días · España & Francia</title>
  <style>
    :root {
      --pine: #2d5a3d; --pine-light: #4a7c59; --pine-pale: #e8f0ea;
      --stone: #5c5346; --sky: #4a7c9b; --amber: #c4874a;
      --sand: #f0ebe3; --sand-dark: #ddd4c8; --text: #2c3338; --text-muted: #6b7280; --white: #fff;
      --shadow: 0 4px 24px rgba(45,90,61,.1); --radius: 16px; --radius-sm: 10px; --header-h: 3.25rem;
    }
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    html{scroll-behavior:smooth}
    body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--sand);color:var(--text);line-height:1.65}
    section{scroll-margin-top:calc(var(--header-h)+.5rem);padding:5rem 0}
    section:nth-child(even){background:var(--white)}
    .container{max-width:1100px;margin:0 auto;padding:0 1.5rem}
    .site-header{position:fixed;top:0;left:0;right:0;z-index:200;height:var(--header-h);display:flex;align-items:center;justify-content:space-between;padding:0 1.25rem;background:rgba(255,255,255,.92);backdrop-filter:blur(14px);border-bottom:1px solid var(--sand-dark)}
    .site-logo{font-family:Georgia,serif;font-size:1.05rem;font-weight:600;color:var(--pine);text-decoration:none}
    .nav-toggle{display:none;width:2.5rem;height:2.5rem;border:1px solid var(--sand-dark);border-radius:var(--radius-sm);background:var(--white);color:var(--pine);font-size:1.25rem;cursor:pointer}
    .site-nav ul{list-style:none;display:flex;flex-wrap:wrap;gap:.15rem .85rem}
    .site-nav a{text-decoration:none;color:var(--text-muted);font-size:.78rem;font-weight:500}
    .site-nav a:hover{color:var(--pine)}
    .hero{position:relative;min-height:88vh;display:flex;align-items:flex-end;overflow:hidden}
    .hero-bg{position:absolute;inset:0;background:url('""" + hero_url + """') center/cover no-repeat}
    .hero-bg::after{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(20,35,28,.88),rgba(45,90,61,.3))}
    .hero-content{position:relative;z-index:2;padding:4rem 2rem 5rem;max-width:900px;margin:0 auto;width:100%}
    .hero-tag{display:inline-block;font-size:.75rem;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--sand);background:rgba(255,255,255,.15);padding:.45rem 1rem;border-radius:100px;margin-bottom:1.25rem}
    .hero h1{font-family:Georgia,serif;font-size:clamp(2.6rem,7vw,4.6rem);color:var(--white);line-height:1.05;margin-bottom:1rem}
    .hero h1 em{font-style:italic;font-weight:400;color:var(--sand)}
    .hero-sub{font-size:1.12rem;color:rgba(255,255,255,.9);max-width:560px;margin-bottom:1.5rem}
    .hero-meta{display:flex;flex-wrap:wrap;gap:1.25rem;color:rgba(255,255,255,.78);font-size:.9rem}
    .section-label{font-size:.72rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--pine);margin-bottom:.75rem}
    .section-title{font-family:Georgia,serif;font-size:clamp(2rem,4vw,2.75rem);margin-bottom:.75rem;line-height:1.15}
    .section-intro{color:var(--text-muted);max-width:680px;margin-bottom:2rem;font-size:1.05rem}
    .intro-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.5rem}
    .intro-card{background:var(--white);border-radius:var(--radius-sm);padding:1.75rem;box-shadow:var(--shadow)}
    .intro-card h3{font-family:Georgia,serif;margin-bottom:.5rem}
    .intro-card p{color:var(--text-muted);font-size:.92rem}
    .day-card{background:var(--white);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);margin-bottom:2.5rem;border:1px solid var(--sand-dark)}
    .day-header{display:flex;flex-wrap:wrap;justify-content:space-between;gap:1rem;padding:1.5rem 1.75rem;background:linear-gradient(135deg,var(--pine-pale),var(--white));border-bottom:1px solid var(--sand-dark)}
    .day-num{font-size:.72rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--pine)}
    .day-title{font-family:Georgia,serif;font-size:1.45rem;margin-top:.25rem}
    .day-meta{display:flex;flex-wrap:wrap;gap:.75rem;font-size:.82rem;color:var(--text-muted)}
    .day-body{padding:1.75rem}
    .route-bar{background:var(--pine-pale);border-radius:var(--radius-sm);padding:.85rem 1rem;font-size:.88rem;margin-bottom:1.25rem;line-height:1.5}
    .route-bar .arrow{color:var(--amber);margin:0 .25rem}
    .day-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:1rem;margin-bottom:1.25rem}
    .stat{text-align:center;padding:.85rem;background:var(--sand);border-radius:var(--radius-sm)}
    .stat-value{display:block;font-size:1.25rem;font-weight:700;color:var(--pine)}
    .stat-label{font-size:.72rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:.06em}
    .day-teaser{color:var(--text-muted);margin-bottom:1rem;font-size:.95rem}
    .day-gallery{display:flex;gap:.65rem;overflow-x:auto;margin-bottom:1.25rem;padding-bottom:.25rem}
    .day-gallery img{flex:0 0 200px;height:130px;object-fit:cover;border-radius:var(--radius-sm)}
    .day-details{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.25rem;margin-bottom:1.25rem}
    .day-detail h4{font-size:.85rem;text-transform:uppercase;letter-spacing:.08em;color:var(--stone);margin-bottom:.5rem}
    .day-detail ul{list-style:none;font-size:.9rem;color:var(--text-muted)}
    .day-detail li{padding:.25rem 0;padding-left:1rem;position:relative}
    .day-detail li::before{content:'→';position:absolute;left:0;color:var(--pine-light)}
    .spot-list{list-style:none}
    .spot-item{display:flex;gap:1rem;padding:.85rem 0;border-bottom:1px solid var(--sand)}
    .spot-item:last-child{border-bottom:none}
    .spot-img{width:88px;height:72px;flex-shrink:0;border-radius:8px;background-size:cover;background-position:center}
    .spot-body strong{display:block;font-size:.92rem;margin-bottom:.2rem}
    .spot-desc{font-size:.85rem;color:var(--text-muted);line-height:1.45}
    .hike-box{background:var(--pine-pale);border-left:4px solid var(--pine);border-radius:0 var(--radius-sm) var(--radius-sm) 0;padding:1rem 1.25rem;margin:1rem 0;font-size:.9rem}
    .hike-box a{color:var(--sky);font-weight:600}
    .btn-map{display:inline-flex;align-items:center;gap:.4rem;margin-top:1rem;padding:.65rem 1.15rem;background:var(--pine);color:var(--white);text-decoration:none;border-radius:100px;font-size:.85rem;font-weight:600}
    .card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
    .card{background:var(--white);border-radius:var(--radius-sm);overflow:hidden;box-shadow:var(--shadow)}
    .card-img{height:180px;background-size:cover;background-position:center}
    .card-body{padding:1.5rem}
    .card-zone{font-size:.72rem;text-transform:uppercase;letter-spacing:.1em;color:var(--sky);margin-bottom:.35rem}
    .card-body h3{font-family:Georgia,serif;margin-bottom:.35rem}
    .card-style{display:inline-block;font-size:.75rem;background:var(--pine-pale);color:var(--pine);padding:.2rem .6rem;border-radius:100px;margin-bottom:.65rem}
    .card-body p{font-size:.9rem;color:var(--text-muted);margin-bottom:.5rem}
    .links-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem}
    .link-card{background:var(--white);border-radius:var(--radius-sm);padding:1.25rem;box-shadow:var(--shadow);border-left:4px solid var(--sky)}
    .link-card h3{font-size:.95rem;margin-bottom:.35rem}
    .link-card p{font-size:.85rem;color:var(--text-muted);margin-bottom:.5rem}
    .link-card a{color:var(--sky);font-size:.85rem;font-weight:600;word-break:break-word}
    .route-legend{display:flex;flex-wrap:wrap;gap:.65rem 1.25rem;font-size:.82rem;color:var(--text-muted);margin-top:1rem}
    .legend-dot{width:12px;height:12px;border-radius:50%;display:inline-block;margin-right:.35rem}
    .map-wrap{border-radius:var(--radius-sm);overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--sand-dark);margin-top:1rem}
    .leaflet-map{height:300px;width:100%}
    .leaflet-map--fullroute{height:480px}
    .map-caption{font-size:.78rem;color:var(--text-muted);padding:.65rem 1rem;background:var(--white);border-top:1px solid var(--sand-dark)}
    .map-pin-wrap{background:transparent;border:none}
    .map-pin{display:flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;color:#fff;font-size:11px;font-weight:700;border:2px solid #fff;box-shadow:0 2px 8px rgba(0,0,0,.25)}
    .leaflet-pane,.leaflet-tile,.leaflet-marker-icon,.leaflet-marker-shadow,.leaflet-tile-container,.leaflet-pane>svg,.leaflet-pane>canvas,.leaflet-zoom-box,.leaflet-image-layer,.leaflet-layer{position:absolute;left:0;top:0}
    .leaflet-container{overflow:hidden;-webkit-tap-highlight-color:transparent;touch-action:pan-x pan-y;background:linear-gradient(180deg,#c5dde8,#8eb5c9);font-size:12px}
    .leaflet-bar{box-shadow:0 1px 5px rgba(0,0,0,.2);border-radius:8px;overflow:hidden}
    .leaflet-bar a{background:#fff;border-bottom:1px solid #ddd;width:30px;height:30px;line-height:30px;display:block;text-align:center;text-decoration:none;color:#333;font:bold 18px monospace}
    .leaflet-popup-content-wrapper{border-radius:12px;box-shadow:0 3px 14px rgba(0,0,0,.25)}
    .leaflet-popup-content{margin:12px 16px;font-size:13px}
    footer{text-align:center;padding:3rem 1.5rem;background:var(--pine);color:rgba(255,255,255,.85)}
    footer em{display:block;font-family:Georgia,serif;font-size:1.2rem;margin-bottom:.5rem;color:var(--white)}
    footer p{font-size:.85rem;opacity:.75}
    @media(max-width:820px){
      section{padding:3.5rem 0}
      .nav-toggle{display:flex;align-items:center;justify-content:center}
      .site-nav{position:absolute;top:100%;left:0;right:0;background:rgba(255,255,255,.98);border-bottom:1px solid var(--sand-dark);max-height:0;overflow:hidden;opacity:0;transition:max-height .3s,opacity .25s}
      .site-nav.is-open{max-height:480px;opacity:1}
      .site-nav ul{flex-direction:column;padding:.75rem 1.25rem 1rem}
      .site-nav a{display:block;padding:.6rem 0;font-size:.9rem}
      .leaflet-map--fullroute{height:320px}
    }
  </style>
</head>
<body>

  <header class="site-header" id="site-header">
    <a class="site-logo" href="#intro">Pirineo</a>
    <button type="button" class="nav-toggle" id="nav-toggle" aria-label="Menú" aria-expanded="false">☰</button>
    <nav class="site-nav" id="site-nav">
      <ul>
        <li><a href="#intro">Introducción</a></li>
        <li><a href="#ruta-completa">Mapa ruta</a></li>
        <li><a href="#itinerario">Itinerario</a></li>
        <li><a href="#alojamiento">Alojamiento</a></li>
        <li><a href="#enlaces">Enlaces</a></li>
        <li><a href="#consejos">Consejos</a></li>
      </ul>
    </nav>
  </header>

  <header class="hero">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <span class="hero-tag">🏔️ Guía primavera · España & Francia</span>
      <h1>Pirineo<br><em>Once días entre dos países</em></h1>
      <p class="hero-sub">Road trip por el Pirineo central español y el Parque Nacional francés: Ordesa, Sobrarbe, Benasque, Canfranc, Gavarnie, Cauterets y el Tourmalet. Paisajes espectaculares, pueblos auténticos y rutas a pie de medio día.</p>
      <div class="hero-meta">
        <span>🌸 Mayo–junio ideal</span>
        <span>🚗 ~920 km totales</span>
        <span>🥾 10 rutas a pie incluidas</span>
      </div>
    </div>
  </header>

  <section id="intro">
    <div class="container">
      <p class="section-label">Bienvenida</p>
      <h2 class="section-title">Por qué el Pirineo en primavera</h2>
      <p class="section-intro">Mayo y junio son el momento dorado: hayas y bosques en verde intenso, cascadas al máximo caudal del deshielo, menos turistas que en agosto y temperaturas agradables para caminar (15–22 °C en valle). Esta guía recorre 6 días por Aragón y Navarra, más 5 días extra cruzando a Francia por Somport y regresando por Portalet.</p>
      <div class="intro-grid">
        <div class="intro-card"><h3>🌸 Primavera activa</h3><p>Flores en praderas, nieve en picos altos pero senderos accesibles hasta 2.000 m. Lleva capas: mañana fría, mediodía templado.</p></div>
        <div class="intro-card"><h3>🗺️ Diez rutas a pie</h3><p>Ordesa, Estós, Gaube, Gavarnie, Bious-Artigues… Desde paseos familiares a medias jornadas con vistas de postal.</p></div>
        <div class="intro-card"><h3>🏘️ Pueblos auténticos</h3><p>Aínsa, Ansó, Lescun, Laruns, Cauterets, Gavarnie… Arquitectura de piedra, queserías artesanales y ritmo lento sin filas de agosto.</p></div>
        <div class="intro-card"><h3>🇫🇷 Cruce frontera</h3><p>Somport y Portalet conectan España y Francia. Lleva DNI/pasaporte, euros en efectivo y comprueba estado de puertos en primavera.</p></div>
      </div>
    </div>
  </section>

  <section id="ruta-completa">
    <div class="container">
      <p class="section-label">Visión global</p>
      <h2 class="section-title">Mapa de la ruta completa</h2>
      <p class="section-intro">Los 11 días en un solo mapa. D1–D6 en España; D7–D11 en Francia y regreso. Cada color es un día de conducción. Funciona sin conexión.</p>
      <div class="map-wrap">
        <div id="map-full-route" class="leaflet-map leaflet-map--fullroute" role="img" aria-label="Mapa ruta completa Pirineo 11 días"></div>
        <p class="map-caption">🗺️ ~920 km en coche · 10 rutas senderistas · Pellizca para zoom</p>
      </div>
      <div class="route-legend">
        <span><span class="legend-dot" style="background:#3d6b4f"></span>D1 Ordesa</span>
        <span><span class="legend-dot" style="background:#4a7c9b"></span>D2 Sobrarbe</span>
        <span><span class="legend-dot" style="background:#6b5a8a"></span>D3 Benasque</span>
        <span><span class="legend-dot" style="background:#c4874a"></span>D4 Tena</span>
        <span><span class="legend-dot" style="background:#2d5a3d"></span>D5 Hecho</span>
        <span><span class="legend-dot" style="background:#5c5346"></span>D6 Jaca</span>
        <span><span class="legend-dot" style="background:#7d6b5a"></span>D7 Canfranc</span>
        <span><span class="legend-dot" style="background:#2e6b8a"></span>D8 Ossau</span>
        <span><span class="legend-dot" style="background:#456b8c"></span>D9 Gaube</span>
        <span><span class="legend-dot" style="background:#8a6b2e"></span>D10 Gavarnie</span>
        <span><span class="legend-dot" style="background:#6b3a5c"></span>D11 Tourmalet</span>
      </div>
    </div>
  </section>

  <section id="itinerario">
    <div class="container">
      <p class="section-label">Día a día</p>
      <h2 class="section-title">Itinerario 11 días</h2>
      <p class="section-intro">Días 1–6 por el Pirineo aragonés y navarro. Días 7–11 cruzan a Francia (Hautes-Pyrénées) y regresan por Portalet. Cada jornada combina conducción corta, pueblos auténticos y una ruta a pie destacada.</p>
      __DAYS__
    </div>
  </section>

  <section id="alojamiento">
    <div class="container">
      <p class="section-label">Dónde dormir</p>
      <h2 class="section-title">Alojamientos sugeridos</h2>
      <p class="section-intro">Bases rurales y hoteles de montaña para no rehacer maletas cada noche. Reserva con antelación en puente de mayo y junio.</p>
      <div class="card-grid">
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M4__')"></div>
          <div class="card-body">
            <p class="card-zone">D1–D2 · Torla</p>
            <h3>Hotel Abetos · Torla</h3>
            <span class="card-style">Hotel montaña · Puerta Ordesa</span>
            <p>A dos minutos del parque. Habitaciones con vistas, parking y desayuno temprano para rutas. Ideal noches 1 y 2 del circuito.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Abetos+Torla" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M7__')"></div>
          <div class="card-body">
            <p class="card-zone">D2 · Aínsa</p>
            <h3>Hotel Mesón de L'Ainsa</h3>
            <span class="card-style">Hotel con encanto · Casco medieval</span>
            <p>Dentro del conjunto histórico. Cenas en la plaza porticada y cero conducción nocturna. Alternativa si prefieres Sobrarbe puro.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Meson+de+L+Ainsa" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M11__')"></div>
          <div class="card-body">
            <p class="card-zone">D3 · Benasque</p>
            <h3>Casa Chanatxin</h3>
            <span class="card-style">Apartamento rural · Benasque</span>
            <p>Apartamentos acogedores en el valle. Cocina propia tras rutas largas. Base perfecta para Estós y Cerler.</p>
            <p><a href="https://www.google.com/maps/search/Casa+Chanatxin+Benasque" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M12__')"></div>
          <div class="card-body">
            <p class="card-zone">D4 · Panticosa</p>
            <h3>Balneario de Panticosa</h3>
            <span class="card-style">Hotel-spa · Valle de Tena</span>
            <p>Experiencia termal de montaña entre picos. Reserva baños con antelación. Lujo merecido tras senderismo.</p>
            <p><a href="https://www.google.com/maps/search/Balneario+Panticosa" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M6__')"></div>
          <div class="card-body">
            <p class="card-zone">D5 · Hecho / Ansó</p>
            <h3>Casa Sarasa · Valle de Hecho</h3>
            <span class="card-style">Casa rural · Navarra</span>
            <p>Hospitalidad navarra en entorno espectacular. Cerca de Selva de Oza y Ansó. Tranquilidad total.</p>
            <p><a href="https://www.google.com/maps/search/Casa+Sarasa+Hecho+Navarra" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M2__')"></div>
          <div class="card-body">
            <p class="card-zone">D6 · Jaca</p>
            <h3>Hotel Conde Aznar</h3>
            <span class="card-style">Hotel céntrico · Jaca</span>
            <p>En el corazón de Jaca, cerca de la ciudadela. Perfecto para la noche antes de cruzar a Francia por Somport.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Conde+Aznar+Jaca" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M13__')"></div>
          <div class="card-body">
            <p class="card-zone">D7 · Lescun</p>
            <h3>La Breche de Roland · Lescun</h3>
            <span class="card-style">Hotel montaña · Valle d'Aspe</span>
            <p>En el corazón del pueblo más bonito del valle d'Aspe. Vistas al Pic d'Anie, cenas caseras y ambiente pirenaico auténtico.</p>
            <p><a href="https://www.google.com/maps/search/La+Breche+de+Roland+Lescun" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M15__')"></div>
          <div class="card-body">
            <p class="card-zone">D8 · Laruns / Gabas</p>
            <h3>Hotel Gabizos · Laruns</h3>
            <span class="card-style">Hotel · Valle de Ossau</span>
            <p>Base ideal para el Col du Soulor y el Lac de Bious. Arquitectura tradicional ossalat con confort moderno.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Gabizos+Laruns" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M17__')"></div>
          <div class="card-body">
            <p class="card-zone">D9 · Cauterets</p>
            <h3>Le Lion d'Or · Cauterets</h3>
            <span class="card-style">Hotel con encanto · Termas</span>
            <p>En el centro del pueblo balneario. A dos pasos del teleférico a Gaube y de las termas. Ambiente victoriano de montaña.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Lion+d+Or+Cauterets" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M1__')"></div>
          <div class="card-body">
            <p class="card-zone">D10 · Gavarnie / Luz</p>
            <h3>Hotel Brèche de Roland · Luz</h3>
            <span class="card-style">Hotel · Valle de Gavarnie</span>
            <p>En Luz-Saint-Sauveur, a 15 min de Gavarnie. Fortalezas Vauban, puentes históricos y acceso temprano al cirque.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Breche+de+Roland+Luz+Saint+Sauveur" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__IMG_M12__')"></div>
          <div class="card-body">
            <p class="card-zone">D11 · Arreau / Bielsa</p>
            <h3>Le Néouvielle · Arreau</h3>
            <span class="card-style">Hotel · Valle d'Aure</span>
            <p>Última noche en Francia o parada antes de cruzar Portalet. Pueblo tranquilo del valle d'Aure, cerca del Tourmalet.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Neouvielle+Arreau" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section id="enlaces">
    <div class="container">
      <p class="section-label">Recursos</p>
      <h2 class="section-title">Enlaces prácticos</h2>
      <div class="links-grid">
        <div class="link-card"><h3>Parque de Ordesa</h3><p>Horarios, restricciones de acceso y bus lanzadera.</p><a href="https://www.ordesa.net/" target="_blank" rel="noopener">ordesa.net →</a></div>
        <div class="link-card"><h3>Turismo de Aragón</h3><p>Rutas, alojamientos y eventos en el Pirineo aragonés.</p><a href="https://www.turismodearagon.com/" target="_blank" rel="noopener">turismodearagon.com →</a></div>
        <div class="link-card"><h3>Turismo Navarra</h3><p>Valle de Hecho, Ansó y Roncal.</p><a href="https://www.turismo.navarra.es/" target="_blank" rel="noopener">turismo.navarra.es →</a></div>
        <div class="link-card"><h3>AEMET · Meteo</h3><p>Predicción por municipios — imprescindible en montaña.</p><a href="https://www.aemet.es/" target="_blank" rel="noopener">aemet.es →</a></div>
        <div class="link-card"><h3>Wikiloc</h3><p>Tracks GPS de senderos verificados por la comunidad.</p><a href="https://es.wikiloc.com/" target="_blank" rel="noopener">wikiloc.com →</a></div>
        <div class="link-card"><h3>Parc National des Pyrénées</h3><p>Senderos, refugios y estado de rutas en el Pirineo francés.</p><a href="https://www.pyrenees-national.fr/" target="_blank" rel="noopener">pyrenees-national.fr →</a></div>
        <div class="link-card"><h3>Cauterets & Gaube</h3><p>Teleférico, Pont d'Espagne y actividades en la zona.</p><a href="https://www.cauterets.com/" target="_blank" rel="noopener">cauterets.com →</a></div>
        <div class="link-card"><h3>Gavarnie · UNESCO</h3><p>Info del cirque, horarios y condiciones del sendero.</p><a href="https://www.gavarnie.com/" target="_blank" rel="noopener">gavarnie.com →</a></div>
        <div class="link-card"><h3>Météo-France</h3><p>Meteorología en Francia — complementa AEMET en la frontera.</p><a href="https://meteofrance.com/" target="_blank" rel="noopener">meteofrance.com →</a></div>
      </div>
    </div>
  </section>

  <section id="consejos">
    <div class="container">
      <p class="section-label">Práctico</p>
      <h2 class="section-title">Consejos esenciales</h2>
      <div class="intro-grid">
        <div class="intro-card"><h3>🚗 Coche</h3><p>Imprescindible. Mejor recogida en Zaragoza (2 h a Jaca) o Pau/Tarbes si empiezas por Francia. Cadenas en maletero hasta junio en puertos altos (Tourmalet, Aubisque). Reposta antes de subir a valles.</p></div>
        <div class="intro-card"><h3>🇫🇷 Frontera</h3><p>DNI o pasaporte en vigor. Somport (D7) y Portalet (D11) suelen abiertos todo el año, pero comprueba nieve en primavera. Algunos peajes/túneles aceptan tarjeta; lleva euros.</p></div>
        <div class="intro-card"><h3>🥾 Equipo senderismo</h3><p>Botas impermeables, bastones, cortavientos y chubasquero. Capas térmicas: en Ordesa o Gavarnie hace frío a las 8:00 aunque en junio haya calor al mediodía.</p></div>
        <div class="intro-card"><h3>🧀 Gastronomía franco-española</h3><p>España: ternasco, chiretas, queso de Tronchón. Francia: garbure (sopa montaña), tomme de brebis (queso oveja), gateau à la broche. Prueba en Lescun, Laruns y Gavarnie.</p></div>
      </div>
    </div>
  </section>

  <footer>
    <em>El Pirineo te espera en verde 🏔️🌸</em>
    <p>Guía primavera · España & Francia · Mapas Leaflet offline</p>
  </footer>

__LEAFLET__
<script>
MAPS_SCRIPT_PLACEHOLDER
</script>
<script>
(function(){
  var h=document.getElementById('site-header'),t=document.getElementById('nav-toggle'),n=document.getElementById('site-nav');
  if(t&&n){t.addEventListener('click',function(){var o=n.classList.toggle('is-open');t.setAttribute('aria-expanded',o?'true':'false');t.textContent=o?'✕':'☰';});n.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){n.classList.remove('is-open');t.setAttribute('aria-expanded','false');t.textContent='☰';});});}
  if(h)window.addEventListener('scroll',function(){h.classList.toggle('is-scrolled',window.scrollY>24);},{passive:true});
})();
</script>
</body>
</html>"""

    html = html.replace("castillo0", "castillo")
    html = html.replace("__DAYS__", days)
    html = html.replace("__LEAFLET__", leaflet_block)
    html = html.replace("MAPS_SCRIPT_PLACEHOLDER", maps_js.strip())
    for key, url in img.items():
        html = html.replace(f"__IMG_{key.upper()}__", url)

    out = BASE / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"Written {out} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
