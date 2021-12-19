'use strict'
/* @license Carl Schwan https://carlschwan.eu/ and others who borrowed it */
// Requires:
// import { DOMPurify } from 'purify.min.js'
// fediHost and fediId JS variables defined in an inline script

function escapeHtml (unsafe) {
  return unsafe
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;')
}

const loadComment = document.getElementById('fedicomments-load')
const fediCommentsList = document.getElementById('fedicomments-list')

loadComment.addEventListener('click', function () {
  loadComment.innerHTML = 'Loading'
  fetch(`https://${fediHost}/api/v1/statuses/${fediId}/context`)
    .then(function (response) {
      return response.json()
    })
    .then(function (data) {
      if (data.descendants &&
         Array.isArray(data.descendants) &&
        data.descendants.length > 0) {
        fediCommentsList.innerHTML = ''
        data.descendants.forEach(function (reply) {
          reply.account.display_name = escapeHtml(reply.account.display_name)
          reply.account.emojis.forEach(emoji => {
            reply.account.display_name = reply.account.display_name.replace(`:${emoji.shortcode}:`,
                `<img src="${escapeHtml(emoji.static_url)}" alt="Emoji ${emoji.shortcode}" height="20" width="20" />`)
          })
          const mastodonComment =
              `<div class="fedicomments">
                 <div class="avatar">
                   <img src="${escapeHtml(reply.account.avatar_static)}" height=60 width=60 alt="">
                 </div>
                 <div class="content">
                   <div class="author">
                     <a href="${reply.account.url}" rel="nofollow">
                       <span>${reply.account.display_name}</span>
                       <span class="disabled">${escapeHtml(reply.account.acct)}</span>
                     </a>
                     <a class="date" href="${reply.uri}" rel="nofollow">
                       ${reply.created_at.substr(0, 10)}
                     </a>
                   </div>
                   <div class="fedicomments-content">${reply.content}</div>
                 </div>
               </div>`
          fediCommentsList.appendChild(DOMPurify.sanitize(mastodonComment, { RETURN_DOM_FRAGMENT: true }))
        })
      } else {
        fediCommentsList.innerHTML = '<p>No comments found 😕</p>'
      }
    })
    .then(() => { loadComment.innerHTML = 'Reload comments' })
})
