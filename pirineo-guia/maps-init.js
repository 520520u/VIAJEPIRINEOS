/* Mapas Pirineo — Google Maps + Leaflet offline */
(function () {
  'use strict';
  var COLORS = {
    sand: '#e8e2d6', pine: '#2d5a3d',
    d1: '#3d6b4f', d2: '#4a7c9b', d3: '#6b5a8a', d4: '#c4874a', d5: '#2d5a3d', d6: '#c45c4a',
    d7: '#7d6b5a', d8: '#2e6b8a', d9: '#456b8c', d10: '#8a6b2e', d11: '#6b3a5c', d12: '#4a8a6b'
  };

  var REGION = {
    type: 'Feature', properties: { name: 'Pirineo ES/FR/CAT' },
    geometry: { type: 'Polygon', coordinates: [[
      [-0.95, 42.48], [-0.65, 42.37], [-0.25, 42.38], [0.15, 42.42], [0.50, 42.52],
      [0.58, 42.72], [0.38, 42.88], [0.45, 43.05], [0.35, 43.18], [0.15, 43.22],
      [-0.15, 43.25], [-0.45, 43.22], [-0.70, 43.10], [-0.85, 42.92], [-0.95, 42.72], [-0.95, 42.48]
    ]] }
  };

  var POIS = {
    jaca: [-0.549, 42.569], torla: [-0.034, 42.626], broto: [-0.123, 42.607],
    praderaOrdesa: [-0.043, 42.656], ainsa: [0.140, 42.415], mediano: [0.035, 42.425],
    escalona: [0.055, 42.445], benasque: [0.525, 42.605], cerler: [0.548, 42.595],
    estos: [0.478, 42.645], biescas: [-0.467, 42.635], panticosa: [-0.283, 42.723],
    sallent: [-0.417, 42.773], hecho: [-0.747, 42.739], anso: [-0.833, 42.758],
    oza: [-0.685, 42.781], fiscal: [-0.095, 42.488], campo: [0.285, 42.535],
    villanua: [-0.380, 42.650], puertoPiedrafita: [-0.320, 42.688], puenteLaReina: [-0.620, 42.720],
    vielha: [0.793, 42.703], taull: [0.852, 42.715], bielsa: [-0.222, 42.652],
    canfranc: [-0.527, 42.760], somport: [-0.546, 42.793], lescun: [-0.583, 42.871],
    accous: [-0.593, 43.035], laruns: [-0.429, 43.055], colSoulor: [-0.383, 42.995],
    gabas: [-0.335, 42.939], argelles: [-0.084, 43.030], cauterets: [-0.116, 42.888],
    pontEspagne: [-0.157, 42.846], gaube: [-0.171, 42.818], gavarnie: [-0.009, 42.735],
    luz: [-0.003, 42.870], payolle: [-0.180, 42.799], tourmalet: [-0.145, 42.907],
    arreau: [0.260, 42.906], puymorens: [1.835, 42.505], puigcerda: [1.928, 42.431],
    llivia: [1.981, 42.464], montlouis: [2.120, 42.508], villefranche: [2.366, 42.387],
    prades: [2.618, 42.618], portalet: [-0.372, 42.799]
  };

  var DAYS = {
    day1: { color: COLORS.d1, stops: [
      { ll: POIS.jaca, name: 'Jaca', n: 1 }, { ll: POIS.broto, name: 'Broto', n: 2 },
      { ll: POIS.torla, name: 'Torla', n: 3 }, { ll: POIS.praderaOrdesa, name: 'Pradera de Ordesa', n: 4 }
    ], path: [POIS.jaca, POIS.broto, POIS.torla, POIS.praderaOrdesa] },
    day2: { color: COLORS.d2, stops: [
      { ll: POIS.torla, name: 'Torla', n: 1 }, { ll: POIS.ainsa, name: 'Aínsa', n: 2 },
      { ll: POIS.mediano, name: 'Mediano', n: 3 }, { ll: POIS.escalona, name: 'Escalona', n: 4 }
    ], path: [POIS.torla, POIS.fiscal, POIS.ainsa, POIS.mediano, POIS.escalona] },
    day3: { color: COLORS.d3, stops: [
      { ll: POIS.ainsa, name: 'Aínsa', n: 1 }, { ll: POIS.benasque, name: 'Benasque', n: 2 },
      { ll: POIS.cerler, name: 'Cerler', n: 3 }, { ll: POIS.estos, name: 'Estós', n: 4 }
    ], path: [POIS.ainsa, POIS.campo, POIS.benasque, POIS.cerler, POIS.estos] },
    day4: { color: COLORS.d4, stops: [
      { ll: POIS.benasque, name: 'Benasque', n: 1 }, { ll: POIS.biescas, name: 'Biescas', n: 2 },
      { ll: POIS.panticosa, name: 'Panticosa', n: 3 }, { ll: POIS.sallent, name: 'Sallent', n: 4 }
    ], path: [POIS.benasque, POIS.villanua, POIS.biescas, POIS.puertoPiedrafita, POIS.panticosa, POIS.sallent] },
    day5: { color: COLORS.d5, stops: [
      { ll: POIS.sallent, name: 'Sallent', n: 1 }, { ll: POIS.hecho, name: 'Hecho', n: 2 },
      { ll: POIS.oza, name: 'Selva de Oza', n: 3 }, { ll: POIS.anso, name: 'Ansó', n: 4 }
    ], path: [POIS.sallent, POIS.biescas, POIS.puenteLaReina, POIS.hecho, POIS.oza, POIS.anso] },
    day6: { color: COLORS.d6, stops: [
      { ll: POIS.anso, name: 'Ansó', n: 1 }, { ll: POIS.bielsa, name: 'Bielsa', n: 2 },
      { ll: POIS.vielha, name: 'Vielha', n: 3 }, { ll: POIS.taull, name: 'Taüll', n: 4 }
    ], path: [POIS.anso, POIS.hecho, POIS.bielsa, POIS.vielha, POIS.taull] },
    day7: { color: COLORS.d7, stops: [
      { ll: POIS.vielha, name: 'Vielha', n: 1 }, { ll: POIS.canfranc, name: 'Canfranc', n: 2 },
      { ll: POIS.somport, name: 'Somport', n: 3 }, { ll: POIS.lescun, name: 'Lescun', n: 4 }
    ], path: [POIS.vielha, POIS.bielsa, POIS.canfranc, POIS.somport, POIS.lescun] },
    day8: { color: COLORS.d8, stops: [
      { ll: POIS.lescun, name: 'Lescun', n: 1 }, { ll: POIS.laruns, name: 'Laruns', n: 2 },
      { ll: POIS.colSoulor, name: 'Col du Soulor', n: 3 }, { ll: POIS.gabas, name: 'Lac Bious', n: 4 }
    ], path: [POIS.lescun, POIS.accous, POIS.laruns, POIS.colSoulor, POIS.gabas] },
    day9: { color: COLORS.d9, stops: [
      { ll: POIS.laruns, name: 'Laruns', n: 1 }, { ll: POIS.cauterets, name: 'Cauterets', n: 2 },
      { ll: POIS.pontEspagne, name: 'Pont d\'Espagne', n: 3 }, { ll: POIS.gaube, name: 'Lac de Gaube', n: 4 }
    ], path: [POIS.laruns, POIS.argelles, POIS.cauterets, POIS.pontEspagne, POIS.gaube] },
    day10: { color: COLORS.d10, stops: [
      { ll: POIS.cauterets, name: 'Cauterets', n: 1 }, { ll: POIS.luz, name: 'Luz', n: 2 },
      { ll: POIS.gavarnie, name: 'Gavarnie', n: 3 }, { ll: POIS.gavarnie, name: 'Cirque UNESCO', n: 4 }
    ], path: [POIS.cauterets, POIS.luz, POIS.gavarnie] },
    day11: { color: COLORS.d11, stops: [
      { ll: POIS.gavarnie, name: 'Gavarnie', n: 1 }, { ll: POIS.tourmalet, name: 'Tourmalet', n: 2 },
      { ll: POIS.payolle, name: 'Payolle', n: 3 }, { ll: POIS.arreau, name: 'Arreau', n: 4 }
    ], path: [POIS.gavarnie, POIS.luz, POIS.tourmalet, POIS.payolle, POIS.arreau] },
    day12: { color: COLORS.d12, stops: [
      { ll: POIS.arreau, name: 'Arreau', n: 1 }, { ll: POIS.puigcerda, name: 'Puigcerdà', n: 2 },
      { ll: POIS.montlouis, name: 'Mont-Louis', n: 3 }, { ll: POIS.villefranche, name: 'Villefranche', n: 4 },
      { ll: POIS.prades, name: 'Prades · Canigó', n: 5 }
    ], path: [POIS.arreau, POIS.puymorens, POIS.puigcerda, POIS.llivia, POIS.montlouis, POIS.villefranche, POIS.prades] }
  };

  var FULL = [
    { key: 'day1', label: 'D1 · Ordesa', color: COLORS.d1 },
    { key: 'day2', label: 'D2 · Sobrarbe', color: COLORS.d2 },
    { key: 'day3', label: 'D3 · Benasque', color: COLORS.d3 },
    { key: 'day4', label: 'D4 · Tena', color: COLORS.d4 },
    { key: 'day5', label: 'D5 · Hecho', color: COLORS.d5 },
    { key: 'day6', label: 'D6 · Val d\'Aran', color: COLORS.d6 },
    { key: 'day7', label: 'D7 · Canfranc', color: COLORS.d7 },
    { key: 'day8', label: 'D8 · Ossau', color: COLORS.d8 },
    { key: 'day9', label: 'D9 · Gaube', color: COLORS.d9 },
    { key: 'day10', label: 'D10 · Gavarnie', color: COLORS.d10 },
    { key: 'day11', label: 'D11 · Tourmalet', color: COLORS.d11 },
    { key: 'day12', label: 'D12 · Cerdanya', color: COLORS.d12 }
  ];

  var maps = {}, pending = [], online = navigator.onLine !== false;

  function pinIcon(num, color) {
    return L.divIcon({
      className: 'map-pin-wrap',
      html: '<span class="map-pin" style="background:' + color + '">' + num + '</span>',
      iconSize: [28, 28], iconAnchor: [14, 14], popupAnchor: [0, -14]
    });
  }

  function baseMapOptions() {
    return {
      zoomControl: true, attributionControl: true, tap: true, touchZoom: true,
      preferCanvas: false, maxBounds: [[42.28, -1.05], [43.35, 2.75]], maxBoundsViscosity: 0.82,
      minZoom: 7, maxZoom: 16
    };
  }

  function tileLayers(map) {
    var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19, attribution: '© OpenStreetMap'
    });
    var topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      maxZoom: 17, attribution: '© OpenTopoMap'
    });
    osm.addTo(map);
    L.control.layers({ 'Mapa': osm, 'Relieve': topo }, null, { position: 'topright' }).addTo(map);
  }

  function addRegion(map) {
    L.geoJSON(REGION, {
      style: { fillColor: COLORS.sand, fillOpacity: 0.35, color: COLORS.pine, weight: 2, opacity: 0.7 }
    }).addTo(map);
  }

  function pathToLatLngs(path) {
    return path.map(function (ll) { return [ll[1], ll[0]]; });
  }

  function addRoute(map, day, color) {
    var c = color || day.color, latlngs = pathToLatLngs(day.path);
    L.polyline(latlngs, { color: c, weight: 5, opacity: 0.9, lineCap: 'round', lineJoin: 'round' }).addTo(map);
    L.polyline(latlngs, { color: '#fff', weight: 2, opacity: 0.5, dashArray: '6 8' }).addTo(map);
    day.stops.forEach(function (p) {
      L.marker([p.ll[1], p.ll[0]], { icon: pinIcon(p.n, c) })
        .bindPopup('<strong>' + p.n + '.</strong> ' + p.name).addTo(map);
    });
    var b = L.latLngBounds(latlngs);
    day.stops.forEach(function (p) { b.extend([p.ll[1], p.ll[0]]); });
    map.fitBounds(b, { padding: [36, 36], maxZoom: 13 });
  }

  function initFullRoute() {
    var el = document.getElementById('map-full-route');
    if (!el || maps.fullRoute) return;
    var map = L.map(el, baseMapOptions()).setView([42.65, 0.2], 8);
    tileLayers(map); addRegion(map);
    var all = [];
    FULL.forEach(function (entry) {
      var day = DAYS[entry.key]; if (!day) return;
      var latlngs = pathToLatLngs(day.path); all = all.concat(latlngs);
      L.polyline(latlngs, { color: entry.color, weight: 4, opacity: 0.88 }).addTo(map);
      day.stops.forEach(function (p) {
        L.marker([p.ll[1], p.ll[0]], { icon: pinIcon(p.n, entry.color) })
          .bindPopup('<strong>' + entry.label + '</strong><br>' + p.n + '. ' + p.name).addTo(map);
      });
    });
    if (all.length) map.fitBounds(L.latLngBounds(all), { padding: [48, 48], maxZoom: 9 });
    maps.fullRoute = map;
    setTimeout(function () { map.invalidateSize(); }, 150);
  }

  function initDayMap(id, dayKey) {
    var el = document.getElementById(id); if (!el || maps[id]) return;
    var day = DAYS[dayKey], map = L.map(el, baseMapOptions());
    tileLayers(map); addRegion(map); addRoute(map, day); maps[id] = map;
    setTimeout(function () { map.invalidateSize(); }, 150);
  }

  function registerMap(id, dayKey) { pending.push({ id: id, dayKey: dayKey }); }

  function bootMap(entry) {
    if (entry.id === 'map-full-route') initFullRoute();
    else initDayMap(entry.id, entry.dayKey);
  }

  function observeMaps() {
    if (!('IntersectionObserver' in window)) { pending.forEach(bootMap); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var match = pending.find(function (p) { return p.id === entry.target.id; });
        if (match) { bootMap(match); io.unobserve(entry.target); }
      });
    }, { rootMargin: '120px', threshold: 0.02 });
    pending.forEach(function (p) { var el = document.getElementById(p.id); if (el) io.observe(el); });
  }

  registerMap('map-full-route', null);
  for (var d = 1; d <= 12; d++) registerMap('map-day' + d, 'day' + d);

  function initMapTabs() {
    document.querySelectorAll('.map-tabs').forEach(function (tabs) {
      var wrap = tabs.closest('.map-stack');
      if (!wrap) return;
      tabs.querySelectorAll('.map-tab').forEach(function (btn) {
        btn.addEventListener('click', function () {
          var mode = btn.getAttribute('data-map');
          tabs.querySelectorAll('.map-tab').forEach(function (b) { b.classList.toggle('is-active', b === btn); });
          wrap.querySelectorAll('.map-panel').forEach(function (p) {
            p.classList.toggle('is-active', p.classList.contains('map-panel--' + mode));
          });
          if (mode === 'leaflet') {
            var lid = wrap.querySelector('.leaflet-map');
            if (lid && lid.id && maps[lid.id]) setTimeout(function () { maps[lid.id].invalidateSize(); }, 80);
          }
        });
      });
    });
  }

  function onReady() {
    observeMaps();
    initMapTabs();
    window.addEventListener('online', function () { online = true; });
    window.addEventListener('offline', function () { online = false; });
    window.addEventListener('orientationchange', function () {
      setTimeout(function () {
        Object.keys(maps).forEach(function (k) { if (maps[k]) maps[k].invalidateSize(); });
      }, 350);
    });
    window.addEventListener('resize', function () {
      Object.keys(maps).forEach(function (k) { if (maps[k]) maps[k].invalidateSize(); });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', onReady);
  else onReady();
})();
