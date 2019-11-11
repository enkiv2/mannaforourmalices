## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Manna for our Malices")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("""\
{b}Introduction{/b}

{i}Manna for our Malices is a time travel mystery set in the small town of Yomiyama.{/i}


{b}Dramatis Personae{/b}{i}

Akagi Ai - Our protagonist, a high school Junior.

Tomoe Aoi - Ai's childhood friend, the daughter of scientists at nearby Yomiyama Polytechnic

The Fujinomiya sisters:
                     
{space=100}Shironeko - the eldest, a slacker who has been held back a year 
{space=110}because of a habit of blowing off homework
                     
{space=100}Kuroneko - Also a junior, she is an academic overachiever and a 
{space=110}skilled violin player
                     
{space=100}Koneko - Despite being a freshman, she is the star of the 
{space=110}Yomiyama track team

Yamada Mimi - Another classmate of Ai's, she handles the school newspaper
{/i}

{b}Cultural and Localization Notes{/b}

Manna for Our Malices{i} is set in Japan, and while I am not Japanese, I have made an effort to keep cultural elements accurate or to justify any inaccuracies I found necessary for the sake of storytelling. This means that some things mentioned in the story will not necessarily be familiar to western audiences (and while this story is very much set in the kind of warped version of Japan seen in anime, readers may nevertheless be confused).

This is also a story about magic, conspiracy theories, and super-science, and I make references to both media and actual events and practices that a general audience will probably not be familiar with.

I am providing the following notes for the sake of such a general audience, so that puzzles that would be nearly impossible without this knowledge become solveable. I found that my in-game explanations in the first release were too oblique for some players, leading to frustration.

{b}Japanese culture{/b}

{b}American military bases{/b} - after the end of the occupation, a lot of american military bases remained on Japanese soil. This is the source of a lot of political friction: Japan relies upon the United States for military protection, since its ability to have its own military is limited constitutionally, so ruining its relationship with the US is an existential threat, but at the same time the continued existence of these bases is seen as a breach of autonomy & there have been many high-profile scandals involving American soldiers committing serious crimes against Japanese locals (including rape and murder) and being percieved as 'getting off easy' in the American military judicial system.

{b}Aniki{/b} - a relatively formal way of saying {/i}older brother{i}, used by yakuza members to refer to people they work with who are senior to them (particularly the people they report directly to). Also used in less organized gangs, in the same way. The feminine equivalent, used in girl gangs, is {/i}aneue{i}. Sometimes, these terms are used as a gendered form of {/i}senpai{i}, but doing so implies that the speaker has a criminal background.

{b}Bancho{/b} - a stereotype of a (male) post-second-world-war juvenile delinquent. Bancho wear pageboy hats (often from school uniforms), black school uniform jackets worn open, baggy pants, wooden sandals, and wrap their stomach with white cloth as protection against blunt weapons. This type was a common trope in 60s and 70s manga aimed at teenage boys. The rough equivalent for female delinquents is {/i}sukeban{i}.

{b}Classrooms{/b} - unlike in the west, where junior high and high school students go to subject-specific classrooms, in Japanese schools, the students stay put while the teachers rotate, with specialized materials like chemistry supplies stored in rooms shared with after school clubs. Students are responsible for cleaning classrooms and performing other forms of maintenance work as a way of encouraging a sense of responsibility and ownership (part of a policy that also encourages them to make their own way to school and bring handouts and notes to the homes of sick classmates). While cleaning duty is assigned to students on a rotating schedule, it can sometimes be reassigned to a different student as a mild form of punishment.

{b}Class S{/b} - a literary genre centering around romanticized relationships between schoolgirls, originally developed in the early 20th century. While the relationships are sometimes explicitly romantic or even explicitly sexual, they are also often just ambiguous enough to provide plausible deniability. While Class S is now often considered problematic, for decades it was the primary way that lesbians were represented in Japanese media outside of sexualized depictions aimed at men. Class S traffics in specific tropes: private all-girls schools, dreamy young women obsessed with the signifiers of western luxury (especially 18th century french high culture), and deep connections between young women that dissolve upon graduation. {/i}Manna{i} is not a Class S work, but I import some tropes from it, and it provides genre justification for the idea that nearly all of the characters in the series are lesbians (rather than only about half).

{b}Devilman{/b} - an extremely popular and influential manga by Go Nagai. This franchise is credited with kicking off the trend of edgy, adult-oriented manga because of its heavy use of sex, violence, and religious imagery. Nagai is also the author of Cutie Honey, which kicked off the modern magical girl formula, and Mazinger, which kicked off the mecha genre.

{b}Festival{/b} - towns in Japan often have {/i}masturi{i} (typically translated as {/i}festivals{i}) once a year. During these festivals, colorful stalls are set up selling junk food, toys, masks, and often-rigged games. Many attendees wear traditional Japanese clothing (and this is one of the rare occasions when it is normal to do so in public). The festivities also involve a parade where a shinto shrine is carried, drumming and traditional dances, and fireworks to mark the end of the festival. Festivals are usually held during the summer, but I moved this one to the spring.

{b}Golden week{/b} - this is the longest block of holidays for most Japanese adults, and one of the longest blocks of holidays for Japanese students. It is a series of national holidays that are close together, spanning from late April to early May. Because weekdays that are between two weekday holidays are considered holidays, and because holidays that fall on a weekend are moved to the weekday they border, most people have an entire week off during this period. (Meanwhile, summer vacation for Japanese students is two weeks long, and a large amount of homework is typically assigned.) Accidents of the calendar and various events can cause Golden Week to be longer -- for instance, in 2019, the ascession of the new emperor lengthened Golden Week to the point that some journalists worried that it would negatively impact students' retention of material. The Japanese school year ends just before Golden Week and begins just after it. {/i}In-universe{i}, Yomiyama Academy adopts the trend of Japanese private schools modeling themselves on western private schools. This manifests as Yomiyama Academy not having Golden Week off -- which is probably not accurate or believable, but allows us to use the western pagan year wheel in conjunction with a story set in a Japanese school.

{b}Golgo 13{/b} - a long-running manga whose peak of popularity was in the 1980s. This series features a secret agent / assassin modeled on James Bond whose overly muscular build is reminiscent of western 80s action heroes.

{b}Halloween{/b} - Halloween is seen as a western holiday, and trick-or-treating is unusual, but starting in the late 90s, local yakuza syndicates began to hold annual Halloween parties for residents of their turf as a PR move.

{b}One does not care to acknowledge the mistakes of one's youth{/b} - this is a translation of a famous line by Char Aznable, the antagonist of the original Gundam series. While in context he is describing a risky but successful military operation for which he retrieved substantial recognition, it became used in anime otaku circles as a tongue-in-cheek way of talking about now-embarassing fandom. This use can be seen in action in the second episode of {/i}Otaku no Video{i}.

{b}Parental absence{/b} - Working adults in Japan work substantially longer hours than westerners of all stripes. Unionization is extremely rare, worker's rights legislation is weak and rarely enforced, and social conventions around respecting one's superiors encourages a lot of unpaid overtime (since it's rude to go home before your boss does). Additionally, it's common for major decisions to be made during informal after-work meetings at bars, where the pressures to avoid insulting superiors are lowered or somewhat ignored. This means that working adults don't spend a lot of time at home. While married women still very often become housewives, those who stay in the workforce are still subject to these same pressures. So, it isn't entirely unrealistic for children whose parents both work to be latch-key kids to a substantially greater degree than in the west (with parents getting home after midnight and leaving before breakfast), though this is often exaggerated for story reasons in anime.

{b}Profanity{/b} - rather than the use of dedicated curse words, one should probably read the use of profanity here as an english rendering of what, in Japanese, would merely be rude and uncouth language. Ai, specifically, speaks like the stereotype of a 70s juvenile delinquent.

{b}School debut{/b} - a recurring trope in anime is the attempt to change one's personal image when transitioning from junior high to high school. Students often go to a high school unconnected to their middle school (even when it's a public school), based on academic performance, entry test results, and the subjects they would prefer to focus on, so high school is often a very different set of peers than middle school. Some students try to drastically change their image for the first day of high school, and going overboard with this is a common gag.

{b}Senpai{/b} - an honorific applied to someone older or more experienced, usually indicating admiration.

{b}Sukeban{/b} - literal translation is something like {/i}girl boss{i}. The term technically refers to the leader of an all-girl gang, but it's strongly tied to a specific subculture of girl gangs that actually existed in some capacity from the late 1960s to the late 1970s, and any member of such a gang or anyone who adopts their distinctive style of dress -- school uniforms with extremely long skirts worn outside of school, carrying a wooden sword -- is commonly referred to as {/i}sukeban{i}. Sometimes also associated with the (very different) style of all-girl motorcycle gangs. The male version is a {/i}bancho{i}.

{b}Yakuza{/b} - Japanese organized crime. For historical reasons related to the development of the criminal justice system and the transition from feudal rule, organized crime syndicates are tolerated substantially more in Japan than elsewhere -- by the police, because they crack down on {/i}dis{i}organized crime and because Japanese police are notoriously corrupt, by politicians, because the yakuza syndicates form the backbone of local political campaigning organization, and by businesses, who often remain tied up deeply with their loans and protection rackets even after becoming successful. Most of the yakuza money is in legal or grey-legal forms of gambling (such as pachinko) or in totally legal loans to large businesses (like Nintendo) these days, and violence against outsiders is relatively rare & taboo. So, the syndicates make efforts to portray themselves as legitimate businesses & gain the favor of citizens.

{b}Yomiyama{/b} - the town of Yomiyama does not exist. The name {/i}Yomiyama{i} translates to something like {/i}hades mountain{i}, and is also used in the gothic death game franchise {/i}Another{i}. In this game, however, the town of Yomiyama is a composite of several fictional locations from Japanese media: {/i}Hinamizawa{i} from the {/i}Higurashi no Naku Koro Ni{i} games, Fuyuki from the {/i}Fate{i} franchise, and the unnamed country town in Michio Yamamoto's {/i}The Vampire Doll{i} (1970). It is in a valley surrounded on all sides by mountains, and is now mostly suburban with a built-up 'down town' strip near the university. Until the university began pulling in big government contracts in the early 1990s, this was a much poorer and more rural town whose economic center was a small US military base, but for about twenty years it has been economically ascending, out of phase with the rest of Japan; this makes the local yakuza syndicate comparatively powerful. Since the source of its wealth is mostly-secret government research (by both the United States and Japan), it has resisted the trend in the rest of rural Japan to seek tourists and immigration, and most of the families there are either associated with the university or have been there since before the second world war.

{b}Magic, mythology, and conspiracy{/b}

{b}Altar{/b} - a table upon which a magical working is performed, usually dedicated to a particular figure (a particular god, saint, demon, or in chaos magic, perhaps a celebrity or fictional character), and usually containing the four magical weapons. It is sometimes convenient to consider the altar itself to be the circle in which a ritual is performed, so that disturbing the ritual objects in a way that doesn't correspond to the working being performed is tantamount to closing the circle and banishing the entities you have called up.

{b}Calendar{/b} - the year wheel, used by wiccans and some other pagans, divides the year into four major pieces, with holidays at the solstices and equinoxes. The spring equinox is associated with May Day, while the fall equinox is associated with All Saint's Day (the day after Halloween). The eve of an equinox is also important because it's considered the point at which the separation between the mundane world and the world of magic and spirits is thinnest -- when magical rituals are at their most powerful and when ghosts and demons have the easiest time visiting us. May Eve (the day before May Day) is also called Walpurgisnacht and has a Halloween-like mythic association attached to it, being the traditional time of the gathering of witches in germanic and scandanavian countries.

{b}Janus{/b} - the roman god of threshholds. He has a young face on one side of his head and an old face on the other. In ritual magic of the western occult tradition he is called upon in conjunction with Saturn to manipulate time, and he is called upon alone in rituals that are about the manipulation of boundaries and transitions. {/i}The Janus Head{i} is also the name of {/i}Nosferatu{i} director F. W. Murnau's now-lost classic unauthorized silent film adaptation of {/i}The Strange Case of Doctor Jeckyll and Mister Hyde{i}, wherein a bust of Janus causes drastic personality changes in a previously honorable man.

{b}Masonry{/b} - speculative or spiritual masonry (as opposed to actual stonemasonry) is a set of institutions (including the royal arch and the scotch rite) that act as private clubs. Masonic institutions have a number of specific attributes: graded initiations (which is to say, members get titles based on seniority and there is a ritual that goes with each title), secret codes including handshakes and gestures, the use of specific construction-related symbols for spiritual or metaphysical ideas, and the 'mason word', itself a secret password. Pseudo-masonic lodges adopt some or all of these attributes without being officially sanctioned offshoots of the lodges of main-line freemasonry. During the eighteenth and nineteenth centuries, pseudo-masonry was extremely common in the west, making its way even into workers unions and technical guilds but absolutely dominating the schools of the western occult tradition (including the Order of the Golden Dawn and its offshoots, the Ordo Templi Orientis and Argentum Astrum). Occult lodges built upon masonic lines tend to be referred to by acronym, with a triangle of three dots between each letter (symbolizing the presence of the 'mason word'), and their physical architecture usually includes a black and white tiled hallway with a pillar on each side, one topped with a globe of the earth while the other is topped with a globe containing a star map. While masonic rituals forbid revealing their contents on penalty of death, their contents are widely published and easily found.

{b}OSS{/b} - Office of Strategic Services, a predecessor of the CIA.

{b}Ouraboros{/b} - a snake forming a circle by swallowing its own tail, an ancient symbol of cycles of renewal.

{b}The Phillip Experiment{/b} - in the 1970s, a group investigated the hypothesis that poltergeist phenomena were caused by the latent psychic abilities of living humans rather than the ghosts of dead humans by making up a plausible backstory for an imaginary ghost named Phillip and then summoning him with traditional seance techniques. A book was written on the subject of the experiment. According to this book, it was successful, and some seances with this imaginary spirit were broadcast on canadian television. While long out of print, The Phillip Experiment was very influential on modern tulpamancy by way of the practices around egregores and servitors in chaos magic in the 80s and 90s.

{b}Project Stargate{/b} - a CIA-funded program investigating the possibility of remote viewing & its applications in espionage, now declassified. It was one of the last of a long run of cold war attempts to use psychic powers for national security.

{b}Scriabin{/b} - an early 20th century composer and occultist. He was involved in the introduction of elements of jazz into modern classical music. He is also associated with the {/i}prometheus chord{i}, a set of notes that he incorporated into many of his works and to which he attributed occult significance, and with his claim that he had composed a work that, if performed, would bring about the apocalypse.

{b}Weapons{/b} - in the western occult tradition, there are four {/i}magical weapons{i}: the wand, the sword, the cup, and the pantacle. Sometimes, the wand is an arrow, the sword is a dagger, the cup is a chalice, and the pantacle is a tablecloth or a plate. There are complicated correspondences between these symbols and all sorts of other things, some of which differ by school. However, in all traditions, the wand and sword make active changes to the world while the cup and pantacle hold or absorb material. In other words, a sacrifice might be performed with the wand or sword and the result 
of that sacrifice stored in the cup.

{/i}

{b}Credits{/b}{i}

Concept, script, and programming by {a=http://www.lord-enki.net/}John Ohno{/a}


{b}Art{/b}
Placeholder art assets: John Ohno
Character art: {a=http://glitch.social/@ryusei}Ryusei{/a}
Background art: {a=http://mastodon.social/@cryptovexillologist}Cryptovexillologist{/a}

{b}Music{/b}
{a=http://infocalypse.nfshost.com}Infocalypse{/a}
{/i}""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "MannaforourMalices"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "music/Infocalypse_-_Manna_for_our_Malices.mp3"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = None


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

define build.itch_project = "enkiv2/manna-for-our-malices"

# Disable resize since our art looks even worse when scaled up
define config.gl_resize = False
# Number of save slots should be limited to 1, so that users won't save-scum
define config.quicksave_slots = 1
define config.autosave_slots = 1

