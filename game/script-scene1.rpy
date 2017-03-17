label scene1:        
    hide listener
    scene bg ithaca
    
    os "The twelve ships of Odysseus left Troy while the ashes of the city still fell."
    os "Odysseus wanted to waste no time in getting home to his beloved family and homeland of Ithaca."
    
    l "You were heading for Ithaca?"
    os "Ay that was the plan, but..."
    
    menu:
        "The winds sent us off course":
            os "...the winds took hold of the ships, sent us far off course."
            $ a_listener.off_course_by = "winds"
        "The waves drove us off course":
            os "...Poseidon had another idea. The tides were against us and we were driven off course."
            $ a_listener.off_course_by = "tides"
    
    l "What happened next?"
    
    menu:
        "When the waves calmed, we set for an island":
            os "Once the waves had calmed we set a course for the nearest island."
            if hasattr(a_listener, "off_course_by") and a_listener.off_course_by == "winds":
                l "I thought you said it was the winds that took you off course?"
                os "Nonsnse, I clearly remember I said \"waves\"."
        "We set for the nearest port after the winds subsided":
            os "Once the winds had subsided we laid a course for the nearest port."
            if hasattr(a_listener, "off_course_by") and a_listener.off_course_by == "tides":
                l "I thought you said it was the tides that threw you off course?"
                os "What? Oh, yes of course..."
                
    jump scene2