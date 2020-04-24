if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js').then(
    function (registration) {
      console.log('serviceWorker registered with scope: ', registration.scope)
    }
  ).catch(
    function (err) {
      console.log('serviceWorker registration failed: ', err)
    }
  )
};
