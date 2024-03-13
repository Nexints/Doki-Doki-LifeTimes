# Act 2
# Each act 2 scene with Sayori, happens 1 year after the start.

label act2_day1_sayo:
    "1 year later..."
    "Act 2, Day 1"
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
    s "Alright, I'll be there!"
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
        yalign 0.8
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
    show natsuki zorder 1 at thide
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
    show sayori at thide
    hide sayori
    mc "Welp, time to focus in class..."
    scene black
    with wipeleft
    x "This is a demo version. See you in the full release!"
    x "We're around ~2\% done with this mod. There's so much more I want to add to this mod."
    return