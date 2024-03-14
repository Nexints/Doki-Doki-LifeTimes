# Sayo's Route pt 1

label sayo_route:
    "1 year later..."
    "Lover's Dreams"
    play music t2
    scene bg bedroom
    with dissolve_scene_full
    mc "It's a fresh morning, just before school."
    mc "What day is it..."
    mc "Ah! It's the first day of school, and we just got our timetables."
    mc "Looks like I share Period 1 with Sayori. That's interesting..."
    mc "Welp, time to get prepared..."
    scene black
    with wipeleft
    "I reminisce about the past year."
    "I met Sayori, learnt more about her, and started hanging out with her almost every day since then."
    "Sometimes she can get a little tiresome, but overall I enjoyed the experience!"
    "I still have food to prepare though... Those thoughts will be preserved for later."
    scene bg kitchen
    with wipeleft
    mc "I know Sayori would want my lunch, so I'll prepare two just in case."
    mc "I'll also prepare my breakfast, because we've got time to kill, and I'm hungry."
    mc "I should probably check up on Sayori."
    mc "We've been friends for only a year, but it feels like forever..."
    scene black
    with wipeleft
    "*Call initiated*"
    mc "Hey, Sayori! Are you up yet?"
    s "Yeah, I am... I'm just really tired."
    mc "I'll be outside soon, waiting for you..."
    mc "I'll even bring extra food for you during lunch!"
    s "Food???"
    s "I'll be there as soon as possible!~"
    "*Call Disconnected*"
    scene bg kitchen
    with wipeleft
    mc "Welp, it's time to go outside and meet Sayori!"
    scene black
    with wipeleft
    scene bg residential_day
    with wipeleft
    show sayori 1x zorder 1 at f11:
        yalign 0.7
    s "Heyy [player]!"
    show sayori 1a zorder 1 at t11:
        yalign 0.7
    mc "Hey, Sayori!"
    show sayori 1q zorder 1 at f11:
        yalign 0.7
    s "You ready to walk to school together?"
    show sayori 1r zorder 1 at t11:
        yalign 0.7
    mc "Sure! We've always walked together anyway, so why not?"
    show sayori 2l zorder 1 at f11:
        yalign 0.7
    s "We now share period 1 together... ehe~"
    show sayori 1k zorder 1 at t11:
        yalign 0.7
    mc "No need to get worked up. We're going to be late if we don't go quickly."
    mc "Wanna race?"
    show sayori 1x zorder 1 at f11:
        yalign 0.7
    s "Sure!"
    "*[player] speeds off into the distance*"
    show sayori 4m zorder 1 at f11:
        yalign 0.7
    s "Uwoa--"
    show sayori 1l zorder 1 at f11:
        yalign 0.7
    s "I should probably catch up~"
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t7
    scene bg class_day
    with wipeleft
    "It's a normal day in class..."
    show natsuki 1a zorder 1 at f11:
        yalign 0.7
    n "H-Hey!"
    "Nevermind."
    show natsuki 1g zorder 2 at t21:
        yalign 0.7
    show sayori 1j zorder 1 at f22:
        yalign 0.7
    s "I was only kidding... ehe~"
    $ n_name = "Natsuki"
    show natsuki 1f zorder 1 at f21:
        yalign 0.7
    show sayori 1j zorder 2 at t22:
        yalign 0.7
    n "Jeez, fine."
    show natsuki 1d zorder 1 at f21:
        yalign 0.7
    show sayori 1i zorder 2 at t22:
        yalign 0.7
    n "But, I get to make fun of you later. Deal?"
    show natsuki 1k zorder 1 at t21:
        yalign 0.7
    show sayori 4n zorder 2 at t22:
        yalign 0.7
    mc "Am I interrupting something here?"
    show natsuki 1k zorder 1 at t11:
        yalign 0.7
    show sayori zorder 2 at thide:
        yalign 0.7
    hide sayori
    mc "Natsuki, why are you making fun of Sayori?"
    show natsuki 1h zorder 1 at f11:
        yalign 0.7
    n "How do you know my name?"
    show natsuki 1g zorder 1 at t11:
        yalign 0.7
    mc "I've been listening in, but that's not important."
    show natsuki 1p zorder 1 at f11:
        yalign 0.7
    n "You...you perv!"
    show sayori 1p zorder 1 at f21:
        yalign 0.7
    show natsuki 1s zorder 1 at t22:
        yalign 0.7
    s "[player]'s not like that!"
    show sayori zorder 2 at thide:
        yalign 0.7
    hide sayori
    show natsuki 1q zorder 1 at f11:
        yalign 0.7
    n "Are you really sure? He seems like a perv to me."
    show natsuki 1s zorder 1 at t11:
        yalign 0.7
    mc "Alright, cut it out Natsuki."
    "So this is the Tsundere of the group."
    "Not really... I think I know why she acts like this."
    show natsuki 5g zorder 1 at f11:
        yalign 0.7
    n "Hmph."
    show natsuki 5g zorder 1 at t11:
        yalign 0.7
    mc "The teacher's going to catch us talking amongst each other."
    show natsuki 5d zorder 1 at f11:
        yalign 0.7
    n "Fine, but you're still a perv!"
    show natsuki 5g zorder 1 at t11:
        yalign 0.7
    mc "Can't win all your battles, can you?"
    show natsuki zorder 1 at thide:
        yalign 0.7
    hide natsuki
    "Turning my focus for a second..."
    play music t5
    show sayori 1k zorder 1 at t11:
        yalign 0.7
    mc "Sayori, are you alright?"
    show sayori 1x zorder 1 at f11:
        yalign 0.7
    s "Yeah, I'm fine!~"
    s "Hey, [player]?"
    show sayori 1a zorder 1 at t11:
        yalign 0.7
    mc "Yeah?"
    show sayori 5a zorder 1 at f11:
        yalign 0.7
    s "Do you mind helping out with this?"
    show sayori 5c zorder 1 at t11:
        yalign 0.7
    mc "Sure... I'll just need a second-"
    show sayori 4m zorder 1 at t11:
        yalign 0.7
    stop music
    play sound "sfx/smack.ogg"
    s "Kyaa--!"
    scene s_cg2_base1
    with dissolve_cg
    play music t8
    s "Oopsies..."
    mc "You okay?"
    s "Yeah, this hurts... a lot..."
    mc "I'll try to find something."
    mc "Just wait here for me, alright?"
    s "Alright..."
    s "(I'm fine with--looking like a unicorn--)"
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t2
    scene bg corridor
    with wipeleft
    mc "What should I get..."
    mc "Ahh, this!"
    mc "This'll have to suffice for now."
    mc "Besides, Sayori likes apple juice, so I'll get it for her."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t8
    scene s_cg2_base1
    with wipeleft
    show s_cg2_exp2
    mc "Here, I got something."
    show s_cg2_base2 behind s_cg2_exp2 at cgfade
    "I hand sayori the bottle that I bought earlier."
    show s_cg2_exp2 at cgfade
    hide s_cg2_exp2
    mc "Sayo, you realise you're supposed to drink this?"
    show s_cg2_exp3 at cgfade
    s "Ahh, sorry..."
    s "I must've forgot~"
    "Sayori starts placing the bottle on her head."
    show s_cg2_exp1 at cgfade
    s "This hurts..."
    mc "It'll be alright. Are you doing okay?"
    hide s_cg2_exp1
    hide s_cg2_exp3
    s "Yeah..."
    mc "That's all that matters."
    show s_cg2_exp3 at cgfade
    s "It still hurts a lot though... ehe~"
    mc "You should get it checked out as soon as possible."
    mc "It'd be good for you."
    hide s_cg2_exp3
    s "Alright..."
    play music t8 fadeout 1.0
    scene bg class_day
    show sayori 1l zorder 2 at f11:
        yalign 0.7
    with dissolve_cg
    s "I'll get this checked out..."
    show sayori 1k zorder 2 at t11:
        yalign 0.7
    mc "Do you know where the nurse's office is?"
    show sayori 1l zorder 1 at f11:
        yalign 0.7
    s "Yeah."
    show sayori 1k zorder 1 at t11:
        yalign 0.7
    mc "Alright. I'll see you at lunch!"
    show sayori 3r zorder 1 at f11:
        yalign 0.7
    s "See you then!~"
    show sayori at thide:
        yalign 0.7
    hide sayori
    mc "Welp, time to focus in class..."
    mc "How didn't the teacher notice what happened?"
    scene black
    with wipeleft
    "But I can't focus in class."
    "I've been trying to concentrate, but all I could think about was the past year."
    "So much has happened, and I've learnt that Sayori and Monika (her friend) were going to start a Literature club soon!"
    "Maybe in the next year or so, but I've been trying to help them with setting up!"
    "I did notice that Sayori acted strangely over the past few days though... Is something up?"
    "I'll have to ask her about it."
    play music t2
    scene bg class_day
    with wipeleft
    mc "It's already lunch?"
    mc "I must've dozed off for a while."
    scene black
    with wipeleft
    "I go over to an isolated spot of the school..."
    scene club_desks
    with wipeleft
    "This place reminds me of Sayori."
    "Sayori told me about this good lunch spot, and occasionally we've stayed here over the times."
    "But, I wonder if anyone's here."
    mc "Is anyone here?"
    show sayori 5b zorder 1 at f41:
        yalign 0.7
    s "No..."
    show sayori 5b zorder 1 at t41:
        yalign 0.7
    mc "Ah, hi Sayori!"
    show sayori 4m zorder 1 at f11:
        yalign 0.7
    s "Ehh???"
    s "How did you find me??"
    show sayori 4n zorder 1 at t11:
        yalign 0.7
    mc "Long story. Do you want a cookie?"
    show sayori 1m zorder 1 at f11:
        yalign 0.7
    s "Cookies???"
    s "You almost never ask..."
    show sayori 3r zorder 1 at f11:
        yalign 0.7
    s "But sure!~"
    show sayori 1x zorder 1 at f11:
        yalign 0.7
    s "I've really wanted a cookie-"
    show sayori 1a zorder 1 at t11:
        yalign 0.7
    play music t7
    mc "And now you don't get it for that trick you played."
    show sayori 1p zorder 1 at f11:
        yalign 0.7
    s "Ehhh?"
    s "You promised!!!"
    s "Uwaa-"
    show sayori 1p zorder 1 at t11:
        yalign 0.7
    play music t5
    mc "I'm only kidding. Come on, let's go!"
    show sayori 1x zorder 1 at f11:
        yalign 0.7
    s "Alright!~"
    scene black
    with wipeleft
    "Sayori's really excited about this cookie..."
    scene bg corridor
    with wipeleft
    mc "...and here's your cookie, Sayori!"
    show sayori 1y zorder 1 at f11:
        yalign 0.7
    s "Thanks..."
    show sayori 1y zorder 1 at t11:
        yalign 0.7
    mc "Is everything alright?"
    show sayori 4y zorder 1 at f11:
        yalign 0.7
    s "Yeah! See?"
    show sayori 1a zorder 1 at t11:
        yalign 0.7
    mc "Alright then..."
    "I doubt Sayori's okay. I should check on her just before school leaves."
    "Bell" "*RING!*"
    mc "Welp, that's our queue to leave."
    mc "Good luck in your classes!"
    show sayori 4y zorder 1 at f11:
        yalign 0.7
    s "Alright, you too [player]!"
    stop music fadeout 0.5
    scene black
    with wipeleft
    "And that's another successful interaction."
    "They still don't suspect that I'm not from their world."
    "But, we'll have to see."
    "We also have Sayori to worry about... She could be taking a liking towards me?"
    play music t9
    scene bg class_day
    with wipeleft
    "I've never really been good with girls though."
    "That could be why I still don't have a girlfriend in real life."
    play music t2
    show sayori 4p zorder 1 at hf11:
        yalign 0.7
    s "[player], are you there?"
    "Must've spaced out too long."
    show sayori 4p zorder 1 at t11:
        yalign 0.7
    mc "Yeah, I must've spaced out for a while."
    show sayori 3x zorder 1 at f11:
        yalign 0.7
    s "Ready to walk home together?"
    show sayori 3a zorder 1 at t11:
        yalign 0.7
    mc "As ready as I can be."
    show sayori 1r zorder 1 at f11:
        yalign 0.7
    s "Alright! Let's go~"
    show sayori 1r at thide:
        yalign 0.7
    mc "Why do the teachers never notice me spacing out?"
    mc "That's odd... I should probably fix that."
    scene black
    with wipeleft
    x "This is where the demo for Doki Doki LifeTimes ends."
    x "We're around ~2\% done with this mod."
    x "There's so much more I want to add to this mod, so check out the github repository!"
    return