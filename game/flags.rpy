######################## STATUS FLAGS
# Ai route
define died = False
$ achievement.register("Stabbed in the back")
define num_deaths=0
$ achievement.register("Some chuunibyo BS") # >2 deaths
define midnight_loop = False
define in_2011 = False
$ achievement.register("Niaga praw emit eht od s'tel") # Warped to Halloween 2011
define halloween_janus_head_inverted = False
# Kuroneko's route unlocks some clues about the mechanisms by which the out of body time warp works.
# Objects or boundaries can be destroyed; one object shifts the time frame from May Eve 2012 to Halloween 2011,
# while another stops reincarnation entirely. Having another character get stabbed by the ceremonial knife will bring
# them into the time loop with you, and allow some state to be persistent with them. The good end involves warping back
# and forth between Halloween 2011 and May Eve 2012 to set things right (for instance, using knowledge about the 
# Yakuza group the Fujinomia family is indebted with, gained via their Halloween party) and setting the various 
# conspiracies against each other before breaking the time loop mechanism. Breaking the mechanism without fixing 
# all the conspiracies & rendering them harmless causes a bad end.
# Good end is a scene at the town's May Day festival. May day festivals would have been considered politically dangerous
# in Japan for a while, so maybe we can fill in why this one was allowed to exist in backstory.
define altar_destroyed = False
$ achievement.register("Bad end")
$ achievement.register("Tama-ya!")
$ achievement.register("Complete")

# Aoi route
define knows_about_aoi_parents = False
$ achievement.register("A mysterious photograph")
define knows_about_missing_lab_notebook = False
# The knows_about_missing_lab_notebook flag opens up several options:
# * one that makes us able to hide in the science club room's locker after school and verify that Aoi took the book
define knows_aoi_took_lab_notebook = False
$ achievement.register("In the closet")
# * one that makes us able to ask shironeko about the 1993 Z-Prize (like trying to get the papers entered)
define read_z_prize_papers = False
$ achievement.register("Peer review")
# * one that lets us skip school at the very beginning of the game by climbing out the window to go investigate in person at Yomiyama Poly's research facility
# That last one branches out: we get killed by a guard having a smoke break behind a pole when we go straight into the employees-only area,
# which opens up a new option to hide behind a neighbouring pole until the guard leaves to do rounds.
define knows_poly_guard_position = False
# We then go up against a keypad lock.
define knows_about_keypad = False
# We inevitably get killed here but now that we know there's a keypad lock we can dare shironeko to get the combination (which will be randomly 
# generated and then stored in persistent storage, so that it's unique to the game copy but the same each time we ask her)
define keycode_try = "0000" # this is input
define keycode_success = False
define keycode = False # this is defined in a python block in start
# Entering the code lets us enter the facility where we eventually find the clone racks. Aoi, who has followed us, kills us here.
define knows_about_clone_racks = False
# Following that death if we do the same operation we open up dialogue trees that will allow us to get Aoi's backstory & info about the clones.
# (But some of the info about the clones should be able to come from getting a copy of the paper from shironeko -- a proposal that probably has 
# fully disconnected cerebellums instead of hypoxic cerebellums. It will be hard to explain the technical details of the cloning in a way consistent
# with even yandere-mode Aoi.)
define knows_whole_aoi_story = False
define aoi_unstuck_in_time = False

# Kuroneko route
define knows_about_kuroneko_concert = False
$ achievement.register("Some Eyes-Wide-Shut MFers")
define knows_about_kuroneko_books = False
define knows_about_oss = False
define knows_kuroneko_book_list = False
define knows_masonic_initiation_phrase = False
define knows_about_scriabin = False
define knows_about_janus = False
define kuroneko_unstuck_in_time = False

# Koneko route
define knows_about_koneko_telepathy = False
$ achievement.register("Touch telepathy")
define saw_milpsi_symbol = False
define knows_about_stargate = False
define knows_milpsi_shell_co_name = False
define koneko_unstuck_in_time = False

# Shironeko route
define knows_about_alien_tech = False
$ achievement.register("The truth is out there")
