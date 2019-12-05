"""Generates JSON to override IndieKit micropub configuration.

Docs: https://paulrobertlloyd.github.io/indiekit/config
Defaults: https://github.com/paulrobertlloyd/indiekit/blob/master/lib/publication/defaults.js

"""
import json


AUTHOR = "Ashwin Vishnu Mohanan"
ALIAS = "ashwinvis"


syndicate_to = [
    #  {
    #      "uid": f"https://twitter.com/{alias}/",
    #      "name": f"{AUTHOR} on Twitter"
    #  },
    {
        "uid": f"https://mastodon.acc.sunet.se/@{ALIAS}",
        "name": f"{AUTHOR} on Mastodon",
    },
    #  {
    #      "uid": f"https://micro.blog/{ALIAS}",
    #      "name": f"{AUTHOR} on Micro.blog"
    #  },
]

post_types = dict.fromkeys(
    (
        "article",
        "note",
        "photo",
        "video",
        "audio",
        "reply",
        "like",
        "repost",
        "bookmark",
        "checkin",
        "event",
    )
)

categories = [
    "indieweb",
]

default_template = "indiekit/default.njk"

for ptype in post_types:
    if ptype == "article":
        dest = "content"
    elif ptype == "note":
        dest = "content/notes"
    elif ptype in ("photo", "video", "audio"):
        dest = "content/media"
    elif ptype in ("like", "repost"):
        dest = "content/mentions"
    else:
        dest = "content/misc"

    assert not dest.endswith("/")
    post_types[ptype] = {
        "post": {
            "path": "%s/{{ published | date('yyyy-MM-dd') }}-{{ slug }}.md"
            % dest,
            "url": "{{ published | date('yyyy-MM-dd') }}-{{ slug }}",
        },
        "template": default_template,
    }
    if ptype in ("photo", "video", "audio"):
        post_types[ptype].update(
            {
                "media": {
                    "path": "content/static/%ss/{{ published | date('yyyy-MM-dd') }}-{{ filename }}"
                    % ptype,
                }
            }
        )


# Finally write the json
with open("config.json", "w") as config:
    json.dump(
        {
            "post_types": post_types,
            "syndicate-to": syndicate_to,
            "categories": categories,
        },
        config,
        indent=2,
    )
