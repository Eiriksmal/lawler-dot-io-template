#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eric Lawler'
SITENAME = u'Lawler.io'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# My own defaults
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['eric_extensions', 'neighbors', 'sitemap']

THEME = 'theme'
LOGO = '/images/logo.png'

DEFAULT_CATEGORY = 'Dross'

DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'tags']

SITEMAP = {
    'format': 'xml',
    'exclude': ['tag/', 'author/']
}

ARTICLE_URL = 'scrivings/{slug}'
ARTICLE_SAVE_AS = 'scrivings/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
CATEGORY_URL = 'categories/{slug}'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
AUTHOR_SAVE_AS = ''
TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'
ARCHIVES_URL = 'archives'
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORIES_URL = 'categories'
TAGS_SAVE_AS = 'tags/index.html'
TAGS_URL = 'tags'

STATIC_PATHS = [
    'images',
    'static',
    'css'
    ]

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
    }

# Theme extras
MENUITEMS = [
  ('Vault', 'archives'),
]

SOCIAL = (
  ('GitHub', 'https://github.com/Eiriksmal'),
  ('Twitter', 'https://www.twitter.com/Eiriksmal'),
  ('LinkedIn', 'https://www.linkedin.com/in/eric-lawler/'),
  ('Flickr', 'https://www.flickr.com/photos/eric-lawler/albums'),
)
