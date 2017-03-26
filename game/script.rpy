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


image listener1_ sweat:
    contains:
        "char/listener1.png"
    contains:
        "fx/drop.png"

image listener2_ sweat:
    contains:
        "char/listener2.png"
    contains:
        "fx/drop.png"
    
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
    #jump scene4            
    return

    