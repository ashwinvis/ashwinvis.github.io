---
Title: Power to the user (CSS)
Author: Ashwin Vishnu Mohanan
Date: 2020-06-24T09:30:09.977624
Slug: power-to-the-usercss
Status: published
Summary: Tweaking the world wide web, one CSS stylesheet at a time
Category: Tech Talk
Tags: software, css
---

You probably know that you can tweak appearance of websites with add-ons like
Stylus.  Ever since I figured out [how to use
Inspector](https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector) and
[how to write](https://github.com/openstyles/stylus/wiki/Writing-styles)
"installable" CSS stylesheets myself, I cannot resist the urge to fix websites
with a uneasy appearance. I try to fix it with a few lines of CSS and share it
with others.

## [GitHub Retro][gh-retro]

GitHub quickly rolled out a new wider interface, which could be done a bit better,
IMHO.

| Before    | After  |
|:---------:|:------:|
| <img src="https://user-images.githubusercontent.com/9155111/85446389-ac604900-b594-11ea-8a1f-1018031719e0.png" width="100%"> | <img src="https://user-images.githubusercontent.com/9155111/85515309-42c85500-b5fd-11ea-94d1-057e972bdc8c.png" width="100%"> |

[Get it here][gh-retro].

## [Mastodon Relax][mr-relax]

This is more advanced as it uses [configurable
parameters](https://github.com/FirefoxBar/xStyle/wiki/Style-format#use-advanced-options-in-styles).
The CSS rules are also less hacky, thanks to identifiable CSS classes in
Mastodon's frontend.

| Before | After |
|:------:|:------:
| ![mr-before](https://raw.githubusercontent.com/ashwinvis/mastodon-relax/master/images/before.png) | ![mr-after](https://raw.githubusercontent.com/ashwinvis/mastodon-relax/master/images/after.png) |

[Get it here][mr-relax].

[gh-retro]: https://gist.github.com/ashwinvis/569e7814ff91f52807554789afa7f107
[mr-relax]: https://github.com/ashwinvis/mastodon-relax

The stylesheets are CC-BY-SA licensed. Hope it is useful for you.
