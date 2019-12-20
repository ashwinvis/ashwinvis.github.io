---
Title: Licensing software to be permissive
Authors: Ashwin Vishnu
Date: 2019-12-21
Status: publised
Category: Tech Talk
Tags: licensing, open-source
Slug: licensing-software
Summarry: Considerations while selecting a permissive license for your open-source project.
---

A while back we were discussing changing the license of
[transonic](https://transonic.rtfd.io) from CeCILL-B to a more recognizable,
but still permissive license. We would soon make that move. The
most obvious candidate was the 3-clause BSD license and I suggested Apache 2.0
as an alternative, due to the potential benefits.

<iframe src="https://fosstodon.org/@chris/101733810026327049/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" allowfullscreen="allowfullscreen"></iframe>

Being a licensing nerd, I found this [amusing
piece](https://writing.kemitchell.com/2019/03/09/Deprecation-Notice.html)
informative on why everyone should avoid MIT and BSD. Patents and ambiguity.
The article also links to [verbose explanation of what the MIT license actually
means](https://writing.kemitchell.com/2016/09/21/MIT-License-Line-by-Line.html),
along with this warning:

> As a result, the shortness of MIT and BSD are reassuring only until you
> actually try to understand them, and find you need a decoder ring. The terms
> are actually dangerous if you read them without knowing you need that decoder
> ring, believing you see the whole picture, which often turns out to be just
> the picture you wanted to see.

A friend of mine had used the MIT license a while ago, commenting that he
understood every word of it! Well, did he?!

---

My arguments *in favour of* Apache 2.0 were as follows:

1. I don't think Apache 2.0 makes any demand from users of transonic or vice-versa. It is [compatible with BSD too](https://softwareengineering.stackexchange.com/questions/40561/is-bsd-license-compatible-with-apache)

2. To quote the license itself from section 1, it makes it adequately clear
   what *derivate works* are:

  > For the purposes of this License, Derivative Works shall not include works
  > that remain separable from, or merely link (or bind by name) to the
  > interfaces of, the Work and Derivative Works thereof.

  [Source](https://www.oreilly.com/library/view/understanding-open-source/0596005814/ch02.html)

3. The key aspect of Apache 2.0 is it [protects developers from patent
   lawsuits](https://snyk.io/blog/mit-apache-bsd-fairest-of-them-all/)

Indeed something more easier to read, but legally sound would be nice, like Blue Oak.

**Note**: Don't use the Blue Oak license ... yet. Once it is approved / vetted
by [ GNU ](https://www.gnu.org/licenses/license-list.html) and
[ OSI ](https://opensource.org/licenses) we can start using it. I seems like a
good license, but I am no expert, and most likely you are not too. Unfamiliar
licenses slows down contributions and use of software.  It is listed on [ SPDX
](https://spdx.org/licenses/BlueOak-1.0.0.html) though!

