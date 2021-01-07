Title: About
Date: 2019-03-15 12:50
Modified: 2019-09-04 13:18
Description: Eric Lawler--who is this red-headed CTO? More about me and this website than you ever cared to know.

<section markdown="1">
## About the man

![My grinning face. The red hair doesn't distract from the overly-busy background...]({static}/images/eric_head.jpg)

*So you instinctively click "About" links too, huh?*

 Welcome. I'm Eric Lawler<label for="sn-eric-count" class="margin-toggle">&#8224;</label><input type="checkbox" id="sn-eric-count" class="margin-toggle"><span class="marginnote">One of many on Earth, I might add. There are 28 Eric Lawlers on LinkedIn alone. Tip: You know which one is the *real* me by the hair&hellip;</span>.
 
I help rapidly-growing companies conquer their growing pains and continue hockey-stick revenue charts. As a software engineer turned engineering leader, my servant-leadership philosophies and focus of working *on* the business, not only *in* the business, drive my results.

(You've caught this website in a beta state: In the near future, this section will link you to my portfolio and resume, which explain who I am *in action*, rather than in mere words. For now, you might be interested in this amusing [list of stuff I've been paid to do.](/stuff-ive-done/))

My wife and I have been married for 10 years, in love for 15 years (and counting!), best friends for 16 years, and known each other for an astonishing 21 years now. We've expanded our family with a boisterous bunch of boys, ages 8, 5, and 2, and a much quieter girl, born November 2020.

"Reformed Evangelical Christian" is the most succinct description of my relationship with Jesus, the foundation of my worldview and source of my strong values.

Outside the office, I'm a serious car enthusiast and gearhead (protip: reduce rotating drivetrain mass to increase smiles per mile) and amateur photographer. During 'Rona season, I got back into an early love--mountain biking! You can find me on our local singletrack each weekend, when I'm not fiddling with the family's bike fleet. Nothing beats flying across rock gardens at 20MPH...
</section>
<section markdown="1">
## About the website

When computer-programming/engineering types have a website, it's traditional to <del>brag about</del> explain the technology used to create and serve the site. I have no idea who actually reads these summaries, but for posterity's sake&hellip;

My goal was to create the fastest-possible website using the brain-dead easiest technical solutions, as I would advise any business. <label for="sn-brain" class="margin-toggle">&#8224;</label><input type="checkbox" id="sn-brain" class="margin-toggle"><span class="marginnote">*Polite cough.* I would actually advise a business to use Netlify and publish their static sites straight from a code repository and *not* run a dedicated web server.</span>

This website is a <a href="https://en.wikipedia.org/wiki/Static_web_page" rel="noopener" target=_blank>static site</a> created by <a href="https://blog.getpelican.com/" rel="noopener" target=_blank>Pelican</a>, a Python static site generator. I added a few custom Python extensions to bend the Jinja2 templating engine to my will.

I created the theme myself&mdash;both the desktop and mobile variants. The basis for the theme is Dave Liepmann's <a href="https://edwardtufte.github.io/tufte-css/" rel="noopener" target=_blank>Edward Tufte CSS</a>, which powers the lovely serifed font and gorgeous margin notes you see throughout the site. The code highlighting theme is Solarized Dark, my preferred color theme for... everything.

The website is hosted by <a href="https://cloud.digitalocean.com/" rel="noopener" target=_blank>Digital Ocean</a><label for="sn-do" class="margin-toggle">&#8224;</label><input type="checkbox" id="sn-do" class="margin-toggle"><span class="marginnote">Why not AWS? That question deserves a standalone article. The short answer: Market competition benefits everyone.</span>, running nginx and CentOS 7 Linux. #redhatforlife

Lastly, everything is [checked into git](https://github.com/Eiriksmal/lawler-dot-io) with my usual level of detail (and delightful sprinkling of wackiness). I'm obsessed with the Annotate feature in the JetBrains IDEs. Eschewing PyCharm, I used my existing copy of PHPStorm throughout development.

### How to build this website
<label for="mn-forme" class="margin-toggle">&#8853;</label><input type="checkbox" id="mn-forme" class="margin-toggle"><span class="marginnote">&hellip;so Eric doesn't forget.</span>
This is pretty straightforward. You need pip<label for="sn-noyoudont" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-noyoudont" class="margin-toggle"><span class="sidenote">Okay, no, you don't *technically* need Pip, you can install all the Python .py files by hand, of course. And you'll have to when pip inevitably stops working in ~2028 because the world has moved on to the next great thing.</span>, the Python package manager:

1. `pip install pelican`
2. `pip install Markdown`
3. `pip install yuicompressor`
4. That's it! You can now run `make devserver` from the root directory and navigate to localhost:8000.
</section>
<section markdown="1">
<em>(Are you a proud member of the 0.001% who use feed readers? Lawler.io has an Atom feed available [here](https://lawler.io/feeds/all.atom.xml), but your reader should automatically discover the feed on any essay page.)</em>
</section>
