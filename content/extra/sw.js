/* https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Offline_Service_workers
 * */
var cacheName = 'ashwin-info-tm-v1'
var contentToCache = [
  '/',
  '/app.js',
  '/index.html',
  '/archives.html',
  '/pages/research.html',
  '/pages/software.html',
  '/pages/cv.html',
  '/pages/contact.html',
  '/pages/planet.html',
  '/static/custom.compiled.css',
  '/static/m-dark.compiled.css',
  '/images/logo_ashwin.png',
  '/images/dp_ashwin_2016.jpg'
]

// Installing Service Worker
self.addEventListener('install', function (e) {
  console.log('[Service Worker] Install')
  e.waitUntil(
    caches.open(cacheName).then(function (cache) {
      console.log('[Service Worker] Caching all: app shell and content')
      return cache.addAll(contentToCache)
    })
  )
})

// Fetching content using Service Worker
self.addEventListener('fetch', function (e) {
  e.respondWith(
    caches.match(e.request).then(function (r) {
      console.log('[Service Worker] Fetching resource: ' + e.request.url)
      return r || fetch(e.request).then(function (response) {
        return caches.open(cacheName).then(function (cache) {
          console.log('[Service Worker] Caching new resource: ' + e.request.url)
          cache.put(e.request, response.clone())
          return response
        })
      })
    })
  )
})
