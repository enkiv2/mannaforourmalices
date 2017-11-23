define credit = Character(None, kind=centered, what_prefix="{cps=2}{b}{size=72}", what_suffix="{/size}{/b}{/cps}<vspace=160}")
label credits:
    scene bg black
    play music "music/Infocalypse_-_Hawkhead_Falconer.mp3"
    credit "Story: John Ohno"
    extend "Music: John Ohno / Infocalypse"
    extend "Art: John Ohno"
    credit "A Double Mojo Production"
    $ achievement.grant("Complete")
    return

