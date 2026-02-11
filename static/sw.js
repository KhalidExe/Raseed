// Service Worker for Raseed PWA
self.addEventListener('install', (event) => {
    console.log('[Service Worker] Installed');
});

self.addEventListener('fetch', (event) => {
    // Basic fetch handler
    // console.log('[Service Worker] Fetching resource: ', event.request.url);
});