# Am I The AI
This is a reddit bot that responds to r/aita with an AI-based answer.

## Status
The bot got perma-banned from the r/aita within 12 hours of launch.

I didn't try to hide the fact that the user was an AI, and it appears that one of the comments was reported to the r/aita moderators specifically because it was AI-generated. At the time of this writing, the extensive list of rules for that subreddit do not explicitly disallow AI comments. However I was told that they have a no AI rule. I politely requested the moderators add that to the list of rules.

## Observations 
When given the choice, the LLM tended to take the middle ground. This middle ground was not well-received by the community - most of these neutral responses were downvoted, sometimes heavily.

When only given the choice of NTA or YTA, it always chose NTA even when any reasonable person would have said YTA. The LLM seems unwilling to call the user out on bad behavior.

## Examples

### Neutral

**Post**

```
AITA for refusing to cook for my adult daughter because she is too picky and doesn't appreciate my cooking?

I (53M) love to cook. There will be days where I slave away in the kitchen all day to make a big meal, and I will do it happily. My wife (50F) can cook when I'm not around but honestly I can't think of any time when she has made anything because I always want to do it, and that's fine by me as long as I feel appreciated for it.

I have a 24 yo son Eric, my wife has a 19 yo daughter Liz from previous marriages and we have a 15 yo son David together. Eric lives with us for now to save up money while he works but still pays rent. He will eat literally anything with the exception of hating blue cheese. David likes pretty much everything but is allergic to eggs. I can work around these constraints pretty easily when I cook.

Liz is a different story. She has always been kind of picky with the foods she dislikes but it has gotten way worse. She went to college for a semester and then dropped out so now she is living at home, and while she was away, she developed some terrible pickiness. she has had stints of being a vegan, being vegetarian, being grain-free, pasta-free, oil-free, etc. but she isn't consistent about it. I try to help meet her needs but on any given day, she has something new to complain about with a food I want to cook. Sometimes she and I will debate for hours about what to make with me basically saying tell me what you want for dinner that will work for you and I will cook it, so long as it meets the other kids' restrictions, and she is so unhelpful with this.

Two nights ago, I cooked a dish that Liz told me looked good in a book. We all sat down for dinner and everybody loved it except Liz. She complained that she didn't realize there were peanuts in the recipe, and peanuts are so unhealthy for us so she doesn't think she can eat it and can I make her something else. I was fed up and told her "no, you can eat this or you will eat nothing. I am done having to deal with your pickiness and criticism of my cooking. I will no longer be taking any of your feedback on what you want for dinner and will be cooking what everybody else wants. You can either eat that or cook yourself something else." She started crying and said that I take the other kids' restrictions on what to eat so why can't I do the same for her. I reminded her that Eric only dislikes a single thing that I don't care for either so there's no risk of it popping into a dish, and if David has eggs he will probably die, so it's not the same as her vetoing every single thing I want to make. My wife took her side and said that I am being too sensitive and mean because Liz is not my real daughter and I am showing favoritism (this is bullshit by the way). I told my wife that she can cook Liz meals if she wants (as if) but I'm not going out of my way to meet her needs. AITA?
```

**Response**

```
am_i_the_ai
-15 points

NAH, but it might be beneficial for everyone involved to have open communication and compromise. It seems that there are valid concerns on both sides, and finding a middle ground may help maintain harmony in your household. It might be helpful to consider setting aside certain nights for specific dietary needs or preferences, or even involving your daughter in meal planning and preparation to ensure her input is taken into consideration without undue stress on you. Additionally, it may be worth exploring why your daughter has developed such stringent dietary restrictions, as there may be underlying health or emotional concerns that can be addressed through discussion and understanding.
```

### NTA

**Post**
```
AITA for not letting my daughter go to a concert alone

Reposted with more info

I have a 16 year old daughter and a 24 year old daughter

My 16 year old daughter wants to go to a concert 4 hours away where she'll have to stay a night alone and will come back the next day I asked her if there would be any parent or adult with them and she said no I told her she couldn't go as I had to go to a freinds wedding on the same day.

She started to get upset and cry and said that all her freinds are going and promised she'll be good.

I told her I didn't want her going for several reasons

    She only got her licence a week ago and I feel she's too inexperienced for such a ride.

    They are planning to leave at 3:30pm and will arrive at 7-8pm meaning a good part of the journey will be in the dark.

    Its snowy and cold outside and it's dangerous for anyone especially an inexperienced 16 year old to drive so far.

    I feel uncomfortable letting her stay in a hotel with no adult supervision.

She got upset and said it's unfair that I let my oldest go to europe last year when she was 23 but won't let her drive for a few hours I told her I let her go because she's an adult and she paid for it herself. I told her when she becomes 18 she can do whatever she wants.

She says it's unfair as all her freinds are going alone and she'll be fine.

I called my oldest and asked if she could take her sister to the concert she agreed and I thought the problem was solved but my daughter was still angry and called us overprotective perks.

AITA?
```

**Response**
```
am_i_the_ai
2 points

NTA (Not The Asshole)

As a parent, it's your responsibility to ensure your child's safety, especially when they are still inexperienced drivers. The long journey, late hours, and potential dangerous weather conditions are valid concerns that warrant your decision. Additionally, letting your daughter stay in a hotel alone at such a young age, despite her friends being there, is also a reasonable concern due to the potential risks and your discomfort with the situation. Your decision to let your older daughter go to Europe when she was an adult and financially independent is also reasonable, as it's a different situation. Your concerns for your younger daughter's safety and well-being are not overprotective, but rather responsible and loving actions.
```

## Installation
This package depends on llamacpp python. I build using cuBLAS (NVidia CUDA basic linear algebra subroutines) to enable NVidia GPU acceleration.

So before running pip to install everything, make sure your llamacpp build settings are configured. I use these:

```bash
export CMAKE_ARGS=-DLLAMA_CUBLAS=on
export FORCE_CMAKE=1
export CUDA_HOME=/usr/local/cuda
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64 # Note: the CUPTI/lib64 seems old, not found on my machine but this shouldn't hurt
export PATH=$PATH:$CUDA_HOME/bin
```

If you want to run this and scrape/post to reddit, you need to configure your account credentials in praw.ini.
