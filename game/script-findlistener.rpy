init python:    
    class Listener:
        def __init__(self):
            self.amusement = renpy.random.random()*0.25 + 0.5
            self.gullibility = renpy.random.random()
            self.perception = renpy.random.random()
            self.thirst = renpy.random.random()*0.2 + 0.1
            self.drink = 1
            self.desc = renpy.random.choice(['kid', 'child', 'lady', 'young woman'])
        

label find_listener:
    scene bg bar    
    os "And here I stand alone at the bar.{p}I'd better find someone to share my story and their with."
    jump .display    
        
label .display:
    $ sing_chance = renpy.random.random()
    $ dance_chance = renpy.random.random()    
    menu:        
        "sing":
            show old man sing
            $ display = "singing"
            if 0.3 > sing_chance:                
                jump .found_listener
        "dance":
            show old man dance
            $ display = "dancing"
            if 0.3 > dance_chance:                
                jump .found_listener
        
    os "All that [display] was for naught.{p}I have to try harder."
    jump .display
                
label .found_listener:
    $ listener = Listener()
    "Seems like a [listener.desc] got attracted by my [display]."
