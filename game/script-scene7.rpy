label scene7:
    
    play music coast fadein 1
    os "Everything went well for the first few days, the winds were good and the sails strong"
    scene bg shipscene with dissolve    
    os "...but soon some of the men started to voice their doubts."
    l "Doubts? What did the men have doubts about?"
    play music shady fadein 1
    os "Odysseus.{p}Some of the men thought that the bag he received from Aeolus contained treasures that he was keeping for himself."
    
    l "Did you agree?"    
    menu:
        "Aye, I got greedy":
            $ a_listener.got_greedy = True
            os "Aye, regretfully greed got the better of me. The way he always held the bag so tightly made me believe it must contain something truly precious."
            l "Did you open the bag?"
        "No, I trusted Odysseus":
            $ a_listener.got_greedy = False
            os "No, Odysseus wouldn't keep something from us unless he had to."
            l "Did they open the bag?"        
    
    stop music fadeout 2
    os "Not at first, there was a lot of talk amongst the men as to when it should be done, it was undecided until Ithaca came into view."
    show bg ithaca with dissolve
    
    l "What happened once Ithaca was in sight?"    
    menu:
        "The men became greedy and stole the bag":
            play music badturn fadein 2
            os "The men who wanted to open the bag became mad with greed, they tore the bag from Odysseus."
            if notice_contradiction() and hasattr(a_listener, "got_greedy") and a_listener.got_greedy:
                l "I thought you wanted to open the bag too?"
                if contradiction_fail( -0.2 ):
                    jump scene6
                os "I had a change of heart."
        "It was our last chance to snatch the bag":
            play music badturn fadein 2
            os "We thought this was our last chance, that once we reached Ithaca Odysseus would have all the riches for himself. so we took the bag."
            if notice_contradiction() and hasattr(a_listener, "got_greedy") and not a_listener.got_greedy:
                l "I thought you didn't want to open the bag?"
                if contradiction_fail( -0.2 ): 
                    jump scene6
                os "I had a change of heart."
                
    l "What was inside the bag?"
    os "Inside the bag were all the winds except the western wind. Aeolus had given them to Odysseus so they wouldn't be bale to blow us off course."
    l "What happened once the bag had been opened?"
    show bg stormyscene:
    os "A storm was unleashed. It threw our ships back and forth."    
    os "We were blown all the way..."
    show bg aeolia with pixellate    
    os "..back to floating islands of Aeolus. Our journey would have ended had it not been for greed."
    stop music fadeout 2
    l "What happened next?"
    os "Well, that, [a_listener.desc], is a story for another day."
    jump outro