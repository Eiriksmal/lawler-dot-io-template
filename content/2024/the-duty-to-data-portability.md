Title: The Duty to Data Portability
Date: 2024-01-14 13:37
Category: ideas
Tags: data cooperatives
Status: Published
Description: Your site is published!

<section markdown="1">

I have just finished reading [The Revolt of the Public](https://press.stripe.com/the-revolt-of-the-public) by Martin Gurri which provides a great analysis of the current sociopolitical climate in the West. I'm a software engineer in Paris<label for="sn-aea" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-aea" class="margin-toggle">
<span class="sidenote">Développeur du cerveau Grug, in French</span>
and - with the self-immolation of Germany's energy sector, Putin knocking on the door and the looming possibility of a Trump holding it open for him - I've started to feel compelled by the informational foundations of the problem to think how Europe can *get its act together*.

Gurri argues that the public's revolt - from the Arab Spring and OWS, to Brexit and Trump - is not just a rebellion against specific policies or leaders, but a fundamental challenge to the top-down, hierarchical structures of the 20th century. This rebellion is fueled by the information explosion, which has democratized knowledge and destabilized traditional power structures.

| ![Intensification 90](images/intensification.png) |
|:--:| 
| Computing center in charge of Интенсификация 90, Gorbachev's plan to fix the communist economy. Source: [Traumazone](https://www.youtube.com/playlist?list=PLSjQL8MYniTTLA3wnZ25U-s6RgR4uJNvL) by Adam Curtis. |


The visual representation of the relationship between public and government I like the most is the principal-agent model, where the public delegates to the agent the ... to act in the behalf of them.<label for="sn-erlang" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-erlang" class="margin-toggle">
<span class="sidenote">
Possibly for its resambleance to Erlang's concurrecy model.
</span>
The problem of this model ...
Yet the necessity for this arises in a situation of information asymmetry, ...

![Principal-Agent](images/principal-agent.svg)

Throughout history the asymmetry of information and thus power has always been tilted in favor of the agent, with a few notable events like the printing press which was at the core of the sucess of the Protenstant reform ... (tradition of thought, smith, hayek etc) ... culminating in a state of perfect information, where all principals have perfect information about the world and there is no need for agents.

In practical terms Doomberg for econ, Lars Doucet for land, Dr. Keefer's for energy. none of these people are govt officials, all have secondary jobs yet. and it's exaclty this diversification that benefits the public and discourages rent-seeking behavior of the agent (self-interest)

<!-- Borrowing from the tradition of thought - from Smith through Hayek into Benkler<label for="sn-tradition" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-tradition" class="margin-toggle">
<span class="sidenote">
The Wealth of Nations, The Use of Knowledge in Society, The Wealth of Networks.
</span> - on the decentralized nature of information and economic systems, and the flashiness of high modernist names, I want to suggest a new acronym for GDPR, the Great Data Power Redistribution. -->

| ![Principal-Agent History](images/principal-agent-history.svg) |
|:-:|
| I' not claiming any accuracy on this, sigmoids are pretty. (cit. gaussian) |

how the consensus on information is reached is out of scope (wikipedia collab model, community notes on twitter)

what this model doesnt capture is how effectively this information is used to enact policy. the advantage of the agent is that it's a small hierarchy, while the principal is many independent actors with different self interests etc.

![Consent](images/consent.png)


While this destabilization has led to chaos in all its major instances, I've anecdotally been experiencing a growing general sentiment against nichilism, prompting for an optimistic vision much like the one at the end of the book... few major technological changes that are starting to make this COORDINATION possible. 

I'll try to avoid modernist takes and grandeurs. 

## The Great Data Powers Redistribution (GDPR)

As revolutionary as cookie banners are<label for="sn-cookies" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-cookies" class="margin-toggle">
<span class="sidenote">
The democratization of cookie clicker! https://orteil.dashnet.org/cookieclicker/
</span>, there's another very important part of the GDPR legislation which has gotten little love over the years: the right to data portability. (coming soon to a jurisdicition near you!)

> The data subject shall have the right to receive the personal data concerning him or her, which he or she has provided to a controller, in a structured, commonly used and machine-readable format and have the right to transmit those data to another controller without hindrance from the controller to which the personal data have been provided[^gdpr]

Of course the article doesn't provide any specific guidance on the implementation so, given the current absence of incentive structures, none of this exists with interoperable standards and any resemblance of a user experience. Yet even in this current state of minimum usability, you can now download the most comprehensive digital representation of your identity, from your Google search history to your private Instagram messages.

This data is a the most comprehensive representation of the internal state of the principal, now we need to standardize as requirement for coordination.

<!-- How do we make sure all of this is used to a good purpose, and most importantnly how is it better than what the government currently does analytics? -->


## Beyond Good & Evil<label for="sn-edge-4" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-edge-4" class="margin-toggle">
<span class="sidenote">
The Principal &#10226; edge.
</span>

[important: draw a difference between people that can do some optimal interpolation -> bayesians, vs people that have very biased interpolation -> moralists. morality bad. spectrum of moralisms -> how quickly you can update your beliefs in a bayesian way]

According to Haidt, the public is fundamentally moral: group selection. Disconnect in perception of legitimacy → the principal might not have as much data about the global state as the agent, so analyzes choice based on internal value and personality model

while the exhaustiveness and exclusiveness of the dimensions is an area of acitve research, the fundamental truth is group behavior.

change this into group selection -> [Personality and morality -> somewhat stable internal state, hard to change. is also praty genetic, carrying over information from the previous generation.]

<!-- Like Haidt, i believe pluralism of moralities is generally positive. yet when i first read his book some years ago i was still finding myself thinking "oh that's how i'm gonna convince these dumb (prograssives/coservatives) that my (conservative/prograssive) view is the best!". I'll provide a more abstract analogy to hopefully avoid this for you. -->

![MFT](images/mft.png)


Imagine politics as an optimization problem using gradient descent. the difference with gradient descent is that local knowledge is not unique: you can image of two forces. we can use one person on the left and one on the right as simplification (this side is steeper! no, this side is steeper!).
The set of points is the same (the empirical truth) but both characters have different interpretations for these points using their morality. (give an example)

with democracy we now have millions of these agents and millions of different moralities -> meaning groups, teams.
For a government to be perceived as legitimate we have to pick the average of all interpretations of the points. the government could also get lucky and reach the optimum picking one of the curves at random, but that's not the point of democracy.

<!-- ![Beyond good and evil](images/nietzsche.jpg)  -->

(???) (LLMs, perusasiveness, theory of mind) -> explain to me policy in a way that reflects how my values have been taken into account, as well as the other people. [paper on personality prediction]

the solution to tribalism is showing how there's nothing unique to tribalism with an llm

## Code integrity and differential privacy<label for="sn-edge-2" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-edge-2" class="margin-toggle">
<span class="sidenote">
The Agent &#10226; edge.
</span>

As much as /r/LocalLLAMA would like us to to believe, if i know there's a better LLM out there, i'll use that one even if it's hosted -> computing power constraints (LLM) + computing power constraits (updating database of policies) -> private targetign 

Lucky for us all this data is locked up and distributed to the cool and secure datacenters around the world, with the legal system waiting for a moose to smash into window to sue the companies for privacy violations.

| ![Lulea Data Center](images/lulea.jpg) |
|:--:| 
| Meta's Luleå Data Center |

Despite efforts by Big Tech to dominate the whole of online activity, there remains a notable separation among their respective datasets: Google has your intents, Facebook your messages and Amazon your items, which are all partial apsects of you. While third-party data processors such as Nielsen and LiveRamp do have access to a wider window into our lives (like household composition and income level), no single entity possesses both a wide and deep view of all the data, except for the individual user themselves.

Personal privacy is of course fundamental. While the ideal state might be the aforementioned blockchain-like society, where perfect information is available, we must consider the realities of our human psychology. The chilling effect occurs when individuals hesitate to search for information or express opinions online due to fear of future repercussions. This not only compromises personal freedom but also hinders creativity, innovation, and the free flow of ideas, which are crucial for a thriving and progressive society.

Yet there's a tradeoff as described by the concept of differential privacy, which ironically enough was first applied by the U.S. Census Bureau. In order for data to be useful and draw predictions from it, we need it in aggregate (also equivalence of aggregation with NNs): [explain quickly]
research has shown that there are many ways to produce very accurate statistics from the database while still ensuring high levels of privacy.[1] 

![Differential privacy utility curve](images/differential-privacy-utility.png)

How do we trust the government to use these demonstrably private alogs and not surveillance? 

confidentiality ... (commercial cloud oct '22) (quickly gloss over sev-snp, hardware collusion and cloud provider corruption)

(How does this data then become useful? Ok, everything is confidential and all but still there's a risk and i'm willing to expose myself only if there's a benefit) Let's draw a parallel with ads. Some people are ok with ads, they find some interesting things and are willing to buy them, for some people ads are completely useless and they've never clicked on one (apparently all the norwegians). Your milage may vary but on average very few of the ads we see have anything to do with us. Why should they have my data if the targeting is so bad? The same applies with government. why would i give all this data? see next paragraph

(maybe add the bit on game theory from EnclaveID market analysis doc)


# Wrapping up

TLDR: Fight for Open-Source, fight for your data rights and fight for your privacy.

[little summary]

the reason i've been talking about ads it's because it's important to do have a diversified income to discourage rent seeking

i've been working around this stuff for years and i'll do for the foreseeable future (opportunity for blended value craetion)

Thanks for reading! 

[^gdpr]: https://gdpr-info.eu/art-20-gdpr/

</section>

