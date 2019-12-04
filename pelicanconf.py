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
    ##  Open font library instead of Google Fonts
    # "https://fontlibrary.org/face/source-code-pro",
    # "https://fontlibrary.org/face/source-sans-pro",
    ## Patched open font library css
    "/static/source-code-pro.css",
    "/static/source-sans-pro.css",
    "/static/m-dark.css",
    # "/static/pygments-dark.css",
]
M_THEME_COLOR = "#22272e"

with open("header.html") as header:
    M_HTML_HEADER = header.read()

PLUGIN_PATHS = ["m.css/plugins", "plugins"]
PLUGINS = ["m.htmlsanity", "m.components"]

M_FAVICON = ("/images/SU_logo.png", "image/png")
M_BLOG_FAVICON = M_FAVICON
M_SITE_LOGO = "/images/SU_logo.png"
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
        "\#",
        "",
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

PLUGINS += [
    "ipynb.markup",
    # "representative_image",
    # "tipue_search",
    # "pelican_bibtex",
]

# ipynb
MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_USE_METACELL = True
#  IPYNB_COLORSCHEME = "solarized-dark"
IPYNB_COLORSCHEME = "monokai"
IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = False
IPYNB_EXPORT_TEMPLATE = "nbconvert.tpl"

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
