if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js').then(
    (registration) => {
      console.log('serviceWorker registered with scope: ', registration.scope)
    }
  ).catch(
    (err) => {
      console.log('serviceWorker registration failed: ', err)
    }
  )
};
