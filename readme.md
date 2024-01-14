# ma9o.com

## How to build this website
1. `python -m venv .venv`
2. `pip install -r requirements.txt`
3. `pnpm add -g yuicompressor`

That's it! You can now run `make devserver` from the root directory and navigate to localhost:8000. 
The `output` directory is tracked by git to make it easier to deploy to Vercel.

### Useful commands
`./generate_entry.py "Post Title Here"` to generate a new post, with metadata placeholders inserted
- `make rsync_upload` to publish the site
- All configuration is in `/pelicanconf.py`
- `/publishconf.py` contains overrides of `pelicanconf` for the `make publish` command (executed by `rsync_upload`). Intended for prod values, keys, etc.
- `pygmentize -S default -f html -a .highlight > default_code.css` For when Pygment/CodeHilite needs a kick in the pants. (Newer versions of Pelican/Pygment/Python Markdown changed how the generated HTML is structured.)

## About the website

Credits: https://github.com/Eiriksmal/lawler-dot-io-template
