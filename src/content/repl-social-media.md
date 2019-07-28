---
Title: REPL for your data
Authors: Ashwin Vishnu
Date: 2019-07-28
Tags: social media, privacy, fediverse
Status: published
Category: Tech Talk
Summary: Use ethical solutions. Archive your data. REPL.
---

So we have heard this time and time again.

1. Data is the new oil.
1. Surveillance capitalism.
1. The most profitable companies on the entire planet rely on your data[^data].

[^data]: Also known as [GAFAM, the big four /
  five](https://en.m.wikipedia.org/wiki/Big_Four_tech_companies). [Framasoft
  gave an excellent talk about it FOSDEM
  2017](https://framatube.org/videos/watch/31225e78-5f41-41dc-bfca-5e63b34e7be4)
  if you don't mind the French accent.

and so on. I believe the agenda for all these companies is to use data to power
their AI research. And our privacy is just a casualty in this process.  Despite
all this news and "shocking" revelations that we hear almost every day in the
news, many tend to stick around and use them, including me[^contra].  There are
solutions however. And it gets better - what I described below require almost
zero investment (except for your attention and time, of course).

[^contra]: Including me. Even this very blog post is right now on GitHub pages,
  and this would seem like a contradiction. In my defence, I started blogging
  here before the acquisition.  As much as I don't like MS products, GitHub
  doesn't look like the worst place in the world and blogs are not private
  places.

### Solutions that do not require deep technical knowledge

1. Jump ship to the new wave of [decentralized social
   networks, which are collectively called
   Fediverse](https://fediverse.party)[^mast].
1. Start using zero-knowledge and FOSS software services for example
   collaborative document editing[^docs] and emails[^email].
1. Prefer end-to-end encrypted chat applications which cannot be
   compromised[^chat].

### Solutions that need you to be a power user

If you are tech-savvy enough, you can start using OpenPGP with email using
[Enigmail](https://emailselfdefense.fsf.org/en/). And for services you can
also consider self-hosting it[^host] in low-power devices such as a Raspberry
Pi. You can even get a URL to point to your server at absolutely no charge[^dns].

### REPL: Read, evaluate, print and loop

[REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) is a
jargon for consoles of all sorts: bash, python etc. In this case I apply this
into our social media usage. Read what others post, evaluate your thoughts,
share your thoughts into the platform, keep doing it. What is unique about REPL
consoles is that **data is ephemeral**. What you type is not meant to last forever.

Therefore, I have started to cleanse my digital data footprint. I [deleted my
Facebook account](https://deletefacebook.com) several months ago. Right now I
am deleting all my tweets[^tweets]. My reasons are more than privacy oriented.
I do not want blood on my hands on a platform that have a proven impact on how
people think, how they vote and do things. And these platforms profit from
selling analytics, and manipulate users using algorithmic timelines and
recommendations. I am therefore progressively transitioning to more ethical
services.

Unless you are in full control, you have to be always to be cautious while
entrusting some of your data with a third-party service. Even if they are
ethical now. I remember a time not so long ago, when I had a positive
impression about Google and its "Don't be evil" tag line[^evil]. I keep archives
of my Mastodon account[^archive] and will soon add expiration to my posts. I
also have this idea:

<iframe src="https://mastodon.acc.sunet.se/@ashwinvis/102518259996206758/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" allowfullscreen="allowfullscreen"></iframe><script src="https://mastodon.acc.sunet.se/embed.js" async="async"></script>

#### Appendix 1: Mass tweet deletion

So the commands described in the blog post[^tweets] seem to work great. Here
is what I did following the instructions:

1. Downloaded an archive from Twitter
1. Copy and modify `tweet.js` into a proper JSON file.
1. Extract the ID of all tweets.
1. Sniff out the POST request as a cURL command using Firefox. I also added
   the silent flag `-s` for cURL.
   Save it as `deletetweet.sh` and make it executable.
1. And a personal twist: send delete requests in parallel:

```sh
cat tweetstodelete.txt | parallel -j4 "echo 'Deleting {}' && ./deletetweet.sh {}" 2>&1 1>> delete.log &
tail -f delete.log
```

And the cURL command looks like:
```sh
curl -s "https://api.twitter.com/1.1/statuses/destroy/$1.json" ...
```

So now I am down from 1400 tweets to 544 tweets. And the difference is almost
correct:

```sh
❯ wc -l tweetstodelete.txt
844 tweetstodelete.txt
```

In step 3, the following command was used to extract the tweets with no
interaction
```sh
cat tweet.json | jq '.[] | select(.favorite_count == "0") | select(.retweet_count == "0") | select(has("in_reply_to_user_id_str") | not)  | .id' -r > tweetstodelete.txt`
```

To get a list of all the tweets:
```sh
cat tweet.json | jq '.[] | .id' -r > tweetstodelete.txt
```

Now we need something similar for undoing all the likes on Twitter.

**EDIT:** A short how-to "dislike" all your tweets.

Get a list of tweets to dislike from your archive in a
similar approach. Take the `like.js` file from your archive and make it a
proper JSON file.

```sh
cat like.json | jq '.[] | .like.tweetId' -r >! tweetstodislike.txt
```

The POST request is also similar and contains "destroy". However the tweet ID
should be in the data / payload. Therefore the curl command looks like (note
the `$1` where the tweet ID gets substituted):

```sh
#!/bin/bash
curl -s 'https://api.twitter.com/1.1/favorites/destroy.json' ...lots of stuff here...\
  --data"id=$1&cards_platform=Web-13& ...even more stuff..."
```

Save the command in a file called `disliketweet.sh` and then,

```sh
cat tweetstodislike.txt | parallel -j4 "echo 'Disliking {}' && ./disliketweet.sh {}" 2>&1 1>> dislike.log &
tail -f dislike.log
```

#### Appendix 2: Unstar GitHub repositories

1. Used [bookmark-github-stars](https://kirtan403.github.io/bookmark-github-stars/)
   to export all my GitHub stars as html and imported into
   [Zotero](https://zotero.org) (you can also import into your browser). I did so
   because because Zotero also retains valuable metadata (programming language,
   license, description etc.).
1. As [Zotero does not automatically fetch metadata in its initial
   import](https://github.com/zotero/zotero/issues/1515), I wrote a [few
   scripts](https://source.coderefinery.org/ashwinvis/zotero-tools) which
   relies on [pyzotero](https://pyzotero.readthedocs.org/en/latest/). The
   documentation is minimal, but you can reuse them if you want.
1. Finally I run [this
   script](https://gist.github.com/ashwinvis/b7c749a652471ddfd12546abe2d58b75.js)
   which relies on [pygithub](https://pygithub.readthedocs.io/en/latest/).

<script src="https://gist.github.com/ashwinvis/b7c749a652471ddfd12546abe2d58b75.js"></script>

[^mast]: Such as [Mastodon](https://joinmastodon.org)
[^docs]: Good alternatives are [Cryptpad](https://cryptpad.fr/) and
  [Etherpad](https://github.com/ether/etherpad-lite/wiki/Sites-that-run-Etherpad-Lite).
[^email]: [See alternatives](https://www.privacytools.io/providers/email/) of
  which I use ProtonMail. The only downsides that I think are: for extra data
  allowance and POP3/IMAP access you need a paid account
[^chat]: [Google docs spreadsheet which compares digital communication
  protocols](https://docs.google.com/spreadsheets/d/1-UlA4-tslROBDS9IqHalWVztqZo7uxlCeKPQ-8uoFOU/htmlview)
[^host]: [Why you no host](https://yunohost.org/)
[^dns]: Using [Dynamic DNS](https://wiki.archlinux.org/index.php/Dynamic_DNS)
  technology. I use a subdomain name provided at
  [afraid.org](https://freedns.afraid.org).
[^evil]: Which was removed in
  [2018](https://en.wikipedia.org/wiki/Don%27t_be_evil) as they no longer
  follow it.
[^tweets]: I followed [@jlelse's tutorial](https://jlelse.blog/posts/mass-delete-tweets/) to delete tweets.
[^archive]: Using [mastodon-archive](https://github.com/kensanata/mastodon-backup)
[^expire]: This is [an interesting
  essay](https://alexschroeder.ch/wiki/2017-04-27_Record_Keeping) on why you
  should expire your posts.
