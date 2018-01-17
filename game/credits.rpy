define credit = Character(None, kind=nvl_narrator, what_prefix="{center}{cps=2}{b}{size=72}", what_suffix="{/size}{/b}{/cps}<vspace=160}{/center}")
label credits:
    scene bg black
    play music "music/Infocalypse_-_Hawkhead_Falconer.mp3"
    credit "Story: John Ohno (http://www.lord-enki.net)"
    extend "Music: John Ohno / Infocalypse (http://infocalypse.ignorelist.com)"
    extend "Background images: John Ohno"
    extend "Original character art: John Ohno"
    extend "New character art: Ryusei (http://glitch.social/@ryusei)"
    credit "A Double Mojo Production"
    $ achievement.grant("Complete")
    return

