image bg imarosshore = "bg/bg ithaca.png"

label scene1:        
    hide listener
    scene bg shipscene with dissolve
    
    os "The twelve ships of Odysseus left Troy while the ashes of the city still fell."
    os "Odysseus wanted to waste no time in getting home to his beloved family and homeland of Ithaca."
    
    l "You were heading for Ithaca?"
    os "Ay that was the plan, but..."
    
    menu:
        "The winds sent us off course":
            scene bg stormyscene with slideawaydown
            os "...the winds took hold of the ships, sent us far off course."
            $ a_listener.off_course_by = "winds"

        "The waves drove us off course":
            scene bg stormyscene with slideawaydown
            os "...Poseidon had another idea. The tides were against us and we were driven off course."
            $ a_listener.off_course_by = "tides"
    
    l "What happened next?"
    
    menu:
        "When the waves calmed, we set for an island":
            scene bg imarosshore with pixellate
            os "Once the waves had calmed we set a course for the nearest island."
            if notice_contradiction() and hasattr(a_listener, "off_course_by") and a_listener.off_course_by == "winds":
                l "I thought you said it was the winds that took you off course?"
                os "Nonsnse, I clearly remember I said \"waves\"."
                if contradiction_fail( -0.2 ): 
                    jump scene1
                
        "We set for the nearest port after the winds subsided":
            scene bg imarosshore with pixellate
            os "Once the winds had subsided we laid a course for the nearest port."
            if notice_contradiction() and hasattr(a_listener, "off_course_by") and a_listener.off_course_by == "tides":
                l "I thought you said it was the tides that threw you off course?"
                os "What? Oh, yes of course..."
                if contradiction_fail( -0.2 ): 
                    jump scene1
                
    jump scene2    
    