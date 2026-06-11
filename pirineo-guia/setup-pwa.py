#!/usr/bin/env python3
"""Genera versión PWA y carpeta docs/ para GitHub Pages."""
import re
import shutil
from pathlib import Path

BASE = Path(__file__).parent.resolve()
ROOT = BASE.parent

PWA_HEAD = """  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="format-detection" content="telephone=no">
  <meta name="theme-color" content="#2d5a3d">
  <meta name="apple-mobile-web-app-title" content="Pirineo">
  <meta name="mobile-web-app-capable" content="yes">
  <link rel="manifest" href="manifest.webmanifest">
  <link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
"""

MANIFEST = """{
  "name": "Pirineo · Guía 12 Días · ES/FR/CAT",
  "short_name": "Pirineo",
  "description": "Guía de viaje por el Pirineo aragonés y navarro con mapas offline, rutas a pie y alojamientos.",
  "lang": "es",
  "start_url": "./index.html",
  "scope": "./",
  "display": "standalone",
  "orientation": "portrait-primary",
  "background_color": "#f0ebe3",
  "theme_color": "#2d5a3d",
  "categories": ["travel", "navigation"],
  "icons": [
    { "src": "./icons/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any" },
    { "src": "./icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any" },
    { "src": "./icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ]
}
"""

SW_JS = """/* Pirineo Guía — Service Worker offline */
const CACHE = 'pirineo-guia-v3';
const APP_SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/apple-touch-icon.png',
  './icons/icon.svg'
];
const IMAGE_HOSTS = ['images.unsplash.com'];

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE).then(function (cache) {
      return cache.addAll(APP_SHELL);
    }).then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) {
        return caches.delete(k);
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (event) {
  var req = event.request;
  if (req.method !== 'GET') return;
  var url;
  try { url = new URL(req.url); } catch (e) { return; }

  if (IMAGE_HOSTS.indexOf(url.hostname) !== -1) {
    event.respondWith(
      caches.open(CACHE).then(function (cache) {
        return cache.match(req).then(function (cached) {
          if (cached) return cached;
          return fetch(req).then(function (res) {
            if (res && res.ok) cache.put(req, res.clone());
            return res;
          }).catch(function () { return cached; });
        });
      })
    );
    return;
  }

  if (req.mode === 'navigate' || url.href.includes('index.html')) {
    event.respondWith(
      fetch(req).then(function (res) {
        if (res && res.ok) {
          var copy = res.clone();
          caches.open(CACHE).then(function (c) { c.put('./index.html', copy); });
        }
        return res;
      }).catch(function () { return caches.match('./index.html'); })
    );
    return;
  }

  event.respondWith(
    caches.match(req).then(function (cached) {
      return cached || fetch(req).then(function (res) {
        if (res && res.ok && url.origin === self.location.origin) {
          var copy = res.clone();
          caches.open(CACHE).then(function (c) { c.put(req, copy); });
        }
        return res;
      });
    })
  );
});
"""

PWA_FOOTER = """    <p>Guía primavera · PWA offline · Mapas Leaflet · Imágenes cacheadas tras 1ª visita</p>
  </footer>

  <div id="pwa-install" class="pwa-install" hidden role="dialog" aria-label="Instalar guía">
    <p class="pwa-install-text">📲 Instala la guía del Pirineo en tu pantalla de inicio</p>
    <div class="pwa-install-actions">
      <button id="pwa-install-btn" type="button" class="pwa-install-btn">Instalar</button>
      <button id="pwa-install-close" type="button" class="pwa-install-close" aria-label="Cerrar">×</button>
    </div>
  </div>
"""

PWA_CSS = """
    .pwa-install {
      position: fixed; bottom: 1rem; left: 1rem; right: 1rem; max-width: 420px; margin: 0 auto;
      padding: 1rem 1rem 1rem 1.25rem; background: var(--pine); color: #fff; border-radius: 14px;
      box-shadow: 0 8px 32px rgba(0,0,0,.2); z-index: 9999; font-size: .9rem;
      display: flex; align-items: center; gap: .75rem;
    }
    .pwa-install[hidden] { display: none !important; }
    .pwa-install-text { flex: 1; line-height: 1.4; }
    .pwa-install-actions { display: flex; align-items: center; gap: .35rem; flex-shrink: 0; }
    .pwa-install-btn {
      padding: .5rem 1rem; background: var(--sand); color: var(--pine); border: none;
      border-radius: 100px; font-weight: 600; cursor: pointer; font-size: .85rem;
    }
    .pwa-install-close {
      width: 2rem; height: 2rem; border: none; border-radius: 50%; background: rgba(255,255,255,.15);
      color: #fff; font-size: 1.25rem; line-height: 1; cursor: pointer;
    }
"""

PWA_SCRIPT = """
<script>
(function () {
  'use strict';
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('./sw.js', { scope: './' }).catch(function () {});
    });
  }
  var DISMISS_KEY = 'pirineo-pwa-banner-dismissed';
  var deferredPrompt;
  var banner = document.getElementById('pwa-install');
  var btn = document.getElementById('pwa-install-btn');
  var closeBtn = document.getElementById('pwa-install-close');

  function hideBanner(persist) {
    if (!banner) return;
    banner.hidden = true;
    if (persist !== false) { try { localStorage.setItem(DISMISS_KEY, '1'); } catch (e) {} }
  }
  function showBanner() {
    if (!banner) return;
    try { if (localStorage.getItem(DISMISS_KEY)) return; } catch (e) {}
    banner.hidden = false;
  }
  if (closeBtn) closeBtn.addEventListener('click', function () { hideBanner(true); });

  if (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone) {
    hideBanner(false);
  } else {
    window.addEventListener('beforeinstallprompt', function (e) {
      e.preventDefault(); deferredPrompt = e; showBanner();
    });
    if (btn) btn.addEventListener('click', function () {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.finally(function () { deferredPrompt = null; hideBanner(true); });
        return;
      }
      alert('En iPhone/iPad: pulsa Compartir en Safari y elige «Añadir a pantalla de inicio».');
    });
    var isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    if (isIOS) setTimeout(function () {
      if (!window.matchMedia('(display-mode: standalone)').matches) showBanner();
    }, 2500);
  }
})();
</script>
"""


def patch_html(html: str) -> str:
    if 'manifest.webmanifest' not in html:
        html = html.replace(
            '  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n  <meta name="theme-color"',
            '  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n' + PWA_HEAD + '  <meta name="theme-color"',
            1,
        )
        html = html.replace('  <meta name="theme-color" content="#2d5a3d">\n', '', 1)

    if '.pwa-install' not in html:
        html = html.replace('  </style>\n</head>', PWA_CSS + '  </style>\n</head>', 1)

    html = re.sub(
        r'    <p>Guía primavera · Aragón.*?</p>\n  </footer>',
        PWA_FOOTER,
        html,
        count=1,
        flags=re.DOTALL,
    )
    if 'pwa-install' not in html:
        html = html.replace(
            '    <p>Guía primavera · Aragón & Navarra · Mapas Leaflet offline</p>\n  </footer>',
            PWA_FOOTER,
            1,
        )

    if 'serviceWorker.register' not in html:
        html = html.replace('</body>', PWA_SCRIPT + '\n</body>', 1)

    ios_tip = """        <div class="intro-card"><h3>📱 Usar offline en iOS</h3><ol><li>Abre <strong>520vip.space/PIRINEOS</strong> o <strong>520520u.github.io/VIAJEPIRINEOS</strong> en Safari</li><li>Pulsa Compartir → «Añadir a pantalla de inicio»</li><li>Con WiFi la primera vez se cachean textos, mapas e imágenes</li></ol></div>"""
    if 'Usar offline en iOS' not in html and 'id="consejos"' in html:
        html = html.replace(
            '<div class="intro-grid">\n        <div class="intro-card"><h3>🚗 Coche</h3>',
            '<div class="intro-grid">\n' + ios_tip + '\n        <div class="intro-card"><h3>🚗 Coche</h3>',
            1,
        )
    elif '520vip.space/PIRINEOS' not in html and 'Usar offline en iOS' in html:
        html = re.sub(
            r'<div class="intro-card"><h3>📱 Usar offline en iOS</h3>.*?</div>',
            ios_tip.strip(),
            html,
            count=1,
            flags=re.DOTALL,
        )

    return html


def deploy_dir(target: Path):
    target.mkdir(parents=True, exist_ok=True)
    icons = target / "icons"
    icons.mkdir(exist_ok=True)
    html = patch_html((BASE / "index.html").read_text(encoding="utf-8"))
    (target / "index.html").write_text(html, encoding="utf-8")
    (target / "manifest.webmanifest").write_text(MANIFEST.strip() + "\n", encoding="utf-8")
    (target / "sw.js").write_text(SW_JS.strip() + "\n", encoding="utf-8")
    for f in (BASE / "icons").glob("*"):
        shutil.copy2(f, icons / f.name)


def main():
    deploy_dir(BASE.parent / "pirineo-pwa")
    print("PWA:", BASE.parent / "pirineo-pwa")


if __name__ == "__main__":
    main()
