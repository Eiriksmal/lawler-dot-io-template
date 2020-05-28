Title: On GitPrime
Date: 2020-05-27 17:20
Category: Business
Tags: management, reference, software-development
Description: An archive of my thoughts on measuring programmer productivity through actual data, rather than abstract Jira tickets and sprint burndown charts.
Status: Published

<section markdown="1">
Copy-pasting my old interview answers for archive here, since Gitprime's lovely blog post has disappeared<label for="sn-technically" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-technically" class="margin-toggle"><span class="sidenote"><em>Technically</em>, it lives on [in a butchered format](https://www.pluralsight.com/blog/platform/how-i-use-gitprime-metrics-with-my-small-team) under their new Pluralsight branding. Congrats on the acquisition, Ben and team.</span>. I fully believed this when writing it three years ago and still believe it today.

Maybe I'll reach enlightenment in another decade and understand why so many programmers believe it's fundamentally impossible to measure their performance by examining their raw output (programming code). Until then, I'll keep experimenting with metrics on how a team is performing using a variety of--gasp--<em>hard numbers</em> and <em>data</em>.

### ​When did you decide that hard data/metrics could be useful in leading your team?

When comparing ourselves to Lawn Love's other business units, full of KPIs and dashboards for every imaginable metric, engineering felt left out. Our performance indicators were very fuzzy and it was difficult to use feelings and anecdotal information to guide reviews. We didn't have a means to devise more effective strategies for shipping more features, faster, when we couldn't measure our current performance.

After reading your compelling arguments for GitPrime versus less nuanced measurements of engineering productivity, we decided our GitHub data is a potential goldmine, ready to be exploited to level up our engineering game.

### How did you implement (or introduce the idea of) GitPrime?

We dove straight in! The team was skeptical of using quantifiable data to measure programmers' productivity, rightfully decrying the measurement of raw lines touched as a poor proxy for performance. We worked through the highlights from your blog posts on "gaming" GitPrime (ie, doing more, better work!) and how it doesn't use naive assumptions to generate its reports. We even had the chance to let the team express some of their concerns to Travis and your team in a video chat.

At first, we would review GitPrime once a month. After a few months, it became obvious that utilizing the tool more frequently could create faster feedback loops and help us all keep our eye on the end goal--delivering more features to improve the business.
   What reports do you use?

We use the daily​ update report every day in our morning engineering standups. We review the leaderboard, project timeline, and snapshot reports once a month, with the whole team.

### What has been the cultural impact?

What's the saying, only measure what you want to improve? We're creating a culture where poor performers can be identified and coached to success, rather than letting performance problems languish in the dark for months... or years.​ When everyone is aware of how the team as a whole is moving, there are more opportunities for more people to suggest improvements to our processes. Everyone wins when projects are better spec'd and processes streamlined so engineers can spend more time doing what they love most--writing code.

### What measurable improvements have you seen?

In our initial roll out of GitPrime, we shared your observations on commit frequency--that more frequent, smaller commits ("small, fast bites" were Travis's words) strongly correlates to a higher overall throughput--to our team. As a result of changing our behavior and actually having a way to measure our progress, commits per day increased by 50% and time to 100 lines of productive code decreased by a similar amount, three months after launch.

18 months later, we're still aligning our engineering processes with the hard data provided by GitPrime's reports. There's always room for more improvement, and we finally have the tools needed to recognize those areas of opportunity.

</section>
<section markdown="1">
## Bonus!
A never-published followup they did the next year with my most-senior engineer surfaced this gem of a quote: 

<blockquote><p>I was somewhat skeptical at first, to be honest.
<p>&hellip;
<p>After getting in the habit of committing more frequently, and more importantly, consistently pumping out work, my [GitPrime metrics have] increased dramatically. I feel this has generally reflected my ability to output code effectively - not just in raw lines, but actually finishing discrete tasks. <strong>I used to fall into the trap of equating working longer hours with outputting more work, but now I am leaving work earlier in the day and accomplishing more in a shorter amount of time</strong>.</p></blockquote>

And that, dear reader, is what I call the very definition of success. Getting more productive work done in a day through the proverbial working smarter, not harder? As the kids say, that's "😍."
</section>
