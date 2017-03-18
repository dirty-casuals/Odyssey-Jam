label scene2:
    os "After we set sail once more we came across an island. The island of Ismaros..."
    
    l "Ismaros Island?"     
    menu:
        "Aye, it's the island of the Cicones." :
            os "Aye, it's the island of the Cicones."
        "Yes. The home to an enemy of Greece." :
            os "Yes. We did not know at the time, but it was home to the Cicones, an enemy of Greece."
    
    l "The Cicones?"
    os "Aye, we fought against them during the battle of Troy. Fierce warriors, but not as skilled in the art of war."    
    menu:
        "We looted the city" :
            scene bg ismaros with pushleft  
            os "They weren't expecting us, so we made light work of the city.{p}We plundered, and took anything we wanted."
            l "What about the people?"
            os "The men were killed where they stood, and the women were taken as slaves."
        "We killed the men" :
            scene bg ismaros
            os "We attacked the city, killed all the men we could find."
            l "What about the women and children?"
            os "The men took them as slaves, as well as anything else of worth."
            
    l "What about you? Did you take any slaves?"
    menu:
        "No, I take orders, not give them":
            os "Me? No, I take orders, not give them.\nHa ha ha."
            $ a_listener.took_slaves = False
            $ a_listener.doesnt_command = True
        "If I didn't then someone else would...":
            os "I did. I felt if I didn't then someone else would, and who knows what they would have done to them. I have enough regrets."
            $ a_listener.took_slaves = True
        "Yes. The spoils of war, as they say.":
            os "Yes. The spoils of war, as they say."
            $ a_listener.took_slaves = True
    
    l "And Odysseus?"
    os "He was no better than the others, he took his fair share.{p}He wanted us to leave once we had done so. We should have listened..."
    
    l "Why? Did something happen?"
    menu:
        "Someone warned the inland tribes.":
            os "One of the men must have survived, or one of the slaves escaped. They went inland, gathered an army to chase us away."
        "We drank too much and fell asleep.":
            os "We all drank and made merry, until we fell asleep. I was awoken by the horns of war, Cicone reinforcements were on their way!"
            
    l "What did you do?"
    menu:
        "Commanded my men to defend the ships":
            os "I stood by my men and gave them orders to defend the ships, so Odysseus could flee to safety and prepare the shipts to sail."
            if notice_contradiction() and hasattr(a_listener, "doesnt_command") and a_listener.doesnt_command:
                l "But, didn't you say earlier you don't give orders"
                os "Hmm, yes... I mean I \"suggested\" we should defend the ships\n and everyone agreed with me."
                if contradiction_fail( -0.2 ): 
                    jump scene2
                
            jump .defend
            
        "I freed the slaves I had been given, told them to head for safety":
            os "I freed the slaves I had been given, told them to head for safety.{p}I then gathered my arms and joined my comrades and prepared to defend ourselves."
            if notice_contradiction() and hasattr(a_listener, "took_slaves") and not a_listener.took_slaves:
                l "I thought you had no slaves?"
                os "Oh yes... Just a slip of the tongue. I meant to say I freed as many as I could see."
                if contradiction_fail( -0.2 ): 
                    jump scene2
                
            os "Odysseus ordered us to defend the ships until we could leave.{p}We were heavily out numbered, they had archers and chariots,{p}it felt like eons passed in those moments."            
            jump .defend
            
        "Waited for Odysseus' orders":
            os "I quickly prepared as well as I could and joined my brothers in arms\n ready to await Odysseus' command."
            l "What was the order?"
            os "Defend the ships until we could retreat."
            jump .defend
            
        "I gathered my things and made for the ships.":
            os "I gathered my things and made for the ships.{p}There were too many for us to fight, and they had chariots and archers."
            jump .retreat            
            
label .defend:
    l "Did you succeed?"
    os "Well I'm sitting here now aren't I?{p}Others weren't as fortunate. They charged with the chariots."
    os "The man next to me was impaled on a scythed wheel as it flew from a destroyed chariot.{p}His body cushioned the blade enough that it didn't stick me too!"
    l "How did you escape?"
    os "Odysseus himself pulled me to my feet and got me to the ship.{p}We managed to get all twelve ships back out to sea, despite the losses."    
    l "Where did you go once you left Ismaros Island?"
    jump scene3
    
label .retreat:
    l "You ran away?"
    os "It was more of a tactical retreat..."
    l "What about the others?"
    os "Odysseus ordered them to defend the ships while we prepared them to sail."
    os "It was chaos, from where I stood you could see bronze and steel meet flesh. Hear the clangs and screams..."
    l "Did the ships escape?"
    os "Aye, we managed to get all twelve ships out to sea.{p}We lost many men though,{p}if only we had been faster, they wouldn't have had to hold the line for so long." 
    l "Where did you go once you left Ismaros Island?"
    jump scene3
