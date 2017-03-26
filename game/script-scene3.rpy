scene bg stormysea:
    zoom 1.1
    xalign 0.5 yalign 0.5
    linear 1.0 rotate 2
    linear 1.0 rotate -2
    alignaround (.5, .5)
    repeat
    
label scene3:
    scene bg shipscene with dissolve
    os "We drifted at sea for nine days,{p}we treated the wounded,{p}fixed any damage to the ships."
    scene bg djerba with pushright
    os "Then we saw land, and headed towards it."
    
    l "Where were you?"
    menu:
        "Uninhabited looking island.":
            os "The navigator said it was called Djerba Island.{p}It looked uninhabited, but we were taking no chances."
            l "How so?"
            os "Odysseus ordered us to anchor the ships off shore,{p}and he sent a group of five men to scout the island."
        "A tiny island.":
            os "A tiny island known as Djerba.{p}From the coast it looked like it belonged to the birds."
            l "And did it?"
            os "We anchored off the coast, Odysseus didn't want a repeat of our last time on land.{p}He sent five men ashore to the island to see if it was safe to make port."
            
    l "What did they find?"    
    
    if renpy.random.random() < 0.5:
        os "Nothing. The scouts didn't return, and no one came looking for us. It was a mystery."
    else:
        os "They didn't return.{p}We waited for three days..."
        
    l "Did anyone go looking for the scouts?"
    os "Aye, three of us were chosen to find them.{p}Adrastus, his brother Diodoros and myself."
    
    l "Why were you chosen?"    
    menu:
        "I was a good soldier.":
            os "Back in those days I knew how to swing a sword if I had to."
        "I was good at tracking.":
            os "You might not think it to look at me, but I can track any beast or man. Learnt from hunting with my father."
        "I was... no idea.":
            os "No idea.{p}Perhaps Odysseus thought it wise to send at least one person with half a brain?"
            
    l "What did you find?"    
    menu:
        "A village":
            os "We found a village, well it was barely that. More a collection of huts."
            l "What happened next?"
            os "We explored the perimeter of the village, to make sure it wasn't a trap. Then we quietly approached the nearest hut."
            l "What was inside?"
            os "A man, he appeared to be sleeping, but he wasn't, he was looking directly at us."
            l "What did he do?"
            os "He smiled."
            os "He stumbled to his feet and slowly walked over to us. We acted casually while tightening our hold on our swords, ready for the worst."
        "Signs of life":
            os "We found signs of life, a primitive settlement. We feared the worst."
            l "Why? What did you think had happened?"
            os "We thought they had been discovered by barbarians, or worse. A barbarian will skin you alive from your feet first, and that's if they like you!"
            l "What did you do?"
            os "We circled the camp, tried to see if we could spot our men, or the barbarians."
            l "Did you?"
            os "Not at first, but when we started to move towards the centre of the village we saw them."
    
    l "Did you kill him?"
    os "No, far from it. As he approached we saw that he was intoxicated, and lethargic, he couldn't harm us even if we handed him our weapons."
    os "He introduced himself to us, he said that he and his people were peaceful, told us to head to the centre of the village to find our men. He didn't prepare us for what we saw there however."
    
    l "What did you see?"
    os "A crowd of people, lethargic and spread across the ground like the aftermath of a battle. Some sleeping, some watching us, and some eating a strange fruit."
    
    menu:
        "Three scouts":
            os "Amongst them we saw the three scouts Odysseus had sent to inspect the island, as limp and indisposed as the inhabitants."
            jump .wrongnumber
        "Four scouts":
            os "Amongst them we saw the four scouts Odysseus had sent to inspect the island, as limp and indisposed as the inhabitants."
            jump .wrongnumber
        "Five scouts":
            os "Amongst them we saw the five scouts Odysseus had sent to inspect the island, as limp and indisposed as the inhabitants."
            jump .rightnumber
            
label .wrongnumber:
    if notice_contradiction():
        l "Wait, I thought you said there were five scouts?"
        os "Oh yes, of course."
        if contradiction_fail( -0.2 ): 
                    jump scene3
    jump .rightnumber

label .rightnumber:
    l "Were they poisoned?"
    os "In a way, it was the fruit. They didn't know who we were, they just wanted to lay there eating the fruit of the lotus, or so they called it."
    os "They had forgotten who they were, and where they were from. We dragged them back to the ships. They protested, but were too weak to stop us."
    l "What did you do once you had returned to the ships?"
    os "We told Odysseus of what we saw, and he saw the condition of the scouts. He ordered them to be imprisoned until the effects of the fruit subsided, and we set sail the very same night."
    l "Where did you go next?"
    jump scene4