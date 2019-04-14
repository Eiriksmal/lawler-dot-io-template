import re
import cgi


def convert_quotes(text):
    """
    Convert quotes in *text* into HTML curly quote entities.

    >>> print(convert_quotes('"Isn\\'t this fun?"'))
    &ldquo;Isn&rsquo;t this fun?&rdquo;
    """

    punct_class = r"""[!"#\$\%'()*+,-.\/:;<=>?\@\[\\\]\^_`{|}~]"""

    # Special case if the very first character is a quote
    # followed by punctuation at a non-word-break. Close the quotes by brute
    # force:
    text = re.sub(r"""^'(?=%s\\B)""" % (punct_class,), '&rsquo;', text)
    text = re.sub(r"""^"(?=%s\\B)""" % (punct_class,), '&rdquo;', text)

    # Special case for double sets of quotes, e.g.:
    #   <p>He said, "'Quoted' words in a larger quote."</p>
    text = re.sub(r""""'(?=\w)""", '&ldquo;&lsquo;', text)
    text = re.sub(r"""'"(?=\w)""", '&lsquo;&ldquo;', text)

    # Special case for decade abbreviations (the '80s):
    text = re.sub(r"""\b'(?=\d{2}s)""", '&rsquo;', text)

    close_class = r'[^\ \t\r\n\[\{\(\-]'
    dec_dashes = '&#8211;|&#8212;'

    # Get most opening single quotes:
    opening_single_quotes_regex = re.compile(r"""
            (
                \s          |   # a whitespace char, or
                &nbsp;      |   # a non-breaking space entity, or
                --          |   # dashes, or
                &[mn]dash;  |   # named dash entities
                %s          |   # or decimal entities
                &\#x201[34];    # or hex
            )
            '                 # the quote
            (?=\w)            # followed by a word character
            """ % (dec_dashes,), re.VERBOSE)
    text = opening_single_quotes_regex.sub(r'\1&lsquo;', text)

    closing_single_quotes_regex = re.compile(r"""
            (%s)
            '
            (?!\s | s\b | \d)
            """ % (close_class,), re.VERBOSE)
    text = closing_single_quotes_regex.sub(r'\1&rsquo;', text)

    closing_single_quotes_regex = re.compile(r"""
            (%s)
            '
            (\s | s\b)
            """ % (close_class,), re.VERBOSE)
    text = closing_single_quotes_regex.sub(r'\1&rsquo;\2', text)

    # Any remaining single quotes should be opening ones:
    text = re.sub("'", '&lsquo;', text)

    # Get most opening double quotes:
    opening_double_quotes_regex = re.compile(r"""
            (
                \s          |   # a whitespace char, or
                &nbsp;      |   # a non-breaking space entity, or
                --          |   # dashes, or
                &[mn]dash;  |   # named dash entities
                %s          |   # or decimal entities
                &\#x201[34];    # or hex
            )
            "                 # the quote
            (?=\w)            # followed by a word character
            """ % (dec_dashes,), re.VERBOSE)
    text = opening_double_quotes_regex.sub(r'\1&ldquo;', text)

    # Double closing quotes:
    closing_double_quotes_regex = re.compile(r"""
            #(%s)?   # character that indicates the quote should be closing
            "
            (?=\s)
            """ % (close_class,), re.VERBOSE)
    text = closing_double_quotes_regex.sub('&rdquo;', text)

    closing_double_quotes_regex = re.compile(r"""
            (%s)   # character that indicates the quote should be closing
            "
            """ % (close_class,), re.VERBOSE)
    text = closing_double_quotes_regex.sub(r'\1&rdquo;', text)

    # Any remaining quotes should be opening ones.
    text = re.sub('"', '&ldquo;', text)

    return text


def typographic_escape(text):
    """
    Change naked single and double quotes, as well as ellipses and hyphens, into their typographic equivalents.
    Also escapes HTML through the deprecated Python2 cgi module. Should be marked with the "safe" Jinja2 filter to
    avoid being auto-escaped later.

    convert_quotes function taken straight from Leo Hemsted's smartypants Python library, which itself implemented John Gruber's
    2003 Perl smartypants library
    # Copyright (c) 2017 Leo Hemsted
    # Copyright (c) 2013, 2014, 2016 Yu-Jie Lin
    # Copyright (c) 2004, 2005, 2007, 2013 Chad Miller
    # Copyright (c) 2003 John Gruber
    """
    text = cgi.escape(text.replace('&#39;', "'").replace('&#34;', '"'))

    text = re.sub(r"""\.\.\.""", '&hellip;', text)
    text = re.sub('--', '&mdash;', text)

    # the meat and potatoes comes from smartypants. What an algorithm!
    text = convert_quotes(text)

    return text
