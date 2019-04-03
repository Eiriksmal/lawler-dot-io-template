#!/usr/bin/python3

import sys, os
from datetime import datetime

TEMPLATE = """
Title: {title}
Date: {year}-{month:02d}-{day:02d} {hour}:{minute:02d}
Category: Dross
Tags:
Description: META
Summary:
Status: Draft

<section markdown="1">
## Subtitle
</section>
"""


def generate_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')

    # Will attempt to make the year's directory. Does not throw an error if it exists
    os.makedirs("content/{}".format(today.year), exist_ok=True)
    new_article = "content/{}/{}.md".format(today.year, slug)

    if os.path.exists(new_article):
        print("Error. Article already exists. Not overwriting.")
        return

    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(new_article, 'w') as w:
        w.write(t)
    print("Article ready for editing: " + new_article)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        generate_entry(sys.argv[1])
    else:
        print("Need an article title to generate a new entry. It's the only argument.")
