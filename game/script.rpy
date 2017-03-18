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
    
    

# The game starts here.

label start:
    $ a_listener = Listener()
    
    #jump find_listener
    jump intro            
    return
