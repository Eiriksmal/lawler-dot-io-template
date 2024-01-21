Title: The Duty to Data Portability
Date: 2024-01-14 13:37
Category: ideas
Tags: data cooperatives
Status: Published
Description: Your site is published!

<section markdown="1">

**DRAFT**

I have just finished reading [The Revolt of the Public](https://press.stripe.com/the-revolt-of-the-public) by Martin Gurri which provides a great analysis of the current sociopolitical climate in the West. I'm a software engineer based in Europe and
\- with the self-immolation of Germany's energy sector, Putin knocking on the door and the looming possibility of a Trump holding it open for him - I've started to think about how to disentangle<label for="sn-aea" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-aea" class="margin-toggle">
<span class="sidenote">Too much complexity, Grug reaching for club.</span> the informational apsects of the argument and help Europe *get its act together*.


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


What this chart doesn't capture is how effectively this information is effectively acted upon. In contrast to a centralized agent, which operates with a streamlined hierarchical structure, the democratic principal comprises numerous independent agents, each driven by their unique self-interests and complex psychologies. This is thoroughly analyzed by Buchanan and Tullock in *The Calculus of Consent*: the complexity and cost of achieving consensus escalates with the addition of participants.

![Consent](images/consent.png)

Maybe the chinese are right in thinking that this is an unrealistically hard problem to solve and we should just have moral leaders, and the current devisive state of democracy could very well be descouraging, yet in our fundamentally democratic societies we should be biased, like Gurri<label for="sn-optimism" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-optimism" class="margin-toggle">
<span class="sidenote">Who's not a techno-optimist. i think it's just people that have a good work-life balance and a good salary are optimist.
</span>, for the optimistic vision.

This vision, I'll argue, has started to exhibit signs of feasibility, thanks to the latest technological advancements, only requiring the support of a modest and, I hope, more manageable cultural shift in our relationship with personal data.

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
 (coming soon to a jurisdicition near you!)</span> doesn't provide any specific guidance on the implementation so, given the current absence of incentive structures, none of this exists with interoperable standards and any resemblance of a user experience. 
 
Yet, for the first point in time, you now have a legal right to demand the most comprehensive digital representation of your identity, from your private Google search history to your Instagram messages and Outlook emails. All this data, collected passively and thus unbiased over the years, is the best proxy to pinpoint the underlying state of the principals.

![Beyond good and evil](images/nietzsche.jpg)

In "The Righteous Mind," Jonathan Haidt highlights the escalating political polarization as a primary barrier to public coordination. This theory suggests that our polarization is influenced by various psychological foundations, such as care/harm, fairness/cheating, loyalty/betrayal, authority/subversion, and sanctity/degradation, bucketing the population into groups that are more influenced by one or the other.

While the exhaustiveness and exclusiveness of the dimensions is an area of acitve research, the fundamental truth is for most humans craving to group behavior is greater than craving for optimality, possibly form genetic roots that transmit predispositions from previous generations in a low-information world.

These differences in moral foundations contribute to varying degrees of polarization. Some individuals lean towards the left, emphasizing care and fairness, while others lean towards the right, valuing loyalty, authority, and sanctity. Then there are those in the middle who are less prone to being influenced by the moral foundations and are less likely to adhere strictly to a single political ideology. 

![MFT](images/mft.png)

If we set aside the aspect of how consensus on "ground truth" is achieved, considering we already have successful examples like the Wikipedia collaboration model and community notes on Twitter or centralized entities like Our World in Data, we can then draw a parallel between political polarization and the concept of gradient descent.

Unlike in gradient descent, where local knowledge (the shape of the surface) is unique, in politics it's distorted due to morality. For simplicity, consider one person on the left and another on the right debating which side of an issue is more 'steep' or pressing. Both are interpreting the same empirical truths but through lenses colored by their moral values.

| ![Gradient descent](images/gradient-descent.png) |
|:-:|
| A strugglesome gradient descent. Source: Dall-e  |

Consider a the average debate on healthcare funding. The individual on the left might argue that increasing funding is crucial for fairness and care, emphasizing the moral duty to support vulnerable populations. In contrast, the right-leaning individual might argue for reduced funding, stressing fiscal responsibility and the sanctity of free-market principles.

Large Language Models (LLMs) like GPT-4 offer a transformative approach to resolving this type of moral stalemates in policy debates. These models have proven able in understanding and integrating a spectrum of moral perspectives[^mft-paper-1][^mft-paper-2], as well as generating explanations and arguments that resonate more profoundly with diverse audiences, acknowledging and valuing their distinct moral frameworks.

| ![Persuasion](images/persuasion.png) |
|:-:|
| Eager to witness these strange outcomes. [Source](https://x.com/sama/status/1716972815960961174) |

<!-- imagine a system where every principal has a way to access a source of truth for policy, then we have an internal db of all the policies ranked by priority and then we have an llm explain the same set of policies according to my morality/mft.  -->

Imagine a system where each stakeholder is proposed policies that are relevant to his moral foundations, as well as tailored explanations crafted to their moral framework. Just as targeted ads are more effective because they are based on the consumer's own interests and online behavior, policy explanations generated by LLMs are likely to be more effective and less divisive when they are based on an understanding of the audience's moral perspectives. The major advantage of this being that the same policy can be reinterpreted in a way that satisfies all groups.

| ![LLM morality](images/llm-morality.png) |
|:-:|
| An example of Mixtral persuading someone for a policy that goes against their moral foundations. |

As much as people over at /r/Locallama would like us to believe otherwise, when it's about morality, anything short of the biggest and the most resource intesive model would be inadequate to the task of self-persuasion. Such a system will necessarily end up being centralized if we want it to be practical, bringing forward once again the problem of self-interest of whoever controls the infrastructure.

## Accountable government<label for="sn-fukuyama" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-fukuyama" class="margin-toggle">
<span class="sidenote">
One of the three pillars of modern government according to Fukuyama, along State Capacity and Rule of Law.
</span>

Again drawing an analogy from advertising, the primary concern is whether a single participant can disrupt the advertising market, either by colluding with the platform to bias the targeting algorithm to show their ads over others or the platform itself implementing some kind of agenda in their targeting algorithm. In our situation these two directly map to the LLM used for persuasion and the policy matching algorithm.

This is where open-source becomes fundamental. An LLM which training and output is provably unbiased can be coupled with confidential computing, only recently available on Azure since October '22. Each actor can verify that the code running inside a remote VM is loading exactly that LLM, the data in transit is encrypted, and is fairly matching tailored policies and explainations to the user profile.

Yet, even with this kind of integrity constraints in place, a system like this poses arguably a bigger psychological threat in case anything goes wrong, as one actor can use this powerful representation of identity for surveillance and coercion, also known as "The chilling effect". This not only compromises personal freedom but also hinders creativity, innovation, and the free flow of ideas, which are crucial for a thriving and progressive society.

| ![Lulea Data Center](images/lulea.jpg) |
|:--:| 
| Meta's Luleå Data Center |


Right now everyone's personal data is locked up and distributed to the cool and secure datacenters around the world, with the legal system waiting for a moose to smash into window to sue the controllers in privacy class actions.<label for="sn-classaction" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-classaction" class="margin-toggle">
<span class="sidenote">
Making a lot of money for the attorneys and very little for the class members.
</span>

Despite Big Tech's attempts to monopolize online activities, their databases remain distinct: Google knows your search intentions, Facebook your communications, and Amazon your shopping habits; and none of these are shared with each other to preserve their competitive edge. While thir-party data providers like Nielsen and LiveRamp do have insights into broader aspects of our lives, such as family makeup and income, no single organization has both a wide and in-depth understanding of our digtal selves, except for the user.

Confidential environments can be rearranged to reflect the same type of organization, also potentially incorporating fancier techniques like federated learning and differential privacy, but the fundamental legal aspect remains. Our society is permeated in a strong - at times too strong - and reasonably decentralized judicial system, which is ready to spring into action where technical guardrails fall short.

## Privacy

I'm not advocating for ignoring privacy concerns, but I suspect our strong emphasis on privacy might reflect a form of group behavior, as described by Jonathan Haidt. This situation creates a polarization: on one end, there's a complete lack of concern for privacy, while on the other, there's an intense insistence on it. Such extremes can lead to consequences like Norway's ban on targeted ads, or the media outrage over Cambridge Analytica.<label for="sn-cambridge" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-cambridge" class="margin-toggle">
<span class="sidenote">
Whose effectiveness was oversold by his employees and overblown by the journalists.
</span>


I want to conclude with the etymology of privacy[^privacy]:
> From Latin *privatus*: set apart from what is public, personal and belonging to oneself, and **not to the state**. 


Despite the parvence of an electoral process in the roman republic, the state was hardly about collaborative governance, with the majority of the population excluded from voting. Given these historical differences, it seems appropriate to reconsider and update our understanding of what privacy means in the modern context, where the relationship between the individual and the state is far more collaborative and inclusive.

![Privacy utility curve](images/differential-privacy-utility.png)

The image above is borrowed from differential privacy explainations, yet it generalizes to how we should percieve our relation with out personal data. The further we go leftwards from the blue dot, the further we go backwards on the principal-agent sigmoid of before, indirectly jutifying the centralization of power to our elites.

# Wrapping up

Despite the justified criticism levied against crypto and the web3 crowd, it's essential to acknowledge in its foundations an ambitious effort to mend the widening rift between technology and society, often deepened by the tech industry's hefty salaries.

This essay strives to mirror that reconciliation, and possibly make you reason about your tech work in terms of duties to the society of Homo Informaticus.

*Get into the prime field Shinji*<label for="sn-nge" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-nge" class="margin-toggle">
<span class="sidenote">
[Closing theme](https://youtu.be/qIZL5qeEKj0)</span> 

[^gdpr]: https://gdpr-info.eu/art-20-gdpr/
[^privacy]: https://www.etymonline.com/word/privacy

[^mft-paper-1]: https://arxiv.org/abs/2209.12106
[^mft-paper-2]: https://r2hcai.github.io/AAAI-23/files/CameraReadys/49.pdf


</section>

