# Sayori's Route, part 2
# Depression Arc

label sayo_route_4:
    "A couple months later..."
    "The Depression Arc"
    scene mcpov
    $ pause(0.01)
    scene black
    with dissolve_cg
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
    "I reminisce about the past couple of months."
    "I met Sayori, learnt more about her, and started hanging out with her almost every day since then."
    "Sometimes she can get a little tiresome, but overall I enjoyed being around her."
    "I still have food to prepare though... Those thoughts will be preserved for later."
    scene bg kitchen
    with wipeleft
    mc "I know Sayori would want my lunch, so I'll prepare two just in case."
    mc "I'll also prepare my breakfast, because we've got time to kill, and I'm hungry."
    mc "I should probably check up on Sayori."
    mc "We've been friends for only a couple months, but it feels like forever..."
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
    mc "Welp, it's time to go outside and meet Sayori."
    scene black
    with wipeleft
    scene bg residential_day
    with wipeleft
    show sayori 1x zorder 1 at f11:
        yalign 0.5
    s "Heyy [player]!"
    show sayori 1a zorder 1 at t11:
        yalign 0.5
    mc "Hey, Sayori!"
    show sayori 1q zorder 1 at f11:
        yalign 0.5
    s "You ready to walk to school together?"
    show sayori 1r zorder 1 at t11:
        yalign 0.5
    mc "Sure! We've always walked together anyway, so why not?"
    show sayori 2l zorder 1 at f11:
        yalign 0.5
    s "We now share period 1 together... ehe~"
    show sayori 1k zorder 1 at t11:
        yalign 0.5
    mc "No need to get worked up. We're going to be late if we don't go quickly."
    mc "Wanna race?"
    show sayori 1x zorder 1 at f11:
        yalign 0.5
    s "Sure!"
    "*[player] speeds off into the distance*"
    show sayori 4m zorder 1 at f11:
        yalign 0.5
    s "Uwoa--"
    show sayori 1l zorder 1 at f11:
        yalign 0.5
    s "I should probably catch up~"
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t7
    scene bg class_day
    with wipeleft
    "It's a normal day in class..."
    show natsuki 1a zorder 1 at f11:
        yalign 0.5
    n "H-Hey!"
    "Nevermind."
    show natsuki 1g zorder 2 at t21:
        yalign 0.5
    show sayori 1j zorder 1 at f22:
        yalign 0.5
    s "I was only kidding... ehe~"
    $ n_name = "Natsuki"
    show natsuki 1f zorder 1 at f21:
        yalign 0.5
    show sayori 1j zorder 2 at t22:
        yalign 0.5
    n "Jeez, fine."
    show natsuki 1d zorder 1 at f21:
        yalign 0.5
    show sayori 1i zorder 2 at t22:
        yalign 0.5
    n "But, I get to make fun of you later. Deal?"
    show natsuki 1k zorder 1 at t21:
        yalign 0.5
    show sayori 4n zorder 2 at t22:
        yalign 0.5
    mc "Am I interrupting something here?"
    show natsuki 1k zorder 1 at t11:
        yalign 0.5
    show sayori zorder 2 at thide:
        yalign 0.5
    hide sayori
    mc "Natsuki, why are you making fun of Sayori?"
    show natsuki 1h zorder 1 at f11:
        yalign 0.5
    n "How do you know my name?"
    show natsuki 1g zorder 1 at t11:
        yalign 0.5
    mc "I've been listening in, but that's not important."
    show natsuki 1p zorder 1 at f11:
        yalign 0.5
    n "You...you perv!"
    show sayori 1p zorder 1 at f21:
        yalign 0.5
    show natsuki 1s zorder 1 at t22:
        yalign 0.5
    s "[player]'s not like that!"
    show sayori zorder 2 at thide:
        yalign 0.5
    hide sayori
    show natsuki 1q zorder 1 at f11:
        yalign 0.5
    n "Are you really sure? He seems like a perv to me."
    show natsuki 1s zorder 1 at t11:
        yalign 0.5
    mc "Alright, cut it out Natsuki."
    "So this is the widely known \"Tsundere\"."
    "I think I know why she acts like this though."
    show natsuki 5g zorder 1 at f11:
        yalign 0.5
    n "Hmph."
    show natsuki 5g zorder 1 at t11:
        yalign 0.5
    mc "The teacher's going to catch us talking amongst each other."
    show natsuki 5d zorder 1 at f11:
        yalign 0.5
    n "Fine, but you're still a perv!"
    show natsuki 5g zorder 1 at t11:
        yalign 0.5
    mc "Can't win all your battles, can you?"
    show natsuki zorder 1 at thide:
        yalign 0.5
    hide natsuki
    "Turning my focus for a second..."
    play music t5
    show sayori 1k zorder 1 at t11:
        yalign 0.5
    mc "Sayori, are you alright?"
    show sayori 1x zorder 1 at f11:
        yalign 0.5
    s "Yeah, I'm fine!~"
    s "Hey, [player]?"
    show sayori 1a zorder 1 at t11:
        yalign 0.5
    mc "Yeah?"
    show sayori 5a zorder 1 at f11:
        yalign 0.5
    s "Do you mind helping out with this?"
    show sayori 5c zorder 1 at t11:
        yalign 0.5
    mc "Sure... I'll just need a second-"
    show sayori 4m zorder 1 at t11:
        yalign 0.5
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
        yalign 0.5
    with dissolve_cg
    s "I'll get this checked out..."
    show sayori 1k zorder 2 at t11:
        yalign 0.5
    mc "Do you know where the nurse's office is?"
    show sayori 1l zorder 1 at f11:
        yalign 0.5
    s "Yeah."
    show sayori 1k zorder 1 at t11:
        yalign 0.5
    mc "Alright. I'll see you at lunch!"
    show sayori 3r zorder 1 at f11:
        yalign 0.5
    s "See you then!~"
    show sayori at thide:
        yalign 0.5
    hide sayori
    mc "Welp, time to focus in class..."
    mc "How didn't the teacher notice what happened?"
    scene black
    with wipeleft
    "But I can't focus in class."
    "I've been trying to concentrate, but all I could think about was the past few months."
    "So much has happened recently, but I've "
    "I did notice that Sayori acted strangely over the past few days though."
    play music t2
    scene bg class_day
    with wipeleft
    mc "It's already lunch?"
    mc "I must've dozed off for a while."
    scene black
    with wipeleft
    "I go over to where I typically hang out..."
    scene club_desks
    with wipeleft
    "This place reminds me of Sayori."
    "Sayori told me about this good lunch spot, and we've stayed here ever since."
    "But, I wonder if she's here this time. I don't see her."
    mc "Is anyone here?"
    show sayori 5b zorder 1 at f41:
        yalign 0.5
    s "No..."
    show sayori 5b zorder 1 at t41:
        yalign 0.5
    mc "Ah, hi Sayori!"
    show sayori 4m zorder 1 at f11:
        yalign 0.5
    s "Ehh???"
    s "How did you know I was here??"
    show sayori 4n zorder 1 at t11:
        yalign 0.5
    mc "You're just as predictable as I am... Do you want a cookie?"
    show sayori 1m zorder 1 at f11:
        yalign 0.5
    s "Cookies???"
    s "You almost never ask..."
    show sayori 3r zorder 1 at f11:
        yalign 0.5
    s "But sure!~"
    show sayori 1x zorder 1 at f11:
        yalign 0.5
    s "I always want cookies-"
    show sayori 1a zorder 1 at t11:
        yalign 0.5
    play music t7
    mc "And now you don't get it for that trick you played."
    mc "Shows how predictable you are."
    show sayori 1p zorder 1 at f11:
        yalign 0.5
    s "Ehhh?"
    s "You promised!!!"
    s "Uwaa-"
    show sayori 1p zorder 1 at t11:
        yalign 0.5
    play music t5
    mc "I'm only kidding. Come on, let's go!"
    show sayori 1x zorder 1 at f11:
        yalign 0.5
    s "Alright!~"
    scene black
    with wipeleft
    "Sayori's really excited about this cookie..."
    scene bg corridor
    with wipeleft
    mc "...and here's your cookie, Sayori!"
    show sayori 1y zorder 1 at f11:
        yalign 0.5
    s "Thanks..."
    show sayori 1y zorder 1 at t11:
        yalign 0.5
    mc "Is everything alright?"
    show sayori 4y zorder 1 at f11:
        yalign 0.5
    s "Yeah! See?"
    show sayori 1a zorder 1 at t11:
        yalign 0.5
    mc "Alright then..."
    "I doubt Sayori's okay. I should try to check on her just before school leaves."
    "Bell" "*RING!*"
    mc "Welp, that's our queue to leave."
    mc "Good luck in your classes!"
    show sayori 4y zorder 1 at f11:
        yalign 0.5
    s "Alright, you too [player]!"
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t9
    "They still don't suspect that I'm not from their world."
    "But, we'll have to see."
    "We also have Sayori to worry about... She could have something, but I'm not sure what it is."
    play music t2
    scene bg class_day
    with wipeleft
    show sayori 4p zorder 1 at hf11:
        yalign 0.5
    s "[player], are you there?"
    "Must've spaced out too long."
    show sayori 4p zorder 1 at t11:
        yalign 0.5
    mc "Yeah, I must've spaced out for a while."
    show sayori 3x zorder 1 at f11:
        yalign 0.5
    s "Ready to walk home together?"
    show sayori 3a zorder 1 at t11:
        yalign 0.5
    mc "As ready as I can be."
    show sayori 1r zorder 1 at f11:
        yalign 0.5
    s "Alright! Let's go~"
    show sayori 1r at thide:
        yalign 0.5
    mc "Why do the teachers never notice me spacing out?"
    mc "That's odd... I should investigate that."
    mc "Oh well..."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t7
    scene bg residential_day
    with wipeleft
    mc "Hey, Sayori?"
    show sayori 3x zorder 1 at f11:
        yalign 0.5
    s "Yeah?"
    show sayori 1a zorder 1 at t11:
        yalign 0.5
    mc "Is there something on your mind?"
    mc "You've been as spaced out as I am most of the time."
    show sayori 4p zorder 1 at hf11:
        yalign 0.5
    s "Meanie!"
    show sayori 1x zorder 1 at f11:
        yalign 0.5
    s "But there's nothing to worry about~"
    show sayori 1a zorder 1 at t11:
        yalign 0.5
    mc "Alright, just let me know if you need anything, alright?"
    "Something's clearly off about Sayori. This is going to be a lot harder than I thought."
    "I should potentially check on her when she least expects."
    show sayori 4y zorder 1 at f11:
        yalign 0.5
    s "Alright..."
    show sayori 4y at thide:
        yalign 0.5
    hide sayori
    "Yeah, something's off with Sayori."
    menu:
        "Should I go check on Sayori?"
        "Yes":
            call sayo_route_5 from _call_sayo_route_5
    scene black
    with wipeleft
    x "This is where this route for Doki Doki LifeTimes ends for now."
    x "We're around ~2\% done with this mod, and this route will get more work done on it!"
    x "There's so much more I want to add to this mod, so check out the github repository!"
    return

label sayo_route_5:
    "I'll go check on Sayori."
    "She's been acting weird recently, and I don't know what's up."