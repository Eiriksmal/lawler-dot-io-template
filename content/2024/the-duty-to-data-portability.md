Title: The Duty to Data Portability
Date: 2024-01-14 13:37
Category: ideas
Tags: data cooperatives
Status: Published
Description: Your site is published!

<section markdown="1">

I have just finished reading [The Revolt of the Public](https://press.stripe.com/the-revolt-of-the-public) by Martin Gurri which provides a great analysis of the current sociopolitical climate in the West. I'm a software engineer based in Europe, and [with Die Grünen cannibalizing Germany’s energy sector ... expand], Putin knocking on the door and the looming possibility of Trump holding it open for him, [something] <label for="sn-aea" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-aea" class="margin-toggle">
<span class="sidenote">Too much complexity, Grug reaching for club</span>

Gurri argues that the public's revolt<label for="sn-gurri" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-gurri" class="margin-toggle">
<span class="sidenote">Arab Spring, Occupy Wall Strett, Tea Party movement, Indignados, Brexit, etc.</span> is not just a rebellion against specific policies or leaders, but a fundamental challenge to the top-down, hierarchical structures of the 20th century. This rebellion is fueled by the information explosion, which has democratized knowledge and destabilized traditional power structures.

The results of such destabilization have been chaos so far, but as I come down the unreasonably optimistic wave of the tech sector,<label for="sn-salaries" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-salaries" class="margin-toggle">
<span class="sidenote">Maybe it's just the severance package?</span> I'm compelled to embrace the vision at the end of the book against such political nihilism: I will argue that in the past coupld of years a number of crucial technological innovations have made this vision possible, and we just need a small cultural step to adopt a framework of this type.

| ![Intensification 90](images/intensification.png) |
|:--:| 
| Computing center in charge of Интенсификация 90, Gorbachev's plan to fix the communist economy. Source: [Traumazone](https://www.youtube.com/playlist?list=PLSjQL8MYniTTLA3wnZ25U-s6RgR4uJNvL) by Adam Curtis. |

<!-- For the theoretical foundations of my thesis, I’ll try to reconcile Fukuyama, Blockchain, Data rights, and Erlang’s actor model (?) oversimplyfing the world like a fellow Grug Brained Developer does.<label for="sn-grug" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-grug" class="margin-toggle">
<span class="sidenote">
[Definitely not Erlang then](https://grugbrain.dev/#grug-on-concurrency), I think I meant the Principal-agent Model.
</span> -->

In The Origins of Political Order, Fukuyama identifies 3 pillars of Modern government: state capacity, accountability and Rule of Law. Up close, these pillars are an intertwined network of actors, as represented by <del>Erlang's concurrency model</del> the principal-agent model, where the public (Principal) hire government offcials (Agent) to enact policy to their benefit. When token prediction models will exterminate humanity and we'll be left with just computers, this model will be no longer needed, and will be more akin to a blockchain, where each actor has perfect information of the world and can be both the agent and the principal. 

Add some words on Friedman, state monopoly over violence, and rule of law at the basis of everything.

If we try to forcibly stretch Fukuyama’s framework over the principal-agent model, we obtain something like this:   

![Principal-Agent Fukuyama](images/principal-agent.png)

With the outgoing edges representing the exchange of information for policy between the actors, and the reflective edges representing accountability...
Here's how each can be improved with technology:

## Hayek and GDPR<label for="sn-edge-1" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-edge-1" class="margin-toggle">
<span class="sidenote">
The Principal &rarr; Agent edge.
</span>

Walking backwards from Yochai Benkler's "The Wealth of Networks", into Hayek's "The Use of Knowledge in Society", and further into "the Wealth of Nations", we see an evolution of the idea of decentralized infromation sourcing from economic benefit into more complex social media.

(some examples about google and facebook data. focus on raw data and possiblity of info for next section)

Privacy regulation (make joke about cookie banners), also something called the right to data portability(note about which legislations uphold it) (canont find this link where it had all countries and if they had the right), establishing that a user of digital services should be able to get out all their information in a "reasonably straightforward" way.

(into a note: Reasonably straightforward, as interpreted by big tech, currently means non standardized,  finding some specific url hidden somewhere in your account netherworld's setting, selecting which categories you need, the archive format, the data format, the file split size, the file destination, and then waiting up to 24 hours for a link that takes you back to the account settings)

Yet in these account takeouts you can get so much information that is invisible when using OpenID, such as you entire google search history, your whole location history, emails, and your private messages 

## Code integrity and differential privacy<label for="sn-edge-2" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-edge-2" class="margin-toggle">
<span class="sidenote">
The Agent &#10226; edge.
</span>

Lucky for us all this data is locked up in the cool and secure (lapland datacenter) datacenters of the tech giants, with the legal system waiting for a moose to smash into window to sue the companies for privacy violations.

There is little cross-contamination between the datasets, Google knowing your searches, Facebook knowing your friends and amazon knowing what you purchase. The traditional third party processors hold some of that data (Nielsen, Liveramp etc), but no one has the full picture except you.

Personal privacy is fundamental, how free would you be if you knew that your every 

Yet i will explain how all this data would be invaluable for a policymaker. 

(borrowing a concept from differential privacy that )

![Differential privacy utility curve](images/differential-privacy-utility.png)

the green dot being a zero-knowledge proof if you're from the web3 crowd

but how do we ensure that the data is indeed used for policy (not surveillance) and is aggregate? confidentiality ... (commercial cloud oct '22)

(How does this data then become useful?) Let's consider our general relation with ads. Some might go to the extent of Norway and even ban targeted ads (or also https://noyb.eu/en). Your milage may vary but on average very few of the ads we see have anything to do with us.<label for="sn-maggots" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-maggots" class="margin-toggle">
<span class="sidenote">
many reasons why: ... 
</span> Why should they have my data if the targeting is so bad? The same applies with government. why would i give all this data? see next paragraph

## Overlooking Like a State<label for="sn-edge-3" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-edge-3" class="margin-toggle">
<span class="sidenote">
The Agent &rarr; Principal edge.
</span>

In Seeing like a State [Discuss the importance of local decisions and how they often contain nuanced data that central authorities miss. Emphasize that governments have limited capacity for data capture and analysis, reinforcing the value of public participation in data sharing...]

|![Munger hall](images/munger-hall.jpg)|
|:--:| 
| 3D render of the Munger Hall plans |

[bring examples specificifying how takeout data can give a better picture than trad. analyses]

What's important is that not only the policy implemented is scientifically sound, but also that it aligns with the morality of the principal.

<!-- [Democracy basically means government by the people, of the people, for the people...](https://www.youtube.com/watch?v=QFgcqB8-AxE) -->

## Legitimate government<label for="sn-edge-4" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-edge-4" class="margin-toggle">
<span class="sidenote">
The Principal &#10226; edge.
</span>

[important: draw a difference between people that can do some optimal interpolation -> bayesians, vs people that have very biased interpolation -> moralists. morality bad. spectrum of moralisms -> how quickly you can update your beliefs in a bayesian way]

According to Haidt, the public is fundamentally moral: Disconnect in perception of legitimacy → the principal might not have as much data about the global state as the agent, so analyzes choice based on internal value and personality model

Personality and morality -> somewhat stable internal state, hard to change. is also praty genetic, carrying over information from the previous generation.

Like Haidt, i believe pluralism of moralities is generally positive. yet when i first read his book some years ago i was still finding myself thinking "oh that's how i'm gonna convince these dumb (prograssives/coservatives) that my (conservative/prograssive) view is the best!". I'll provide a more abstract analogy to hopefully avoid this for you.

Imagine politics as an optimization problem using gradient descent. the difference with gradient descent is that local knowledge is not unique: you can image of two forces. we can use one person on the left and one on the right as simplification (this side is steeper! no, this side is steeper!).
The set of points is the same (the empirical truth) but both characters have different interpretations for these points using their morality. (give an example)

with democracy we now have millions of these agents and millions of different moralities.
For a government to be perceived as legitimate we have to pick the average of all interpretations of the points. the government could also get lucky and reach the optimum picking one of the curves at random, but that's not the point of democracy.

(Nietzsche, beyond good and evil)

(???) (LLMs, perusasiveness, theory of mind) -> explain to me policy in a way that reflects how my values have been taken into account, as well as the other people. [paper on personality prediction]

# Wrapping up

[little summary]

the reason why I've mentioned the A word (👻 advertising 👻) before is that advertising is central to this. (blended value)

Thanks for reading so far! Send me an email if you wanna help out (get into the eva shinji)

</section>

