#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
#  from pelicanconf import *

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
PLUGINS = ["m.htmlsanity"]

M_FAVICON = ("/images/KTH_logo.png", "image/png")
#  M_BLOG_FAVICON = ("/images/KTH_logo.png", "image/png")
#  M_SITE_LOGO = "/images/KTH_logo.png"
M_SITE_LOGO_TEXT = "Ashwin Vishnu's Website"

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
    ("Contact", "pages/contact/", "contact", []),
]

M_LINKS_NAVBAR2 = [
    (
        "Showcase",
        "showcase/",
        "",
        [
            ("CV", "pages/cv", ""),
            ("Research", "pages/research", ""),
            ("Software", "pages/software", ""),
        ],
    )
]

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
