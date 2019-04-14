"""
Random, small Python snippets I've written to extend the basic Jinja2 functionality.
"""

from pelican import signals
from . import current_copyright
from . import typographic_escape


def add_filter(pelican):
    pelican.env.filters.update({'current_copyright': current_copyright.current_copyright})
    pelican.env.filters.update({'typographic_escape': typographic_escape.typographic_escape})


def register():
    signals.generator_init.connect(add_filter)
