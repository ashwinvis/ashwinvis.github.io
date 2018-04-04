#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

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

STATIC_PATHS = ['images']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'backdrop'

## Backdrop specific variables
SITESUBTITLE = 'Ph. D. student in Geophysical Fluid Mechanics and Turbulence'
# FIXME: static paths are not working
# PROFILE_IMAGE = '{filename}/images/KTH_logo.png'

# Blogroll
LINKS = (('KTH', 'https://kth.se'),
         ('Linné FLOW Centre', 'https://www.flow.kth.se'),
         ('FluidDyn Project', 'https://fluiddyn.bitbucket.io'),
         ('Student Profile', 'https://www.mech.kth.se/mech/info_staff.xhtml?ID=381'),
         ('Python.org', 'https://python.org/'),
         )

# Social widget
EMAIL = 'Ashwin Vishnu Mohanan <avmo [at] kth.se>'
SOCIAL = (('Github', 'https://github.com/ashwinvis'),
          ('Bitbucket', 'https://bitbucket.org/avmo'),
          ('LinkedIn',
           'https://www.linkedin.com/in/ashwinvishnu/')
          )
RESEARCH = (('ResearchGate',
             'https://www.researchgate.net/profile/Ashwin_Vishnu_Mohanan'),
            )
YEAR = date.today().year
LICENSE = r'''
    <a
    href="https://github.com/ashwinvis/ashwinvis.github.io/blob/develop/LICENSE">
    CC-BY-SA 4.0</a>'''

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

# HTML Template
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives', 'index')
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search',
                     ))


