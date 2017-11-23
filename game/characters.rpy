######################### CHARACTER DEFINITIONS

# The 'comment' character is for in-game reminders of TODO issues, during dev
# Remember to remove it before shipping to make sure we have the script completed!
define comment = Character("Comment")
define quote = nvl_narrator

# Ai has two character objects: 'n', used for internal monologue, and 'ai', 
# used for speech.
# NB: 'n' is used with extend + bold to represent 'current Ai', when arguing
# with 'ghost Ai'.
image ai_icon = "ai_icon.png"
define n = Character("Akagi Ai", what_prefix="{i}", what_suffix="{/i}", image="ai_icon")
define ai = Character("Akagi Ai", color="#000000", image="ai_icon")

image aoi_icon = "aoi_icon.png"
define aoi = Character("Tomoe Aoi", color="#0000af", image="aoi_icon")
image aoi happy = "aoi.png"
image aoi hearteyes = "aoi hearteyes.png"
image aoi pout = "aoi akimbo.png"
image aoi blush = "aoi blush.png"
image aoi yandere = "aoi yandere.png"

image kuroneko_icon = "kuroneko_icon.png"
define kuroneko = Character("Fujinomiya Kuroneko", color="#aa0000", image="kuroneko_icon")
image kuroneko normal = "kuroneko.png"
image kuroneko pout = "kuroneko.png" # XXX
image kuroneko happy = "kuroneko smile.png"

image shironeko_icon = "shironeko_icon.png"
define shironeko = Character("Fujinomiya Shironeko", color="#77aaaa", image="shironeko_icon")
image shironeko happy = "shironeko happy.png"
image shironeko normal = "shironeko.png"
image shironeko pout = "shironeko pout.png"
image shironeko surprised = "shironeko surprised.png"

image koneko_icon = "koneko_icon.png"
define koneko = Character("Fujinomiya Koneko", color="#777700", image="koneko_icon")
image koneko normal = "koneko.png"
image koneko happy = "koneko smile.png"
image koneko pout = "koneko pout.png"

image mimi_icon = "mimi_icon.png"
define mimi = Character("Yamada Mimi", color="#ff7777", image="mimi_icon")
image mimi normal = "mimi.png"
image mimi angry = "mimi angry.png"
image mimi pensive = "mimi pensive.png"
image mimi smug = "mimi smug.png"
image mimi scoop = "mimi scoop.png"

image misa_icon = "misa_icon.png"
define misa = Character("Umeji Misa", color="#77ff77", image="misa_icon")
# Misa: UFO cultist, appears to be pure / yamato nadeshiko type character
# UFO cult worships aryan space brothers; cult leader doesn't believe in it & uses cultists as cheap labor
# Misa believes in the divinity of the space brothers because of direct contact (with the tentacle aliens that the YIPI brought, pretending to be space bros)
