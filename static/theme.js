/* Theme switcher
 *
 * Courtesy:
 * Marcin https://medium.com/@mwichary/dark-theme-in-a-day-3518dde2955a
 * Ekiatz https://ekaitz.elenq.tech/dark-light-theme.html
 * */
'use strict'

var themeSwitch = document.getElementById('dark-light-switch')

function init (color) {
  change(color, true)
}
function invert (color) {
  return (color === 'light') ? 'dark' : 'light'
}
function change (color, nowait) {
  // Discard transition is nowait is set
  if (nowait !== true) {
    window.setTimeout(function () {
      document.documentElement.classList.remove('color-theme-in-transition')
    }, 1000)
    document.documentElement.classList.add('color-theme-in-transition')
  }

  // Set attribute to <html> tag
  document.documentElement.setAttribute('data-theme', color)
  themeSwitch.setAttribute('color', color)

  var im = document.getElementById('m-landing-image')
  if (im !== null) {
    im.style.backgroundImage = im.style.backgroundImage.replace(invert(color), color)
  }
  console.log('Setting theme =>', color)
}
function themeChangeRequested () {
  var currentColor = themeSwitch.getAttribute('color')
  var newColor = invert(currentColor)
  change(newColor)

  // Preference is stored in localStorage only when explicitly requested
  console.log('Storing color preference ->', newColor)
  localStorage.setItem('color', newColor)
}
function getCurrentColor () {
  // Color was set before in localStorage
  var storageColor = localStorage.getItem('color')
  if (storageColor !== null) {
    console.log('Retreiving stored color preference <-', storageColor)
    return storageColor
  } else {
    // If local storage is empty, make CSS media query prefers-color-scheme
    var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
    console.log('Honouring prefers-color-scheme')
    return (prefersDark ? 'dark' : 'light')
  }
}
// Execute
init(getCurrentColor())
themeSwitch.addEventListener('click', themeChangeRequested)
