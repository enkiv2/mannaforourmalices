
# Notes on endgame:
# ritual takes place near midnight walpurgisnacht, not may day proper
# kuroneko gets ai & the others robes so they can sneak in unnoticed
# shortly before the ritual begins, gunfire is heard. some cultists panic. cult leader tells them to continue, but there's tension whether or not it'll start
# ai & the others sneak into the altar room while kuroneko plays in a magic circle just outside the lodge proper
# she plays over loud gunshots and nearly hits the wrong note a couple times, but finally the first bar is finished and ai smashes the altar
# a sudden wind sweeps through, and parts of the lodge actually are blown off. the yakuza house next door catches fire but it's unclear if that's related.
# kuroneko runs in and says "we need to have a sacrifice, now!"
# options are (all of the unstuck) + "wait"
# all of the options other than aoi & wait end with ai being killed + general bad end
# picking aoi leads to an end where the world is saved but ai "killed aoi twice"/ wracked with guilt
# "wait" leads to kuroneko saying "we don't have any time, we need a sacrifice now"
# followed by a menu that's the same options but "wait" is replaced with "wait let me think"
# "wait let me think" gets a similar response, same menu but "wait" is now "there has to be another way"
# that leads to menu with "magic", "clones", "aliens"
# correct answer is clones; all others lead to killed by ritual blowback + bad end
# clones -> 
# ai "we need to get one of those clones!"
# aoi "you knew?"
# n "but how..."
# same menu again but now the right answer is aliens
# ai "koneko, can you contact the others?"
# koneko "yes, but..."
# ai "tell them i can give them all the headspace they need if they open a portal from here to the basement of the yomipoly biomedical research lab"
# aoi "you knew."
# portal opens
# ai hugs aoi as she goes to the portal
# ai "yes, i knew"
# ai goes into the portal and comes out carrying her clone
# koneko "okay tell them the rest of the deal quick because they're getting impatient"
# ai "tell them to take the drugs from the military facility they trashed and used them on the clones in that basement"
# ai "their hippocampuses"
# kuroneko "hippocami"
# ai "fuck you, hippocampuses. their hippocampuses ae fine but their cerebellums"
# kuroneko "cerebella"
# ai "are underclocked. their memory banks are functional but empty. they're already being used for organ storage so just use their brains too"
# kuroneko "they say okay"
# ai "alright i'm doing this"
# ai "i guess this is the end of my dream of a life full of junk food and heavy drinking with impunity"
# ai stabs her clone
# wind stops, sky clears, jump festival
# note: if halloween yakuza debt arc isn't cleared then gunshots & building on fire don't happen, rather than jump to festival we jump to another bad end where after defeating the ritual everyone goes to the fujinomia house to find their parents dead and more armed yakuza waiting for them

label aoi_bad_end:
    ai "Aoi-chan, could y--"
    "Aoi looked at me tearfully and took the dagger in her hands"
    aoi "Of course."
    "She plunged it into her chest, and with all the stabbing we've been doing it took me a moment to..."
    ai "AOI-CHANNN"
    "Sobs cramped me into a kneel and I gathered her up."
    n "I didn't love you as a woman but"
    ai "I fucking loved you!"
    n "I still"
    ai "I LOVE YOU"
    n "I've made"
    ai "oh fuck oh jesus"
    kuroneko "It wasn't your..."
    kuroneko "You had no choice."
    "I glared at her from behind Aoi's limp form."
    "I held her like a doll to my chest but"
    n "I killed you tw"
    n "I killed you twice i killed you twice ikilledyoutwiceikilledyoutwice"
    scene bg black
    with fade
    scene bg morning
    with fade
    "It's been almost a month."
    scene bg downstairs
    with fade
    "People act like normal. Like she never existed."
    scene bg street
    with fade
    show aoi
    hide aoi
    with fade
    "It's weird. You'd think they'd investigate a somebody holding the corpse of a dead girl with a knife sticking out of her."
    "Nobody mentions her at school or at home. Like they've forgotten."
    show aoi pout
    hide aoi
    with fade
    "Even though I keep seeing her out of the corner of my eye, I'm not sure I remember what she looks like either."
    "On my way to school, there was a man repeatedly walking into a lamppost."
    "I think I can remember what she looks like if I concentrate."
    "I brush past a woman a few years older than me, doing a two-step, shuffling back and forth on the sidewalk. Back and forth, back and forth. Her shirt is halfway tucked into her stockings. A long string of drool hangs from one corner of her mouth."
    "If I could remember what Aoi looked like, maybe I could..."
    "The bright street ahead became dark. Above, a carapace eclipsed the sun on long, long legs."
    $ achievement.grant("Aoi bad end")
    return

label fujinomiya_bad_end:
    scene bg street dark
    "Bruised but giddy, we made our way down the street to the Casa Fujinomiya."
    kuroneko "We deserve to treat ourselves!"
    ai "It's not every night you save the fucking world, that's for fucking sure."
    aoi "I'll make everybody omlettes!"
    "Koneko nodded firmly"
    ai "Ahh, Koneko-chan, you're so earnest!"
    "I put my arm around her and bring her in for a big smooch on the head."
    kuroneko "Wait a second."
    "Everyone slows down, but we're still too giddy to stop."
    "Koneko goes stiff and I remove my arm from her shoulder."
    koneko "The lights are on"
    kuroneko "My parents are never up after midnight. They must have heard us sneak out."
    "Koneko nodded"
    kuroneko "You guys stay here a minute. We'll go in & make sure they just left it on by accident or something."
    kuroneko "We'll text you or wave out the window or something if you need to head home."
    "Kuroneko and Koneko walked into their house, preemptively hanging their heads in case they need to feign guilt."
    ai "Well, I guess it's not so surprising."
    aoi "It's not?"
    ai "That wind literally blew a building apart. The whole town should be awake. It couldn't be worse if we had fire engines blowing through."
    "A cold breeze rustled through the trees and I was thankful that I opted to keep the stolen wool robe."
    aoi "Ai-chan, can I share your robe?"
    "I pulled her close and wrapped one side of the robe around her. She held onto my waist with both hands and shivered."
    ai "What kind of school makes students wear summer uniforms in April? Well, May now, I guess."
    aoi "The kind of school that doesn't give us Golden Week off?"
    ai "Precisely."
    "A beer can slowly rolled down the sidewalk in front of the Fujinomiya house."
    "The can hit a snag inbetween pieces of concrete and made a little epicycle before being blown into the gutter by a sudden gust."
    aoi "It's been a while, hasn't it?"
    ai "It feels like that, yeah."
    "I checked my phone. No messages, and we'd been waiting about five minutes."
    ai "You got any messages?"
    "Aoi shook her head."
    ai "Maybe they're starting the rice or something and got distracted."
    aoi "No fair, that's my job!"
    ai "Let's check. There's no way they wouldn't have signalled to us by now if they were sent to bed."
    "We walked toward the house and stepped over another discarded beer can on the steps."
    "Inside the door were too many shoes."
    "We turned the corner and there was too much blood."
    "Yakuza enforcer" "Looks like we've caught two more little kittens."
    "He lifted his bat."
    scene bg black
    scene bg white
    scene bg black with fade
    # achievement.grant("Fujinomiya bad end")
    return
