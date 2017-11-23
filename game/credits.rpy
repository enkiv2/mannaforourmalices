define credit = Character(None, kind=nvl_narrator, what_prefix="{cps=2}{b}{size=72}", what_suffix="{/size}{/b}{/cps}<vspace=160}")
label credits:
    play music "music/Infocalypse_-_Hawkhead_Falconer.mp3"
    credit "Story: John Ohno"
    credit "Music: John Ohno / Infocalypse"
    credit "Art: John Ohno"
    credit "A Double Mojo Production"
    $ achievement.grant("Complete")
    return

