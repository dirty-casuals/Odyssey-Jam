label intro:        
    scene bg bar
    show listener at right

    #"I tell them a story, they sip me a drink.\nIt's how it works."

    l "Woah friend, that is a serious looking scar you have there.{p}How did you get it?"
    
    menu: 
        "I got it during the war.":
            os "I got it during the Trojan War."
        "A Trojan gave it to me.":
            os "A Trojan gave it to me.{p}I gave him something in return."
        "I cut myself shaving...":
            os "I cut myself shaving when I was in Troy."
            
    l "You were in the Trojan War? Who did you serve?"
    os "I served under Odysseus of Ithaca."
    l "Odysseus of Ithaca?! He's a legend!{p}I'm sure you must have heroic tales from the war?"
    
    menu:
        "Those happened after the war!":
            os "Heroic tales? Those, [a_listener.desc], happened after we left Troy!"
        "There are no heroes in war.":
            os "There are no heroes in war. If you want to hear a story,{p}you should hear of the journey home from Troy."
        "The war was just the start.":
            os "The Trojan War was just the start of Odysseus' troubles,{p}that's where the real story lies!"
            
    l "What happened old timer?"
    l "Here, let me re-fill your cup."
    jump scene1