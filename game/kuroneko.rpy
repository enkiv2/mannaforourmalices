# Kuroneko's route is the main one
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
    show kuroneko pout
    kuroneko "It wants me to play combinations of notes that normally would be done on two different instruments."
    kuroneko "In order to play both notes at the same time on the same instrument I have to hold my fingers like..."
    scene splash kuroneko fingering
    extend " Here, you see what I'm doing with my hand?"
    "Her fingers were held in a kind of claw shape, and her wrist was at an awkward angle. Some fingers were pressing on multiple strings simultaneously at different angles."
    kuroneko "I have to go from that to another equally complicated chord in the space of one beat."
    scene bg music room
    show kuroneko pout
    kuroneko "The whole piece is like that."
    ai "Why don't you play something else? Or get a second violinist?"
    kuroneko "You know those weirdos out in that building with the green roof?"
    ai "The octagonal building? Out behind the convenience store?"
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
    show kuroneko pout
    "Kuroneko's expression suddenly changed, becoming serious and almost even respectful."
    if kuroneko_unstuck_in_time:
        if kuroneko_unstuck_first_time:
            kuroneko "You transmigrated me."
            ai "I guess I did."
            ai "I didn't mean to. The knife just--"
            kuroneko "The knife has {i}telos{/i}. It knows its task."
            kuroneko "You're transmigrated too?"
            ai "Not by choice. I got stabbed on the street. I keep getting stabbed on the street."
            kuroneko "By a dwarf in a red rain coat?"
            ai "Wh-- No. I don't know. It was from behind."
            kuroneko "You're the preliminary sacrifice, then. I guess it's too late to tell you not to get involved."
            ai "Why are you involved?"
            kuroneko "My parents... We need the money."
            kuroneko "They couldn't really afford to send the three of us to private school. They took money from the yakuza. I don't think Shironeko has noticed."
            ai "I see."
            ai "The ritual --"
            kuroneko "I thought they were rich nutjobs. I didn't think any of what they were doing would actually work."
            ai "What is the ritual supposed to do?"
            kuroneko "Transmigrate everybody. Freed from the body and from time. Some bullshit about being freed from regrets, too."
            ai "I heard the guy in charge failed out of music school."
            kuroneko "Sounds about right."
            ai "Is there any way to stop it?"
            kuroneko "The ritual, and all the backup stuff to reverse it in case it goes wrong, is in a book of shadows under the altar. I'll take you there."
        else:
            kuroneko "Are we going to transmigrate someone else?"
            ai "Something like that."
        jump show_to_janus_bust
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
        "What is the role of Janus in our practices?" if knows_about_janus:
            jump kuroneko_janus_info
        "What is the role of Scriabin in our practices?" if knows_about_scriabin:
            jump kuroneko_scriabin_info
        "I come on behalf of Frater Zeus" if knows_zeus_role:
            jump zeus_info
        "Who is the master who makes the grass green?":
            kuroneko "I... Uh..."
            ai "Test failed! I hereby revoke your fellow craft status!"
            "I hurry away before Kuroneko can ask me any questions."
            jump afternoon_classes

label zeus_info:
    menu:
        "Take me to the lodge, and show me the Janus bust." if knows_janus_role:
            jump show_to_janus_bust
        "Hop on one foot while singing Touryanse backwards":
            "She looks confused for a moment, and then starts to do it."
            kuroneko "Sen-ya-rito sennnn-ya-rito, mo ra-ga-na i-wa-ko~~"
            "I hurry away before Kuroneko notices I've pranked her."
            jump afternoon_classes
label lodge_halloween:
    kuroneko "Come along, then. We'd better check for those pages, quick."
    scene bg hallway
    "She leads me downstairs..."
    scene bg street
    "... out the building ..."
    scene bg oss exterior
    "... to the lodge ..."
    scene bg oss altar
    "... and into the sanctum."
    if halloween_janus_head_inverted:
        scene bg altar inverted
    else:
        scene bg altar
    "She rummages under the altar, and pulls out the book."
    kuroneko "OK, here. It says... we can only abort the ritual after the promethean composition has begun, by smashing the altar and offering a... sacrifice."
    ai "What kind of sacrifice?"
    kuroneko "Judging by... what they did to you, human probably."
    ai "Ugh."
    kuroneko "Well... I guess it's a noble one. Otherwise, the whole world's gonna be dealing with eternal recurrence."
    ai "I guess. Still... These guys are pretty kill-happy. Maybe we should see if just smashing the altar will suffice."
    kuroneko "Assuming we can ever get back to that date. This ritual isn't really meant for supporting inter-equinox time travel, so I'm not so sure it'll work."
    ai "You understand their metaphysics pretty well. Do you think the sacrifice is necessary?"
    kuroneko "You and I needed to be killed to transmigrate. It stands to reason that stopping time travel requires as much energy as starting it."
    ai "..."
    $ seen_missing_pages = True
    ai "We ought to get back."
    jump halloween_afternoon
label show_to_janus_bust:
   kuroneko "Come along, then."
   scene bg hallway
   "She leads me downstairs..."
   scene bg street
   "... out the building ..."
   scene bg oss exterior
   "... to the lodge ..."
   scene bg oss altar
   "... and into the sanctum."
   if janus_head_inverted:
       scene bg altar inverted
   else:
       scene bg altar
   if kuroneko_unstuck_in_time:
       if kuroneko_unstuck_first_time:
           kuroneko "The book should be under--"
           "She rummages through a little shelf under the altar proper, hidden by the altar cloth draped over it."
           kuroneko "Here it is!"
           "The book is leather-bound, with an inverted pentagram inlayed in gold leaf on the front."
           "She opens it, and flips through."
           kuroneko "The pages -- they're torn out!"
           kuroneko "I know the pages on how to abort the ritual were here. I saw them a few weeks ago, but only very briefly."
           ai "Any more leads?"
           kuroneko "If their metaphysics are right, we should be able to..."
           kuroneko "See, Janus is the god of threshholds. His head is two-faced. One face is old, and one is young."
           kuroneko "If you move the bust to face the wrong way on the year wheel, the transmigrated souls should..."
           $ janus_head_inverted = True
           scene bg altar inverted
           ai "Should what?"
           kuroneko "Should end up on the far side of the year wheel."
           kuroneko "OK, time to get back to class."
           jump afternoon_classes
   menu:
       "Pick up the knife":
           jump pick_up_knife
       "Invert the Janus head":
           jump invert_head
label invert_head:
    if janus_head_inverted:
        $ janus_head_inverted = False
        scene bg altar
    else:
        $ janus_head_inverted = True
        scene bg altar inverted
    ai "Now, we go back to class."
    jump afternoon_classes
label pick_up_knife:
    if kuroneko_unstuck_in_time:
        "The knife feels heavy in my hands, but calm. It's as though I am holding the leash of a guard dog who, for now, is simply alert and cautious."
        "There is none of the force of before."
        $ has_knife = True
    else:
        "I barely touch the grip, but it seems to jump into my hand."
        show kuroneko pout
        "It twists like a snake, but I can't let go -- it won't let me."
        ai "Hey, what's--"
        "It pulls my arm over my head and prepares to..."
        ai "Get out of the--"
        "... sweep down in a powerful arc, right into the top of Kuroneko's head."
        hide kuroneko
        ai "Shit. Shit shit shit."
        "Blood drips down from the new hole in the bottom of her chin, and the knife pulls clean out as her legs fall out from beneath her."
        "Static fills my vision as I, too, collapse."
        $ kuroneko_unstuck_in_time = True
        $ kuroneko_unstuck_first_time = True
        jump death
    ai "Now, we go back to class."
    jump afternoon_classes
label kuroneko_lodge_info:
    kuroneko "Frater Zeus."
    $ knows_zeus_role = True
    menu:
        "What is the role of Janus in our practices?" if knows_about_janus:
            jump kuroneko_janus_info
        "What is the role of Scriabin in our practices?" if knows_about_scriabin:
            jump kuroneko_scriabin_info
        "Who is the master who makes the grass green?":
            kuroneko "I... Uh..."
            ai "Test failed! I hereby revoke your fellow craft status!"
            "I hurry away before Kuroneko can ask me any questions."
            jump afternoon_classes
label kuroneko_janus_info:
    kuroneko "Janus, lord of threshholds, has a special role at the equinox. The Janus bust is the representative of time in the ritual of transmigration."
    $ knows_janus_role = True
    menu:
        "Who is your usual Worshipful Master at the O:.S:.S Lodge?" if knows_about_oss:
            jump kuroneko_lodge_info
        "What is the role of Scriabin in our practices?" if knows_about_scriabin:
            jump kuroneko_scriabin_info
        "Who is the master who makes the grass green?":
            kuroneko "I... Uh..."
            ai "Test failed! I hereby revoke your fellow craft status!"
            "I hurry away before Kuroneko can ask me any questions."
            jump afternoon_classes
label kuroneko_scriabin_info:
    kuroneko "Scriabin formulated the ritual of the transmigration, having understood the hidden power of the Prometheus Chord."
    $ knows_scriabin_role = True
    menu:
        "Who is your usual Worshipful Master at the O:.S:.S Lodge?" if knows_about_oss:
            jump kuroneko_lodge_info
        "What is the role of Janus in our practices?" if knows_about_janus:
            jump kuroneko_janus_info
        "Who is the master who makes the grass green?":
            kuroneko "I... Uh..."
            ai "Test failed! I hereby revoke your fellow craft status!"
            "I hurry away before Kuroneko can ask me any questions."
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

