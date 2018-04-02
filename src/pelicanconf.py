#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ashwin Vishnu Mohanan'
SITENAME = "Ashwin Vishnu's Website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'backdrop'

# Plugins
PLUGIN_PATHS = ['../theme/pelican-plugins']
PLUGINS = ['sitemap', 'representative_image', 'tipue_search',
           ]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly',
        'pages': 'monthly'
    }
}

# Pagination
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives', 'index')
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search',
                     ))
