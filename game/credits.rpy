# Ending credits
define credit = Character(None, kind=nvl_narrator, what_prefix="{center}{cps=2}{b}{size=72}", what_suffix="{/size}{/b}{/cps}\n{vspace=160}{/center}")
label credits:
    scene bg black
    play music "music/Infocalypse_-_Hawkhead_Falconer.mp3"
    credit "Story: John Ohno (http://www.lord-enki.net)"
    extend "Music: John Ohno / Infocalypse (http://infocalypse.ignorelist.com)"
    extend "Placeholder art assets: John Ohno"
    extend "Character art: Ryusei (http://glitch.social/@ryusei)"
    extend "Background art: Cryptovexillologist (http://mastodon.social/@cryptovexillologist)"
    credit "A Double Mojo Production"
    $ achievement.grant("Complete")
    return

