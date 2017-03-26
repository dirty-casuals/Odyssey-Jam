label scene5:
    scene bg stormyscene:
    play music disturbance
    os "We were caught in a great storm, it blew us off course, further out to sea. We became lost."
    l "Lost? Surely you had navigators? Couldn't they use the stars to guide you?"
    os "I'm sure they could have had we seen any stars. The storm lasted days. We were at the mercy of the sea."
    l "Did the storms ease?"
    
    menu:
        "Aye, after a few days the wind stopped":
            show bg ship with dissolve
            stop music fadeout 2
            os "Aye, after a few days the tides died down and the wind stopped...\nBut they never picked up."
            os "We stood and waited"
        "We got stuck in the doldrums.":
            os "Too much so! We were stuck in the doldrums."
            l "The doldrums?"
            show bg ship with dissolve
            stop music fadeout 2
            os "It's a nautical term, it means there was no wind to blow the sails,\n not tide to push the ship. We were floating island of wood."
            
    play music spooky fadein 4
    os "It felt like an age had passed.\nWe were dead in the water."
    l "What did you do?"
    os "Odysseus called a meeting of all the ships captains to discuss how we would escape."
    l "Did you go?"
        
    menu:
        "No, I stayed on the ship":
            os "Me? No, I wasn't a captain. I stayed on the ship and waited to hear what was going on."
            l "So what happened in the meeting?"
            os "I don't know exactly, because I wasn't there."
            l "What was decided?"
            os "Odysseus came back to the ship, he said we would row the ships until we found a wind."
            os "Then men weren't pleased but understood that it was the only way home."
            jump .after_plan
        "Aye, I rowed the boat for Odysseus":
            os "Aye, I rowed the boat for Odysseus to take him to the meeting in the most central ship."
            l "What happened in the meeting?"
            os "The ship captains discussed with Odysseus our options on how to escape our situation."
            
    l "What were the options?"    
    menu:
        "Row the ships":
            $ a_listener.wait_for_wind = False
            os "One captain suggested we row the ships until we found a wind or tide once more. He said we were wasting provisions by not doing anything."
        "Wait for the wind":
            $ a_listener.wait_for_wind = True
            os "One captain suggested we wait, surely the clouds would clear and we could navigate again, at least enough for us to see the sun."        
    
    l "Did you agree?"
    os "Wasn't my place to agree or disagree, I was there to row Odysessus' boat, nothing more."
    l "What did Odysseus think?"
    menu:
        "He agreed we should wait":
            os "He agreed that we should wait, a wind would come eventually, and we still had the cyclops' sheep, so food wasn't a problem."
            if notice_contradiction() and hasattr(a_listener, "wait_for_wind") and not a_listener.wait_for_wind:
                l "But, didn't you say the captain suggested rowing the ships."
                os "Oh sorry, yes. Ahem, I mean Odysessus agreed to a different plan."
                if contradiction_fail( -0.2 ): 
                    jump scene5
                os "And it was decided we would wait..."
        "He agreed we should row":
            os "He agreed that we were wasting resources by staying, we should row the ships until we find a tide."
            if notice_contradiction() and hasattr(a_listener, "wait_for_wind") and a_listener.wait_for_wind:
                l "But, the captain suggested waiting for the wind?" 
                os "Oh sorry, yes. Ahem, I mean Odysessus agreed to a different plan."
                if contradiction_fail( -0.2 ): 
                    jump scene5
                os "And it was decided we would row the ships..."        
    
    l "So it was settled then?"
    os "Aye, each captain went back to the ship to inform their men. I rowed Odysseus back to our ship, so he could do the same."
            
label .after_plan:
    
    l "What happened? Did the plan work?"
    stop music fadeout 3
    os "Aye, three days later the wind picked up."    
    jump scene6