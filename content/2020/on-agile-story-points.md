Title: On “Agile” Story Points
Date: 2020-03-16 14:00
Category: Business
Tags: software-development
Description: Brief thoughts on the age-old struggle that of how to measure the complexity of software development tasks.
Status: Published

<section markdown="1">
## The question
<blockquote><p>Hi! I was wondering how you guys do Story Pointing? Do you follow the fibonacci sequence? If not, what do you do?
<footer>- Senior Business Systems Analyst</footer></blockquote>

An innocent-enough question, yes? But this question has created more bitter discussions than almost any other philosophical discussion of business software development.

I dashed off this quick email in response, but wanted to post it to The Greater World<label for="mn-corona" class="margin-toggle">&#8853;</label><input type="checkbox" id="mn-corona" class="margin-toggle"><span class="marginnote">Written while the world is grappling with the Wuhan Coronavirus Epidemic, 2020.</span> in the hopes that someone will read something lacking in my response... and [quickly correct me](https://www.xkcd.com/386/). Please, send any semi-articulate thoughts to my first name @ this domain.
</section>
<section markdown="1">
## Response

 Ah, this is truly a question for the ages.

Silversheet, like my previous engineering team, uses the fibonacci sequence for story points. But, like all teams, we do it "wrong" in the sense that we're really just using it as a proxy for hours. "Hmm, I think that will take me half a day to complete--3 points." or "Gee, sounds tricky. That's probably a 2-ish day ticket? Probably? 8 points."

I recently read [this treatise](https://fberriman.com/2020/01/22/fruit-salad-a-scrum-estimation-scale/) on the subject from one of the Netlify pro[ject/duct] managers (a fast-growing tech company) and loved it. Using something wacky to break the link between points, which are supposed to measure complexity, and the usual amount of time required to complete a task sounds ingenious.

More importantly, in my experience, is to agree to a hard limit on how big a task can be before it gets decomposed. Basically, as I'm sure you've observed, the larger our estimation of complexity or time, the bigger that over/under on estimation gets. Woody Zuill, the "discovered" of mob programming principles, has a vicious exercise he does on software estimates. (Any of [his essays on how useless estimates are](http://zuill.us/WoodyZuill/category/no-estimating/) might prove thought-provoking.) In his exercise, he has everyone time themselves on filling out a tic-tac-toe grid with numbers from 1-9 without repeating a number. Then he asks everyone what their estimate is on how long it would take to do the task again. Estimates are all in the range of 8-15 seconds.

So he has everyone do it again--oh, but, hang on, there's a slight difference this time. The top row needs to add up to 5 and the left column needs to add up to 7. Immediately, this little constraint blows up everyone's times. He repeats it a few time, then ends by introducing an impossible constraint. He wrote a program to detail every possible combination of 1-9 in a 3x3 grid, then ask for you to create the grid with a series of constraints that are literally impossible--but you wouldn't know they're impossible until you write a similar search algorithm to exhaust all the possibilities... Posing as the business user, he would continually ask "Tell me why this is different! It's still just writing 5 lines and 9 numbers! How can this task possibly take ten minutes when you just told me it would take 8 seconds?"

To mitigate the classic "Why can't we ever seem to estimate correctly?" you can clamp story sizes to enforce nothing larger than a 3-point task<label for="sn-cowards" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-cowards" class="margin-toggle"><span class="sidenote">Most people aren't bold enough to do this, so it's more common to see an 8-point limit. 8's too big.</span>. Then, when your 3-pointer runs aground on the craggy rocks of Reality, it slumps into what you'd expect a 5-point ticket to take, but it's not the end of the world.

But when you've secretly packed three 3-point tickets masquerading as an 8-point task, you can run the risk of hiding 21-points of complexity (and time) in the innocent, not-well-understood task: How those 3 tasks combine can create a lot more complexity than tackling them in isolation.
</section>
