# Ending credits
label credits:
    window hide
    scene bg black with dissolve
    play music "music/Infocalypse_-_Hawkhead_Falconer.mp3"
    centered "{cps=5}{color=#fff}Story: {a=http://www.lord-enki.net}{color=#fff}John Ohno{/color}{/a}{/color}{/cps}"
    scene bg black with dissolve
    centered "{cps=5}{color=#fff}Music: {a=http://infocalypse.nfshost.com}{color=#fff}John Ohno / Infocalypse{/color}{/a}{/color}{/cps}"
    scene bg black with dissolve
    centered "{cps=5}{color=#fff}Placeholder art assets: John Ohno{/color}{/cps}"
    scene bg black with dissolve
    centered "{cps=5}{color=#fff}Character design & sketches: {a=http://glitch.social/@ryusei}{color=#fff}Ryusei{/color}{/a}{/color}{/cps}"
    scene bg black with dissolve
    centered "{cps=5}{color=#fff}Character art inking & coloring: John Ohno{/color}{/cps}"
    scene bg black with dissolve
    centered "{cps=5}{color=#fff}Background art: {a=http://mastodon.social/@cryptovexillologist}{color=#fff}Cryptovexillologist{/color}{/a}{/color}{/cps}"
    scene bg black with dissolve
    centered "{cps=5}{color=#fff}Sound effect: \"Fireworks, Standard, A.wav\" by InspectorJ (www.jshaw.co.uk) of Freesound.org{/color}{/cps}"
    centered ""
    scene bg black with dissolve
    centered "{cps=2}{color=#fff}A {/color}{color=#f00}D{/color}{color=#fa0}o{/color}{color=#ff0}u{/color}{color=#0f0}b{/color}{color=#00f}l{/color}{color=#f0f}e {/color}{color=#f00}M{/color}{color=#0f0}o{/color}{color=#ff0}j{/color}{color=#f0f}o{/color}{color=#fff} Production{/color}{/cps}"
    $ achievement.grant("Complete")
    call screen confirm("Do you want to save?", yes_action=[ShowMenu(save), Return()], no_action=Return())
    window show
    return

