label scene4:
    scene bg cave fog with fogfadein
    stop music fadeout 3
    os "We sailed through the night, through a dense and ominous fog.{p}As dawn approached the fog began to clear..."
    show bg cave with fogfadeout
    play music calm fadein 1.0
    os "we saw a land of lush forests and green fields, supplies were low so we anchored the ships and went ashore."
    l "What did you find there?"    
    os "We saw a flock of large sheep on the pasture outside a cave.{p}As we approached the sheep we saw that the cave was full of food and drink."
        
    l "Did it belong to anyone? Did you go in?"
    menu:
        "We went in and had a feast":
            $ a_listener.steal_food = False
            os "The owner wasn't there. So we went inside the cave and filled our bellies with as much as we could eat."
            stop music fadeout 3
            os "We left nothing behind us."            
        "We took the food to the ships":
            $ a_listener.steal_food = True
            os "We weren't going to wait to find out! We packed up as much as we could carry back to the ships."
            stop music fadeout 3
            os "All the food was soon in bags and crates."            
    
    play music disturbance
    os "As we prepared to leave, the owner returned..."
    l "Oh no! Who was the owner?"
    show cyclops
    os "A cyclops by the name of Polyphemus."
        
    l "A cyclops?! What did he do?"
    stop music fadeout 0.6
    os "He introduced himself. He said he was about to eat, and that we were welcome to join him."        
    os "He lit torches near the cave entrance, and then pulled a boulder to block the opening, our only exit was gone."
    l "You were trapped, but he was friendly?"
    os "Or so we thought..."
    play music badturn fadein 1
    os "The very next moment he was filled to the brim with fury."
    
    menu:
        "...because we ate all of his food":
            os "He must have seen that we had been eating his food and drinking his wine,{p}he grabbed two of the men and devoured them with a blood curdling crunch."
            if notice_contradiction() and hasattr(a_listener, "steal_food") and a_listener.steal_food:
                l "I thought you were just planning to steal his food?"
                os "Oh yes, my mistake..."
                if contradiction_fail( -0.2 ): 
                    jump scene4
                    
        "...because we were stealing his food":            
            os "He must have seen that we planned to steal his food, he grabbed two of the men and devoured them with a blood curdling crunch."
            if notice_contradiction() and hasattr(a_listener, "steal_food") and not a_listener.steal_food:
                l "I thought you decided to eat had all been eating his food?"
                os "Oh yes, my mistake..."
                if contradiction_fail( -0.2 ):
                    jump scene4
    
    os "He took away our weapons and imprisoned us all in a large cage, with the intent to eat us one by one."
    os "He said \"I can never turn down the chance to eat man, although thief tastes bitter\"we all thought this was the end..."    
    hide cyclops
    stop music fadeout 2
    os "...but not Odysseus"
    l "What was Odysseus doing?"
    play music crucial
    os "Planning."    
    os "At first he thought we should kill the cyclops there and then, but realised we would be trapped inside the cave."
    l "Because of the boulder? So what was the plan?"
    os "Odysseus gathered all the men while the cyclops slept, and told us to try and find any weapons we could, and to try and reach the wine we had brought with us."
    
    menu:
        "We found a bow and an arrow":
            $ a_listener.cave_weapon = "Bow"
            os "One of the men managed to find a bow, and another found enough materials to craft a single arrow. We also managed to get hold of a single amphora of wine."
        "We found a spear":
            $ a_listener.cave_weapon = "Spear"
            os "One of the men managed to find a wooden staff which could be made into a spear. We also managed to get hold of a single amphora of wine."
        "We found determination":
            $ a_listener.cave_weapon = "None"
            os "We managed to get hold of a single amphora of wine, but we couldn't reach any weapons or materials."
            os "Odysseus wasn't dishearted by this, and said the plan would still work."
            
    l "What happened next?"
    os "Odysseus told us to rest, and that he would reveal the rest of the plan to us when the beast left to tend to his flock."
    
    l "What was the plan?!"    
    menu:        
        "To get the cyclops to open the cage":
            os "We needed to find a way to get the cyclops to open the cage, and a way outside without being eaten."
            if notice_contradiction() and hasattr(a_listener, "cave_weapon"):
                if a_listener.cave_weapon == "Bow":
                    l "Wait, didn't you need to craft an arrow for the bow?"
                    os "Oh yes of course, that was the first part of the escape plan."
                    if contradiction_fail( -0.1 ):
                        jump scene4
                if a_listener.cave_weapon == "Spear":
                    l "Wait, didn't you need to craft a spear out of that staff?"
                    os "Oh yes of course, that was the first part of the escape plan."
                    if contradiction_fail( -0.1 ):
                        jump scene4
                        
        "Firstly, to crafted the weapon":
            os "Firstly, we crafted the materials we got into a weapon, and then we needed to find a way to get the cyclops to open the cage, and finally a way to get outside."
            if notice_contradiction() and hasattr(a_listener, "cave_weapon"):
                if a_listener.cave_weapon == "None":
                    l "Wait, I thought you couldn't find any materials?"
                    os "Oh yes... we improvised when the time came."
                    if contradiction_fail( -0.1 ):
                        jump scene4
            
    l "So how did you get the cyclops to open the cage?"
    os "When the cyclops returned from herding his flock, Odysseus opened the wine and poured a few of the men a drink, telling them to act merry and loud to draw the beast's attention."
    l "To what end?"
    os "Polyphemus came over to the cage to see why his prisoners were jovial, he saw the wine and wanted it for himself. Odysseus offered to share the wine with him, and said there was more hidden in the cave."
    os "The cyclops thought about if for a second, then he pushed the boulder back into place then smiled and agreed, he opened the cage and Odysseus gave him the wine."
    l "Oh no, with the exit blocked you wouldn't be able to leave?!"
    menu:
        "It was all part of the plan...":
            os "It was all part of the plan..."
            l "What happened?"
            stop music fadeout 4.0
            os "Odysseus and the cyclops drank together, and they talked. Polyphemus eventually asked Odysseus his name, to which Odysseus replied \"my name is Nobody\""
        "I had no idea what was going on":
            stop music
            os "That's what I thought too, but Odysseus seemed to know it would happen."
            l "What happened?"
            os "The cyclops drank and talked with Odysseus. When he asked Odysseus for his name, he said \"I am Nobody\", the cyclops said he thought it a strange name for a man, but said man is a strange creature."
    
    os "Eventually the cyclops fell asleep, and Odysseus signalled for us to begin the next stage of the plan."
    
    l "Which was?"
    menu:
        "Shoot the arrow into the cyclops eye.":
            play music combat
            os "The arrow was set it alight, and fired into the cyclops' eye. He screamed a deafening scream, I have never heard such agony from a beast."
            if notice_contradiction() and hasattr(a_listener, "cave_weapon"):
                if not a_listener.cave_weapon == "Bow":
                    l "What arrow?"
                    os "Oh, the arrow I menitoned earlier, didn't I?{p}I mean we shot something."
                    if contradiction_fail( -0.2 ):
                        jump scene4
                    os "Anyway..."
                        
        "Use the spear to blind the cyclops.":
            play music combat
            os "The spear was heated until red hot, then plunged into Polyphemus' eye. He screamed a deafening scream, I have never heard such agony from a beast."
            if notice_contradiction() and hasattr(a_listener, "cave_weapon"):
                if not a_listener.cave_weapon == "Spear":
                    l "But you didn't have a spear?"
                    os "Oh, I mean, we found one lying around, I think."
                    if contradiction_fail( -0.2 ):
                        jump scene4
                    os "Anyway..."
                        
        "Improvise a weapon.":
            play music combat
            os "Since we had no weapons at the time we filled a bowl with red hot coals from the fire, then poured them into the beast's eye! He screamed a deafening scream, I have never heard such agony!"
            if notice_contradiction() and hasattr(a_listener, "cave_weapon"):
                if not a_listener.cave_weapon == "None":
                    if a_listener.cave_weapon == "Spear":
                        l "I thought you had a spear?"
                    if a_listener.cave_weapon == "Bow":
                        l "I thought you had made an arrow?"
                    os "Oh yes, it must have slipped my mind..."
                    if contradiction_fail( -0.2 ):
                        jump scene4
                    os "Anyway..."
        
    os "The cyclops' screams drew his neighbours to investigate."     
    show cyclopsA at midleft
    show cyclopsB at midright
    os "Odysseus told us all to hide and be ready to run to the ships."
    os "And so we waited for one of the other cyclopes to move the boulder..."    
    l "Did one of them do it?"
    stop music fadeout 0.3
    os "No...{p}One asked Polyphemus why he was screaming, to which he replied \"Nobody is killing me!\"..."
    os "...there was a long pause, and then the voice outside replied \"Ok then\" and left."
    hide cyclopsA 
    hide cyclopsB
    os "We were trapped until morning."    
    l "What happened in the morning?"    
    os "At dawn the sheep became restless and wished to go out and graze.\nPolyphemus stumbled to his feet and moved towards the boulder.\nHe pushed it aside then began feeling around, making sure no men passed."
    l "How did you escape?"
    play music buildup
    os "Odysseus signalled for us to cling onto the bellies of the sheep so Polyphemus couldn't feel for us."
    l "Did it work?"
    os "Like a charm! Once we were outside we herded the sheep onto the ships and set sail."     
    os "Polyphemus eventually realised he had been fooled and rushed to the beach."
    os "He was too late, we were already out at sea when he arrived. The cyclops shouted \"curse you Nobody!\""
    stop music fadeout 3
    l "So you got away unpunished?"    
    os "Not quite." 
    os "Odysseus' vanity got the better of him. He shouted at the cyclops \"You have been bested by Odysseus of Ithaca, you foolish wretch!\". The cyclops fell to his knees in prayer."
    l "He was praying? To who?"
    os "His father... Poseidon."
    l "What happened after you left the land of the cyclopes?"
    jump scene5