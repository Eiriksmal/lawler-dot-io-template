# Lawler.io

This is it. Everything you need to clone [Lawler.io](https://lawler.io) is here.

The _master_ branch was [renamed](https://stackoverflow.com/questions/53377423/removing-github-profile-repos-from-google-search) to _lawler_ so Google and friends won't crawl its contents.
## How to build this website
You need pip, the Python package manager:

1. `pip install pelican`
2. `pip install Markdown`
3. `pip install yuicompressor`
4. That's it! You can now run `make devserver` from the root directory and navigate to localhost:8000.

## About the website

When computer-programming/engineering types have a website, it's traditional to <del>brag about</del> explain the technology used to create and serve the site. I have no idea who actually reads these summaries, but for posterity's sake&hellip;

The website is a [static site](https://en.wikipedia.org/wiki/Static_web_page) created by [Pelican](https://github.com/getpelican/pelican), a Python static site generator. I added a few custom Python extensions to bend the Jinja2 templating engine to my will.

I created the theme myself&mdash;both the desktop and mobile variants. The basis for the theme is Dave Liepmann's [Edward Tufte CSS](https://edwardtufte.github.io/tufte-css/), which powers the lovely serifed font and gorgeous margin notes you see throughout Lawler.io.

The code highlighting theme is Solarized Dark, my preferred color theme for... everything.

Major thanks to Jody Frankowski's [Blue Penguin theme](https://github.com/jody-frankowski/blue-penguin) (which, itself, was based on pelican-mockingbird) and Claudio Walser's [FH5CO marble theme](https://github.com/claudio-walser/pelican-fh5co-marble-example) as guides to figure out how to use some of Pelican's less-documented areas for advanced themes.
