label music_room:
    "I placed the box by the door to the science club's room, and went across the hall."
    scene bg music room
    "The music room was large, with carpeted walls and a stadium-style step arrangement in the floor."
    "In the center, playing a violin and looking irritated, was Kuroneko."
    scene splash kuroneko violin
    with dissolve
    # XXX If we know about the music room from before, we look more carefully and see that Kuroneko has some books with scraps of sheet music shoved in them
    # These are not music-related books but occult-related books.
    if knows_about_kuroneko_concert:
        "The first time this happened, I didn't really pay attention to what else was in the room."
        "This time, I let Kuroneko continue playing, unaware of my presence, while I glanced around."
        "For the most part, the music room was as it usually is at the beginning of practice. All the instruments are put away."
        "I noticed some papers stuffed in Kuroneko's violin case, and a pile of books on a nearby stool."
        "The books had scraps of sheet music sticking out of them, but they were not sheet music books. Instead, they were thick, leather-bound, and looked quite heavy."
        "The book on the very top of the pile was open, and there was a piece of paper sitting on top of it, covered in scribbled notes, and a pencil."
        "There were some geometrical figures on the paper."
        "The bindings of the books had titles in some european language, and a funny-looking symbol."
        $ knows_about_kuroneko_books = True
    # We can ask Mimi or Shironeko to research them.
    # The occult books indicate that Kuroneko knows more than she initially seems to about the purpose of the concert.
    # Once you know the details, you can ask her about that stuff up-front. She will think you are a superior from the lodge sent to supervise her.
    ai "Having trouble?"
    stop music
    play music "music/Infocalypse_-_scathing_frolic.mp3"
    scene bg music room
    with dissolve
    show kuroneko pout
    "Kuroneko jumped."
    show kuroneko normal
    kuroneko "The fingering is hard on this piece."
    ai "That's what she said."
    show kuroneko pout
    kuroneko "If you're done..."
    ai "Don't worry, I'm not just here to fuck with you."
    ai "I'm all wiped out from lugging heavy boxes, and I happened to hear some pretty music."
    show kuroneko happy
    kuroneko "Oh yeah?"
    ai "Yeah. And I figured I could rest my bones a while here."
    extend "\nThey say the key to happiness is wine, women, and song. Two out of three ain't bad, right?"
    show kuroneko pout
    kuroneko "Just don't interrupt, OK?"
    ai "Fine, fine."
    show kuroneko normal
    scene splash kuroneko violin
    with dissolve
    play music "music/mystic chord practice.mp3"
    pause 23
    scene bg music room
    show kuroneko pout
    stop music
    play music "music/Infocalypse_-_scathing_frolic.mp3"
    kuroneko "I'm getting nowhere with this."
    ai "What is it, exactly, that you're trying to do?"
    show kuroneko normal
    kuroneko "This score is just really weird."
    extend "\nIt's the same six notes over and over in different combinations."
    ai "What's so weird about that?"
    kuroneko "It wants me to play combinations of notes that normally would be done on two different instruments."
    kuroneko "In order to play both notes at the same time on the same instrument I have to hold my fingers like..."
    scene splash kuroneko fingering
    extend " Here, you see what I'm doing with my hand?"
    "Her fingers were held in a kind of claw shape, and her wrist was at an awkward angle. Some fingers were pressing on multiple strings simultaneously at different angles."
    kuroneko "I have to go from that to another equally complicated chord in the space of one beat."
    scene bg music room
    show kuroneko normal
    kuroneko "The whole piece is like that."
    ai "Why don't you play something else? Or get a second violinist?"
    kuroneko "You know those weirdos out in that building with the gold roof?"
    ai "The cylindrical building? Out behind the convenience store?"
    kuroneko "Yeah. They gave me this."
    ai "And?"
    show kuroneko happy
    kuroneko "They offered me a lot of money to play at a concert they have coming up."
    show kuroneko pout
    extend "\nBut I have to play this piece, and they said it has to be exactly as notated."
    ai "When's the concert?"
    kuroneko "The first."
    ai "May first?!"
    kuroneko "That's why I'm in here practicing after dark!"
    ai "Do those fuckers know what they're asking of you?"
    show kuroneko happy
    kuroneko "The money is {i}very{/i} good."
    extend "\nI was suspicious but they told me it wasn't for an orgy or anything."
    ai "Thank god. I don't think I could bear living in a town with that kind of eyes wide shut shit going on."
    $ knows_about_kuroneko_concert = True
    ai "Wait, did you say it was after dark?"
    extend "\nShit, I need to get home!"
    ai "My mom's gonna fucking kill me."
    ai "Thanks for the set, Fujinomya! I gotta jet!"
    kuroneko "Sure, Ai. Just leave me here to stew in my failure."
    extend "\nLater."
    $ achievement.grant("Some Eyes-Wide-Shut MFers")
    scene bg hallway dark
    with dissolve
    jump walk_home

label kuroneko_book_content:
    "All the books she checked out are currently on the shelves."
    menu:
        "Check out the Speculative Masonry thing":
            "\"The worshipful master says 'I now present my right hand in token of the continuance of friendship and brotherly love, and will invest you with the pass-grip, pass-word, real grip and word of a Fellow Craft'\""
            n "Weird..."
            $ knows_masonic_initiation_phrase = True
            jump afternoon_classes
        "Check out the Scriabin book":
            "\"Scriabin's obsession with the occult is most famously associated with his final piece, which he intended to be played during the apocalypse, but the Prometheus Chord has its own numerological significance.\""
            n "I don't know anything about music OR the occult, so this is fucking jibberish to me."
            $ knows_about_scriabin = True
            jump afternoon_classes
        "Check out the Hellenistic magic book":
            "\"Because Janus is associated with the transition into the new year, he can, with the help of Hecate, be called upon for the same kind of time-related workings as Chronos.\""
            "\"A sacrifice is necessary for such a working. A bull is customary, but for extremely difficult tasks, the priest is said to have sometimes sacrificed himself or a virgin girl with the ritual knife.\""
            $ knows_about_janus = True
            jump afternoon_classes
        "Nevermind":
            jump lunch_library
label kuroneko_masonry_roof:
    "Kuroneko's expression suddenly changed, becoming serious and almost even respectful."
    "She offered me her hand and we performed a strange handshake."
    n "Jesus, I guess I have to pretend to be her superior now?"
    ai "I have... graduated you to the status of... um... fellow craft... for a reason!"
    n "Um, come on, think of a reason..."
    ai "I have... an important task for you!"
    ai "But... first... um..."
    ai "I need to test you!"
    menu:
        "Who is your usual Worshipful Master at the O:.S:.S Lodge?" if knows_about_oss:
            jump kuroneko_lodge_info
        "What is the role of Janus in or practices?" if knows_about_janus:
            jump kuroneko_janus_info
        "What is the role of Scriabin in our practices?" if knows_about_scriabin:
            jump kuroneko_scriabin_info
        "Who is the master who makes the grass green?":
            kuroneko "I... Uh..."
            ai "Test failed! I hereby revoke your fellow craft status!"
            "I hurry away before Kuroneko can ask me any questions."
            jump afternoon_classes

label kuroneko_lodge_info:
    comment "XXX fill in lodge info"
    jump afternoon_classes
label kuroneko_janus_info:
    comment "XXX fill in janus info"
    jump afternoon_classes
label kuroneko_scriabin_info:
    comment "XXX fill in scriabin info"
    jump afternoon_classes

# Notes on dagger mechanic:
# Stabbing someone with the ritual dagger forces their soul from their body but also kills anyone else who is unstuck
# So, unsticking someone else is fatal. This is the dagger's "kick"
# kick manifests as waves of nausea, dizziness, and then bleeding from the eyes

# Notes on kuroneko route in 2011:
# dying in 2011 will send you back to 2012 unless you also reverse the janus head there.
# kuroneko and ai sneak into the lodge in 2012 in order to find the book of shadows containing details about the ritual
# the section about how to abort the ritual safely has been torn out
# they go back to 2011 to fetch an earlier version & find it, using dagger & kick to jump to the beginning of halloween day. "sure is convenient, but it fuckin hurts don't it?"
# that version says that the altar must be destroyed during the ritual, after the first bar of music but before the third, and must be followed by a human sacrifice with the ritual dagger.
# this is endgame.

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

