# Festival (good end)
label festival:
    play music "music/Infocalypse_-_scathing_frolic.mp3"
    scene bg downstairs
    "Mom" "Ai-chan, are you ready? Aoi-chan's already waiting!"
    ai "Yeah, just making some final adjustments."
    "The day after the incident, things calmed down almost immediately. I think the Others might have done us a favor and fogged some memories."
    ai "Alright, here I come!"
    "Mom" "Ai-chan, you look great in a yukata. Why don't you wear traditional clothes more often?"
    ai "Same reason you don't."
    show aoi yukata
    aoi "Ai-chan, you're beautiful!"
    ai "Thank you! Yours suits you too!"
    show aoi yukata blush
    aoi "Shall we?"
    ai "We shall."
    "Mom" "Oh, before you go -- I heard some news. That syndicate broke apart. You know, the one you used to go to for halloween? Such nice young men."
    ai "They were gangsters, mom."
    "Mom" "Even so! But it was funny. Apparently they schismed because of accusations that somebody embezzled 60 million yen."
    "Mom" "Nice house like that, you'd think they could afford to lose 60 million yen here and there."
    ai "Get to the point! I wanna eat the takoyaki while it's hot."
    "Mom" "Well anyway, don't go down there this year. It'll probably be dangerous."
    ai "Ok, I'll keep that in mind in six months."
    show bg street
    show aoi yukata
    aoi "Festival~ Festivall~~~"
    ai "It's nice to enjoy the simple things in life once in a while."
    aoi "Good takoyaki isn't simple! Those people are artists."
    ai "Tell them that and they might even give you a discount."
    play music "music/honey.mp3"
    scene bg festival
    show kuroneko yukata at right
    kuroneko "Just who I was looking for! Get caught in traffic?"
    ai "My dear mother instructed us on current events. Apparently the yakuza are having a falling out over your tuition."
    show kuroneko yukata smile at right
    kuroneko "Serves 'em right."
    ai "So, is Koneko-chan here?"
    kuroneko "Down, girl. That's my sister, ya perv."
    show aoi yukata hearteyes at left
    aoi "I don't mind sharing you with Koneko-san, as long as you're still my Ai-chan forever~~"
    ai "You guys, come on. It's not like that."
    kuroneko "It sure looks like that to me."
    show aoi yukata pout at left
    "Aoi gives an exaggerated nod"
    ai "She's just... She's earnest and she tries really hard. It makes you want to protect her, you know? Like a kitten or something."
    kuroneko "Well, she's here but not with us. She came with her new boyfriend. Somebody from that facility."
    ai "That makes sense. Well, good for her."
    "A few stalls down on the far side, Mimi was kneeling at the goldfish game."
    ai "Hey, Aoi. Wanna catch me some goldfish?"
    show aoi yukata hearteyes at left
    aoi "WOULD I?!"
    hide aoi
    "Aoi ran off down the path."
    kuroneko "That was certainly an adventure."
    ai "It was a fucking trip. You don't know the half of it."
    kuroneko "You think this town has any more secrets?"
    show aoi yukata
    show mimi yukata at left
    "Just then, Aoi returned with a bag full of goldfish in one arm and a blushing Yamada Mimi in the other."
    aoi "Look who I found!"
    mimi "G-Good evening."
    "I wink at Mimi. She scrunches her face in mock anger."
    ai "So the gang's pretty much all accounted for. I assume Shironeko-san's at home?"
    kuroneko "No way. Knowing her, she's already won all the prizes in the shooting gallery and is lording them over passing children."
    hide mimi
    show shironeko yukata at left
    shironeko "You underestimate me. No, I sold them back to the proprietor for double what I paid to shoot."
    hide mimi
    hide shironeko
    hide aoi
    show shironeko yukata
    show kuroneko yukata pout at left
    koneko "Anee, you're rotten."
    kuroneko "Where's your beau?"
    koneko "Decompressing. Hard for him in crowds."
    ai "Makes sense."
    hide kuroneko
    show mimi yukata at right
    mimi "It does?"
    "Just then, all the stall lights went out."
    play sound "sfx/fireworks.wav"
    "{b}Pop pop pop{/b}"
    "{b}BOOM{/b}"
    window hide
    scene splash fireworks with dissolve
    pause 2
    $ achievement.grant("Tama-ya!")
    call screen confirm("Do you want to save?", yes_action=[ShowMenu("save"), Return()], no_action=Return())
    jump credits
