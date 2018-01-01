label ritual:
    "As planned, Kuroneko met us in the convenience store bathroom with dark woolen robes. We put them on and then waited until a crowd of similarly-robed cultists walked past."
    "We hovered in the back, near the lodge's service door, as the cultists formed a rough ring around the magic circle and Kuroneko took her place in the center."
    if debt_erased:
        "Muffled gunshots were audible. The cultists began to break rank."
        "Father Nikolai" "Stay in the circle!"
        "Cultist" "But Father, the gangsters--"
        "Father Nikolai" "So long as you continue the ritual, even if you perish, your soul shall persist in space and be ressurrected infinitely. If the ritual fails, your soul shall be forfeit!"
        "More shots rang out, clearer now."
    "Fother Nikolai" "Begin the chant."
    "Kuroneko readied her violin and began playing."
    "Cultists" "I call you to life, oh mysterious forces!"
    if debt_erased:
        "More shots rang out, and a note was cut off too sharply. She regained her tempo."
    "Cultists" "Drowned in the obscure depths"
    "Cultists" "Of the creative spirit, timid"
    "The wind picked up, sending dried leaves and bits of grass into slow waltzes"
    if debt_erased:
        "Smoke began to fill the air."
    "Cultists" "Shadows of life, to you I bring audacity!"
    ai "That's the cue -- the end of the first stanza."
    "I ducked into the lodge and grabbed the knife from the altar. It felt heavy, like it had its own inertia."
    "I smashed it against the Janus statue, and the choking claustrophobic feeling, that staleness in the air that had creeped up on me slowly, instantly disappated."
    "The merry little dances of the airborne grasses became manic spins, and gusts like huge fists shoved cultists down or sent them up."
    "Kuroneko ducked into the lodge. The dagger was still squirming against my hand."
    kuroneko "Sacrifice! Now!"
    ai "Wait, I didn't plan that far a--"
    kuroneko "I thought we'd have more time, but something's angry out there."
    "A large piece of roofing tore off the building and whipped around back through the far window, landing neatly beside me. The dagger seemed attracted to it."
    if debt_erased:
        "Through the now-empty windowframe, I saw flames flickering in a nearby building"
    kuroneko "SACRIFICE. NOW."
    menu:
        "Aoi" if aoi_unstuck_in_time:
            jump aoi_bad_end
        "Kuroneko" if kuroneko_unstuck_in_time:
            jump sacrifice_kuroneko
        "Koneko" if koneko_unstuck_in_time:
            jump sacrifice_koneko
        "Wait":
            ai "Wait, hold on a se--"
            kuroneko "WE. DON'T. HAVE. TIME."
            jump sacrifice_now
label sacrifice_now:
    menu:
        "Sacrifice Aoi" if aoi_unstuck_in_time:
            jump aoi_bad_end
        "Sacrifice Kuroneko" if kuroneko_unstuck_in_time:
            jump sacrifice_kuroneko
        "Sacrifice Koneko" if koneko_unstuck_in_time:
            jump sacrifice_koneko
        "Hold on, let me thi--":
            kuroneko "NO TIME. SACRIFICE NOW."
            jump sacrifice_now_2
label sacrifice_now_2:
    menu:
        "Aoi":
            jump aoi_bad_end
        "Kuroneko":
            jump sacrifice_kuroneko
        "Koneko":
            jump sacrifice_koneko
        "there must be another way":
            jump another_way
label another_way:
    menu:
        "Oh fuck oh fuck oh fuck":
            jump sacrifice_now
        "Think, damnit":
            jump think_damnit
label think_damnit:
    n "OK, three things, three random-ass things"
    n "Things I know about in this fucking town and if they can hurt us maybe they can save us too"
    menu:
        "magic":
            n "Maybe we can use magic to... Fuck..."
            n "Whatever is out there has us way out-gunned in terms of magic."
            jump sacrifice_now
        "clones":
            jump endgame_clones
        "aliens":
            n "Maybe if Koneko-chan can call the aliens we can sacrific---"
            n "No way. I saw those things take out an entire heavily-armed military base. I can't stab it with a knife."
            jump sacrifice_now
        "ohfuckohfuckohfuck":
            jump sacrifice_now

label endgame_clones:
    ai "I know what we need to do! We need to get one of those clones."
    aoi "Ai-chan, you knew?"
    n "but how..."
    menu:
        "magic":
            n "Maybe we can use magic to... Fuck..."
            n "Whatever is out there has us way out-gunned in terms of magic."
            jump sacrifice_now
        "clones":
            n "We can't use clones if we don't have them. Shit."
            jump sacrifice_now
        "aliens":
            n "Maybe if Koneko-chan can call the aliens we can sacrific---"
            n "No way. I saw those things take out an entire heavily-armed military base. I can't stab it with a knife."
            n "Wait, I've got it!"
            jump endgame_aliens
        "ohfuckohfuckohfuck":
            jump sacrifice_now
label endgame_aliens:
    ai "koneko, can you contact the others?"
    koneko "yes, but..."
    ai "tell them i can give them all the headspace they need if they open a portal from here to the basement of the yomipoly biomedical research lab"
    aoi "you knew."
    portal opens
    ai hugs aoi as she goes to the portal
    ai "yes, i knew"
    ai goes into the portal and comes out carrying her clone
    koneko "okay tell them the rest of the deal quick because they're getting impatient"
    ai "tell them to take the drugs from the military facility they trashed and used them on the clones in that basement"
    ai "their hippocampuses"
    kuroneko "hippocami"
    ai "fuck you, hippocampuses. their hippocampuses ae fine but their cerebellums"
    kuroneko "cerebella"
    ai "are underclocked. their memory banks are functional but empty. they're already being used for organ storage so just use their brains too"
    kuroneko "they say okay"
    ai "alright i'm doing this"
    ai "i guess this is the end of my dream of a life full of junk food and heavy drinking with impunity"
    "I steady the knife and try not to look at the uncomprehending eyes of my doppelganger as I sink the blade into her neck."
    "The wind clears and the cloud cover disappates."
    ai "I guess that's that, then."
    ai "I need to wash my hands."
    if debt_erased:
        jump festival
    jump fujinomiya_bad_end

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
    scene bg fujinomiya household dark
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
