#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
import shutil
import logging

# sys.path.append(os.curdir)
# from pelicanconf import *

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

THEME = "m.css/pelican-theme"
THEME_STATIC_DIR = "static"
STATIC_PATHS = ["images", "showcase", "pdf", "static"]
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
    # "https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600",
    "/static/m-dark.css",
    #  "/static/pygments-dark.css",
]
M_THEME_COLOR = "#22272e"

PLUGIN_PATHS = ["m.css/plugins", "plugins"]
PLUGINS = ["m.htmlsanity", "m.components"]

M_FAVICON = ("/images/SU_logo.png", "image/png")
M_BLOG_FAVICON = M_FAVICON
M_SITE_LOGO = "/images/SU_logo.svg"
M_SITE_LOGO_TEXT = "Home"

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
        "",
        "#",
        [
            ("CV", "pages/cv", ""),
            ("Research", "pages/research", ""),
            ("Software", "pages/software", ""),
            ("Talks", "talks", "[talks]",)
        ],
    ),
]

M_LINKS_NAVBAR2 = [
    ("Contact", "pages/contact", "[contact]", []),
]
M_LINKS_FOOTER1 = [
    ("Social", ""),
    # To be uncommented when font-awesome implements fa-gnupg
    #  ('GnuPG',
    #   'https://pgp.mit.edu/pks/lookup?op=vindex&search=0x2BF1534545A73FAD'),
    ("GitHub", "https://github.com/ashwinvis"),
    ("Gitlab", "https://source.coderefinery.org/ashwinvis/"),
    ("Bitbucket", "https://bitbucket.org/avmo"),
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
M_FINE_PRINT = """

.. role:: raw-html(raw)
    :format: html

`CC-BY-SA 4.0 <https://github.com/ashwinvis/ashwinvis.github.io/blob/develop/LICENSE>`_ | `GnuPG: 45A73FAD <https://keys.openpgp.org/vks/v1/by-fingerprint/05A85046340A0249B9EFF1572BF1534545A73FAD>`_ :raw-html:`<div> </div>` """


# For landing page
FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description', 'badge']
M_NEWS_ON_INDEX = ("Latest posts", 5)

# TODO:
M_HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = True

if not shutil.which('latex'):
    logging.warning("LaTeX not found, fallback to rendering math as code")
    M_MATH_RENDER_AS_CODE = True

PLUGINS += [
    "representative_image",
    "tipue_search",
    "ipynb.markup",
    "pelican_bibtex",
]

# ipynb
MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_USE_METACELL = True
#  IPYNB_COLORSCHEME = "solarized-dark"
IPYNB_COLORSCHEME = "monokai"
IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = False
IPYNB_EXPORT_TEMPLATE ="nbconvert.tpl"

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
