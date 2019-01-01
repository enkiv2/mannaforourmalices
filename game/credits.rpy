# Ending credits
define credit = Character(None, kind=nvl_narrator, what_prefix="{cps=2}{b}{size=72}", what_suffix="{/size}{/b}{/cps}\n{vspace=160}", xalign=0.5, yalign=0.5)
label credits:
    scene bg black
    play music "music/Infocalypse_-_Hawkhead_Falconer.mp3"
    credit "Story: {a=http://www.lord-enki.net}John Ohno{/a}"
    credit "Music: {a=http://infocalypse.nfshost.com}John Ohno / Infocalypse{/a}"
    credit "Placeholder art assets: John Ohno"
    credit "Character art: {a=http://glitch.social/@ryusei}Ryusei{/a}"
    credit "Background art: {a=http://mastodon.social/@cryptovexillologist}Cryptovexillologist{/a}"
    credit ""
    credit "A Double Mojo Production"
    $ achievement.grant("Complete")
    return

