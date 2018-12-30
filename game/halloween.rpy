# This is the primary file for the section of the game that occurs on Halloween of 2011
label halloween:
    $ achievement.grant("Niaga praw emit eht od s'tel") # Warped to Halloween 2011 
    play music "music/Infocalypse_-_vapor_intrusion.mp3"
    scene bg morning
    play sound "sfx/alarm-clock.wav"
    "Alarm clock" "Ring Ring Ring Ring"
    n "Ughhhhh"
    "Alarm clock" "Ring Ring Ring Ring"
    n "What the hell happened last night?"
    "Alarm clock" "Ring Ring Ring Ring"
    n "I shouldn't be so goddamned tired"
    "Alarm clock" "BiBiBiBiBiBi"
    if died:
        n "Was it all a dream? I distinctly remem..."
        extend "{b}Hey! What the fuck?{/b}"
        extend "Wow, I must still be dr--"
        extend "{b}Why is there a voice in my hea--{/b}"
        if num_deaths > 1:
            # TODO: add more variation to this section, based on flags
            extend "This is going to be hard to ex--"
            extend "{b}I'm going crazy, aren't I?{/b}"
            extend " Look, shut the fuck up a minute. "
            extend "{b}You want me to shut up? It's my fucking head.{/b}"
            extend " Shut up and listen."
            n "OK. Look, I'm you. It's a long story, but I'm you from the future."
            extend "\n{b}I'm listening.{/b}"
            n "I keep dying. And, whenever I die, I end up back here, now, as a voice in my past self's head."
            n "OK?"
            extend "\n{b}...{/b}"
            extend "{b} I guess that isn't any less acceptable than the alternative.{/b}"
            n "OK. You're going to have to trust me and take my advice if you want to eventually not die."
            extend "\n{b}You've lost me there. I'm supposed to obey a voice in my head? If you're me, then you know exactly how unimpressed I am by that suggestion.{/b}"
            n "I'll do what I can to explain the situation. But, if you don't trust me at least a little we'll be stuck in this loop forever."
            n "{b}OK. For now, I'll accept your story. But, if you start telling me to do anything crazy...{/b}"
        else:
            extend "The fuck is going on?! I died and now I'm--"
            extend "{b}You're --{/b}"
            extend "{b} I'm---{/b}"
            extend "{b} dead?{/b}"
            extend "I remember dying, and now there's a voice in my head."
            n "{b}This is my head, fucker.{/b}"
            extend "\nFine, whatever. Your head."
            n "{b}Who the fuck are you anyway?{/b}"
            extend "\nYou first."
            extend "\n{b}No, you first. I'm not letting a strange ghost squat in my skull. The least you can do is fucking introduce yourself.{/b}"
            n "I'm Akagi Ai."
            extend "\n{b}No, {u}I{/u} am Akagi Ai. Try again.{/b}"
            n "No, seriously. I'm Akagi Ai. I'm a junior at Yomiyama Girls' Academy. My student ID number is XXXXX."
            n "{b}You're saying you're me?{/b}"
            n "I guess?"
            n "{b}OK, then. What's my darkest secret?{/b}"
            n "It would have to be that time at the pool in sixth grade, when the..."
            n "{b}OK OK STOP FINE ENOUGH{/b}"
            extend "\n{b}I guess I believe you, OK?{/b}"
            extend "\n{b}But I'm not dead{/b}"
            n "I think I might be you from the future."
            extend "\n{b}What?{/b}"
            extend "{b} Weird.{/b}"
            n "I remember dying and then seeing, like, a white light. Then I woke up here."
            extend "\n{b}How does that make you from the future?{/b}"
            extend "\nBecause you don't remember dying."
    "I slap the snooze button, and then look at the clock's face."
    stop sound
    ai "God damn it!"
    "7 o'clock."
    n "I'm going to be late for school"
    "I throw my clothes on and rush downstairs."
    scene bg downstairs
    with fade
    "Mom" "Don't swear so much, honey. It's not ladylike."
    ai "I learned from the best!"
    "Mom" "... Fuck you."
    scene bg street
    "Mom" "By the way, Aoi's already waiting"
    show aoi happy
    "Mom" "Before you go -- I know you wanted to attend that party after school, so just call me and let me know when you'll be home, OK?"
    aoi "Are you excited?"
    "Party... what party?"
    ai "Excited for what?"
    aoi "Excited to see my cute costume, of course!"
    ai "Why are you... you know what, nevermind. Of course I'm excited to see your cute costume. What is it?"
    aoi "A kitty cat!"
    ai "That sounds pretty cute."
    show aoi nekomimi blush
    n "Wow. She can put Koneko-chan to shame sometimes..."
    ai "Are you gonna wear that all day?"
    aoi "Sure am!"
    scene bg classroom halloween
    show kuroneko at left
    kuroneko "Well that's sweet."
    show aoi nekomimi blush at right
    aoi "Thank you very much, Fujinomiya-san!"
    n "This is awfully different from previous loops..."
    n "What the heck is with the costume anyway?"
    kuroneko "Are you two going to match tonight?"
    ai "What's tonight?"
    show aoi nekomimi pout at right
    aoi "The party! You promised we'd go together. You cheater..."
    show kuroneko pout at left
    kuroneko "The local syndicate is having a Halloween party, remember? A kind of 'thank you' for all the protection money they extort..."
    ai "Halloween? But it's..."
    "The board says 10/31."
    if kuroneko_unstuck_in_time:
        if kuroneko_unstuck_first_time:
            jump lodge_halloween
    comment "XXX fill in morning"
    jump halloween_afternoon
label halloween_afternoon:
    scene bg classroom halloween
    comment "XXX fill in afternoon"
    jump yakuza_party
label yakuza_party:
# getting the yakuza to wipe debts requires Koneko to do touch telepathy, which means her arc needs to be complete
# Notes: all the unstuck characters are allowed into the general party because the bouncer (old, shaved head, leering) thinks they're hot
# however, to get physical access to the back room, we need to tell aoi to tell them she represents yomi poly & is there to broker a deal -- so we need to finish her arc too
# koneko sneaks up behind a high-ranking guy, touches him on the neck, and runs away. He suddenly gets up and yells at an underling:
# 
# koneko complains about how icky their brains are / how disgusting it is to connect to someone telepathically
# none of the girls are wearing a costume, but aoi is wearing cat ears
    scene bg yakuza halloween party
    "There's a mix of teens like us & permed low-level yakuza, mingling. Few are costumed."
    "One hulking gorilla of a man in a poor-fitting black pinstripe suit, bowtie, and waistcoat stands in front of a curtain in the corner, looking uncomfortable. His eyes widen when he sees Aoi."
    "Gorilla yakuza" "Mistress Tomoe!"
    show aoi nekomimi
    aoi "Taro-chan! It's been sooo long!"
    "He bows deeply, blushing."
    "Taro" "About three weeks, mistress."
    aoi "Have you grown?"
    "Taro" "Only horizontally, mistress. What brings you here?"
    aoi "The party, of course!"
    "Taro" "Oh! Of course. I thought maybe you had wanted to speak to Aniki."
    ai "You know this guy?"
    aoi "Yeah! Taro is Taro, y'know~"
    "Taro" "The Yomiyama Crew owes a great deal to the Tomoe family. As the prestige of the university's research grows in certain circles, so does our influence in the syndicate."
    show kuroneko pout at right
    kuroneko "In other words, as long as Yomiyama is on the map, you guys can get payouts from military contractors?"
    "Taro bows again."
    "Taro" "Mistress Tomoe's friend is very astute."
    aoi "Taro-chan! Taro-chan! Isn't my costume cute?!"
    "Taro" "The ears suit you, mistress."
    hide aoi
    hide kuroneko
    "Giving quick bows, we drift out of Taro's earshot."
    ai "Hey, Kuro, is this the crew your folks have a debt to?"
    show kuroneko pout
    kuroneko "Sure is. This is that precise hive of scum and villany."
    kuroneko "Aoi-san may have weight to throw around, but I don't think she can get it forgiven on her own."
    if knows_about_yipi:
        if koneko_unstuck_in_time:
            ai "Not on her own."
            ai "Aoi, can you get us behind that curtain? It doesn't need to be for long."
            show aoi nekomimi at left
            aoi "Abbbbsooolutely!"
            ai "Koneko-chan, can your touch-telepathy inject ideas?"
            show koneko at right
            koneko "Yes, but..."
            ai "I'm going to need you to take one for the team. The guy's bound to be fucking gross, but we can eliminate your debt & you won't have to be a guinea pig anymore."
            n "Not that you can, considering the whole place was demolished by tentacle monsters. {b}What?!{/b}"
            koneko "... Understood."
            ai "Great. I love it when a plan comes the fuck together."
            "We begin edging back toward the curtain."
            aoi "Taro-chan, I think I should see your aniki after all. It'd be rude if I came all this way without at least saying hi."
            "Taro" "Of course. You and your friends are welcome any time."
            aoi "He's a very busy man, so we'll just pop in quick, OK?"
            "Taro" "He will be happy to see you. Please stay as long as you want."
            scene bg yakuza office
            "We duck inside the curtain, careful to be quiet. We are behind a man at a fancy desk, reading papers. There is another man, at a less fancy desk, on the far side of the room."
            "Koneko puts her hand on the man's shoulder, and he suddenly sits straight up. She flinches and hides behind us."
            "Man at fancy desk" "Why the hell is the Fujinomiya debt still in this ledger?! They paid their sixty mil last week. Fix it right now and then go apologize, or you lose another finger!"
            "Underling" "A-a-ah-Of course, right away, Aniki."
            "We duck back through the curtain."
            scene bg yakuza halloween party
            show aoi nekomimi
            aoi "He was a little too busy. We'll come back and pay our respects later."
            "Aoi winks at Taro. Taro blushes."
            $ debt_erased = True
            $ achievement.grant("Jubilee")
            ai "Girl, I didn't know you had it in you!"
            aoi "Had what?"
            ai "The ability and willingness to toy with a young man's heart!"
            aoi "Heart? No way. That's just how Taro-chan is. You're the only one for me, Ai-chan~"
            show kuroneko at right
            kuroneko "He's clearly into you, Aoi-san."
            show koneko at left
            koneko "Affirmative."
            aoi "No way. He's just shy, y'know."
            aoi "..."
            aoi "...."
            show aoi nekomimi pout
            aoi "Oh no. I'm terrible. I should go back and apologize right now."
            ai "Hold your tits. This is for the greater good."
            aoi "So it's ok?"
            kuroneko "Absolutely justified."
            "Koneko nods her head emphatically."
    "We grabbed some refreshments from passing low-level soldiers, who had been dressed in bunny-girl outfits and told to circulate with platters."
    "They were holding up remarkably well. Perhaps the Yomiyama Crew doesn't have to worry about eruptions of rage among their rank and file."
    "My phone rang."
    ai "Hello?"
    "Mom (telephone)" "Hi, hon! Are you still at the party?"
    ai "Sure am."
    "Mom (telephone)" "Aoi-chan's folks called and asked me to make sure you took her home soon."
    ai "They could have called me directly. Or her."
    "Mom (telephone)" "They found Aoi's phone out of batteries and under her bed."
    ai "Fair enough."
    ai "Yo, Aoi-chan -- your phone's under your bed."
    aoi "I thought I looked there!"
    ai "OK, mom. I'll get her home right away."
    "I hung up."
    ai "Well, it's been real. I gotta take this one home."
    show aoi nekomimi hearteyes
    aoi "You're taking me hooooome???"
    ai "To your home."
    show aoi nekomimi pout
    aoi "But you always take me there!"
    ai "No complaining! Come on."
    show aoi nekomimi
    aoi "Bye Fujinomiya-san! Bye other Fujinomiya-san!"
    scene bg street dark
    show aoi nekomimi blush
    "Despite all her complaints, once she was out the door, she happily clung to my arm."
    n "Now, I just have to watch out for knife-wielding dwarves in red rain coats."
    ai "Ok, end of the line. All passengers must exit."
    show aoi nekomimi pout
    aoi "It's always too soon."
    "I ring the bell."
    ai "Delivery for the Tomoe family! One girl, fun-sized, must present stamp on reciept!"
    "The door opens."
    "Mrs Tomoe" "Thank you, Ai-chan."
    ai "All in a day's work."
    hide aoi
    scene bg downstairs
    ai "Mom, I'm beat. I've already eaten, so I'm just gonna crash, OK?"
    "Mom" "Sleep well!"
    scene bg morning
    "The bed looked so inviting. It's nice to get to sleep without being killed."
    scene bg black
    jump halloween_night
label halloween_night:
    if halloween_janus_head_inverted:
        jump halloween
    jump core_story
