Title: Notes From The Goal
Date: 2019-04-02 22:33
Modified: 2019-04-04 21:04
Category: Business
Tags: books, management, notes, reference
Description: Eric's key takeaways from Eliyahu M. Goldratt's The Goal.
Summary: The Goal is still one of my favorite business books. The theory of constraints manifests itself everywhere! These are notes I took during my second read through.
Status: Published

<section markdown="1">
## King of business books
<span class="newthought">*The Goal* remains one of the best business books.</span> Facts are true. Their truth does not change with the passage of time. No matter how our hairstyles evolve and computers continue to shrink, the <a href="https://en.wikipedia.org/wiki/Theory_of_constraints" target=_blank rel="noopener">theory of constraints</a> remains a powerful explanation for how work is accomplished. Very few business books have stood this same test of time.

30 years after his initial book was published, an anniversary edition was released containing praise from Kevin Behr, a co-author of *The Phoenix Project*<label for="sn-phoenix" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-phoenix" class="margin-toggle"><span class="sidenote" markdown="1">Mr. Behr's book is an attempt to rewrite *The Goal* for computer-y types---ditching the manufacturing setting for the dull vinyl flooring of a Fortune 1000 company's IT department.</span>. <blockquote><p>Now more than ever, *The Goal* is my first recommendation for CIOs, CTOs and DevOps to better see What to Change, What to Change to and just How to Cause the Change. Thank you, Eli!<footer>Kevin Behr, co-author of *The Phoenix Project*</footer></blockquote>

Despite taking more words to describe the same concepts, *The Phoenix Project* is landing on numerous "Top 10 Books Every New And Experienced Engineering Manager Should Read" listicles written in the past year. I heartily recommend every CTO or CIO read the *original* dissertation on the Theory of Constraints before reading Mr. Behr's less-useful, devops-heavy application of ToC.

</section>
<section markdown="1">
## Key takeaways
While <del>stuck at jury duty</del> chosen to serve the lovely people of beautiful San Diego County, I took the following notes.<label for="mn-meta" class="margin-toggle">&#8853;</label><input type="checkbox" id="mn-meta" class="margin-toggle"><span class="marginnote">Anything in quotes is a direct quote. Everything else is my synthesis.</span>
<div class="epigraph"><blockquote><p>Productivity is meaningless unless you know what your goal is.<footer>Goldratt, 1984, p. 32</footer></blockquote></div>
### Building the foundation (pages 32-59)
<p>The goal is to **make money**. Profit, ROI, and cash flow measure this. Efficiencies, good people, high tech solutions, selling quality products, capturing market share, etc.---these merely *enable* a company to make money, but should never be confused with The Goal.</p>

Net profit and a solid ROI is not enough to stay in business. Cash flow is vital---are we bringing in enough money to meet our expenses each month?

<span class="newthought" markdown="span">**THE GOAL**</span> is <label for="mn-thegoal" class="margin-toggle">&#8853;</label><input type="checkbox" id="mn-thegoal" class="margin-toggle"><span class="marginnote">All three must increase at the same time---no cheating for short-term pops in share price.</span> "to make money by increasing net profit, while simultaneously increasing return on investment, while simultaneously increasing cash flow." (page 49)

### Defining the terms (pages 60-75)
Measurements for daily operation of a manufacturing plant.<label for="mn-expl" class="margin-toggle">&#8853;</label><input type="checkbox" id="mn-expl" class="margin-toggle"><span class="marginnote">Put another way, throughput is money coming in. Inventory is money circulating inside the system. Opex is money paid <em>out</em> to make that throughput money come <em>in</em>.</span> These are a form of expressing "The" Goal in terms a plant understands (Mr. Behr does something similar for IT work in *The Phoenix Project*). See if you can pick up the common element:

- Throughput: The rate at which the system generates <u>money</u> through sales.
- Inventory: All the <u>money</u> that the system has invested in purchasing things it intends to sell.
- Operational expense<label for="sn-opex" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-opex" class="margin-toggle"><span class="sidenote">Opex, in a non-consulting company, includes *all* employee time. Working? Idle? No matter what the employee is doing, it's still opex.</span>: All the <u>money</u> the system spends in order to turn inventory into throughput.

To make money, the value of the product---and the amount charged!---has to be greater than the combination of the investment in inventory and the total operational expense per *sold* unit. Units waiting to sell do not make you money.

Even buildings and machines are inventory<label for="sn-invest" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-invest" class="margin-toggle"><span class="sidenote">When you see "investment", think "inventory."</span>. You can depreciate part of them as opex, but whatever value is left can theoretically be sold as throughput. Making the machine...inventory!

### Understanding flow (pages 80-101)
Trimming production capacity to precisely meet marketing demand is doomed to failure.

- Dependent events and statistical fluctuations necessitate having a buffer on capacity.
- Keeping everyone "busy" in a plant creates excessive inventory.

Statistical fluctuations are the possible range of time a task can take. If the *average* time to solder a wire takes 4.3 minutes, but the range is 2.1 -> 6.4 minutes, no one can predict whether any individual wire will take 2.1 or 4.3 or even 7 minutes to complete<label for="sn-max" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-max" class="margin-toggle"><span class="sidenote">Setting a new maximum time for soldering.</span>.

(Uh, sorry. This needs serious context, but is just for my personal recall.) Even with all the boys *walking* the same speed, even minor *pauses*<label for="sn-pause" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-pause" class="margin-toggle"><span class="sidenote">This is critical. Do you see? You have a bunch of kids walking the same speed, but they're all randomly *pausing* the "work," causing the line to stretch out down the trail...😵</span> to adjust backpacks creates additional length in the line. But the length can't *decrease* because you can't walk in front of the kid you're following! Only the line leader has a pace that can be independently set.

- "Dependency limits the opportunities for higher fluctuations. That can improve throughput." (page 101)
- Throughput is the rate at which the *last* dependent event happens---not the first.

<h3>Taking it to the real world (pages 110+)</h3>

<div class="epigraph"><blockquote><p>We always run, never stop; the other option, having some workers idle, is taboo.<footer>Goldratt, 1984, p. 113</footer></blockquote></div>

Local maxima are useless.<label for="mn-morelater" class="margin-toggle">&#8853;</label><input type="checkbox" id="mn-morelater" class="margin-toggle"><span class="marginnote">(More to come as I finish digesting the final portion of the book)</span> The *entire* system must be optimized. All processing centers *cannot* have the same capacity. Downstream centers need *additional* capacity to absorb the statistical fluctuations from upstream centers.
</section>
<section markdown="1">
## Curious what to read next?
Ken Cone, CTO of Radeus Labs<label for="mn-ken" class="margin-toggle">&#8853;</label><input type="checkbox" id="mn-ken" class="margin-toggle"><span class="marginnote">CTO, co-owner, and lean manufacturing wizard!</span>, encourages anyone interested in the ToC to turn to Dr. Goldratt's followup, *Critical Chain*. It provides a detailed explanation of the drum-buffer-rope methodology for controlling the flow of materials through bottlenecks.

If you like this kind of un-orthodox thinking, and are involved in software development, you should also read *Kanban: Successful Evolutionary Change for Your Technology Business* by David J. Anderson, inventor of the Kanban (capital K) agile software method. He takes a similarly counter-intuitive principle---limiting how many simultaneous tasks development teams can work on---and builds on it to create flexible solutions that scale from 2-man teams all the way up to Microsoft-levels of bureaucracy.
</section>
