Title: The Duty to Data Portability
Date: 2024-01-14 13:37
Category: ideas
Tags: data cooperatives
Status: Published
Description: Your site is published!

<section markdown="1">

I have just finished reading [The Revolt of the Public](https://press.stripe.com/the-revolt-of-the-public) by Martin Gurri which provides a great analysis of the current sociopolitical climate in the West. As an European
\- with the self-immolation of Germany's energy sector, Putin knocking on the door and the looming possibility of a Trump holding it open for him - I've started to feel compelled 

As a software enginner<label for="sn-aea" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-aea" class="margin-toggle">
<span class="sidenote">Self importnat term for Grug brained developer</span> ...  attacking the informational aspects of the problem to ... how Europe can *get its act together*.

| ![Intensification 90](images/intensification.png) |
|:--:| 
| Computing center in charge of Интенсификация 90, Gorbachev's plan to fix the communist economy. Source: [Traumazone](https://www.youtube.com/playlist?list=PLSjQL8MYniTTLA3wnZ25U-s6RgR4uJNvL) by Adam Curtis. |

Gurri argues that the public's revolt - from the Arab Spring and OWS, to Brexit and Trump - is not just a rebellion against specific policies or leaders, but a fundamental challenge to the top-down, hierarchical structures of the 20th century. This rebellion is fueled by the information explosion, which has democratized knowledge and destabilized traditional power structures, but has largely resulted in chaos.

The visual representation of the relationship between public and government I like the most is the principal-agent model,<label for="sn-erlang" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-erlang" class="margin-toggle">
<span class="sidenote">
Possibly for its resambleance to Erlang's concurrecy model.
</span> where the principal (citizens) delegates to the agent (government) the authority to act on their behalf. The problem of this model is that it inherently creates a dynamic where the agent may pursue their own interests rather than those of the principals, leading to issues like moral hazard and conflict of interest, resulting in policies that don't necessarily reflect the public's needs or desires. Yet the necessity for this arises in a situation of information asymmetry, where the agents have access to more detailed information and expertise than the general public.

![Principal-Agent](images/principal-agent.svg)

Throughout history, the asymmetry of information and thus power has always been tilted in favor of the agent, with a few notable events like the printing press, which was at the core of the success of the Protestant Reformation, challenging this imbalance. 

This shift resonates with the tradition of Western thought, as articulated by thinkers like Adam Smith, Friedrich Hayek, and Yochai Benkler, who emphasize the importance of information flow in societal and economic structures<label for="sn-tradition" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-tradition" class="margin-toggle">
<span class="sidenote">
The Wealth of Nations, The Use of Knowledge in Society, The Wealth of Networks.
</span>. These developments have been steadily pushing towards an ideal of perfect information, where all principals are fully informed, obviating the need for agents and thereby transforming power dynamics and decision-making processes. (like in a blockchain)

<!-- In practical terms Doomberg for econ, Lars Doucet for land, Dr. Keefer's for energy. none of these people are govt officials, all have secondary jobs yet. and it's exaclty this diversification that benefits the public and discourages rent-seeking behavior of the agent (self-interest).
-> much like the founding fathers of the us, all had second jobs and were committing to politics for the public good rather than as an mean of itself. Washington was a planter, John Adams was a lawyer, Jefferson. but don't quote me on that -->

| ![Principal-Agent History](images/principal-agent-history.svg) |
|:-:|
| I' not claiming any accuracy on this, sigmoids are pretty. (cit. gaussian) |


What this chart doesn't capture is how effectively this information is made sense of. In contrast to a centralized agent, which operates with a streamlined hierarchical structure, the principal comprises numerous independent agents, each driven by their unique agendas. This is thoroughly analyzed by Buchanan and Tullock in *The Calculus of Consent*: the complexity and cost of achieving consensus escalates with the addition of participants.

![Consent](images/consent.png)

Maybe the chinese are right in thinking that this is an unrealistically hard problem to solve and we should just have moral leaders, and the current devisive state of democracy could very well be descouraging, yet in our case we should argue, like Gurri<label for="sn-optimism" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-optimism" class="margin-toggle">
<span class="sidenote">Who's not a techno-optimist. i think it's just people that have a good work-life balance and a good salary are optimist.
</span>, for the optimistic vision.

This vision, I'll argue, has started to exhibit signs of feasibility, thanks to the latest technological advancements, all supported by a modest and, I hope, more manageable cultural shift in our self-perception.

## The Great Data Powers Redistribution<label for="sn-modernism" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-modernism" class="margin-toggle">
<span class="sidenote">Had to let out my physiological high-modernist needs somewhere.</span>

As revolutionary as cookie banners are,<label for="sn-cookies" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-cookies" class="margin-toggle">
<span class="sidenote">
The democratization of cookie clicker! https://orteil.dashnet.org/cookieclicker/
</span> there's another very important piece of the GDPR which has gotten little love over the years: the right to data portability.

> The data subject shall have the right to receive the personal data concerning him or her, which he or she has provided to a controller, in a structured, commonly used and machine-readable format and have the right to transmit those data to another controller without hindrance from the controller to which the personal data have been provided[^gdpr]

Of course the article<label for="sn-gdpr" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-gdpr" class="margin-toggle">
<span class="sidenote">
 (coming soon to a jurisdicition near you!)</span> doesn't provide any specific guidance on the implementation so, given the current absence of incentive structures, none of this exists with interoperable standards and any resemblance of a user experience. Yet even in this current state of minimum usability, you can now download the most comprehensive digital representation of your identity, from your private Google search history to your Instagram messages and Outlook emails.

Good proxy for what the internal state of the principal might be, now we need to standardize as requirement for coordination.

## Beyond Good & Evil

In The Righteous Mind, Haidt points to the increasing political polarization of the public as the main reason why the public is struggling to coordinate. 

this is due to instict of going around groups, ... a genetic component carrying over information from the previous generation.

[examples of morality from mft book]

there are degrees of polarization, some people left, some people right, and some people in the middle (bayesians) of MFT

![MFT](images/mft.png)

while the exhaustiveness and exclusiveness of the dimensions is an area of acitve research, the fundamental truth is for most humans craving to group behavior is greater than craving for optimality

assuming consensus on information is reached is out of scope (wikipedia collab model, community notes on twitter)

why polarization is bad, post truth:
Imagine politics as an optimization problem using gradient descent. the difference with gradient descent is that local knowledge is not unique: you can image of two forces. we can use one person on the left and one on the right as simplification (this side is steeper! no, this side is steeper!).
The set of points is the same (the empirical truth) but both characters have different interpretations for these points using their morality. (give an example)
with democracy we now have millions of these agents and millions of different moralities -> meaning groups, teams. fuck up bro

| ![Gradient descent](images/gradient-descent.png) |
|:-:|
| A strugglesome gradient descent. Source: Dall-e  |

We need to build an LLM that has average morality: the better it generalizes the better it can persuade.
(LLMs, perusasiveness, theory of mind) -> explain to me policy in a way that reflects how my values have been taken into account, as well as the other people. [paper on personality prediction]

https://arxiv.org/abs/2209.12106

https://r2hcai.github.io/AAAI-23/files/CameraReadys/49.pdf

https://x.com/sama/status/1716972815960961174

This is already a reality with the bigger models. the bigger the model the better it averages [paper]

imagine a system where every principal has a way to access a source of truth for policy, then we have an internal db of all the policies ranked by priority and then we have an llm explain the same set of policies according to my morality/mft. 

This of course runs quickly into resource constraints ... computing power constraints (LLM) + computing power constraits (updating database of policies) ... need for centralization

How can i be freed from the fear of letting myself be persuaded, if other actors control the process?
How can we make sure the process is unbiased and there is not risk of surveillance?

## Accountable government<label for="sn-fukuyama" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-fukuyama" class="margin-toggle">
<span class="sidenote">
From the 3 pillars
</span>

as for advertising, the problem is not whether targeting is accurate, but whether a single actor (like cambridge analytica, although wasn't working) can skew the market -> (either with biased psych model, or with biased policies) -> code integrity

open source llms + confidentiality ... (commercial cloud oct '22) (quickly gloss over sev-snp, hardware collusion and cloud provider corruption)

a system like this poses arguably a bigger psychological privacy threat ->  right now data is locked up and distributed to the cool and secure datacenters around the world, with the legal system waiting for a moose to smash into window to sue the companies in privacy class actions, (note: making a lot of money for the attorneys and very little for the class members). -> Despite efforts by Big Tech to dominate the whole of online activity, there remains a notable separation among their respective datasets: Google has your intents, Facebook your messages and Amazon your items, which are all partial apsects of you. While third-party data processors such as Nielsen and LiveRamp do have access to a wider window into our lives (like household composition and income level), no single entity possesses both a wide and deep view of all the data, except for the individual user themselves.

| ![Lulea Data Center](images/lulea.jpg) |
|:--:| 
| Meta's Luleå Data Center |

we can get even fancier with federation and differential privacy to address The chilling effect if there is a breach or collusion, 

but the fundamental thing is to leverage the rule of law to ensure confidentiality. 

## Privacy

i don't want to disregard privacy but i have a feeling that our clinging onto privacy is another way of displaying group behavior as Haidt says. polarization: complete unsconsciousness about privacy and on the other side complete clinging onto privacy. results in things like norway banning targeted ads, making ads even less useful 

I want to conclude with the definition of privacy:
> From Latin *privatus*: set apart from what is public, personal and belonging to oneself, and **not to the state**. 

https://www.etymonline.com/word/privacy

The romans had a very different hierarchy from what we have today -> the state was much less of a collaborative process, many categories couldnt vote -> i feel like we need to update what privacy means 

going back to the principal-agent concept the further 
 ... grpah used in differential privacy contexts, which still makes sense in this case.

![Privacy utility curve](images/differential-privacy-utility.png)

the more you slide back on the curve away from the blue point, the more you're going back down the sigmoid.



<!-- Personal privacy is of course fundamental. While the ideal state might be the aforementioned blockchain-like society, where perfect information is available, we must consider the realities of our human psychology. The chilling effect (from knowing that someone could have access ot all this data at one time) occurs when individuals hesitate to search for information or express opinions online due to fear of future repercussions. This not only compromises personal freedom but also hinders creativity, innovation, and the free flow of ideas, which are crucial for a thriving and progressive society. -> this is arguably a bigger problem than surveillance in a lwful society -->

<!-- (How does this data then become useful? Ok, everything is confidential and all but still there's a risk and i'm willing to expose myself only if there's a benefit) Let's draw a parallel with ads. Some people are ok with ads, they find some interesting things and are willing to buy them, for some people ads are completely useless and they've never clicked on one (apparently all the norwegians). Your milage may vary but on average very few of the ads we see have anything to do with us. Why should they have my data if the targeting is so bad? The same applies with government. why would i give all this data? see next paragraph -->


# Wrapping up

**TLDR**: Fight for open source and fight for data rights.

crypto has been getting a lot of - well deserved - hate -> but still on the basis there's game theory and society -> an attempt to reconcile society and tech, usually shielded by the massive salaries

*Get into the elliptic curve Shinji* Closing themre https://youtu.be/qIZL5qeEKj0

[^gdpr]: https://gdpr-info.eu/art-20-gdpr/

</section>

