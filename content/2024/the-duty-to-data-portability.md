Title: The Duty to Data Portability
Date: 2024-01-14 13:37
Category: ideas
Tags: data cooperatives
Status: Published
Description: Your site is published!

<section markdown="1">

I have just finished reading [The Revolt of the Public](https://press.stripe.com/the-revolt-of-the-public) by Martin Gurri which provides a great analysis of the current sociopolitical climate in the West. I'm a software engineer based in Europe, and with the self-immolation of Germany's energy sector, Putin knocking on the door and the looming possibility of a Trump holding it open for him, <span style="text-decoration: red wavy underline;">I've begun to search my expertise for how to disentangle.</span> 

<label for="sn-aea" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-aea" class="margin-toggle">
<span class="sidenote">Too much complexity, Grug reaching for club</span>

Gurri argues that the public's revolt<label for="sn-gurri" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-gurri" class="margin-toggle">
<span class="sidenote">Arab Spring, Occupy Wall Strett, Tea Party movement, Indignados, Brexit, etc.</span> is not just a rebellion against specific policies or leaders, but a fundamental challenge to the top-down, hierarchical structures of the 20th century. This rebellion is fueled by the information explosion, which has democratized knowledge and destabilized traditional power structures.

While this destabilization has led to chaos in all its major instances, I've anecdotally been experiencing the growing sentiment against nichilism in my day-to-day, prompting for an optimistic vision much like the one at the end of the book.
<span style="text-decoration: red wavy underline;">
I will argue that in the past couple of years a number of crucial innovations have made it possible to nudge the system towards this vision [+ small cultural step needed]
</span>

| ![Intensification 90](images/intensification.png) |
|:--:| 
| Computing center in charge of Интенсификация 90, Gorbachev's plan to fix the communist economy. Source: [Traumazone](https://www.youtube.com/playlist?list=PLSjQL8MYniTTLA3wnZ25U-s6RgR4uJNvL) by Adam Curtis. |

<!-- In The Origins of Political Order, -->

The fundamental structure underlying govenrment and all of its problems is the  principal-agent model, where the public (Principal) hire government offcials (Agent) to [enact policy] to the benefit of the public. The necessity of such a model arises in scenarios of imperfect information, (unlike, for example, in a cryptocurrency).<label for="sn-blockchain" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-blockchain" class="margin-toggle">
<span class="sidenote">
When token prediction models will exterminate humanity and we'll be left with just computers, this model will be no longer needed, and will be more akin to a blockchain, where each actor has perfect information of the world and can be both the agent and the principal. 
</span>

In order for this relationship to be fruitful at scale, Fukuyama identifies 3 pillars of *modern government*: State Capacity, Accountability and Rule of Law. [explain them]

From a purely informatics perspective we can address some aspects of state capacity and accountability, assuming a working underlying rule of law (which westerns states have too much of -> US) and state monopoly over violence (which even worse states have), the most important prerogative according to Friedman. 

If we try to overlay these attributes on our <del>Erlang's concurrency</del> principal-agent model, we obtain a structure like the following: the outgoing edges representing the state's capacity to capture data and enact effective policies with it, the self-edges representing accountability 

![Principal-Agent Fukuyama](images/principal-agent.png)

I'll now go into each edge.

## The Great Data Power Redistribution (GDPR)<label for="sn-edge-1" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-edge-1" class="margin-toggle">
<span class="sidenote">
The Principal &rarr; Agent edge.

</span>

In line with the tradition of thought - from Smith through Hayek into Benkler<label for="sn-tradition" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-tradition" class="margin-toggle">
<span class="sidenote">
The Wealth of Nations, The Use of Knowledge in Society, The Wealth of Networks.
</span> - on the decentralized nature of information and economic systems, I want to suggest my own acronym for GDPR, the Great Data Power Redistribution.

As revolutionary as cookie banners are<label for="sn-cookies" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-cookies" class="margin-toggle">
<span class="sidenote">
It's basically a democratization of cookie clicker
</span>, there's another very important part of the legislation which has gotten little love over the years: the right to data portability.

> The data subject shall have the right to receive the personal data concerning him or her, which he or she has provided to a controller, in a structured, commonly used and machine-readable format and have the right to transmit those data to another controller without hindrance from the controller to which the personal data have been provided[^gdpr]

Of course the article doesn't provide any specific guidance on the implementation so, given the current absence of incentive structures, none of this exists with interoperable standards and any resemblance of a user experience. Yet even in this current state of minimum usability, you can now access the most comprehensive digital model of your identity, from your private Google search history to your Instagram messages.

(some examples about google and facebook data. focus on raw data and possiblity of info for next section)

How do we make sure all of this is used to a good purpose, and most importantnly how is it better than what the government currently does?

## Code integrity and differential privacy<label for="sn-edge-2" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-edge-2" class="margin-toggle">
<span class="sidenote">
The Agent &#10226; edge.
</span>

Lucky for us all this data is locked up in the cool and secure (lapland datacenter) datacenters of the tech giants, with the legal system waiting for a moose to smash into window to sue the companies for privacy violations.

There is little cross-contamination between the datasets, Google knowing your searches, Facebook knowing your friends and amazon knowing what you purchase. The traditional third party processors hold some of that data (Nielsen, Liveramp etc), but no one has the full picture except you.

Personal privacy is fundamental, how free would you be if you knew that your every 

Yet i will explain how all this data would be invaluable for a policymaker. 

(borrowing a concept from differential privacy that was actually created for government)

![Differential privacy utility curve](images/differential-privacy-utility.png)

the green dot being a zero-knowledge proof if you're from the web3 crowd

but how do we ensure that the data is indeed used for policy (not surveillance) and is aggregate? confidentiality ... (commercial cloud oct '22)

(How does this data then become useful?) Let's consider our general relation with ads. Some might go to the extent of Norway and even ban targeted ads (or also https://noyb.eu/en). Your milage may vary but on average very few of the ads we see have anything to do with us.<label for="sn-maggots" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-maggots" class="margin-toggle">
<span class="sidenote">
many reasons why: ... 
</span> Why should they have my data if the targeting is so bad? The same applies with government. why would i give all this data? see next paragraph

## Gross Generalization Like a State<label for="sn-edge-3" class="margin-toggle sidenote-number"></label>
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

## Legitimacy and morality<label for="sn-edge-4" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-edge-4" class="margin-toggle">
<span class="sidenote">
The Principal &#10226; edge.
</span>

[review this part]

[important: draw a difference between people that can do some optimal interpolation -> bayesians, vs people that have very biased interpolation -> moralists. morality bad. spectrum of moralisms -> how quickly you can update your beliefs in a bayesian way]

According to Haidt, the public is fundamentally moral: group selection. Disconnect in perception of legitimacy → the principal might not have as much data about the global state as the agent, so analyzes choice based on internal value and personality model

change this into group selection -> [Personality and morality -> somewhat stable internal state, hard to change. is also praty genetic, carrying over information from the previous generation.]

<!-- Like Haidt, i believe pluralism of moralities is generally positive. yet when i first read his book some years ago i was still finding myself thinking "oh that's how i'm gonna convince these dumb (prograssives/coservatives) that my (conservative/prograssive) view is the best!". I'll provide a more abstract analogy to hopefully avoid this for you. -->

Imagine politics as an optimization problem using gradient descent. the difference with gradient descent is that local knowledge is not unique: you can image of two forces. we can use one person on the left and one on the right as simplification (this side is steeper! no, this side is steeper!).
The set of points is the same (the empirical truth) but both characters have different interpretations for these points using their morality. (give an example)

with democracy we now have millions of these agents and millions of different moralities -> meaning groups, teams.
For a government to be perceived as legitimate we have to pick the average of all interpretations of the points. the government could also get lucky and reach the optimum picking one of the curves at random, but that's not the point of democracy.

(Nietzsche, beyond good and evil)

(???) (LLMs, perusasiveness, theory of mind) -> explain to me policy in a way that reflects how my values have been taken into account, as well as the other people. [paper on personality prediction]

# TLDR

Thanks for reading so far!

[little summary]

the reason why I've mentioned the A word (👻 advertising 👻) before is that advertising is central to this. (blended value)

Send me an email if you wanna help out (get into the eva shinji)

[^gdpr]: https://gdpr-info.eu/art-20-gdpr/

</section>

