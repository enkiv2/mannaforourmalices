# Ending credits
define credit = Character(None, kind=nvl_narrator, what_prefix="{cps=2}{b}{size=72}", what_suffix="{/size}{/b}{/cps}\n{vspace=160}", xalign=0.5, yalign=0.5)
label credits:
    scene bg black
    play music "music/Infocalypse_-_Hawkhead_Falconer.mp3"
    credit "Story: {a=http://www.lord-enki.net}John Ohno{/a}"
    extend "Music: {a=http://infocalypse.nfshost.com}John Ohno / Infocalypse{/a}"
    extend "Placeholder art assets: John Ohno"
    extend "Character art: {a=http://glitch.social/@ryusei}Ryusei{/a}"
    extend "Background art: {a=http://mastodon.social/@cryptovexillologist}Cryptovexillologist{/a}"
    credit "A Double Mojo Production"
    $ achievement.grant("Complete")
    return

