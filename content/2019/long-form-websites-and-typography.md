Title: Long-form websites and typography
Date: 2019-04-08 22:48
Modified: 2019-04-09 10:42
Category: Dross
Tags: meta, long-form
Description: A brief explanation of typography, readability, and the temporal nature of content in the age of Medium.com blog posts.
Status: Published

<section markdown="1">
## Or, how to build an anti-Medium.com

Two curiously-related pieces of content were shared on Hacker News today. The first was a short article by [Joshua Li](https://jrl.ninja/etc/1), explaining how a few basic CSS styles can make for a great-looking website---across varying devices. The second was a longer post by Marco Fioretti on how [Google is "forgetting" the old web](http://stop.zona-m.net/2018/01/indeed-it-seems-that-google-is-forgetting-the-old-web/).

The latter post kicked up the usual fierce debates <label for="mn-seo" class="margin-toggle">&#8224;</label><input type="checkbox" id="mn-seo" class="margin-toggle"><span class="marginnote">...and people arguing about whether a search engine should actually return results matching what you type in.</span> around whether the internet is still an open place if *one* gatekeeper determines whether you can find and read certain content.

The former article was berated for having too much CSS <label for="mn-ornot" class="margin-toggle">&#8224;</label><input type="checkbox" id="mn-ornot" class="margin-toggle"><span class="marginnote">...or not enough CSS. Or not including styles for printers.</span> or for using the CSS "rem" unit, instead of ems or pixels or vws.

But what really drew my eye was a comment from [Marcus Holmes](https://news.ycombinator.com/item?id=19610271):
<blockquote><p>Is it just me, then, that hates the "narrow strip of text down the middle of my large monitor" school of web design?
               
I don't understand why I'm being forced to scroll when there's all this blank space to the sides.<footer>Marcus Holmes, comment on news.ycombinator.com</footer></blockquote>

Great question, Marcus. <label for="mn-actually" class="margin-toggle">&#8224;</label><input type="checkbox" id="mn-actually" class="margin-toggle"><span class="marginnote">*Actually*, it's so I can use these sick side notes and margin notes! Thank you, Tufte CSS.</span> Why *doesn't* this website fill 100% of your 1080p or 4K monitor's screen with text? There's a very specific reason, and that is [*text measure*](https://en.wikipedia.org/wiki/Line_length).

<blockquote><p>A block of text or paragraph has a maximum line length that fits a determined design. If the lines are too short then the text becomes disjointed; if they are too long the content loses rhythm as the reader searches for the start of each line.<footer>Wikipedia entry on &ldquo;Measure (typography)&rdquo;, 2019</footer></blockquote>
 
 The optimal width of a paragraph of text is anywhere from 50--80 characters<label for="sn-character" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-character" class="margin-toggle"><span class="sidenote">In both typography- and computer-speak, a *character* is an individual letter or typographic mark.</span> per line, depending on which of the many studies you cite. If a paragraph is *too* wide, your eye loses its place when [tracking back](https://en.wikipedia.org/wiki/Eye_movement_in_reading#Saccades) to the beginning of the next line. This decreases reading comprehension---and increases my irritation when I realize I'm re-reading the same line. 🤦

### So what's the point?
 
For <label for="mn-firefox" class="margin-toggle">&#8224;</label><input type="checkbox" id="mn-firefox" class="margin-toggle"><span class="marginnote">Firefox offers a "Reader" mode that will automatically constrain the page to the same ~68 character maximum width. Again, this is not a coincidence!</span> this website, I chose a text measure that is approximately 70 characters wide, with average line widths of 65-68 characters. After your eye adjusts to the "constrained" width for reading long articles, Wikipedia begins to tire you out.
 
It took several iterations to strike [the right balance](https://github.com/Eiriksmal/lawler-dot-io/commit/68f052e9bf8bbe9c835d3b6683d036971a1d6d82) in this design between too-wide and too-narrow. My final measurement was to drag a bunch of books off the shelf, type out a line from each of them, and arrive at my own ideal width based on what the professionals chose. To my surprise, regardless of the book's physical page sizes and typeface size, all of them were *exactly* 66 characters wide.<label for="sn-duh" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-duh" class="margin-toggle"><span class="sidenote">Given how many web typography dissertations I read in the course of refining this design, I shouldn't have been surprised the professionals use consistent text measures---across publishers.</span>
 
</section>
<section markdown="1">
## What's this have to do with the other article?

The Fioretti article references a serious problem with the most-used search engine on the planet: It literally will not answer search results for sites that are "too old." This could be a post written in 2007, or 2012. No one knows exactly how the Google algorithms rank and prune pages.

Lawler.io was inspired by [Gwern](https://www.gwern.net/About), a self-proclaimed "freelance writer & researcher who lives in Virginia." He wrote something concerning his own website that runs deeply counter to the current online culture: Gwern.net is home to "stable long-term essays which improve over time."

### Stable, long-term

A key ingredient to Gwern's website is his decision to use incredibly robust computer-y bits behind the scenes, to ensure his website isn't going anywhere for a long, long time.

While I am not going to the same extremes as Gwern to keep lawler.io online for decades, it *is* very appealing to create a simple, easy-to-maintain website that can persist for years to come.

Much has been written about [link rot](https://en.wikipedia.org/wiki/Link_rot), the phenomena that most of what goes on the internet disappear after a few weeks or months. Frankly, a lot of the content deserves to rot and disappear. The world has no need for another listicle of 13 Must-Know Viral Memes<label for="sn-believe" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-believe" class="margin-toggle"><span class="sidenote">You won't believe #7!</span>.

The first challenge is putting content on that website that *deserves* to persist. The second, easier<label for="sn-easier" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-easier" class="margin-toggle"><span class="sidenote">Easier for this hacker-generalist CTO, at least.</span> challenge, is keeping it online and living at the same web address.

### Kaizen: Continuous improvement over time

Journalists are paid to write articles. Buzzfeed-esque <label for="sn-buzz" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-buzz" class="margin-toggle"><span class="sidenote">I'm going to use "Buzzfeed" as the Kleenex of "short web articles with outlandish titles and a splashy lead image to get people to click to open the article and share with all their friends but otherwise leave no impact on the 'reader' whatsoever." I understand Buzzfeed News has "real" journalists now and does "serious" work. This does not change the impact they had on online content.</span> listicles come from "content farms" that pay writers to... write. Your writing must hit certain key metrics or your paychecks will dry up. The most important metric? How many people open up your article, of course!

This incentivizes the creation of short articles that draw lots of clicks<label for="sn-engage" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-engage" class="margin-toggle"><span class="sidenote">"Engagement" in social media marketing terms.</span>, but don't leave much of an impact on the reader.

For this kind of content, it almost makes sense that Google would stop surfacing Buzzfeed articles from 2012. It wasn't worth reading then and it *certainly* isn't worth reading now.

### Medium.com

Medium.com exploded in popularity because it, too, used to respect the typography rules we discussed above. <label for="mn-now" class="margin-toggle">&#8224;</label><input type="checkbox" id="mn-now" class="margin-toggle"><span class="marginnote">Today, it's a bit too wide for my personal taste: ~77 characters</span> It used simple black-ish text on a white-ish background. A straight-forward design that got out of your way and *let you read.* And read we did.

But Medium needed to make money. As more authors poured onto the site, as more companies chose to host their blogs on white-labeled Medium.com domains, Medium's design evolved. Nowadays, it's cluttered with crap. Here's a screenshot of a "Recommended" article from tonight:

<figure class="fullwidth"><img src="/images/2019/medium.com.png" alt="Medium.com is a mess"><caption>Screenshot of an article linked to from Medium.com's homepage. (The thin typeface got squished when the image was resized)</caption></figure>

It's cluttered with a huge call to action to join the website, a bunch of nav on the top, and a social widget that follows you down the page during the entire read. Of course, when you hit the bottom, the clutter maximizes with *more* call-to-actions, obligatory comment boxes<label for="sn-engagement" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-engagement" class="margin-toggle"><span class="sidenote">Never forget your engagement KPIs.</span> and other content you might want to read.

I digress. The real thing that Medium.com has changed is expectations on what "long" content is. The pictured article has an impressive 5-minute reading estimate<label for="sn-squint" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-squint" class="margin-toggle"><span class="sidenote">Squint and you can see it under the author's name and link to follow her writing on Medium.</span>. Most of the content I see on Medium are 2-3 minute reads. Any more than that and you *seriously* risk losing readers. 

In fact, that's the second point in the quote I led off with. "I don't understand why I'm being forced to scroll." Though we can be assured Mr. Holmes is willing to scroll on a computer to read long articles, most of the people on the internet can't be bothered. Buzzfeed knows this. Medium.com knows this, too.

But is there another form of consumer? Is there a form of content on the internet that takes longer than 5 minutes to read? Is anyone writing longer articles that repulse the casual surfer, mindlessly flicking through links on their iPhone X? Apparently, such a fiend does exist! Quietly typing away, hundreds of individuals are crafting articles designed to be truly thought-provoking, to stand the test of time and Deserve To Be Read decades later.

Gwern's <label for="mn-metoo" class="margin-toggle">&#8224;</label><input type="checkbox" id="mn-metoo" class="margin-toggle"><span class="marginnote">I, too, quietly tidy up these <del>humble</del> scrivings, tightening them over time. Full edit histories, with explanatory commit messages, are [in GitHub](https://github.com/Eiriksmal/lawler-dot-io/tree/main/content) for interested parties.</span> taken this approach to the next level---he continuously updates his posts as he learns new information on the topic. His experiments will have periodic updates for years. Years!

### Aspirations

My aspiration is to create some substantive content that Deserves To Be Read. While this piece is certainly not one of them, it's a start. A way of painfully filing off the rust from my long-neglected long-form writing skills. A way of unblocking writers block and getting the juices flowing.
</section>
<section markdown="1">
## The answer

What do these two articles have to do with one another? Simple: My website was designed to fit into both categories. An aesthetically-pleasing, easy-to-read website with no tracking codes. A home for long-form content that repulses article skimmers. A place for writing that Google will certainly ignore in 5 years.
</section>
