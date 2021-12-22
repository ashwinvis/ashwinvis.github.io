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
          let fediCommentContent
          if (reply.spoiler_text === '') {
            fediCommentContent = reply.content
          } else {
            fediCommentContent =
                 `<details><summary><span id="fedicomment-cw">CW: ${escapeHtml(reply.spoiler_text)}</span></summary>
                    ${reply.content}
                 </details>`
          }
          const mastodonComment =
              `<div class="fedicomment">
                 <div class="author">
                   <span class="avatar">
                     <img src="${escapeHtml(reply.account.avatar_static)}" height=60 width=60 alt="">
                   </span>
                   <span class="name">
                     <a href="${reply.account.url}" rel="nofollow">
                       <span title="${escapeHtml(reply.account.acct)}">
                        ${reply.account.display_name}
                       </span>
                     </a>
                   </span>
                   <span class="date">
                     <a href="${reply.uri}" rel="nofollow">
                       ${reply.created_at.substr(0, 10)}
                     </a>
                   </span>
                 </div>
                 <div class="content">
                   <div class="fedicomment-content">${fediCommentContent}</div>
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
