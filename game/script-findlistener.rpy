init python:    
    ListenerDescs = {
        'listener1' : ['lady', 'young woman'],
        'listener2' : [ 'kid', 'child', 'boy', ],
        'listener3' : [ 'cloaked figure', 'mysterious pal' ],
        'listener4' : [ 'young man', 'dude', 'soldier' ],
    }
    
    class Listener:                
        def __init__(self):
            self.amusement = renpy.random.random()*0.25 + 0.5
            self.gullibility = renpy.random.random() * 0.7
            self.perception = renpy.random.random() * 0.5 + 0.5 
            self.thirst = renpy.random.random()*0.2 + 0.1
            self.drink = 1
            self.graphic = renpy.random.choice(['listener1','listener2','listener3','listener4']);
            renpy.copy_images( self.graphic, "listener" );
            
            global l
            l = Character(self.desc.title())
            
        @property
        def desc(self):            
            return renpy.random.choice( ListenerDescs[self.graphic] )
            
    def contradiction_fail( score ):
        global l, os, a_listener
        a_listener.amusement += score * ( 1 - a_listener.gullibility )
        if a_listener.amusement <= 0:
            renpy.show( "listener" )
            l( "I had enough of your nonsense, old man.{p}This story is full of lies.I'm leaving." )
            renpy.hide( "listener" )
            renpy.say( "", "...and so the [a_listener.desc] left" )
            renpy.call( "find_listener" )
            renpy.show( "listener" )
            l( "Hey old man, can I get you something to drink." )
            os( "I can't refuse a good [a_listener.desc] like you." )
            os( "In return let me tell you a story..." )
            return True
        return False
        
    def notice_contradiction() :
        global a_listener
        return a_listener.perception >= renpy.random.random()

label find_listener:
    scene bg bar    
    os "Here I stand alone at the bar.{p}I'd better find someone to share my story and their with."
    jump .display    
        
label .display:
    $ sing_chance = renpy.random.random()
    $ dance_chance = renpy.random.random()    
    menu:        
        "sing":
            show oldsoldier sing
            $ display = "singing"
            if 0.5 > sing_chance:                
                jump .found_listener
        "dance":
            show oldsoldier dance
            $ display = "dancing"
            if 0.5 > dance_chance:                
                jump .found_listener
        "perform":
            show oldsoldier sing
            $ display = "performing"
            if 0.5 > sing_chance:                
                jump .found_listener
                
    os "All that [display] was for naught.{p}I have to try harder."
    jump .display
                
label .found_listener:
    $ a_listener = Listener()
    "Seems like a [a_listener.desc] got attracted by my [display]."
    hide oldsoldier
    return    
    