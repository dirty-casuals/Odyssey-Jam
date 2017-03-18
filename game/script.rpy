# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define os = Character("Old Soldier")
define l = Character("Listener")

# The game starts here.

label start:
    $ a_listener = Listener()
    
    #jump find_listener
    jump intro            
    return
