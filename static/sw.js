/* https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Offline_Service_workers
 * */
var cacheName = 'ashwin-info-tm-v1';
var urlsToCache = [
  '/',
  '/index.html',
  '/archives.html',
  '/pages/research.html',
  '/pages/software.html',
  '/pages/cv.html',
  '/pages/contact.html',
  '/pages/planet.html',
  '/static/custom.compiled.css',
  '/static/m-dark.compiled.css',
  'images/logo_ashwin.png',
  'images/dp_ashwin_2016.jpg',
];

self.addEventListener('install', (event) => {
  console.log('[Service Worker] Install');
  event.waitUntil(
    caches.open(cacheName).then((cache) => {
          console.log('[Service Worker] Caching all: app shell and content');
      return cache.addAll(contentToCache);
    })
  );
});

self.addEventListener('fetch', (event) => {
    console.log('[Service Worker] Fetched resource '+event.request.url);
});

