###################### SCRIPT
# Manna for our Malices (c) 2017-2019 John Ohno
# The game starts here.
label start:
    python:
        from random import Random
        random=Random()
        if not keycode:
            keycode="".join([str(random.choice(range(0, 10))),str(random.choice(range(0, 10))),str(random.choice(range(0, 10))),str(random.choice(range(0, 10)))]) 
    #quote "DEBUG: [keycode]"
    $ renpy.movie_cutscene("trailer.avi")
    if not persistent.saw_trailer:
        $ renpy.movie_cutscene("trailer.avi")
        $ persistent.saw_trailer = True
    play music "music/Infocalypse_-_yesterday_the_shadows_grew_again.mp3"
    window hide
    scene bg black
    centered "{color=#fff}{cps=15}\"The outrageous is the reasonable, if introduced politely.\"{/cps}{/color}"
    extend "{color=#fff}{cps=15}\n{space=500}- Charles Fort,{/cps}{/color}"
    extend "{color=#fff}{cps=15}\n{space=400}The Book of the Damned{/cps}{/color}"
    scene bg white with dissolve
    scene bg black with dissolve
    centered "{color=#fff}{cps=20}In the year 2012, in the small town of Yomiyama, a series of deaths occurred.{/cps}{/color}"
    extend "{color=#fff}{cps=20}\nDespite investigation, many mysteries remain.{/cps}{/color}"
    extend "{color=#fff}{cps=20}\nBelow the surface of this town, a great deal of machinery was in motion.{/cps}{/color}"
    window show
    jump core_story

