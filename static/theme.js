/* Theme switcher
 *
 * Courtesy:
 * Marcin https://medium.com/@mwichary/dark-theme-in-a-day-3518dde2955a
 * Ekiatz https://ekaitz.elenq.tech/dark-light-theme.html
 * */
'use strict'

var themeSwitch = document.getElementById('dark-light-switch')
var body = document.getElementsByTagName('BODY')[0]

function init (color) {
  change('light', color, true)
}
function change (oldColor, newColor, nowait) {
  // Discard transition is nowait is set
  if (nowait !== true) {
    window.setTimeout(function () {
      document.documentElement.classList.remove('color-theme-in-transition')
    }, 1000)
    document.documentElement.classList.add('color-theme-in-transition')
  }

  document.documentElement.setAttribute('data-theme', newColor)
  themeSwitch.setAttribute('color', newColor)
  localStorage.setItem('color', newColor)

  console.log(`Changing theme from ${oldColor} to ${newColor}`)

  var im = document.getElementById('m-landing-image')
  if (im !== null) {
    im.style.backgroundImage = im.style.backgroundImage.replace(
      oldColor, newColor
    )
  }
}
function themeChangeRequested () {
  var color = themeSwitch.getAttribute('color')
  if (color === 'light') { change(color, 'dark') } else { change(color, 'light') }
}
function getCurrentColor () {
  // Color was set before in localStorage
  var storageColor = localStorage.getItem('color')
  if (storageColor !== null) {
    return storageColor
  }

  // If local storage is not set check the background of the page
  // This is dependant of the CSS, be careful
  var background = getComputedStyle(body).getPropertyValue('background-color')
  if (background === 'rgb(255, 255, 255)') {
    return 'light'
  } else {
    return 'dark'
  }
}
init(getCurrentColor())
themeSwitch.addEventListener('click', themeChangeRequested)
