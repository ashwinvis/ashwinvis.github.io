---
Title: REPL your data footprint
Authors: Ashwin Vishnu
Date: 2019-07-28
Tags: social media, privacy, fediverse
Status: draft
Category: Tech Talk
---

So we have heard this time and time again.

1. Data is the new oil.
1. Surveillance capitalism.
1. The most profitable companies on the entire planet rely on data[^data]

[^data]: Also known as [GAFAM, the big four / five](https://en.m.wikipedia.org/wiki/Big_Four_tech_companies).
  [Framasoft gives excellent talks about it](https://old.framatube.org/media/lets-de-google-ify-the-internet-floss-positive-alt),
  if you don't mind the French accent.

and so on. Despite all these news and "shocking" revelations that we hear
almost every day in the news, many tend to stick around and use them, including
me[^contra].  There are solutions however. And it gets better - what I
described below require almost zero investment (except for your attention and
time, of course).

[^contra]: Including me. Even this very blog post is right now on GitHub pages,
  and this would seem like a contradiction. In my defence, I started blogging
  here before the acquisition.  Ss much as I don't like MS products, GitHub
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

If you are techie enough, you can start using OpenPGP with email using
[Enigmail](https://emailselfdefense.fsf.org/en/). And for services you can
also consider self-hosting it[^host] in low-power devices such as a Raspberry
Pi. You can even get a URL to point to your server at absolutely no charge[^dns].

### REPL: Read, evaluate, print and loop

[REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) is a
jargon for consoles of all sorts: bash, python etc. In this case I apply this
into our social media usage. Read what others post, evaluate your thoughts,
share your thoughts into the platform, keep doing it. What is unique about REPL
consoles are these are ephemeral. They are not meant to last forever.

Therefore I started by cleansing my digital data footprint. I [deleted my
Facebook account](https://deletefacebook.com) several months ago. Right now I
deleting all my tweets[^tweets]. My reasons are more than privacy oriented. I
do not want blood on my hands on a platform that have a proven impact on how
people think, how they vote and do things. And these are all manipulated by
their analytics for anyone who pays, and algorithmic timelines and recommendations
on the user end. I progressively transitioning to more ethical services.

Unless you are in full control you have to be always to be cautious while
entrusting some of your data with a third-party service. Even if they are
ethical now. I remember a time not so long ago, when I had a positive
impression about Google and its "Don't be evil" tagline[^evil]. I keep archives
of my Mastodon account[^archive] and will soon add expiration to my posts.

#### Appendix: mass tweet deletion

So the commands described in the blog post[^tweets] seem to work great --
almost. Here is what I did following the instructions:

1. Downloaded an archive from Twitter
1. Copy and modify `tweet.js` into a proper JSON file.
1. Extract the ID of all tweets
1. Sniff out the POST request as a cURL command using Firefox which starts
   like: `curl "https://api.twitter.com/1.1/statuses/destroy/$1.json" ...`,
   save it as `deletetweet.sh` and make it executable.
1. And a personal twist: send delete requests in parallel: `cat tweetstodelete.txt | parallel -j4 "echo 'Deleting {}' && ./deletetweet.sh {}" 2>&1 1>> delete.log &`

So now I am down from 1400 tweets to 544 tweets. And the difference is almost
correct:

```sh
❯ wc -l tweetstodelete.txt
844 tweetstodelete.txt
```

In step 3, which uses the command:
```sh
cat tweet.json | jq '.[] | select(.favorite_count == "0") | select(.retweet_count == "0") | select(has("in_reply_to_user_id_str") | not)  | .id' -r > tweetstodelete.txt`
```

we are missing out on some tweets and I have see what they are.

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
