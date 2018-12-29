######################### CHARACTER DEFINITIONS

# The 'comment' character is for in-game reminders of TODO issues, during dev
# Remember to remove it before shipping to make sure we have the script completed!
define comment = Character("Comment")
define quote = nvl_narrator

# Ai has two character objects: 'n', used for internal monologue, and 'ai', 
# used for speech.
# NB: 'n' is used with extend + bold to represent 'current Ai', when arguing
# with 'ghost Ai'.
image side ai = "ai_icon.png"
define n = Character("Akagi Ai", what_prefix="{i}", what_suffix="{/i}", image="ai")
define ai = Character("Akagi Ai", color="#000000", image="ai")

image side aoi = "aoi_icon.png"
define aoi = Character("Tomoe Aoi", color="#0000af", image="aoi")
image aoi normal = "aoi.png"
image aoi happy = "aoi.png"
image aoi hearteyes = "aoi hearteyes.png"
image aoi pout = "aoi akimbo.png"
image aoi blush = "aoi blush.png"
image aoi yukata happy = "aoi yukata.png"
image aoi yukata hearteyes = "aoi yukata hearteyes.png"
image aoi yukata pout = "aoi yukata akimbo.png"
image aoi yukata blush = "aoi yukata blush.png"
image aoi nekomimi happy = "aoi nekomimi.png"
image aoi nekomimi hearteyes = "aoi nekomimi hearteyes.png"
image aoi nekomimi pout = "aoi nekomimi akimbo.png"
image aoi nekomimi blush = "aoi nekomimi blush.png"
image aoi yandere = "aoi yandere.png"
image aoi yandere2 = "aoi yandere2.png"

image side kuroneko = "kuroneko_icon.png"
define kuroneko = Character("Fujinomiya Kuroneko", color="#aa0000", image="kuroneko")
image kuroneko = "kuroneko.png"
image kuroneko normal = "kuroneko.png"
image kuroneko pout = "kuroneko.png" # XXX
image kuroneko happy = "kuroneko smile.png"
image kuroneko yukata normal = "kuroneko yukata.png"
image kuroneko yukata pout = "kuroneko yukata.png" # XXX
image kuroneko yukata happy = "kuroneko yukata smile.png"

image side shironeko = "shironeko_icon.png"
define shironeko = Character("Fujinomiya Shironeko", color="#77aaaa", image="shironeko")
image shironeko = "shironeko.png"
image shironeko happy = "shironeko happy.png"
image shironeko normal = "shironeko.png"
image shironeko pout = "shironeko pout.png"
image shironeko surprised = "shironeko surprised.png"

image side koneko = "koneko_icon.png"
define koneko = Character("Fujinomiya Koneko", color="#777700", image="koneko")
image koneko = "koneko.png"
image koneko normal = "koneko.png"
image koneko happy = "koneko smile.png"
image koneko pout = "koneko pout.png"
image koneko yukata normal = "koneko yukata.png"
image koneko yukata happy = "koneko yukata smile.png"
image koneko yukata pout = "koneko yukata pout.png"

image side mimi = "mimi_icon.png"
define mimi = Character("Yamada Mimi", color="#ff7777", image="mimi")
image mimi = "mimi.png"
image mimi normal = "mimi.png"
image mimi angry = "mimi angry.png"
image mimi pensive = "mimi pensive.png"
image mimi smug = "mimi smug.png"
image mimi scoop = "mimi scoop.png"
image mimi yukata = "mimi yukata.png"
image mimi yukata angry = "mimi yukata angry.png"
image mimi yukata pensive = "mimi yukata pensive.png"
image mimi yukata smug = "mimi yukata smug.png"
image mimi yukata scoop = "mimi yukata scoop.png"

image side null = "side_null.png"

