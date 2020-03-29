#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://ashwin.info.tm"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = False

try:
    idx_css = M_CSS_FILES.index("/static/m-dark.css")
    path_css = M_CSS_FILES.pop(idx_css)
    M_CSS_FILES.insert(idx_css, path_css[:-3] + "compiled.css")
except NameError:
    pass

PLANET_FEEDS = read_opml("planet.opml", ("Blogroll", "Planets"))

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

# m.css specific

