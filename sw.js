/* References
-------------
https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Offline_Service_workers
https://serviceworke.rs/strategy-network-or-cache_service-worker_doc.html
https://github.com/mozilla/serviceworker-cookbook
 */
var CACHE = 'fluid.quest-v22.01.19'
var contentToCache = [
  '/',
  '/app.js',
  '/index.html',
  '/archives.html',
  '/pages/research.html',
  '/pages/software.html',
  '/pages/sponsors.html',
  '/pages/cv.html',
  '/pages/contact.html',
  '/static/custom.compiled.css',
  '/static/m-unified.css',
  '/static/theme.js',
  '/static/webmention.min.js',
  '/images/logo_ashwin.png',
  '/images/dp_ashwin_2016.jpg'
]

// On install, cache some resource.
self.addEventListener('install', function (evt) {
  console.log('[Service Worker] The service worker is being installed.')

  // Ask the service worker to keep installing until the returning promise
  // resolves.
  evt.waitUntil(precache())
})

// On fetch, use cache but update the entry with the latest contents
// from the server.
self.addEventListener('fetch', function (evt) {
  console.log('[Service Worker] The service worker is serving the asset.')
  // Try network and if it fails, go for the cached copy.
  evt.respondWith(fromNetwork(evt.request, 5000).catch(function () {
    return fromCache(evt.request)
  }))
})

// Open a cache and use `addAll()` with an array of assets to add all of them
// to the cache. Return a promise resolving when all the assets are added.
function precache () {
  return caches.open(CACHE).then(function (cache) {
    return cache.addAll(contentToCache)
  })
}

// Time limited network request. If the network fails or the response is not
// served before timeout, the promise is rejected.
function fromNetwork (request, timeout) {
  return new Promise(function (resolve, reject) {
    // Reject in case of timeout.
    var timeoutId = setTimeout(reject, timeout)
    // Fulfill in case of success.
    fetch(request).then(function (response) {
      clearTimeout(timeoutId)
      resolve(response)
    // Reject also if network fetch rejects.
    }, reject)
  })
}

// Open the cache where the assets were stored and search for the requested
// resource. Notice that in case of no matching, the promise still resolves
// but it does with `undefined` as value.
function fromCache (request) {
  return caches.open(CACHE).then(function (cache) {
    return cache.match(request).then(function (matching) {
      return matching || Promise.reject(new Error('[Service worker] No-matching cache'))
    })
  })
}
