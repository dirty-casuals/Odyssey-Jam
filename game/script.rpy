# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define os = Character("Old Soldier")
define l = Character("Listener")

transform midleft:  
  anchor (0.25, 1.0)
  pos (0.25, 1.0)

transform midright:
  anchor (0.75, 1.0)
  pos (0.75, 1.0)
    
transform dropdown:
    ypos 0
    linear 10 ypos 100

define fogfadein = Dissolve(2.0)
define fogfadeout = Dissolve(4.0)
image cyclopsA = "char/cyclops.png"
image cyclopsB = "char/cyclops.png"
image oldsoldier = "char/speaker1.png"

define audio.calm = "music/seaside.ogg"
define audio.disturbance = "music/forth-to-adventure.ogg" 
define audio.dilema = "music/creepy-wahwah.ogg"
define audio.coast = "music/village-on-the-coast.ogg"
define audio.buildup = "music/march-unto-war.ogg"
define audio.combat = "music/march-unto-war-part2.ogg"
define audio.spooky = "music/creepy-ghost.ogg"
define audio.crucial = "music/slow-vampire.ogg"
define audio.badturn = "music/church-chorus.ogg"
define audio.shady = "music/somber-night.ogg"
    
image bg shipscene:
    "bg/bg ship.png"
    zoom 1.1
    xalign 0.5 
    yalign 0.5
    linear 5 rotate 2
    linear 5 rotate -2
    alignaround (.5, .5)
    repeat
    
image bg stormyscene:
    "bg/bg stormysea.png"
    zoom 1.1
    xalign 0.5 
    yalign 0.5
    ease 2 rotate 3
    ease 2 rotate -3
    alignaround (.5, .5)
    repeat

# The game starts here.

label start:
    $ a_listener = Listener()
    
   
    jump intro
    #jump find_listener
    #jump outro
    return
