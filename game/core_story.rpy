# core_story is the beginning of the core story loop
# Each time the protagonist dies she is brought back here.
label core_story:
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
    if read_z_prize_papers and not knows_whole_aoi_story:
        n "More importantly, if I want to know what's going on with Aoi, this is really my only chance."
        n "{b}With Aoi?{/b}"
        n "There's something going on with her, and with her parents."
        n "She was in the science room and she took a notebook."
        n "{b}She was in the science room?! She fucking hates science!{/b}"
        n "The notebook contained photographic evidence of a prize ceremony that officially never happened."
        n "A ceremony in which her parents won an award for work on forbidden human germline research, involving cloning humans and harvesting their organs."
        n "I've never survived past this evening so I think if I'm going to figure out what they're doing in that synthetic bio lab, I'm going to have to start early."
        menu:
            "Nah":
                jump dont_sneak_to_yomipoly
            "Sneak out":
                jump sneak_to_yomipoly
label dont_sneak_to_yomipoly:
    "I throw my clothes on and rush downstairs."
    scene bg downstairs
    with fade
    "Mom" "Don't swear so much, honey. It's not ladylike."
    ai "I learned from the best!"
    "Mom" "... Fuck you."
    scene bg street
    "Mom" "By the way, Aoi's already waiting"
    show aoi happy
    if knows_about_clone_racks and not knows_whole_aoi_story:
        play music "music/Infocalypse_-_Dickless_Whore__The_Disembodied_.mp3"
        aoi "Ai-chan~"
        ai "Aoi..."
        aoi "Ai-chan~~"
        n "I don't know how to respond when she's like this."
        ai "How's... life?"
        aoi "Life is wonderful, now that I'm with you~!"
        n "She doesn't remember. Act normal. She doesn't remember."
        show aoi happy
        aoi "By the way, Ai-chan~~~"
        show aoi pout
        aoi "You wouldn't maybe happen to have today's biology homework, would you?"
        ai "Jesus, Aoi."
        n "She really doesn't remember..."
        ai "Yeah, sure. You can copy it again."
        show aoi hearteyes
        aoi "{i}Squeee!{/i}"
        n "{b}Remember what?{/b}"
        n "She's acting so normal right now, so it's hard to imagine she could kill me."
        n "No, that's not it. Whatever led to her killing me is latent in this moment. Those racks exist. It's just that she doesn't know I know about them yet."
        n "{b}She killed...{/b}"
        n "Those racks are a secret she'd even kill me for. Or maybe she only killed me because it was me."
    else:
        play music "music/Infocalypse_-_scathing_frolic.mp3"
        aoi "Ai-chan~"
        ai "I don't know how you're so fucking energetic in the morning, Aoi."
        aoi "Why wouldn't I be?"
        extend "\nAfter all..."
        show aoi hearteyes
        extend " I get to see"
        extend " my"
        extend " beloved"
        extend " Ai~"
        extend " chan~"
        extend "~"
        extend "~"
        n "I don't know how to respond when she's like this."
        show aoi happy
        aoi "By the way, Ai-chan~~~"
        n "Here it comes..."
        aoi "You wouldn't maybe happen to have today's biology homework, would you?"
        ai "Jesus, Aoi."
        ai "Yeah, sure. You can copy it again."
        show aoi hearteyes
        aoi "{i}Squeee!{/i}"
        ai "Your parents must be reconsidering their whole field. What are the odds of the child of two genius geneticists being such a ditz!"
        show aoi pout
        pause 1
        aoi "Meanie~"
        show aoi happy
        if knows_about_aoi_parents and not knows_whole_aoi_story:
            n "I seriously do wonder what's going on with her."
            extend "\nI knew her folks were smart, but the Z Prize is..."
            extend "\n{b}What?{/b}"
            extend "\nHer parents won the Z Prize back in the 90s. I found a picture of them holding it."
            n "I wonder why she never said anything about it."
            extend "\n{b}She gets enough flack for being dense as it is.{/b}"
            extend "\n{b}If people knew her parents weren't just smart but winners of the closest thing synthetic biology has to a Fields Medal...{/b}"
            n "I guess you're right."
        "We continued to make smalltalk the rest of the way to school."
    hide aoi
    # TODO: add more variation to this section, based on flags
    scene bg classroom
    show kuroneko pout at left
    "As we entered the classroom, we saw Fujinomiya Kuroneko muttering angrily to herself, stewing over some private betrayal."
    if knows_about_kuroneko_concert:
        n "That deadline must be eating away at her."
        extend "\n{b}What deadline?{/b}"
        n "Those guys that own the anthrosophy lodge behind the convenience store are paying her to play tomorrow night."
        extend "\n{b}And she's not ready?{/b}"
        extend "\nNot even remotely."
        n "{b}That's not like her...{/b}"
        extend "\nThey must have suggested it at short notice."
        extend " I don't think she'd take an offer like that if she wasn't really hurting for money though."
    ai "Fujinomiya! What crawled up your ass and died today?"
    "She took my greeting as a serious question."
    kuroneko "My sister's playing hooky again."
    show aoi happy at right
    aoi "Koneko-chan?"
    window hide
    scene koneko shojo with fade
    scene bg classroom with fade
    window show
    show kuroneko pout at left
    show aoi happy at right
    kuroneko "Are you an idiot? Koneko hasn't so much as been tardy once since preschool!"
    if knows_about_koneko_telepathy and not knows_milpsi_shell_co_name:
        n "Something very weird is going on with Koneko-chan."
        extend "\n{b}Weirder than a ghost in her head?{/b}"
        extend "\nMaybe."
        n "{b}What could be weirder than that?{/b}"
        extend "\nShe knew about the ghost in my head."
        extend "\n{b}In a previous iteration?{/b}"
        extend "\nYeah. And she was in a lot of pain, too."
        n "{b}We're going to find a way to help her, right?{/b}"
        n "I think we should. Ghosts and telepaths in the same town can't possibly be a coincidence. Helping her might also help us not get shanked."
        n "{b}Do we have any leads?{/b}"
        extend "\nShe said something about an appointment before school..."
        extend "\n{b}So we could catch her as she was leaving it.{/b}"
        menu:
            "Don't bother":
                jump dont_look_for_koneko_before_school
            "Look for her":
                jump look_for_koneko_before_school
label dont_look_for_koneko_before_school:
    # TODO: add more variation to this section, based on flags
    aoi "Then... Shironeko-senpai?"
    n "Why is that a question?!"
    kuroneko "It seems even Tomoe-san is capable of using the process of elimination."
    show kuroneko happy at left
    show aoi pout at right
    aoi "Ai~chan~~~! Fujinomia-san is making fun of me~~"
    "I patted her on the head"
    ai "There, there."
    show aoi hearteyes at right
    show kuroneko normal at left
    kuroneko "You enable her too much, Ai."
    show aoi happy at right
    ai "Look who's talking. If you and Koneko-chan worked together, you could physically carry Shironeko-senpai to school, and she wouldn't miss so much class."
    show kuroneko happy at left
    kuroneko "She's been doing nothing but eating pocky and sitting at the computer lately. I doubt even Koneko could pick her up now."
    show kuroneko normal at left
    extend "\nWhat she does on there all day is a mystery to me."
    ai "Maybe she's sore about not having Golden Week off."
    kuroneko "If that was the case, she wouldn't be skipping the rest of the year too."
    "Teacher" "Alright, settle down."
    stop music
    hide kuroneko
    hide aoi
    "Class rep" "Rise..."
    extend " Bow..."
    extend " Sit"
    play music "music/Infocalypse_-_scathing_frolic.mp3" fadein 5
    "The teacher took a look at the attendence sheet, muttering to herself."
    "Teacher" "{size=-3}Hmm... Fujinomiya is absent again... And Umeji...{/size}"
    "Teacher" "Now, let us quickly review the last chapter."
    "Teacher" "Let me see... We left off with the Genpei War."
    extend " Who can tell me the name of the two eras that this conflict borders?"
    extend " ... "
    extend "\nSince nobody's volunteering, Tomoe?"
    show aoi blush
    aoi "Ummm..."
    extend " The Nara period and the Meiji period?"
    "The teacher sighed."
    n "Sweet merciful fuck this girl is dense. Not only do those periods not border each other, but there's a thousand year gap!"
    "Teacher" "Sit down, Tomoe."
    hide aoi
    "Teacher" "Yamada?"
    show mimi
    mimi "Um..."
    show mimi pensive
    "Mimi picked up a small notebook and nervously flipped through the pages."
    show mimi scoop
    extend " She made a surprised face and then stood up straight."
    show mimi smug
    mimi "The Jisho and the Juei. Hence the alternate name, the Jisho-Juei War."
    "Teacher" "Correct, Yamada. But you should really remember this. You won't be able to consult your notebook for the test."
    show mimi angry
    "Teacher" "Ok, so who were the two sides?"
    hide mimi
    extend " ... Fujinomiya"
    show kuroneko happy
    kuroneko "The Minamoto and the Taira. Genpei is an alternate reading of the two names stuck together."
    "Teacher" "Correct, as always. I should give you a harder one next time."
    show kuroneko normal
    kuroneko "If you try to stump me, you will fail..."
    "Teacher" "Wh-- "
    extend "Nevermind. "
    hide kuroneko
    extend "Okay, Akagi. What sparked the conflict?"
    ai "The Minamoto and the Taira kept bitch-slapping each other over their place in the imperial court's hierarchy, which is stupid because having favor would just make them a target anyway."
    ai "This culminated in the Hogen and Heiji rebellions, where the Minamoto tried to fuck up the Taira but fucked themselves over instead."
    ai "Then the Taira made a toddler emperor, which pissed off the previous emperor's other kid Mochihito, so Mochihito went and helped out the Minamoto."
    ai "Of course, he and his Minamoto buddy got killed anyway so what was the point?"
    ai "Anyway, Mochihito started building up an army, and the Taira heir -- not the rugrat, the geezer -- tried to lock him up. They chased him through Mii-dera and finally got him on the Uji bridge, and the other Minamoto offed himself."
    "Teacher" "Not... incorrect."
    extend " But again I need to remind you to watch your language in class."
    extend "\nSee me after school."
    "The class continued. We didn't even finish covering the Genpei War by the time the bell rang and second period began."
    "Second period should have been biology, but the teacher never showed up."
    "Instead, halfway through the period, a substitute came in and announced a self-study period."
    show kuroneko normal at left
    kuroneko "That's strange. Our bio teacher is usually pretty reliable."
    show mimi pensive
    mimi "Indeed. The last time she missed a class was..."
    "Mimi ruffled through her notebook."
    show mimi smug
    mimi "February third, nineteen seventy four."
    show mimi normal
    show aoi pout at right
    aoi "Yamada-kun, how is it that you know all these things?"
    kuroneko "Nevermind why you even have that information -- how did you look it up so fast?"
    mimi "I have a mnemonic system."
    show mimi smug
    show aoi blush at right
    mimi "You know how a kanji dictionary is organized by radical?"
    mimi "I have a system sort of like that in this book, but organized by shapes."
    mimi "I'm a visual thinker so I associate ideas with specific symbols, and then if I forget a detail I can look it up by shape."
    show kuroneko smile at left
    kuroneko "So I'll bet you're even better at looking up things that are already shapes, right?"
    mimi "Yeah. I usually don't have a hard time remembering those unless they're really obscure, though."
    kuroneko "Comes in handy for the school newspaper?"
    mimi "It would, if that rag did any real journalism."
    show aoi pout at right
    aoi "Ai-chan~"
    extend " Yamada-kun's m-mn-mnewhatsit thing isn't going to make you fall for her, is it?"
    "She stuck out her lower lip and looked at me with puppy-dog eyes, looking almost at the edge of tears."
    "I patted her head."
    ai "You're the only one for me, Aoi~"
    show aoi hearteyes at right
    show mimi angry
    show kuroneko normal at left
    n "She's practically vibrating. It's absurd that such a small display of affection pleases her so much."
    n "One of these days that possessiveness is going to bite me in the ass, though."
    "Mimi got up from her seat."
    mimi "Listen, since lunch is next, I'm going to head to the cafeteria and grab some lunch before the morning rush."
    if died:
        menu:
            "Let her go":
                jump dont_follow_mimi
            "Make an excuse to follow her":
                jump follow_mimi
label dont_follow_mimi:
    aoi "Don't worry, Ai-chan. I brought a bento for you~"
    hide mimi
    ai "I can make my own lunches, you know."
    show aoi pout at right
    aoi "But then our lunches wouldn't match!"
    kuroneko "I'll leave you love birds to your nesting. I'm going to go claim a good spot on the roof."
    ai "Sure, Fujinomiya. Abandon me. I'll be fine."
    show kuroneko smile at left
    kuroneko "I'm sure you will."
    hide kuroneko
    show aoi hearteyes at right
    aoi "You're not alone, Ai-chan~ I'm here with you~~"
    if num_deaths < 1:
        jump lunch_classroom
    n "Where should I eat lunch?"
    menu:
        "In the classroom":
            jump lunch_classroom
        "In the cafeteria":
            jump lunch_cafeteria
        "On the roof":
            jump lunch_roof
        "In the library":
            jump lunch_library
label lunch_library:
    scene bg library
    "There are a few students milling around in the stacks, but the library is otherwise deserted."
    "Even the student who's supposed to be on checkout duty has skipped out."
    "The library isn't a popular place to have lunch -- probably because of the signs that say eating and drinking is prohibited here."
    menu:
        "Snoop around in the checkout desk":
            jump snoop_library_checkout_desk
        "Find some books":
            jump find_books
        "Look around":
            jump look_around_library
        "Just eat lunch":
            "The library is quiet, and the lunch I packed is a goddamned masterpiece."
    jump afternoon_classes
label snoop_library_checkout_desk:
    "The checkout desk is messy. The computer was left unlocked."
    menu:
        "Let's see what kind of weird books Kuroneko has been checking out":
            "According to the computer, she has several books currently checked out. The titles seem to be in Latin."
            "There are a couple titles she's renewed several times in the past six months:"
            "Rituals and Practices of Speculative Masonry by Sir Theonius Tunt"
            "Aleksandr Scriabin: The Secret Histories by Pyotr Fyodorov"
            "The Hellenic Revival: Rites and Practices for the Olympian Pantheon in the Modern Day by Ravyn Rowanwulf"
            $ knows_kuroneko_book_list = True
            jump snoop_library_checkout_desk
        "Let's see what Aoi's been checking out":
            "Aoi has only ever checked a book out from this library once. In freshman year, she checked out Microwave Cooking for Two and returned it the following day."
            jump snoop_library_checkout_desk
        "Let's see what Shironeko's been checking out":
            "Shironeko checked out a copy of Understanding Your 6502: Assembly, Microcode, and Internals four years ago and hasn't returned it yet."
            jump snoop_library_checkout_desk
        "Let's see what Koneko-chan's been checking out":
            "Koneko-chan currently has a copy of The Four Hour Body checked out. She recently returned a copy of The Phillip Experiment."
            jump snoop_library_checkout_desk
        "Why the fuck am I looking at library records?":
            "That's really fucking rude of me. I should do something else."
            jump lunch_library
label look_around_library:
    "Umeji-san is in the stacks, but nobody else familiar is around."
    "She looks upset. It would be rude to greet her, since she isn't very close."
    jump lunch_library
label find_books:
    menu:
        "Find the books Kuroneko was into" if knows_kuroneko_book_list:
            jump kuroneko_book_content
        "Find a manga or something":
            "The library hasn't gotten the new Golgo 13 tankoban yet, so I reread Devilman instead."
            jump lunch_library
label lunch_roof:
    scene bg roof
    play music "music/Infocalypse_-_Fingernails.mp3"
    "It's cold up here. The wind has knives and an intent to kill."
    show kuroneko pout
    "Or maybe the intent to kill is Kuroneko's. She's leaning against the railing, glaring down into the distance."
    "The wind keeps picking up her hair and throwing it in her face."
    ai "It'd be a nice day if we were ice-fishing, but hanging out on the roof in this weather is just fucking unpleasant."
    kuroneko "What, did you have a marital spat?"
    menu:
        "\"I now present my right hand in token of the continuance of friendship and brotherly love...\"" if knows_masonic_initiation_phrase:
            jump kuroneko_masonry_roof
        "\"It's not like that.\"":
            kuroneko "Then you should see a couples' counsellor."
            ai "No, I mean, I don't return her feelings."
            kuroneko "You might want to tell her that. Poor girl's gonna be heartbroken anyway, though."
            ai "Well, yeah. That's what I'm afraid of."
            kuroneko "So, do you actually have anything relevant to say? I'm kind of busy."
            n "Busy with what? You're staring into space in the middle of a windstorm."
            ai "No, I just thought I'd be friendly."
            "I found a spot that sheltered me somewhat from the elements and started to eat my bento."
            "Several pieces were caught by gusts and carried away to lands unknown. So it goes."
            "When I left, Kuroneko still hadn't moved from that spot."
    play music "music/Infocalypse_-_scathing_frolic.mp3" fadein 5
    jump afternoon_classes
label lunch_cafeteria:
    scene bg cafeteria
    "The cafeteria is crowded, and smells strongly of spices and overcooked meat."
    "A swarm of people circles the stuffed bread vendor. They will have sold out by this point, like they do every day."
    "People who have decided to purchase less popular meals are milling around with trays, or sitting at tables."
    "I don't see anybody I know."
    "I find a quiet corner and dig into my bento."
    n "Eating a packed bento in a cafeteria is underrated. Most of the stress in cafeteria dining comes from trying to buy food, after all."
    n "I guess it's different for the terminally popular, but after my tragic high school debut debacle, I don't have to worry about that."
    n "Who would have thought geta & newsboy caps would ever go out of style? I wasn't just mocked, but written up for dress code violation too."
    n "That might have been the open jacket & chest wrappings, though."
    n "Oh well. One does not care to acknowledge the mistakes of one's youth."
    jump afternoon_classes
label lunch_classroom:
    # TODO: add more variation to this section, based on flags
    "I had lunch in the classroom with Aoi."
    aoi "Say aaah~"
    ai "I can feed myself, you know."
    aoi "I know. But I can feed you, and that's a lot more fun!"
    "The boxed lunch had hot dogs shaped like octopi, little hearts made of bologna, and very few vegetables."
    ai "You sure have a protein-heavy diet, don't you?"
    aoi "My parents say that meat and fat are good for the brain."
    n "I sure hope so..."
    ai "Don't you ever feel like you want some vegetables? Or some rice?"
    aoi "I have some!"
    "She holds up a small, limp broccoli florette -- the only one in the lunch box. There's also a dollop of rice in one corner."
    ai "Girl, I don't know how you survive with such an imbalanced diet."
    "We finished eating. I think most of Aoi's lunch ended up in my stomach. My attempts to fend off her chopsticks were in vain."
    "I can't say I regret it, though. Despite her academic shortcomings, Aoi is a damned good cook."
    "I wouldn't mind her feeding me for the rest of my life, if not for what it would imply -- and what it would do to my arteries."
    hide aoi
    jump afternoon_classes
label afternoon_classes:
    # TODO: add more variation to this section, based on flags, & beef it up / add more content
    scene bg classroom
    "The first period after lunch was English."
    if has_knife:
        if aoi_unstuck_in_time:
            $ pass
        else:
            "The knife is restless, and Aoi's closeness makes it wriggle in my hand."
            menu:
                "Stab Aoi":
                    "I give in, and let the knife work."
                    "Despite myself, my mouth contorted into a manic grin as the blood and eye fluid made a warm mess out of my face."
                    "People rushed in and circled around the spectacle, but I was already collapsing into a heap atop Aoi's crumpled body."
                    $ aoi_unstuck_in_time = True
                    jump death
                "Don't stab Aoi":
                    "I held the knife tightly, hiding it under my skirt."
                    "Aoi looked at me worriedly, and I gave her a sharp glance. She looked away."
                    "The knife, frustrated, cut little circles in my thigh. I held my tongue and focused on keeping it to heel."
    "The bell rang and the teacher came in."
    "He was pretty young, and a foreigner. His Japanese was shit, but since he was teaching an immersion-oriented English class it wasn't too much of a problem."
    "English Teacher" "{k=2}Good morning, class!{/k}"
    "Class" "{k=2}Good morning, sensei{/k}"
    "English Teacher" "{k=2}Please open your textbooks to page 68. We'll be covering prepositions.{/k}"
    "Sometime during English class, I dozed off, and only awoke partway into math, when being called upon."
    "Math Teacher" "Akagi, if you're confident enough in your abilities that you are willing to sleep through my lessons, then please demonstrate how to solve this for the class."
    "The problem wasn't one from homework, and involved topics we hadn't yet covered, but I had read ahead in the book slightly so it looked familiar."
    "With some difficulty, I solved it."
    "The teacher deflated slightly."
    "Math Teacher" "Tomoe, can you explain Akagi's solution?"
    n "Had to find somebody to pick on, huh?"
    show aoi pout
    aoi "Ummm~~~"
    "Math Teacher" "Go on. You weren't paying attention either."
    aoi "Ai-chan, how did you do it~~~"
    ai "Well..."
    hide aoi
    "Math Teacher" "Alright, fine. Explain, Akagi."
    "I made something up about partial integration. It must not have been totally correct, but what I described was confused enough that the teacher somehow saw a correct answer somewhere in it."
    "Math Teacher" "Good. Did everyone follow that?"
    n "I guess that wasn't any less clear than his usual explanations, though."
    "Apparently satisfied, he didn't pick on me for the rest of the period. While I didn't fall asleep again, I was not entirely awake."
    if died:
        n "Dying really takes it out of ya."
    "After the end of the class, a few students came over to try to get a clearer explanation, and when they left, Aoi came around."
    show aoi
    aoi "Ai-chan, how did you do thaaat?"
    if aoi_unstuck_in_time:
        ai "I would have expected you to remember, given the number of times you've heard me explain it."
        aoi "I don't remember at aaaall~~~"
        ai "I guess that's in-character for you."
    else:
        ai "Magic!"
        aoi "Reeealy! I didn't know you knew magic, Ai-chan!"
        aoi "Cast a spell on me!"
        aoi "Make it a looooove spell~~~"
        ai "I don't think you need any more of that."
        aoi "I can always use more Ai-love~"
        ai "If I cast a love spell on you, it would give you more Aoi love, not more Ai-love."
        show aoi pout
        aoi "But I'm already 80%% love."
        n "It's growing?!"
    hide aoi
    "Finally, the bell rang."
    "I was about to leave until..."
    "Teacher" "Akagi."
    n "Oh, right."
    "Teacher" "It was the elder Fujinomya's turn to clean the classroom today. Since she isn't in, I'd like you to do it."
    n "Laaaame"
    "Teacher" "Or, if you prefer, you can bring her all her missed printouts."
    "She pointed at a thick stack of printouts on the desk, which looked very heavy."
    if died is False:
        n "Nahhhhhh"
        ai "Cleaning the classroom sounds just fucking fine!"
        "Teacher" "... I'll accept that answer, I guess."
        jump clean_classroom
    menu:
        "Clean the classroom":
            jump clean_classroom
        "Deliver printouts":
            jump deliver_printouts
        "Stab Koneko" if has_knife and not koneko_unstuck_in_time:
            scene bg hallway
            "The knife practically dragged me downstairs."
            scene bg track
            "I walked out onto the track, a direct line to where Koneko was running on the far side."
            "As she passed, the blade's cuts made festive streamers of crimson blood."
            "She picked up speed, trying to escape, but a knick is all you need from this blade, and soon the same torpor that had made her stumble and collapse was also sucking my soul down into the outside of time."
            $ koneko_unstuck_in_time = True
            jump death
        "Disrupt the ritual" if seen_missing_pages:
            play music "music/Spontaneous Salmon.mp3"
            scene bg hallway
            "I left the classroom,"
            scene bg science room
            "running to the science club room to fetch Aoi,"
            scene bg hallway
            "then"
            scene bg music room
            "to the music room, to coordinate with Kuroneko."
            scene bg hallway
            "After that,"
            scene bg track
            "To the track, to get Koneko-chan."
            scene bg hallway
            "Kuroneko provided us with robes, and told us to hide in the woods near the lodge, and to be ready at midnight."
            scene bg street
            "Kuroneko went ahead, and the rest of us waited at the arcade."
            scene bg arcade
            show koneko at right
            koneko "..."
            "Koneko stared at the robe as if to say, 'is this really necessary?'"
            show aoi robe at left
            aoi "Ai-chan, guess whoooo~"
            ai "... I guess it'll do a good job of hiding your identity once it gets dark, assuming you don't squee too much."
            show aoi robe hearteyes at left
            aoi "Squee~~~~"
            show koneko pout at right
            koneko "..."
            ai "Are you gonna have any of that squid? We won't really have a chance to have a proper dinner."
            koneko "... I don't want to touch anything with tentacles."
            ai "... Fair enough."
            aoi "More for meeee"
            "Aoi shoveled the entire basket of dried squid into her mouth."
            show aoi robe pout at left
            aoi "My tummy hurts..."
            "An alarm on my phone went off."
            ai "Alright, time to go."
            scene bg street dark
            "We went down the block & hid in the woods by the lodge. We watched people pull into the convenience store parking lot & leave."
            jump ritual
label clean_classroom:
    play music "music/Infocalypse_-_lost_staircase.mp3"
    "The classroom isn't particularly dirty."
    "I stacked up the desks and started cleaning the floor."
    "In the corner of the room there's a box of glassware on loan from the science clubroom."
    if died:
        menu:
            "Ignore the box":
                jump ignore_box
            "Return the box":
                jump return_box
    else:
        jump ignore_box
label ignore_box:
    "The glassware can wait. I think it's been here for weeks already anyway."
    "I look out the window. There's a solitary figure running around the track."
    window hide
    scene koneko shojo with fade
    window show
    n "Must be Koneko-chan. She sure works hard."
    scene bg classroom
    if died:
        menu:
            "Continue tidying up.":
                jump dont_visit_track
            "Go see Koneko-chan":
                jump visit_track
    else:
        jump dont_visit_track
label dont_visit_track:
    if died:
        n "She's busy training for the track meet. I'd better not disturb her."
    n "This is exhausting."
    if died:
        menu:
            "Take a nap":
                jump take_nap
            "Continue cleaning":
                jump dont_take_nap
    else:
        jump take_nap
label dont_take_nap:
    n "I'd better not take a nap. I should finish cleaning and head home."
    n "..."
    n "But I'm so fucking tired right now. I guess a little one can't hurt."
    n "That's right..."
    n "A little one. Just a cat nap."
    jump take_nap
label take_nap:
    n "Nobody's in the school, and I have nowhere to go."
    n "I guess I might as well take a little nap."
    n "Then I'll have the energy to finish up."
    "I pull out a desk and chair and fall asleep."
    pause
    n "{cps=1}...{/cps}"
    extend "..."
    extend "zzz"
    extend "zzz"
    n "{cps=1}zzz{/cps}"
    scene bg black
    n "{cps=1}zzZ{/cps}"
    stop music
    n "{cps=1}zz{/cps}Oh shit"
    scene bg classroom dark
    n "Shitfuck"
    jump walk_home_from_classroom
label walk_home_from_classroom:
    scene bg classroom dark
    stop music
    n "Shit"
    n "The sun has gone down. How late is it?"
    n "I'd better get home."
    "I gather my things and head home."
    scene bg hallway dark
    pause 1
    jump walk_home
label walk_home:
    scene bg street dark
    play music "music/Infocalypse_-_Light.mp3"
    if died is False:
        n "Are the streetlights malfunctioning? I don't remember the walk home ever being this dark..."
    else:
        n "{b}Are the streetlights malfunctioning? I don't remember the walk home ever being this dark...{/b}"
    if died:
        n "Shit shit shit"
        extend "\n{b}What?{/b}"
        n "This is where I---"
    else:
        n "I have a bad feeling..."
    "Suddenly"
    play music "music/Infocalypse_-_Harvest.mp3"
    extend " I feel a pinch and a strange pressure in my chest."
    "I look down."
    scene splash blood one
    n "Oh shit shit shit shit"
    "A crimson stain"
    n "shit shit shit shit"
    scene splash blood two
    "Vermillion droplets on the ground"
    n "shit shit sh"
    "The outline of a blade poking out of the center of my chest."
    jump death
    
label death:
    play music "music/Infocalypse_-_Try_to_remember.mp3"
    scene bg black
    n "God damn it..."
    n "I'm dying..."
    if died:
        n "Why the hell do I keep dying?"
        if num_deaths > 2:
            n "What kind of stupid-ass chuunibyo bullshit is this?"
            $ achievement.grant("Some chuunibyo BS")
            call screen confirm("Do you want to save?", yes_action=[ShowMenu(save), Return()], no_action=Return())
            if num_deaths > 5:
                n "If there's a god, I hope he's ready to get an earful."
                n "Jesus fuck. [num_deaths] times? Really?"
            n "People are only supposed to die once, you know!"
    $ num_deaths += 1
    $ has_knife = False
    if altar_destroyed:
        jump bad_end
    jump rebirth

label rebirth:
    scene bg white
    if died:
        n "I guess it happened again"
    else:
        n "I guess this is what dying is like."
        n "I was never much for religious conjecture. I never thought about life after death or anything like that."
        n "I figured I'd find out firsthand eventually."
        n "I didn't expect it to be this soon, though."
    $ died = True
    $ achievement.grant("Stabbed in the back")
    call screen confirm("Do you want to save?", yes_action=[ShowMenu(save), Return()], no_action=Return())
    if in_2011:
        if halloween_janus_head_inverted:
            $ pass
        else:
            $ in_2011 = False
    else:
        if janus_head_inverted:
            $ achievement.grant("Niaga praw emit eht od s'tel") # Warped to Halloween 2011
            call screen confirm("Do you want to save?", yes_action=[ShowMenu(save), Return()], no_action=Return())
            $ in_2011 = True
    if in_2011:
        jump halloween
    jump core_story

label bad_end:
    scene splash blood two
    centered "BAD END"
    $ achievement.grant("Bad end")
    call screen confirm("Do you want to save?", yes_action=[ShowMenu(save), Return()], no_action=Return())
    return
    
