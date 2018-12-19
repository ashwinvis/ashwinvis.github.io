#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
import sys
import os

sys.path.append(os.curdir)
from util import encrypt_email


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

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'backdrop'
STATIC_PATHS = ['images', 'pdf']

# Backdrop specific variables
SITESUBTITLE = 'Ph. D. student in Geophysical Fluid Mechanics and Turbulence'
SITE_DESCRIPTION = '''
My research centers around geophysical flows, particularly with
gravity waves and vortices, studied from a turbulence perspective. I am trained
in computational, theoretical and experimental tools to do this. I am also a
strong advocate for open-source, open-data and open-science.'''
PROFILE_IMAGE = '/images/dp_ashwin.jpg'
EMBLEMS = (
    ('/images/KTH_Logotyp_RGB_2013-2.svg', 'https://kth.se'),
)
FAVICON = '/images/KTH_logo.png'

# Carousel
CAROUSEL = (
    ('Curriculum Vitae', 'images/caro_cv.png', 'pages/cv.html'),
    ('At Linné FLOW Centre, Department of Mechanics, KTH', 'images/caro_kth.jpg',
     'https://www.mech.kth.se/mech/info_staff.xhtml?ID=381'),
)

# Blogroll
LINKS = (
    ('Linné FLOW Centre', 'https://www.flow.kth.se'),
    ('FluidDyn Project', 'https://fluiddyn.bitbucket.io'),
    ('Student Profile', 'https://www.mech.kth.se/mech/info_staff.xhtml?ID=381'),
    ('Python.org', 'https://python.org/'),
)

# Social widget
EMAIL = encrypt_email(AUTHOR, rev_username='sivniwhsa', domain='pm', tld='me')
GPG = 'https://pgp.mit.edu/pks/lookup?op=vindex&search=0x2BF1534545A73FAD'
MASTODON = 'https://scholar.social/@ashwinvis'
SOCIAL = (
    # To be uncommented when font-awesome implements fa-gnupg
    #  ('GnuPG',
    #   'https://pgp.mit.edu/pks/lookup?op=vindex&search=0x2BF1534545A73FAD'),
    ('Github', 'https://github.com/ashwinvis'),
    ('Gitlab', 'https://source.coderefinery.org/ashwinvis/'),
    ('Bitbucket', 'https://bitbucket.org/avmo'),
    ('LinkedIn',
     'https://www.linkedin.com/in/ashwinvishnu/'),
)
RESEARCH = (
    ('Zotero', 'https://zotero.org/ashwinvis'),
    ('ResearchGate',
     'https://www.researchgate.net/profile/Ashwin_Vishnu_Mohanan'),
    ('Google-Scholar',
     'https://scholar.google.se/citations?user=zv4wwKoAAAAJ'),
    ('ORCID', 'https://orcid.org/0000-0002-2979-6327'),
    ('Zenodo',
     'https://zenodo.org/search?page=1&size=20&q=Mohanan,%20Ashwin%20Vishnu'),
)

YEAR = date.today().year
LICENSE = r'''
    <a
    href="https://github.com/ashwinvis/ashwinvis.github.io/blob/develop/LICENSE">
    CC-BY-SA 4.0</a> | GnuPG: 45A73FAD
    '''

# Plugins
PLUGIN_PATHS = ['../theme/pelican-plugins']
PLUGINS = [
    'sitemap', 'representative_image', 'tipue_search',
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
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives', 'index', 'pages')
DIRECT_TEMPLATES = ((
    'index', 'tags', 'categories', 'archives', 'search',
))
