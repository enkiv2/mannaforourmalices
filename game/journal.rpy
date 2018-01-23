# Journal

init -2 python:
    class generateJournalContent:
        def __call__(self):
            ret=[]
            if(in_2011):
                ret.append("The date is October 31st, 2011.")
            else:
                ret.append("The date is April 31st, 2012.")
            ret.append("\n\n   ")
            if(died): ret.append("Every time I die, I go back in time.")
            if(died): ret.append("I have died "+str(num_deaths)+" times.")
            if(midnight_loop): ret.append("I also loop in time when I go to sleep for the night -- presumably, at midnight. I don't need to be killed for this to happen.")
            ret.append("\n\n   ")
            ret.append("Tomoe Aoi is my best friend. We've known each other since we were little kids.")
            if(knows_about_aoi_parents): ret.append("In the science clubroom after school, I found a notebook with a weird scientific paper and a picture of Aoi's parents winning the Z-Prize in 1993.")
            if(knows_about_missing_lab_notebook): 
                ret.append("The notebook wasn't in the room at lunchtime, when I went with Mimi.")
                ret.append("Officially, the 1993 Z-Prize ceremony was cancelled. There was a bomb threat, and journalists in particular weren't allowed in. However, since there was controversy related to illegal human germline research beforehand, some people suspect a coverup and a media blackout.")
            if(knows_aoi_took_lab_notebook): ret.append("The reason Aoi was in the science clubroom after school was to pick up the notebook. Presumably, she also brought it in.")
            if(read_z_prize_papers): 
                ret.append("The paper that Aoi's parents won the award for described a method for human cloning for replacement organs wherein the neocortex is disconnected -- keeping the clones mentally disabled enough to be unable to understand they are organ farms.")
                ret.append("That paper was sitting on one of Yomiyama Polytechnic's computers, where Aoi's parents currently work, despite officially not existing. It seems likely that they are still doing research along those lines, and that they're doing it at YomiPoly.")
            if(knows_poly_guard_position): ret.append("There is an armed guard at the reception desk for YomiPoly's biological research building. He's a heavy smoker.")
            if(knows_about_keypad): ret.append("There's a keypad-locked door in the basement of the bio research building.")
            if(knows_keycode): ret.append("The code for unlocking the door is "+str(keycode)+".")
            if(knows_about_clone_racks): ret.append("Behind that door, there are racks upon racks of human clones hooked up to tubes and monitors.")
            if(knows_whole_aoi_story): ret.append("It turns out that when Aoi hit her head playing with me when we were kids, she actually died. Because her parents had clones of all the kids born around that time, they replaced her with her clone. They ended up needing to make the neocortext hypoxic instead of totally disconnected in order to prevent developmental problems, so Aoi could be brought up to a normal intelligence range using nootropic drugs and a special diet.")
            if(aoi_unstuck_in_time): ret.append("I stabbed Aoi with a ritual knife and now she is unstuck in time with me.")
            ret.append("\n\n   ")
            ret.append("Kuroneko is a friend and classmate. She's a very good student, and even though she's pretty harsh, she's not a bad person.")
            if(knows_about_kuroneko_concert): ret.append("The masonic lodge behind the 7/11 is paying her to play a complicated violin piece on May 1st.")
            if(knows_about_kuroneko_books): ret.append("She was practicing that piece in the music room after school, with some thick books written in a european language. She had a lot of notes, and some strange symbols drawn.")
            if(knows_about_oss): ret.append("The lodge is actually a cult called the O:.S:.S, run by a Russian music student. They combine some elements of freemasonry into their practice but they aren't recognized by other lodges.")
            if(knows_kuroneko_book_list): ret.append("Kuroneko recently repeatedly checked out books about freemasonry, Aleksandr Scriabin's occult practices, and how to do magic with the Greek pantheon.")
            if(knows_masonic_initiation_phrase): ret.append("There's a phrase used by freemasons to initiate people into the second grade. It goes like: \"I now present my right hand in token of the continuance of friendship and brotherly love, and will invest you with the pass-grip, pass-word, real grip and word of a Fellow Craft\".")
            if(knows_about_scriabin): ret.append("Scriabin apparently tried to write a piece of music that would bring about the end of the world.")
            if(knows_about_janus): ret.append("According to this book, the god Janus can be used for time-related magic if you sacrifice an animal or a human being.")
            if(halloween_janus_head_inverted): ret.append("The Janus bust on the altar in the O:.S:.S lodge on October 31st of 2011 is inverted.")
            if(altar_destroyed): ret.append("The altar in the O:.S:.S lodge has been destroyed.")
            if(kuroneko_unstuck_in_time): ret.append("I stabbed Kuroneko with a ritual knife and she is now unstuck in time.")
            ret.append("\n\n   ")
            ret.append("Koneko is Kuroneko's little sister. She's a track star, and very serious, and ADORABLE! I just want to hug her and squeeze her and take her home!!")
            if(knows_about_koneko_telepathy): ret.append("Apparently she has touch telepathy. She's also been meeting someone before and after school.")
            if(saw_milpsi_symbol): ret.append("The people she's been meeting are doing some kind of secret military experiments in a compound. I was taken to an interrogation room there. Everybody acted confused, and I started feeling foggy too. Then, big tentacled aliens came through a portal and killed everyone.")
            if(knows_milpsi_shell_co_name): ret.append("That military facility is going under the fake name 'Yomiyama Industrial Products, Inc'.")
            if(knows_about_stargate): ret.append("There was a CIA research program called Project Stargate that attempted to use clairvoyance to perform psychic spying. Official documentation claims they contacted aliens from other dimensions.")
            if(knows_about_yipi): ret.append("The organization calling itself Yomiyama Industrial Products is some kind of heavy military intelligence operation, under direct control of the Diet. They identify teenagers with latent psychic powers through various tests. They take the promising ones and try to improve their abilities through a combination of potent drugs and intense training. The burnout rate is high: all but one of their volunteers have succumbed to major health problems and dropped out within six months.")
            if(koneko_unstuck_in_time): ret.append("I stabbed Koneko-chan with a ritual knife, and now she's unstuck in time with me!")
            ret.append("\n\n   ")
            ret.append("Shironeko is Kuroneko's older sister. She's lazy and hardly ever comes into school, but she's super competitive and very good with computers.")
            if(knows_about_alien_tech): ret.append("She told me about some documents she found, involving space ships made of genetically engineered alien plant life.")
            return "{font=angelina.TTF}"+(" ".join(ret))+"{/font}"
    def __str__(self):
        self.call()

screen notes:
    tag menu
    use game_menu(_("Notes"), scroll="viewport"):
            style_prefix "about"
            vbox:
                label _("Notes:")
                label (generateJournalContent()())

