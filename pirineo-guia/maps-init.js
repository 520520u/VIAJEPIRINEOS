/* Mapas Pirineo — Leaflet offline (España + Francia) */
(function () {
  'use strict';
  var COLORS = {
    sea: '#4a7c9b', sand: '#e8e2d6', pine: '#2d5a3d', stone: '#5c5346',
    route: '#c4874a', snow: '#f4f7fa',
    d1: '#3d6b4f', d2: '#4a7c9b', d3: '#6b5a8a', d4: '#c4874a', d5: '#2d5a3d', d6: '#5c5346',
    d7: '#7d6b5a', d8: '#2e6b8a', d9: '#456b8c', d10: '#8a6b2e', d11: '#6b3a5c'
  };

  /* Corredor Pirineo central: Aragón, Navarra y Hautes-Pyrénées */
  var REGION = {
    type: 'Feature', properties: { name: 'Pirineo central · ES/FR' },
    geometry: { type: 'Polygon', coordinates: [[
      [-0.95, 42.48], [-0.85, 42.42], [-0.65, 42.38], [-0.45, 42.37],
      [-0.25, 42.38], [-0.05, 42.40], [0.15, 42.42], [0.35, 42.46],
      [0.50, 42.52], [0.58, 42.62], [0.55, 42.72], [0.38, 42.80],
      [0.20, 42.88], [0.30, 42.98], [0.28, 43.08], [0.10, 43.15],
      [-0.15, 43.22], [-0.40, 43.25], [-0.65, 43.18], [-0.78, 43.05],
      [-0.85, 42.92], [-0.92, 42.78], [-0.95, 42.65], [-0.95, 42.48]
    ]] }
  };

  var POIS = {
    jaca: [-0.549, 42.569], torla: [-0.034, 42.626], broto: [-0.123, 42.607],
    praderaOrdesa: [-0.043, 42.656], ainsa: [0.140, 42.415], mediano: [0.035, 42.425],
    escalona: [0.055, 42.445], benasque: [0.525, 42.605], cerler: [0.548, 42.595],
    estos: [0.478, 42.645], biescas: [-0.467, 42.635], panticosa: [-0.283, 42.723],
    sallent: [-0.417, 42.773], hecho: [-0.747, 42.739], anso: [-0.833, 42.758],
    oza: [-0.685, 42.781], santaCruz: [-0.675, 42.523], sanJuanPena: [-0.667, 42.507],
    fiscal: [-0.095, 42.488], campo: [0.285, 42.535], villanua: [-0.380, 42.650],
    puertoPiedrafita: [-0.320, 42.688], puenteLaReina: [-0.620, 42.720],
    canfranc: [-0.527, 42.760], somport: [-0.546, 42.793], lescun: [-0.583, 42.871],
    accous: [-0.593, 43.035], laruns: [-0.429, 43.055], colSoulor: [-0.383, 42.995],
    gabas: [-0.335, 42.939], argelles: [-0.084, 43.030], cauterets: [-0.116, 42.888],
    pontEspagne: [-0.157, 42.846], gaube: [-0.171, 42.818], gavarnie: [-0.009, 42.735], luz: [-0.003, 42.870],
    payolle: [-0.180, 42.799], tourmalet: [-0.145, 42.907], arreau: [0.260, 42.906],
    bielsa: [-0.222, 42.652], portalet: [-0.372, 42.799]
  };

  var DAYS = {
    day1: {
      color: COLORS.d1,
      stops: [
        { ll: POIS.jaca, name: 'Jaca (llegada)', n: 1 },
        { ll: POIS.broto, name: 'Broto', n: 2 },
        { ll: POIS.torla, name: 'Torla', n: 3 },
        { ll: POIS.praderaOrdesa, name: 'Pradera de Ordesa', n: 4 }
      ],
      path: [POIS.jaca, POIS.broto, POIS.torla, POIS.praderaOrdesa]
    },
    day2: {
      color: COLORS.d2,
      stops: [
        { ll: POIS.torla, name: 'Torla', n: 1 },
        { ll: POIS.ainsa, name: 'Aínsa', n: 2 },
        { ll: POIS.mediano, name: 'Embalse de Mediano', n: 3 },
        { ll: POIS.escalona, name: 'Escalona', n: 4 }
      ],
      path: [POIS.torla, POIS.fiscal, POIS.ainsa, POIS.mediano, POIS.escalona]
    },
    day3: {
      color: COLORS.d3,
      stops: [
        { ll: POIS.ainsa, name: 'Aínsa', n: 1 },
        { ll: POIS.benasque, name: 'Benasque', n: 2 },
        { ll: POIS.cerler, name: 'Cerler', n: 3 },
        { ll: POIS.estos, name: 'Valle de Estós', n: 4 }
      ],
      path: [POIS.ainsa, POIS.campo, POIS.benasque, POIS.cerler, POIS.estos]
    },
    day4: {
      color: COLORS.d4,
      stops: [
        { ll: POIS.benasque, name: 'Benasque', n: 1 },
        { ll: POIS.biescas, name: 'Biescas', n: 2 },
        { ll: POIS.panticosa, name: 'Panticosa', n: 3 },
        { ll: POIS.sallent, name: 'Sallent de Gállego', n: 4 }
      ],
      path: [POIS.benasque, POIS.villanua, POIS.biescas, POIS.puertoPiedrafita, POIS.panticosa, POIS.sallent]
    },
    day5: {
      color: COLORS.d5,
      stops: [
        { ll: POIS.sallent, name: 'Sallent de Gállego', n: 1 },
        { ll: POIS.hecho, name: 'Valle de Hecho', n: 2 },
        { ll: POIS.oza, name: 'Selva de Oza', n: 3 },
        { ll: POIS.anso, name: 'Ansó', n: 4 }
      ],
      path: [POIS.sallent, POIS.biescas, POIS.puenteLaReina, POIS.hecho, POIS.oza, POIS.anso]
    },
    day6: {
      color: COLORS.d6,
      stops: [
        { ll: POIS.anso, name: 'Ansó', n: 1 },
        { ll: POIS.jaca, name: 'Jaca', n: 2 },
        { ll: POIS.santaCruz, name: 'Santa Cruz de la Serós', n: 3 },
        { ll: POIS.sanJuanPena, name: 'San Juan de la Peña', n: 4 }
      ],
      path: [POIS.anso, POIS.hecho, POIS.jaca, POIS.santaCruz, POIS.sanJuanPena]
    },
    day7: {
      color: COLORS.d7,
      stops: [
        { ll: POIS.jaca, name: 'Jaca', n: 1 },
        { ll: POIS.canfranc, name: 'Canfranc (estación)', n: 2 },
        { ll: POIS.somport, name: 'Paso de Somport', n: 3 },
        { ll: POIS.lescun, name: 'Lescun (Francia)', n: 4 }
      ],
      path: [POIS.jaca, POIS.canfranc, POIS.somport, POIS.lescun]
    },
    day8: {
      color: COLORS.d8,
      stops: [
        { ll: POIS.lescun, name: 'Lescun', n: 1 },
        { ll: POIS.accous, name: 'Accous · Valle de Aspe', n: 2 },
        { ll: POIS.laruns, name: 'Laruns · Valle de Ossau', n: 3 },
        { ll: POIS.gabas, name: 'Gabas · Lac Bious', n: 4 }
      ],
      path: [POIS.lescun, POIS.accous, POIS.laruns, POIS.colSoulor, POIS.gabas]
    },
    day9: {
      color: COLORS.d9,
      stops: [
        { ll: POIS.laruns, name: 'Laruns', n: 1 },
        { ll: POIS.cauterets, name: 'Cauterets', n: 2 },
        { ll: POIS.pontEspagne, name: 'Pont d\'Espagne', n: 3 },
        { ll: POIS.gaube, name: 'Lac de Gaube', n: 4 }
      ],
      path: [POIS.laruns, POIS.argelles, POIS.cauterets, POIS.pontEspagne, POIS.gaube]
    },
    day10: {
      color: COLORS.d10,
      stops: [
        { ll: POIS.cauterets, name: 'Cauterets', n: 1 },
        { ll: POIS.luz, name: 'Luz-Saint-Sauveur', n: 2 },
        { ll: POIS.gavarnie, name: 'Gavarnie', n: 3 },
        { ll: POIS.gavarnie, name: 'Cirque de Gavarnie', n: 4 }
      ],
      path: [POIS.cauterets, POIS.luz, POIS.gavarnie, POIS.gavarnie]
    },
    day11: {
      color: COLORS.d11,
      stops: [
        { ll: POIS.gavarnie, name: 'Gavarnie', n: 1 },
        { ll: POIS.tourmalet, name: 'Col du Tourmalet', n: 2 },
        { ll: POIS.payolle, name: 'Lac de Payolle', n: 3 },
        { ll: POIS.bielsa, name: 'Bielsa (España)', n: 4 }
      ],
      path: [POIS.gavarnie, POIS.luz, POIS.tourmalet, POIS.payolle, POIS.arreau, POIS.portalet, POIS.bielsa]
    }
  };

  var FULL = [
    { key: 'day1', label: 'D1 · Ordesa', color: COLORS.d1 },
    { key: 'day2', label: 'D2 · Sobrarbe', color: COLORS.d2 },
    { key: 'day3', label: 'D3 · Benasque', color: COLORS.d3 },
    { key: 'day4', label: 'D4 · Tena', color: COLORS.d4 },
    { key: 'day5', label: 'D5 · Hecho', color: COLORS.d5 },
    { key: 'day6', label: 'D6 · Jaca', color: COLORS.d6 },
    { key: 'day7', label: 'D7 · Canfranc', color: COLORS.d7 },
    { key: 'day8', label: 'D8 · Ossau', color: COLORS.d8 },
    { key: 'day9', label: 'D9 · Gaube', color: COLORS.d9 },
    { key: 'day10', label: 'D10 · Gavarnie', color: COLORS.d10 },
    { key: 'day11', label: 'D11 · Tourmalet', color: COLORS.d11 }
  ];

  var maps = {}, pending = [];

  function pinIcon(num, color) {
    return L.divIcon({
      className: 'map-pin-wrap',
      html: '<span class="map-pin" style="background:' + color + '">' + num + '</span>',
      iconSize: [28, 28], iconAnchor: [14, 14], popupAnchor: [0, -14]
    });
  }

  function baseMapOptions() {
    return {
      zoomControl: true, attributionControl: false, tap: true, touchZoom: true,
      preferCanvas: true, maxBounds: [[42.30, -1.0], [43.30, 0.75]], maxBoundsViscosity: 0.85
    };
  }

  function addRegion(map) {
    L.geoJSON(REGION, {
      style: { fillColor: COLORS.sand, fillOpacity: 0.95, color: COLORS.pine, weight: 2, opacity: 0.9 }
    }).addTo(map);
  }

  function pathToLatLngs(path) {
    return path.map(function (ll) { return [ll[1], ll[0]]; });
  }

  function addRoute(map, day, color) {
    var c = color || day.color, latlngs = pathToLatLngs(day.path);
    L.polyline(latlngs, { color: c, weight: 4, opacity: 0.85, dashArray: '8 6', lineCap: 'round' }).addTo(map);
    day.stops.forEach(function (p) {
      L.marker([p.ll[1], p.ll[0]], { icon: pinIcon(p.n, c) })
        .bindPopup('<strong>' + p.n + '.</strong> ' + p.name).addTo(map);
    });
    var b = L.latLngBounds(latlngs);
    day.stops.forEach(function (p) { b.extend([p.ll[1], p.ll[0]]); });
    map.fitBounds(b, { padding: [32, 32], maxZoom: 11 });
  }

  function initFullRoute() {
    var el = document.getElementById('map-full-route');
    if (!el || maps.fullRoute) return;
    var map = L.map(el, baseMapOptions()).setView([42.72, -0.25], 8);
    addRegion(map);
    var all = [];
    FULL.forEach(function (entry) {
      var day = DAYS[entry.key]; if (!day) return;
      var latlngs = pathToLatLngs(day.path); all = all.concat(latlngs);
      L.polyline(latlngs, { color: entry.color, weight: 3, opacity: 0.88, dashArray: '8 6' }).addTo(map);
      day.stops.forEach(function (p) {
        L.marker([p.ll[1], p.ll[0]], { icon: pinIcon(p.n, entry.color) })
          .bindPopup('<strong>' + entry.label + '</strong><br>' + p.n + '. ' + p.name).addTo(map);
      });
    });
    if (all.length) map.fitBounds(L.latLngBounds(all), { padding: [40, 40], maxZoom: 9 });
    maps.fullRoute = map;
    setTimeout(function () { map.invalidateSize(); }, 120);
  }

  function initDayMap(id, dayKey) {
    var el = document.getElementById(id); if (!el || maps[id]) return;
    var day = DAYS[dayKey], map = L.map(el, baseMapOptions());
    addRegion(map); addRoute(map, day); maps[id] = map;
    setTimeout(function () { map.invalidateSize(); }, 120);
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
    }, { rootMargin: '80px', threshold: 0.05 });
    pending.forEach(function (p) { var el = document.getElementById(p.id); if (el) io.observe(el); });
  }

  registerMap('map-full-route', null);
  for (var d = 1; d <= 11; d++) registerMap('map-day' + d, 'day' + d);

  function onReady() {
    observeMaps();
    window.addEventListener('orientationchange', function () {
      setTimeout(function () {
        Object.keys(maps).forEach(function (k) { if (maps[k]) maps[k].invalidateSize(); });
      }, 300);
    });
    window.addEventListener('resize', function () {
      Object.keys(maps).forEach(function (k) { if (maps[k]) maps[k].invalidateSize(); });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', onReady);
  else onReady();
})();
