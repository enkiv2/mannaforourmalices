# Ending credits
define credit = Character(None, kind=nvl_narrator, what_prefix="{color=#fff}{cps=2}{b}{size=72}", what_suffix="{/size}{/b}{/cps}\n{/color}", xalign=0.5, yalign=0.5)
label credits:
    scene bg black
    play music "music/Infocalypse_-_Hawkhead_Falconer.mp3"
    credit "Story: {a=http://www.lord-enki.net}John Ohno{/a}"
    scene bg black
    credit "Music: {a=http://infocalypse.nfshost.com}John Ohno / Infocalypse{/a}"
    scene bg black
    credit "Placeholder art assets: John Ohno"
    scene bg black
    credit "Character art: {a=http://glitch.social/@ryusei}Ryusei{/a}"
    scene bg black
    credit "Background art: {a=http://mastodon.social/@cryptovexillologist}Cryptovexillologist{/a}"
    scene bg black
    credit ""
    scene bg black
    credit "A Double Mojo Production"
    $ achievement.grant("Complete")
    return

