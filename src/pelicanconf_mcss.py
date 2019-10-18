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
    "https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600",
    "/static/m-dark.css",
]
M_THEME_COLOR = "#22272e"

PLUGIN_PATHS = ["m.css/plugins"]
PLUGINS = ["m.htmlsanity"]

M_FAVICON = ("/images/KTH_logo.png", "image/png")
#  M_BLOG_FAVICON = ("/images/KTH_logo.png", "image/png")
#  M_SITE_LOGO = "/images/KTH_logo.png"
M_SITE_LOGO_TEXT = "Ashwin Vishnu's Website"

# Navbar
M_LINKS_NAVBAR1 = [
    (
        "Posts", "archives", "[blog]",
        [
            ("Blog", "categories/blog.html", ""),
            ("Tech Talk", "categories/tech-talk.html", ""),
        ],
    ),
    ("Contact", "contact/", "contact", []),
]

M_LINKS_NAVBAR2 = [
    ("Showcase", "showcase/", "[showcase]",
        [
            ("Research", "pages/research", ""),
            ("Software", "pages/software", ""),
        ]
    ),
]
