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
label halloween_afternoon
    scene bg classroom halloween
    comment "XXX fill in afternoon"
    jump yakuza_party
label yakuza_party:
# getting the yakuza to wipe debts requires Koneko to do touch telepathy, which means her arc needs to be complete
# Notes: all the unstuck characters are allowed into the general party because the bouncer (old, shaved head, leering) thinks they're hot
# however, to get physical access to the back room, we need to tell aoi to tell them she represents yomi poly & is there to broker a deal -- so we need to finish her arc too
# koneko sneaks up behind a high-ranking guy, touches him on the neck, and runs away. He suddenly gets up and yells at an underling:
# "Why the hell is the Fujinomiya debt still in this ledger?! They paid their sixty mil last week. Fix it right now and then go apologize, or you lose another finger!"
# koneko complains about how icky their brains are / how disgusting it is to connect to someone telepathically
# none of the girls are wearing a costume, but aoi is wearing cat ears
    $ debt_erased = True
    $ achievement.grant("Jubilee")
label halloween_night:
    if halloween_janus_head_inverted:
        jump halloween
    jump core_story
