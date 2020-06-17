---
Title: Tesing Indieweb Stack
Author: Ashwin Vishnu Mohanan
Date: 2020-03-31T22:54:39.019340
Modified: 2020-03-01T13:24:00
Slug: tesing-indieweb-stack
Status: published
Summary: A simple test page to see what parts of Indieweb actually works
Category: Tech Talk
Tags: software
---

Indieweb consists of the following building blocks:

- Microformats 2
- Webmentions

This allows one to Publish Own and Syndicate Somewhere Else (POSSE). I have
logged in my progress in the [Indieweb
wiki](https://indieweb.org/User:Ashwin.info.tm).

## Update: POSSE works

I managed to publish this post, semi-automatically by sending Bridgy a
webmention as follows:

- Embed a blank hyperlink to `https://brid.gy/publish/mastodon` as
  [mentioned here](https://brid.gy/about#webmentions)
- Send a request [using cURL](https://indieweb.org/Webmention-developer#How_to_send_webmentions_with_cURL)

```bash
❯ curl -i -d source=https://ashwinvis.github.io/tesing-indieweb-stack.html -d target=https://brid.gy/publish/mastodon https://brid.gy/publish/webmention
HTTP/2 201 
content-type: application/json; charset=utf-8
cache-control: no-cache
access-control-allow-origin: *
content-security-policy: script-src https: localhost:8080 my.dev.com:8080 'unsafe-inline'; frame-ancestors 'self'; report-uri /csp-report;
strict-transport-security: max-age=16070400; preload
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
location: https://mastodon.acc.sunet.se/@ashwinvis/103920181819443082
x-cloud-trace-context: 89f23f15ae3916e5ae535cfe3d1b5152;o=1
date: Tue, 31 Mar 2020 23:08:54 GMT
server: Google Frontend
content-length: 3401

{
  "id":"103920181819443082",
  "created_at":"2020-03-31T23:08:53.759Z",
  ...
```

- Ensure that accidental duplicate posts are avoided.

```bash
❯ curl -i -d source=https://ashwinvis.github.io/tesing-indieweb-stack.html -d target=https://brid.gy/publish/mastodon https://brid.gy/publish/webmention
HTTP/2 400 
content-type: application/json; charset=utf-8
cache-control: no-cache
access-control-allow-origin: *
content-security-policy: script-src https: localhost:8080 my.dev.com:8080 'unsafe-inline'; frame-ancestors 'self'; report-uri /csp-report;
strict-transport-security: max-age=16070400; preload
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
x-cloud-trace-context: 1691edd117aa780e68a530ff0f116824;o=1
date: Tue, 31 Mar 2020 23:09:55 GMT
server: Google Frontend
content-length: 3731

{
  "error":"Sorry, you've already published that page, and Bridgy Publish doesn't support updating existing posts. Details: https://github.com/snarfed/bridgy/issues/84",
  "original":{
    "id":"103920181819443082
    ...
```

### End result

<iframe src="https://mastodon.acc.sunet.se/@ashwinvis/103920181819443082/embed" class="mastodon-embed" style="max-width: 100%; border: 0" allowfullscreen="allowfullscreen"></iframe><script src="https://mastodon.acc.sunet.se/embed.js" async="async"></script>

### Next steps

To automate this process into CI?
