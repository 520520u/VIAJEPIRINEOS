#!/usr/bin/env python3
"""Genera index.html de la guía del Pirineo."""
import re
import urllib.parse
from pathlib import Path

BASE = Path(__file__).parent
ROOT = BASE.parent

from images_data import SITES  # noqa: E402 — images-data.py importado como módulo

IMG = {
    "hero": "photo-1519681393784-d120267933ba",
}


def u_unsplash(key, w=800):
    return f"https://images.unsplash.com/{IMG[key]}?w={w}&q=85"


def site(key):
    s = SITES[key]
    return s["url"], s.get("full", s["url"]), s.get("cap", key)


def gmaps_embed(stops):
    """Iframe Google Maps con ruta interactiva (sin API key)."""
    enc = [urllib.parse.quote_plus(s) for s in stops]
    if len(enc) == 1:
        return f"https://maps.google.com/maps?q={enc[0]}&z=12&output=embed"
    if len(enc) == 2:
        return f"https://maps.google.com/maps?saddr={enc[0]}&daddr={enc[1]}&dirflg=d&output=embed"
    mid = "+to:".join(enc[1:-1])
    return f"https://maps.google.com/maps?saddr={enc[0]}&daddr={mid}+to:{enc[-1]}&dirflg=d&output=embed"


def gallery(*keys):
    items = []
    for k in keys:
        url, full, cap = site(k)
        items.append(
            f'<button type="button" class="gallery-item" data-full="{full}" data-cap="{cap}" aria-label="Ampliar: {cap}">'
            f'<img src="{url}" alt="{cap}" loading="lazy" decoding="async"></button>'
        )
    return "".join(items)


def spot(key, title, desc):
    url, full, cap = site(key)
    return f"""<li class="spot-item">
                  <button type="button" class="spot-img spot-zoom" data-full="{full}" data-cap="{cap}" aria-label="Ampliar {title}">
                    <img src="{url}" alt="{cap}" loading="lazy" decoding="async">
                  </button>
                  <div class="spot-body"><strong>{title}</strong><span class="spot-desc">{desc}</span></div>
                </li>"""


def day_block(num, zone, title, drive_km, drive_time, hike_km, hike_time, route_text, teaser,
              gallery_html, activities, schedule, spots_html, hike_html, gmaps_url, gmaps_stops, map_id, day_key_label):
    embed = gmaps_embed(gmaps_stops)
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
          <p class="gallery-hint">Toca cualquier foto para ampliar y hacer zoom</p>
          <div class="day-gallery">{gallery_html}</div>
          {hike_html}
          <div class="day-details">
            <div class="day-detail"><h4>Actividades</h4><ul>{activities}</ul></div>
            <div class="day-detail"><h4>Horario sugerido</h4><ul>{schedule}</ul></div>
            <div class="day-detail day-detail--spots"><h4>Qué verás</h4><ul class="spot-list">{spots_html}</ul></div>
          </div>
          <div class="map-stack">
            <div class="map-tabs" role="tablist">
              <button type="button" class="map-tab is-active" data-map="google" role="tab">🗺️ Google Maps</button>
              <button type="button" class="map-tab" data-map="leaflet" role="tab">📍 Mapa offline</button>
            </div>
            <div class="map-panel map-panel--google is-active">
              <iframe class="gmap-embed" title="Ruta día {num} en Google Maps" loading="lazy" allowfullscreen
                referrerpolicy="no-referrer-when-downgrade" src="{embed}"></iframe>
            </div>
            <div class="map-panel map-panel--leaflet">
              <div id="{map_id}" class="leaflet-map" role="img" aria-label="Mapa offline día {num}"></div>
            </div>
            <p class="map-caption">Ruta interactiva con zoom · Cambia a mapa offline si no hay conexión</p>
          </div>
          <a class="btn-map" href="{gmaps_url}" target="_blank" rel="noopener">📍 Abrir ruta en app Google Maps</a>
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

    from itinerary import build_days
    days = build_days(day_block, gallery, spot)

    hero_url = u_unsplash("hero", 1920)
    full_gmaps = gmaps_embed([
        "Jaca, Huesca", "Torla, Huesca", "Aínsa, Huesca", "Benasque, Huesca",
        "Vielha, Lleida", "Canfranc, Huesca", "Lescun, France", "Cauterets, France",
        "Gavarnie, France", "Puigcerdà, Spain", "Prades, France",
    ])
    card_img = {k: site(k)[0] for k in (
        "torla", "ainsa", "benasque", "panticosa", "hecho", "vielha",
        "lescun", "laruns", "cauterets", "gavarnie", "payolle", "villefranche",
    )}

    html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="theme-color" content="#2d5a3d">
  <title>Pirineo · Guía 12 Días · ES / FR / CAT</title>
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
    .day-teaser{color:var(--text-muted);margin-bottom:.5rem;font-size:.95rem}
    .gallery-hint{font-size:.78rem;color:var(--text-muted);margin-bottom:.65rem}
    .day-gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:.65rem;margin-bottom:1.25rem}
    .gallery-item{border:none;padding:0;background:none;cursor:zoom-in;border-radius:var(--radius-sm);overflow:hidden;position:relative}
    .gallery-item::after{content:'🔍';position:absolute;right:.4rem;bottom:.35rem;font-size:.75rem;background:rgba(0,0,0,.45);color:#fff;padding:.15rem .35rem;border-radius:6px}
    .gallery-item img{width:100%;height:120px;object-fit:cover;display:block;transition:transform .2s}
    .gallery-item:active img{transform:scale(1.03)}
    .day-details{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.25rem;margin-bottom:1.25rem}
    .day-detail h4{font-size:.85rem;text-transform:uppercase;letter-spacing:.08em;color:var(--stone);margin-bottom:.5rem}
    .day-detail ul{list-style:none;font-size:.9rem;color:var(--text-muted)}
    .day-detail li{padding:.25rem 0;padding-left:1rem;position:relative}
    .day-detail li::before{content:'→';position:absolute;left:0;color:var(--pine-light)}
    .spot-list{list-style:none}
    .spot-item{display:flex;gap:1rem;padding:.85rem 0;border-bottom:1px solid var(--sand)}
    .spot-item:last-child{border-bottom:none}
    .spot-img{width:96px;height:76px;flex-shrink:0;border-radius:8px;border:none;cursor:zoom-in;padding:0;overflow:hidden}
    .spot-img img{width:100%;height:100%;object-fit:cover;display:block}
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
    .map-stack{border-radius:var(--radius-sm);overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--sand-dark);margin-top:1rem}
    .map-tabs{display:flex;background:var(--white);border-bottom:1px solid var(--sand-dark)}
    .map-tab{flex:1;border:none;background:transparent;padding:.75rem .5rem;font-size:.82rem;font-weight:600;color:var(--text-muted);cursor:pointer}
    .map-tab.is-active{background:var(--pine-pale);color:var(--pine);box-shadow:inset 0 -2px 0 var(--pine)}
    .map-panel{display:none;background:var(--white)}
    .map-panel.is-active{display:block}
    .gmap-embed{width:100%;height:420px;border:0;display:block}
    .map-wrap{border-radius:var(--radius-sm);overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--sand-dark);margin-top:1rem}
    .leaflet-map{height:420px;width:100%}
    .leaflet-map--fullroute{height:520px}
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
    .lightbox{position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,.92);display:none;align-items:center;justify-content:center;padding:1rem}
    .lightbox.is-open{display:flex}
    .lightbox-inner{max-width:min(96vw,1200px);max-height:92vh;display:flex;flex-direction:column;align-items:center}
    .lightbox-img{max-width:100%;max-height:78vh;object-fit:contain;border-radius:8px;touch-action:pinch-zoom}
    .lightbox-cap{color:#fff;margin-top:.75rem;font-size:.9rem;text-align:center;max-width:640px}
    .lightbox-close{position:absolute;top:1rem;right:1rem;width:2.5rem;height:2.5rem;border:none;border-radius:50%;background:rgba(255,255,255,.15);color:#fff;font-size:1.4rem;cursor:pointer}
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
      <span class="hero-tag">🏔️ Aragón · Catalunya · França</span>
      <h1>Pirineo<br><em>Doce días, tres territorios</em></h1>
      <p class="hero-sub">De Ordesa al Canigó: Aragón, Navarra, Val d'Aran, Hautes-Pyrénées y Catalunya Nord. Mapas Google interactivos, fotos reales ampliables y rutas a pie por paisajes UNESCO.</p>
      <div class="hero-meta">
        <span>🌸 Mayo–junio ideal</span>
        <span>🚗 ~1.050 km totales</span>
        <span>🥾 12 rutas a pie</span>
      </div>
    </div>
  </header>

  <section id="intro">
    <div class="container">
      <p class="section-label">Bienvenida</p>
      <h2 class="section-title">Por qué el Pirineo en primavera</h2>
      <p class="section-intro">Mayo y junio: hayas en verde, cascadas al máximo del deshielo y menos turistas que en agosto. <strong>6 días</strong> por Aragón, Navarra y el Val d'Aran (Pirineo catalán español), más <strong>6 días</strong> en Francia: Occitanie y Catalunya Nord hasta el Canigó.</p>
      <div class="intro-grid">
        <div class="intro-card"><h3>🌸 Primavera activa</h3><p>Senderos accesibles hasta 2.000 m. Capas térmicas: mañana fría, mediodía templado.</p></div>
        <div class="intro-card"><h3>🗺️ Mapas Google + offline</h3><p>Cada día incluye ruta interactiva en Google Maps (zoom, satélite) y mapa offline con relieve OSM.</p></div>
        <div class="intro-card"><h3>📸 Fotos reales</h3><p>Imágenes de cada lugar (Wikipedia Commons). Toca para ampliar y hacer zoom con los dedos.</p></div>
        <div class="intro-card"><h3>🏴 Pirineo catalán</h3><p>Val d'Aran, Puigcerdà, Llívia, Villefranche-de-Conflent y el Canigó — más allá del Pirineo aragonés.</p></div>
      </div>
    </div>
  </section>

  <section id="ruta-completa">
    <div class="container">
      <p class="section-label">Visión global</p>
      <h2 class="section-title">Mapa de la ruta completa</h2>
      <p class="section-intro">Los 12 días en un mapa. Pestaña Google Maps para zoom detallado; pestaña offline con relieve y capas OSM.</p>
      <div class="map-stack">
        <div class="map-tabs" role="tablist">
          <button type="button" class="map-tab is-active" data-map="google" role="tab">🗺️ Google Maps</button>
          <button type="button" class="map-tab" data-map="leaflet" role="tab">📍 Mapa offline</button>
        </div>
        <div class="map-panel map-panel--google is-active">
          <iframe class="gmap-embed" title="Ruta completa Pirineo" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade" src="__FULL_GMAPS__"></iframe>
        </div>
        <div class="map-panel map-panel--leaflet">
          <div id="map-full-route" class="leaflet-map leaflet-map--fullroute" role="img" aria-label="Mapa ruta completa 12 días"></div>
        </div>
        <p class="map-caption">~1.050 km · 12 rutas senderistas · Google Maps requiere conexión</p>
      </div>
      <div class="route-legend">
        <span><span class="legend-dot" style="background:#3d6b4f"></span>D1 Ordesa</span>
        <span><span class="legend-dot" style="background:#4a7c9b"></span>D2 Sobrarbe</span>
        <span><span class="legend-dot" style="background:#6b5a8a"></span>D3 Benasque</span>
        <span><span class="legend-dot" style="background:#c4874a"></span>D4 Tena</span>
        <span><span class="legend-dot" style="background:#2d5a3d"></span>D5 Hecho</span>
        <span><span class="legend-dot" style="background:#c45c4a"></span>D6 Val d'Aran</span>
        <span><span class="legend-dot" style="background:#7d6b5a"></span>D7 Canfranc</span>
        <span><span class="legend-dot" style="background:#2e6b8a"></span>D8 Ossau</span>
        <span><span class="legend-dot" style="background:#456b8c"></span>D9 Gaube</span>
        <span><span class="legend-dot" style="background:#8a6b2e"></span>D10 Gavarnie</span>
        <span><span class="legend-dot" style="background:#6b3a5c"></span>D11 Tourmalet</span>
        <span><span class="legend-dot" style="background:#4a8a6b"></span>D12 Cerdanya</span>
      </div>
    </div>
  </section>

  <section id="itinerario">
    <div class="container">
      <p class="section-label">Día a día</p>
      <h2 class="section-title">Itinerario 12 días</h2>
      <p class="section-intro">D1–D5: Pirineo aragonés y navarro. D6: Val d'Aran (catalán). D7–D12: Francia — Occitanie y Catalunya Nord.</p>
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
          <div class="card-img" style="background-image:url('__CARD_torla__')"></div>
          <div class="card-body">
            <p class="card-zone">D1–D2 · Torla</p>
            <h3>Hotel Abetos · Torla</h3>
            <span class="card-style">Hotel montaña · Puerta Ordesa</span>
            <p>A dos minutos del parque. Habitaciones con vistas, parking y desayuno temprano para rutas. Ideal noches 1 y 2 del circuito.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Abetos+Torla" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_ainsa__')"></div>
          <div class="card-body">
            <p class="card-zone">D2 · Aínsa</p>
            <h3>Hotel Mesón de L'Ainsa</h3>
            <span class="card-style">Hotel con encanto · Casco medieval</span>
            <p>Dentro del conjunto histórico. Cenas en la plaza porticada y cero conducción nocturna. Alternativa si prefieres Sobrarbe puro.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Meson+de+L+Ainsa" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_benasque__')"></div>
          <div class="card-body">
            <p class="card-zone">D3 · Benasque</p>
            <h3>Casa Chanatxin</h3>
            <span class="card-style">Apartamento rural · Benasque</span>
            <p>Apartamentos acogedores en el valle. Cocina propia tras rutas largas. Base perfecta para Estós y Cerler.</p>
            <p><a href="https://www.google.com/maps/search/Casa+Chanatxin+Benasque" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_panticosa__')"></div>
          <div class="card-body">
            <p class="card-zone">D4 · Panticosa</p>
            <h3>Balneario de Panticosa</h3>
            <span class="card-style">Hotel-spa · Valle de Tena</span>
            <p>Experiencia termal de montaña entre picos. Reserva baños con antelación. Lujo merecido tras senderismo.</p>
            <p><a href="https://www.google.com/maps/search/Balneario+Panticosa" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_hecho__')"></div>
          <div class="card-body">
            <p class="card-zone">D5 · Hecho / Ansó</p>
            <h3>Casa Sarasa · Valle de Hecho</h3>
            <span class="card-style">Casa rural · Navarra</span>
            <p>Hospitalidad navarra en entorno espectacular. Cerca de Selva de Oza y Ansó. Tranquilidad total.</p>
            <p><a href="https://www.google.com/maps/search/Casa+Sarasa+Hecho+Navarra" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_vielha__')"></div>
          <div class="card-body">
            <p class="card-zone">D6 · Vielha · Val d'Aran</p>
            <h3>Hotel Vielha · Val d'Aran</h3>
            <span class="card-style">Hotel · Pirineo catalán</span>
            <p>Base en la capital aranesa tras Taüll. Perfecto antes de cruzar a Francia por Somport al día siguiente.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Vielha+Val+d+Aran" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_lescun__')"></div>
          <div class="card-body">
            <p class="card-zone">D7 · Lescun</p>
            <h3>La Breche de Roland · Lescun</h3>
            <span class="card-style">Hotel montaña · Valle d'Aspe</span>
            <p>En el corazón del pueblo más bonito del valle d'Aspe. Vistas al Pic d'Anie, cenas caseras y ambiente pirenaico auténtico.</p>
            <p><a href="https://www.google.com/maps/search/La+Breche+de+Roland+Lescun" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_laruns__')"></div>
          <div class="card-body">
            <p class="card-zone">D8 · Laruns / Gabas</p>
            <h3>Hotel Gabizos · Laruns</h3>
            <span class="card-style">Hotel · Valle de Ossau</span>
            <p>Base ideal para el Col du Soulor y el Lac de Bious. Arquitectura tradicional ossalat con confort moderno.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Gabizos+Laruns" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_cauterets__')"></div>
          <div class="card-body">
            <p class="card-zone">D9 · Cauterets</p>
            <h3>Le Lion d'Or · Cauterets</h3>
            <span class="card-style">Hotel con encanto · Termas</span>
            <p>En el centro del pueblo balneario. A dos pasos del teleférico a Gaube y de las termas. Ambiente victoriano de montaña.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Lion+d+Or+Cauterets" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_gavarnie__')"></div>
          <div class="card-body">
            <p class="card-zone">D10 · Gavarnie / Luz</p>
            <h3>Hotel Brèche de Roland · Luz</h3>
            <span class="card-style">Hotel · Valle de Gavarnie</span>
            <p>En Luz-Saint-Sauveur, a 15 min de Gavarnie. Fortalezas Vauban, puentes históricos y acceso temprano al cirque.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Breche+de+Roland+Luz+Saint+Sauveur" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_payolle__')"></div>
          <div class="card-body">
            <p class="card-zone">D11 · Arreau</p>
            <h3>Le Néouvielle · Arreau</h3>
            <span class="card-style">Hotel · Valle d'Aure</span>
            <p>Tras el Tourmalet y Payolle. Base tranquila antes del tramo catalán del día 12.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Neouvielle+Arreau" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>
        <article class="card">
          <div class="card-img" style="background-image:url('__CARD_villefranche__')"></div>
          <div class="card-body">
            <p class="card-zone">D12 · Prades / Canigó</p>
            <h3>Hotel Le Mas Fleuri · Prades</h3>
            <span class="card-style">Hotel · Catalunya Nord</span>
            <p>Última noche con vistas al Canigó. Cerca de Villefranche-de-Conflent y el tren amarillo.</p>
            <p><a href="https://www.google.com/maps/search/Hotel+Prades+Canigo" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
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
        <div class="link-card"><h3>Val d'Aran</h3><p>Turismo del Pirineo catalán español.</p><a href="https://www.turismevaldaran.com/" target="_blank" rel="noopener">turismevaldaran.com →</a></div>
        <div class="link-card"><h3>Catalunya Nord</h3><p>Cerdanya, Canigó y Conflent.</p><a href="https://www.catalunya.com/" target="_blank" rel="noopener">catalunya.com →</a></div>
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

  <div id="lightbox" class="lightbox" hidden role="dialog" aria-modal="true" aria-label="Imagen ampliada">
    <button type="button" class="lightbox-close" aria-label="Cerrar">×</button>
    <div class="lightbox-inner">
      <img class="lightbox-img" src="" alt="" referrerpolicy="no-referrer">
      <p class="lightbox-cap"></p>
    </div>
  </div>

  <footer>
    <em>El Pirineo te espera en verde 🏔️🌸</em>
    <p>Guía 12 días · Aragón · Catalunya · França · Mapas Google + offline</p>
  </footer>

__LEAFLET__
<script>
MAPS_SCRIPT_PLACEHOLDER
</script>
<script>
(function(){
  var h=document.getElementById('site-header'),t=document.getElementById('nav-toggle'),n=document.getElementById('site-nav');
  if(t&&n){t.addEventListener('click',function(){var o=n.classList.toggle('is-open');t.setAttribute('aria-expanded',o?'true':'false');t.textContent=o?'✕':'☰';});n.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){n.classList.remove('is-open');t.setAttribute('aria-expanded','false');t.textContent='☰';});});}
  var lb=document.getElementById('lightbox'),lbImg=lb&&lb.querySelector('.lightbox-img'),lbCap=lb&&lb.querySelector('.lightbox-cap'),lbClose=lb&&lb.querySelector('.lightbox-close');
  function openLb(full,cap){if(!lb)return;lbImg.src=full;lbImg.alt=cap||'';lbCap.textContent=cap||'';lb.hidden=false;lb.classList.add('is-open');document.body.style.overflow='hidden';}
  function closeLb(){if(!lb)return;lb.classList.remove('is-open');lb.hidden=true;lbImg.src='';document.body.style.overflow='';}
  document.addEventListener('click',function(e){var t=e.target.closest('[data-full]');if(t){e.preventDefault();openLb(t.getAttribute('data-full'),t.getAttribute('data-cap'));}});
  if(lbClose)lbClose.addEventListener('click',closeLb);
  if(lb)lb.addEventListener('click',function(e){if(e.target===lb)closeLb();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')closeLb();});
})();
</script>
</body>
</html>"""

    html = html.replace("castillo0", "castillo")
    html = html.replace("__DAYS__", days)
    html = html.replace("__FULL_GMAPS__", full_gmaps)
    html = html.replace("__LEAFLET__", leaflet_block)
    html = html.replace("MAPS_SCRIPT_PLACEHOLDER", maps_js.strip())
    for key, url in card_img.items():
        html = html.replace(f"__CARD_{key}__", url)

    out = BASE / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"Written {out} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
