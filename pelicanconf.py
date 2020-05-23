#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
import shutil
import logging
from datetime import datetime

import m
import pelican_ashwinvis as av
import pelican_planet
#  from pelican.plugins import webring
from pelican_ashwinvis.util.util import read_opml


AUTHOR = "Ashwin Vishnu Mohanan"
SITENAME = "Ashwin Vishnu's Website"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Stockholm"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Metadata
DEFAULT_METADATA = {
    'author': AUTHOR,
    'category': "Blog",
    'summary': "",  # Disable auto-generated summary
    # TODO:
    # 'status': 'draft',  # Avoid accidently publishing articles
}

THEME = "m.css/pelican-theme"
THEME_STATIC_DIR = "static"
STATIC_PATHS = ["images", "showcase", "pdf", "static"]
EXTRA_PATH_METADATA = {
    f'extra/{resource}': {'path': resource}
    for resource in ("robots.txt", "manifest.webmanifest", "sw.js", "app.js")
}
STATIC_PATHS.extend(EXTRA_PATH_METADATA)

DIRECT_TEMPLATES = (
    "index",
    "tags",
    "categories",
    "archives",
    # Requires tipue_search
    #  "search",
    # Requires pybtex
    #  "publications",
)

M_CSS_FILES = [
    "/static/custom.compiled.css",
]
M_THEME_COLOR = "#22272e"

with open("header.html") as header:
    M_HTML_HEADER = header.read()

PLUGINS = [m.htmlsanity, m.components, m.code, m.metadata]

M_SITE_LOGO = "/images/logo_ashwin.png"
M_SITE_LOGO_TEXT = "ashwin.info™"
M_FAVICON = (M_SITE_LOGO, "image/png")
M_BLOG_FAVICON = M_FAVICON
# m.metadata
FORMATTED_FIELDS = ['description', 'badge']

# Navbar
M_LINKS_NAVBAR1 = [
    (
        "Posts",
        "archives",
        "[blog]",
        [
            ("Blog", "category/blog.html", ""),
            ("Tech Talk", "category/tech-talk.html", ""),
        ],
    ),
    (
        "Showcase",
        "pages/showcase.html",
        "",
        [
            ("CV", "pages/cv.html", ""),
            ("Research", "pages/research.html", ""),
            ("Software", "pages/software.html", ""),
            ("Talks", "talks", "[talks]",)
        ],
    ),
]

M_LINKS_NAVBAR2 = [
    ("Planet", "pages/planet.html", "[planet]", []),
    ("Contact", "pages/contact.html", "[contact]", []),
]
M_LINKS_FOOTER1 = [
    ("Social", ""),
    # To be uncommented when font-awesome implements fa-gnupg
    #  ('GnuPG',
    #   'https://pgp.mit.edu/pks/lookup?op=vindex&search=0x2BF1534545A73FAD'),
    ("GitHub", "https://github.com/ashwinvis"),
    ("Gitlab", "https://source.coderefinery.org/ashwinvis/"),
    ("Heptapod", "https://foss.heptapod.net/avmo"),
    ("LinkedIn", "https://www.linkedin.com/in/ashwinvishnu/"),
    ("Mastodon", "https://mastodon.acc.sunet.se/@ashwinvis"),
]
M_LINKS_FOOTER2 = [
    ("Research", "/"),
    ("Zotero", "https://zotero.org/ashwinvis"),
    ("ResearchGate", "https://www.researchgate.net/profile/Ashwin_Vishnu_Mohanan"),
    ("Google-Scholar", "https://scholar.google.se/citations?user=zv4wwKoAAAAJ"),
    ("ORCID", "https://orcid.org/0000-0002-2979-6327"),
    ("Zenodo", "https://zenodo.org/search?page=1&size=20&q=Mohanan,%20Ashwin%20Vishnu"),
]

with open("footer.rst") as footer:
    M_FINE_PRINT = footer.read().format(year=datetime.now().year)


# For landing page
FORMATTED_FIELDS = ['summary', 'landing',
                    'header', 'footer', 'description', 'badge']
M_NEWS_ON_INDEX = ("Latest posts", 5)

# TODO:
M_HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = True

if not shutil.which('latex'):
    logging.warning("LaTeX not found, fallback to rendering math as code")
    M_MATH_RENDER_AS_CODE = True

M_BRIDGY_PUBLISH = "mastodon"

PLUGINS += [
    #  webring,
    av.ipynb.markup,
    pelican_planet,
    # "representative_image",
    # "tipue_search",
    # "pelican_bibtex",
]

# ipynb
MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_USE_METACELL = True
IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = False

# pelican_planet / webring
PLANET_FEEDS = read_opml("planet.opml", ["Planets"])
PLANET_TEMPLATE = 'templates/planet.md.j2'
PLANET_PAGE = 'content/pages/planet.md'
PLANET_MAX_ARTICLES_PER_FEED = 1
PLANET_MAX_ARTICLES = max(42, PLANET_MAX_ARTICLES_PER_FEED * len(PLANET_FEEDS))
PLANET_MAX_SUMMARY_LENGTH = 140

WEBRING_FEED_URLS = list(PLANET_FEEDS.values())
WEBRING_ARTICLES_PER_FEED = PLANET_MAX_ARTICLES_PER_FEED
WEBRING_MAX_ARTICLES = max(42, WEBRING_ARTICLES_PER_FEED * len(WEBRING_FEED_URLS))
WEBRING_SUMMARY_LENGTH = 140
TEMPLATE_PAGES = {"planet.html": "planet.html"}


# Pagination
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2

# Publications with pybtex
PUBLICATIONS_SRC = 'content/static/CV.bib'

# HTML Template
#  PAGINATED_TEMPLATES = ("category", "archives", "index", "pages")
DIRECT_TEMPLATES = (
    "index",
    "tags",
    "categories",
    "archives",
    # Requires tipue_search
    #  "search",
    # Requires pybtex
    #  "publications",
)

AV_THEME = "light"

if AV_THEME == "light":
    M_CSS_FILES.insert(0, "/static/m-light.css")
    IPYNB_COLORSCHEME = "solarized-light"
elif AV_THEME == "dark":
    M_CSS_FILES.insert(0, "/static/m-dark.css")
    M_CSS_FILES.append("/static/bibbase-m-dark.css")
    IPYNB_EXPORT_TEMPLATE = "nbconvert.tpl"
    IPYNB_COLORSCHEME = "monokai"
