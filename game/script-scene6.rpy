label scene6:    
    scene bg shipscene
    
    os "We were moving forth at sea as we saw a shimmer in the distance."
    os "We had no idea what it was, as we drew nearer it seemed to be land,{p}but in the sky..."
    show bg aeolia with pixellate
    l "Was there anything on the islands?"
    os "They were the home of Aeolus, the ruler of the winds.{p}We dropped achors and decided to land."
    l "How did you get on to the islands if they were in the sky?"
    os "With great difficulty!{p}We used ropes to climb up to the island closest to the sea,"
    os "and then we created a series of bridges and ladders between the islands."
    
    l "What was at the top?"        
    menu:
        "A palace made of crystal":
            os "A magnificent palace made of crystal, it glistened in the sun like the ocean at sunset."
            l "Was Aeolus inside?"
            os "Aye, he sat on a throne that reached into the heavens, he seemed annoyed by our presence."
            $ a_listener.aeolus_pleased = False
        "A tree with golden leaves":
            os "A beautiful tree with golden leaves, the wind seemed to dance around it."
            l "Where was Aeolus?"
            os "He sat at the base of the tree with his mind deep in thought. Once he noticed we were there he looked pleased."
            $ a_listener.aeolus_pleased = True        
            
    l "What happened next?"
    menu:
        "He indroduced himself and greeted each of us":
            os "He stood up, introduced himself, then greeted each man individually."              
            if notice_contradiction() and hasattr(a_listener, "aeolus_pleased") and not a_listener.aeolus_pleased:
                l "That doesn't sound right, you said he seemed annoyed that you were there?"    
                os "Oh yes of course, my mistake...{p=0.5}he demanded we introduce ourselves and explain our intrusion into his domain."
                if contradiction_fail( -0.1 ): 
                    jump scene6            
            
        "He demanded we explain our intrusion immediately":
            os "Aeolus demanded we introduce ourselves and explain our intrusion into his domain."            
            if notice_contradiction() and hasattr(a_listener, "aeolus_pleased") and a_listener.aeolus_pleased:
                l "Wait, I thought you said he was pleased when he saw you?"
                os "Oh yes, what I meant to say was...{p=0.5}He stood up, introduced himself, then greeted each man individually."
                if contradiction_fail( -0.1 ): 
                    jump scene6
                    
    l "What did he do next?"
    os "He wished to speak to our leader, Odysseus stepped forward, and then they left together."
    l "Where did they go?"
    os "I don't know, one minute they were there and the next they were not."
    l "Did Odysseus return?"
    os "Of course, they both did. Odyssesus was clutching a leather bag tightly.\nAeolus gave us a westerly wind, and used his power to lift us all back to the ships."
    os "He said that if we would be home in Ithaca within ten days."
    l "Were you?"
    os "Not exactly..."
    jump scene7