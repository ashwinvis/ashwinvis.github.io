---
Title: The good old blog with a new name
Author: Ashwin Vishnu Mohanan
Date: 2021-08-30T21:06:13.588973
Slug: domain-name
Status: draft
Summary: I bought a domain name - an address, a virtual place to call it home. The what, the how, the why and all those details for the curious.
Category: Blog
Tags: meta, software
---

**TLDR;** The URL would soon be [fluid.quest][blog]

Today, the thirtieth day of August 2021, as rain continue to shower on
Stockholm nearly every day, I dedicated a few days on the hunt for a succinct
domain name. For a long time, I was not convinced to spent a good handful of
money on a virtual assets.

After jumping ships from Blogger, to Wordpress, to Tumblr and finally to
[GitHub][GitHub] pages using Pelican static-site generator, I thought I was
done. I had full control on the content and the site generation. It was made
using open-source software, which means there was no way the toolchain will not
work in the foreseeable future. Therefore, in short the internals were intact.
Moreover, my precious visitors to my blog then do not get served ads, cookies
or third party tracking scripts.

Everything seemed fine. Until Microsoft bought it. Just because it is a free
service and has a large user base does not give you any guarantee that it might
stay like this forever. I recall how I used to adore following other blogs on
Google Reader until [Google swung the axe, decided it was not profitable
enough](https://killedbygoogle.com/). However feed readers were easy, they
continued to exist and it was still possible to find alternatives (server based
and server-less). In fact this is not an isolated incident. Large corporations
always change services, buy new ones, shutdown old ones on their whims and
fancies. They would come abruptly and I should be prepared for this.

> In fact, blog and email servers are like
> [Hotel California (*You can check out any time you like, but you can never leave*)][california]
> as long as you care about others to be able to find you.

By buying a domain name, you get an address which stays the same,
irrespective of where you host it. The host could be GitHub, Gitlab,
[Codeberg][codeberg] or even a small server powered by a Raspberry Pi!
The readers will still be able to find you. And as a bonus, you can choose a
domain name which represents your interests better.

Talking about interests, did you know there are a lot of [TLDs][TLDs] (top
level domain names) right now. Dull `.com`, `.net` TLDs of yore are old-fashioned.
The prices can vary a lot! And there are lot of gotchas to be considered in choosing
the "domain registrar". Where to buy can be confusing to a total beginner.

## Doing the research pre-purchase

The research that I did was a bit of informal hear say in the interweb. For instance the [following comics by Julia Evans][b0rk] were really useful.

![choosing a domain registrar](https://wizardzines.com/comics/registrar/registrar.png)
![whois protection can](https://wizardzines.com/comics/domain-privacy/domain-privacy.png)
[![TLDs](https://wizardzines.com/comics/tld/tld.png)][TLDs]
![subdomains](https://wizardzines.com/comics/subdomains/subdomains.png)

And this one on receiving
[emails](https://wizardzines.com/comics/receiving-email/) which I will think
about later. Self hosting emails is not an easy feat.

On the choosing the domain registrar question, I got a really good tip from
[Jan Lukas-Else](https://jlelse.blog/dev/free-website) who had good experience
with [Porkbun][Porkbun]. Therefore, I went there and there were many good deals
going on.

## How I bought the domain name

No single correct or optimal answer exists to which domain name one should buy
-- given the plethora of [TLDs][TLDs] in the market! The [prices][prices] are
nearly fixed for a given TLD. This caught my eye, and I decided to scrap the
table for offline brainstorming.

> The result was a small [domain-name-search Python tool](https://codeberg.org/ashwinvis/domain-name-search)

By doing so, I was able to check availability of a different combinations of
domain names using `whois` and visualize costs in an interactive plot. Of
course it was not perfect, a few domain names which were available were up for
premium registration (prices often exceeding thousands of dollars). Which were
not for me.  Once I had a shortlist done, it was easy to reduce the options.

> And thus I registered [fluid.quest][blog]

## Why [fluid.quest][blog]

For now, I can say that:

- It is an ode to the skill that I have been trained in for nearly a decade, Fluid Mechanics.
- The quest post Ph.D. still continues

## What happens next?

First I will archive a snapshot of the landing page and this post, in case
someone runs into the blog years later with the old URL and receives a 404,
wondering what had happened.

I will soon a register [subdomain][subdomain] to point to this very website to
the [new URL][blog]. Hopefully, all visits to the current URL
[ashwinvis.github.io](https://ashwinvis.github.io) would be redirected by
[GitHub][GitHub] as long I continue to use their service.

Over a longer period of time, I can turn to a different host with more ethical
business model such as [Codeberg][codeberg].

[blog]: https://fluid.quest
[GitHub]: https://pages.github.com/
[subdomain]: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages 
[codeberg]: https://codeberg.page/
[TLDs]:https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains 
[california]: https://genius.com/37517]
[b0rk]: https://wizardzines.com
[Porkbun]: https://porkbun.com
[prices]: https://porkbun.com/products/domains
