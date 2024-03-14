# Day 1

label act1:
    $ persistent.sayori_relation = 0
    stop music fadeout 0.5
    "Act 1. Day 1 (2012)."
    "First encounter with Sayori!"
    play music t2
    scene bg bedroom
    with dissolve_scene_full
    mc "Ahh, a fresh day."
    mc "Let's get ready..."
    play music t7
    mc "Wait... I'm in VM3"
    mc "Hmm...  This is quite strange, but let's act naturally."
    mc "This is going to be interesting though."
    mc "Since I'm here, might as well make a light breakfast"
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene bg kitchen
    with wipeleft
    play music t2
    mc "Ahh yes, breakfast."
    mc "I'll cook some food for myself, and one more just in case."
    scene black
    with wipeleft
    "Three meals later..."
    scene bg kitchen
    with wipeleft
    mc "Alright. I've got my breakfast and lunch ready."
    mc "I also got a third meal, you never know when you need it!"
    mc "I'll head to school quickly. I'm already late, and I don't want the teachers to start worrying."
    mc "But before I do..."
    scene black
    with wipeleft
    "I decide to eat my breakfast."
    "That breakfast was amazing..."
    scene bg residential_day
    with wipeleft
    mc "Alright. Let's get out of here."
    scene black
    with wipeleft
    scene school
    with wipeleft
    $ s_name = "???"
    mc "I'm in school now."
    mc "Let's see what our schedule is."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t3
    scene bg class_day
    with wipeleft
    mc "Welp, I'm not too late."
    mc "However, this seems to be history of all things."
    mc "This class is really boring."
    mc "I hate this already."
    stop music fadeout 0.5
    scene black
    with wipeleft
    "And as such, [player] begins to nap in class."
    play music t5
    scene bg class_day
    with wipeleft
    mc "That was a nice nap..."
    play music t7
    mc "Wait. Where's everyone?"
    mc "Is it already lunch???"
    mc "I should probably get downstairs to eat."
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene bg corridor
    with wipeleft
    play music t2
    mc "I should probably have my lunch here."
    show sayori 1bu zorder 2 at t11:
        yalign 0.6
    mc "I noticed this blue-eyed \"cinnamon bun\" feeling down while walking to school..."
    show sayori zorder 1 at thide:
        yalign 0.6
    hide sayori
    mc "I'm overthinking again. It *should be* nothing much, as I don't know her yet."
    mc "I'll enjoy my lunch for now, and see what happens later on."
    scene black
    with wipeleft
    "After one wholesome lunch..."
    scene bg corridor
    with wipeleft
    mc "That was amazing!"
    mc "It seems as if my cooking skills have improved."
    "Bell" "\"RING!\""
    mc "Fine... I'll get back to class."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t5
    scene bg class_day
    with wipeleft
    mc "It's time to study. I need to ensure that I look focused, and I can't disappoint my parents."
    mc "My parents are currently on vacation in this VM"
    mc "It's none of my business though."
    scene black
    with wipeleft
    scene bg class_day
    with wipeleft
    mc "Wait, it's already over?"
    mc "That went by relatively smoothly."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t2
    scene bg corridor
    with wipeleft
    mc "School sucks... I wanna leave as soon as I can."
    scene black
    with wipeleft
    scene school
    with wipeleft
    mc "Finally, I'm out of that place..."
    play music t7
    if persistent.wallace_gone == 0:
        call act1_wallace from _call_act1_wallace
    else:
        call act1_nowallace from _call_act1_nowallace
    call act1_day2 from _call_act1_day2
    return

label act1_wallace:
    s "Hey! Do you want to play with me?"
    w "No."
    s "Why not? Ehe~"
    w "You fucking suck, you know that?"
    s "WHAT ARE YOU DOING?"
    play music td
    "I can only watch in horror, as this innocent girl dies right in front of me."
    scene black
    with dissolve_cg
    "She's dead... By WALLACE..."
    "I do the only thing I can."
    $ persistent.sayori_dead = 1
    $ run_input(input="os.delete(\"Wallace.chr\")", output="Access Denied.")
    $ run_input(input="renpy.createchr(\"Sayori\")", output="Access Denied.")
    hide screen console_screen
    "NOOOOO... Damn you, Wallace."
    "Maybe I should have chosen a different path."
    call act1_ripsayori from _call_act1_ripsayori
    return

label act1_nowallace:
    s "Hey!"
    "Girl 1" "\"Screw off\""
    s "Did I annoy you? Ehe~"
    "Girl 1" "\"You're just a stupid idiot!\""
    "I have a feeling this girl may be important to me."
    $ persistent.sayori_dead = 0
    menu:
        "Do I approach this girl?"
        "Yes":
            $ persistent.sayori_relation = 1
            call act1_sayori from _call_act1_sayori
        "No":
            $ persistent.sayori_relation = 0
            call act1_nosayori from _call_act1_nosayori
    return

label act1_nosayori:
    "I decide not to approach."
    $ x_name = "Narrator"
    mc "Welp, it's time to head home."
    mc "I guess I'll take a quick stop at the nearby park though..."
    mc "Let's see what happens."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t5
    scene park_entrance
    with wipeleft
    call act1_route2 from _call_act1_route2
    return

label act1_ripsayori:
    "Can't do anything now though..."
    $ x_name = "Narrator"
    x "[player] heads towards the nearest park, to relax."
    scene black
    with wipeleft
    scene park_enterance
    with wipeleft
    x "[player] is pretty stupid though to leave someone like that."
    mc "Wait... Why is there a narrator here?"
    mc "I didn't code one in."
    mc "What's going on?"
    x "I should probably explain myself..."
    call act1_route2 from _call_act1_route2_1
    return

label act1_route2:
    if persistent.sayori_dead == 0:
        mc "Ah... This place feels amazing."
        mc "I'll probably visit this place again."
        mc "Or, maybe I'll go to the library?"
        mc "There's so many opporotunities here..."
        mc "It feels almost limitless as to what I could do."
        mc "Even though this is just a VM, I appreciate the finer things that this VM provides."
        scene black
        with wipeleft
        scene park_entrance_sunset
        with wipeleft
        mc "Wait... It's already sunset?"
        mc "I spent way too long here, so I really need to go home."
        mc "I don't want to be late for school tomorrow, as something big is happening then."
        mc "I need to preserve the VM state before things collapse more."
    else:
        x "The person you saw die..."
        x "Her name was Sayori."
        x "She was supposed to be your childhood friend..."
        x "...Since you saw Sayori die, this environment glitched out really badly."
        x "and I popped into existance."
        x "I'm just trying to help as a developer."
        mc "Oh, okay..."
        x "This game must be really broken right now."
        mc "Wait, I thought this was just a VM? This is a game???"
        x "Yeah... I thought so too."
        mc "Ah. Welp, I'll be heading home now..."
        x "Alright. Go ahead, I'm not stopping you. I'm just the narrator."
    stop music fadeout 0.5
    scene black
    with dissolve_cg
    play music t2
    scene residential_sunset
    with dissolve_cg
    "And as such, [player] starts to head home, ready for sleep."
    scene black
    with wipeleft
    scene bedroom_night
    with wipeleft
    mc "Dang, I really need to sleep."
    mc "It's been a long day, and I should probably start sleeping."
    stop music fadeout 0.5
    scene black
    with dissolve_scene_full
    return

label act1_sayori:
    "I approach cautiously..."
    stop music fadeout 0.5
    scene black
    with wipeleft
    scene sidewalk
    with wipeleft
    play music t9
    show sayori 4bu zorder 2 at t11:
        yalign 0.6
    mc "Hey... What seems to be the issue?"
    show sayori 4bu zorder 2 at hf11:
        yalign 0.6
    s "I don't know what to do... This girl is calling me stupid."
    show sayori 4bu zorder 2 at t11:
        yalign 0.6
    mc "Don't worry. I'll help you."
    mc "This girl shouldn't call people stupid for no reason."
    show sayori 1bv zorder 2 at f11:
        yalign 0.6
    s "Wait, really?"
    show sayori 1bv zorder 2 at t11:
        yalign 0.6
    mc "Yeah. What's your name?"
    show sayori 3by zorder 2 at f11:
        yalign 0.6
    $ s_name = "Sayori"
    s "Sayori."
    show sayori 3by zorder 2 at t11:
        yalign 0.6
    mc "Ah, I'm [player]."
    show sayori 1bn zorder 2 at t11:
        yalign 0.6
    play music t7
    "Girl 1" "\"Who's this [player]?\""
    mc "I'll go have a talk with them."
    show sayori 4bq zorder 2 at f11
    s "Okay!"
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t7
    scene street
    with wipeleft
    menu:
        "What should I do?"
        "Talk with them":
            $ persistent.america = 0
            "Girl 1" "\"Oh sh-\""
            mc "Leave, and don't mess with us again. Go pick on other people, you knuckleheads."
            mc "I know you're hiding. Don't try to hide it."
        "L'AMERICA":
            $ persistent.america = 1
            "Girl 1" "\"OH NO HE HAS A GUN! HIDE\""
            mc "Don't try to hide! It's AMERICA TIME!"
            "And as such, the MC starts to shoot the characters."
            "The MC missed though."
    scene black
    with wipeleft
    scene sidewalk
    with wipeleft
    show sayori 4bt zorder 2 at t11:
        yalign 0.6
    if persistent.america == 0:
        "Sayori seems happy by this..."
    else:
        "Sayori seems slightly distressed... but overall decently happy."
    show sayori 1bl zorder 2 at f11:
        yalign 0.6
    play music t9
    s "After that incident, I was about to go home..."
    show sayori 1bl zorder 2 at t11:
        yalign 0.6
    mc "I'm sorry for what happened."
    mc "That jerk can screw themselves."
    mc "By the way, are you doing okay?"
    show sayori 1bt zorder 2 at hf11:
        yalign 0.6
    s "Yeah... I hope so, ehe~"
    show sayori 1bt zorder 2 at t11:
        yalign 0.6
    mc "Alright. I'll head home now."
    show sayori 1bu zorder 2 at t11:
        yalign 0.6
    s "Alright..."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t2
    scene bg residential_day
    with wipeleft
    show sayori 4bn zorder 2 at f11:
        yalign 0.6
    s "Wait, you're still here!"
    show sayori 4bn zorder 2 at t11:
        yalign 0.6
    mc "Yeah. We live really close to each other!"
    show sayori 3bl zorder 2 at f11:
        yalign 0.6
    s "Ehe~ I guess I'll be seeing you more often now!"
    show sayori 3bl zorder 2 at t11:
        yalign 0.6
    mc "Alright then."
    show sayori 1br zorder 2 at f11:
        yalign 0.6
    s "Oh, also..."
    show sayori 1bq zorder 2 at t11:
        yalign 0.6
    play music t10
    scene black
    with dissolve_cg
    scene s_cg4
    with dissolve_cg
    s "Thank you for helping me back there."
    mc "Any time."
    s "I've... just never had someone do that for me..."
    mc "I'll be that person you never had."
    mc "It's been just a few hours, but I appreciate you being here."
    s "Thank you...  [player]"
    mc "Any time. I appreciate you for who you are."
    s "By chance, Where do you live? I wanna see if I can spend more time with you!~"
    call act1_route1 from _call_act1_route1
    return

label act1_route1:
    scene black
    with dissolve_cg
    scene residential_sunset
    with dissolve_cg
    show sayori 1br zorder 2 at t11:
        yalign 0.6
    mc "Ah, I live right..."
    show sayori 1bn zorder 2 at h11:
        yalign 0.6
    mc "There!"
    play music t2
    show sayori 1bm zorder 2 at f11:
        yalign 0.6
    s "No way! We're neighbors!!!"
    show sayori 1bm zorder 2 at t11:
        yalign 0.6
    mc "No need to get worked up."
    show sayori 1bl zorder 2 at f11:
        yalign 0.6
    s "Ahaha~ Now I can spend more time with you!"
    show sayori 1bk zorder 2 at t11:
        yalign 0.6
    mc "Why don't we both get inside? It's pretty late..."
    show sayori 1bd zorder 2 at f11:
        yalign 0.6
    s "Alright then..."
    show sayori 1bd zorder 2 at t11:
        yalign 0.6
    scene black
    with wipeleft
    scene house_night
    with wipeleft
    show sayori 1bk zorder 2 at t11:
        yalign 0.6
    mc "This is where we'll depart for now."
    mc "See you later, Sayori!"
    show sayori 4ba zorder 2 at f11:
        yalign 0.6
    s "See you later [player]!"
    show sayori zorder 1 at thide:
        yalign 0.6
    hide sayori
    "This was a nice interaction!"
    if persistent.america == 1:
        "Tomorrow, It's America time."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t5
    scene bedroom_night
    with wipeleft
    "Dang, I really need to sleep."
    "It's been a long day, and I should probably start sleeping."
    scene black
    with dissolve_scene_full
    stop music fadeout 0.5
    return

# Day 2

label act1_day2:
    $ x_name = "Nexint"
    "Act 1. Day 2 (2012)."
    if persistent.america == 1:
        "AMERICA TIME!"
        call act1_day2_america from _call_act1_day2_america
    elif persistent.sayori_relation == 1:
        "Talking with Sayori."
        mc "Oh god... This VM has every single character fall in love with [mc]"
        mc "Let's fix this up."
        $ run_input(input="ddlc.settings.datesim = False", output="Command processed.")
        mc "Okay. This should make things better."
        hide screen console_screen
        call act1_day2_sayo from _call_act1_day2_sayo
    else:
        "Other Doki's."
        x "This is a demo version. See you in the full release!"
        x "We're around ~2\% done with this mod. There's so much more I want to add to this mod."
    return

label act1_day2_america:
    play music t2
    scene bg bedroom
    with dissolve_scene_full
    mc "Ahh, a fresh American day."
    mc "Let's go use this M-16 I found underneath my bed!"
    mc "Not like I had to detonate another \"Fat Boy\" nuclear warhead in my room to find it."
    mc "Doesn't matter though, this is just a VM right?"
    scene black
    with wipeleft
    scene bg residential_day
    with wipeleft
    mc "Is that Sayori over there?"
    s "Wait up!"
    mc "I have to use this M-16 though."
    show sayori 1p zorder 2 at hf11:
        yalign 0.6
    s "Hey [player]!"
    show sayori 1p zorder 2 at t11:
        yalign 0.6
    mc "IT'S AMERICA TIME!"
    show sayori 1n zorder 2 at f11:
        yalign 0.6
    s "Ooo, what is it?"
    show sayori 1n zorder 2 at t11:
        yalign 0.6
    "*[player] fires gunshots everywhere*"
    show sayori 4r zorder 2 at f11:
        yalign 0.6
    s "Can I try too?"
    show sayori 4q zorder 2 at t11:
        yalign 0.6
    mc "Sure!"
    mc "I'll just quickly..."
    scene black
    with wipeleft
    scene school
    with wipeleft
    play music t7
    mc "It's time to die."
    show monika 1q zorder 2 at t11:
        yalign 0.6
    "Girl 1" "I'm screwed..."
    x "(Context: Monika's sprite is used as a placeholder. It's heavily contradicted, as seen in Act 2.)"
    show monika zorder 1 at thide:
        yalign 0.6
    hide monika
    stop music fadeout 0.5
    "*Bang*"
    play music t2
    mc "That girl bullying Sayori is gone."
    mc "It's time to live the AMERICAN DREAM!"
    scene black
    with wipeleft
    scene bg residential_day
    with wipeleft
    mc "I'm back!"
    show sayori 4r zorder 2 at hf11:
        yalign 0.6
    s "Thanks for dealing with them!"
    show sayori 1d zorder 2 at f11:
        yalign 0.6
    s "Mind if I join you?"
    show sayori 1d zorder 2 at t11:
        yalign 0.6
    menu:
        "Should I let Sayori join me?"
        "Yes":
            mc "Sure! I don't mind..."
            show sayori 1r zorder 2 at f11:
                yalign 0.6
            s "Ehe~"
            show sayori 4a zorder 2 at f11:
                yalign 0.6
            s "Things are going to be great!"
            call act1_day2_sayoriamerica from _call_act1_day2_sayoriamerica
        "No":
            mc "I'd rather not..."
            show sayori 1x zorder 2 at f11:
                yalign 0.6
            s "That's alright. Thanks anyway for dealing with her!"
            show sayori 1a zorder 2 at t11:
                yalign 0.6
            mc "No problem."
            scene black
            with wipeleft
            "And as such, [player] starts to shoot everything else in sight."
            "[player] ends up with 15 charges of armed assault."
    "American Ending."
    stop music fadeout 0.5
    return

label act1_day2_sayoriamerica:
    stop music fadeout 0.5
    scene black
    with wipeleft
    scene breakdown
    with wipeleft
    "[player] and Sayori have a great time, shooting other people."
    scene residential_night
    with wipeleft
    play music t2
    show sayori 3x zorder 2 at f11:
        yalign 0.6
    s "Hey, [player]?"
    show sayori 1a zorder 2 at t11:
        yalign 0.6
    mc "Yeah?"
    show sayori 1x zorder 2 at f11:
        yalign 0.6
    s "I just wanted to say..."
    show sayori 4m zorder 2 at f11:
        yalign 0.6
    s "Oops!"
    show sayori 4m zorder 2 at t11:
        yalign 0.6
    "This ended up in Sayori accidentally shooting a window."
    show sayori 4n zorder 2 at t11:
        yalign 0.6
    mc "Should've known you would do this..."
    show sayori 5d zorder 2 at f11:
        yalign 0.6
    s "I'm just clumsy like that... Hmph."
    "And as such, [player] lives the all american dream with Sayori, shooting people with his M-16"
    return

label act1_day2_sayo:
    play music t2
    scene bg bedroom
    with dissolve_scene_full
    "It's a brand new day..."
    s "Hey MC!"
    mc "Hey! Isee you through the window there..."
    s "No fair... I thought you wouldn't see me."
    mc "Was I that dense before?"
    s "What do you mean? We've just met..."
    "Almost accidentally blew my cover there."
    mc "Wait, we're going to be late!"
    mc "I'll head to school now, see you soon!"
    scene black
    with wipeleft
    scene bg kitchen
    with wipeleft
    "Packing a lunch just in case."
    "I'm hungry..."
    scene black
    with wipeleft
    scene bg house
    with wipeleft
    show sayori 4p zorder 2 at f11:
        yalign 0.6
    s "Wait!"
    show sayori 1l zorder 2 at f11:
        yalign 0.6
    s "We go to the same school, do you wanna walk together?"
    show sayori 1k zorder 2 at t11:
        yalign 0.6
    mc "Alright then, but we gotta walk quickly..."
    stop music fadeout 0.5
    scene black
    with wipeleft
    menu:
        "Did you grow apart from Sayori?"
        "Yes (Not done)":
            "This menu is still in progress."
        "No":
            call act1_day2_sayoroute from _call_act1_day2_sayoroute
    return

label act1_day2_sayoroute:
    "Alright. Let's see how this goes."
    play music t2
    scene bg corridor
    with wipeleft
    mc "It's lunchtime."
    mc "Thank goodness I packed my lunch, I'm starving!"
    s "Did you say... lunch??"
    show sayori 1p zorder 2 at t11:
        yalign 0.6
    "I must've talked too loudly..."
    show sayori 1p zorder 2 at f11:
        yalign 0.6
    s "Found you!"
    show sayori 1p zorder 2 at t11:
        yalign 0.6
    mc "Fine... you win. I'm starving though, do you want to split my lunch?"
    mc "And why are you taking my lunch?"
    show sayori 5b zorder 2 at f11:
        yalign 0.6
    s "I'm hungry..."
    show sayori 5b zorder 2 at t11:
        yalign 0.6
    mc "I'll split my lunch with you."
    mc "Just don't take everything..."
    show sayori 3a zorder 2 at f11:
        yalign 0.6
    s "Alright!"
    show sayori 1a zorder 2 at t11:
        yalign 0.6
    stop music fadeout 0.5
    scene black
    with wipeleft
    "And thus, begins MC and Sayori's friendship."
    "Lunch and classes whiz by without anything going wrong, and [player]'s ready to go home..."
    play music t3
    scene bg class_day
    with wipeleft
    s "Hey, [player]!"
    s "Ready to walk home?"
    mc "Sure. I'll be outside in a second."
    s "Alright!"
    "I should probably get going quickly then."
    scene black
    with wipeleft
    scene school_sunset
    with wipeleft
    mc "I'm here!"
    show sayori 1r zorder 2 at f11:
        yalign 0.6
    s "Ready?"
    show sayori 1q zorder 2 at t11:
        yalign 0.6
    mc "Let's get outta here. I wouldn't want to waste time without you!"
    show sayori 1a zorder 2 at f11:
        yalign 0.6
    s "Alright!"
    show sayori 1a at thide
    hide sayori
    mc "Sayori's so energetic... I wish I could be like her."
    mc "I should get going though. I need to meet Sayori outside."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t9
    scene street
    with wipeleft
    "Dang, this world is so expansive..."
    "I never knew this world could render things like these."
    "It's almost as if... this world is my lifetime."
    show sayori 1h zorder 2 at f11:
        yalign 0.6
    s "Hey, [player]?"
    show sayori 1e zorder 2 at t11:
        yalign 0.6
    mc "Yeah?"
    show sayori 1l zorder 2 at f11:
        yalign 0.6
    s "I just wanted to know... did you mean what you said earlier?"
    show sayori 1m zorder 2 at t11:
        yalign 0.6
    mc "I did. I enjoy spending time with you Sayo, and I wouldn't trade the world for it."
    show sayori 1y zorder 2 at f11:
        yalign 0.6
    s "It's just... I've never had someone else say that to me."
    show sayori 1u zorder 2 at f11:
        yalign 0.6
    s "Everyone else has always used me... ehe~"
    show sayori 1u zorder 2 at t11:
        yalign 0.6
    mc "It's going to be alright."
    mc "I won't use you like those jerks who did."
    mc "Everything's going to be fine..."
    show sayori 1t zorder 2 at f11:
        yalign 0.6
    s "Thank you, [player] for being there with me."
    show sayori 1t zorder 2 at t11:
        yalign 0.6
    mc "Anything for you, Sayori."
    mc "Wait, why weren't you at school yesterday?"
    show sayori 1l zorder 2 at f11:
        yalign 0.6
    s "I didn't feel like going yesterday..."
    show sayori 1x zorder 2 at f11:
        yalign 0.6
    s "Besides, I'm feeling much better now that you're here!"
    show sayori 1a zorder 2 at f11:
        yalign 0.6
    mc "Ah, makes sense."
    "This girl is starting to get really clingy towards me... It's only been a few days though."
    scene black
    with dissolve_scene_full
    stop music fadeout 0.5
    call act2_day1_sayo from _call_act2_day1_sayo
    return

label act1_day2_nosayo:
    if persistent.sayori_dead == 1:
        play music t9
        w "Hey, [player]."
        w "I tried to get in the VM to enact revenge on you."
        w "But, I accidentally broke a ton of things here, and these manifested as me killing Sayori."
        w "I've had an epiphany, and I realised that I can't just destroy VM3 like that."
        w "If you forgive me, I'll try to fix everything."
        menu:
            "Do I forgive Wallace for what he did?"
            "Yes":
                w "Thank you."
                $ run_input(input="renpy.addPermission(\"Wallace\")", output="Added Permissions for Wallace.")
                $ run_input(input="renpy.createchr(\"Sayori\")", output="Created Sayori.")
                $ run_input(input="renpy.debug(\"*.*\")", output="Fixed all bugs.")
                w "I'm going to try setting the variables properly again."
                w "Did you approach Sayori?"
                menu:
                    "Do I approach Sayori?"
                    "Yes":
                        $ persistent.sayori_relation = 1
                        w "Alright."
                        w "Final question: Did you become American?"
                        menu:
                            "Did I turn into an american?"
                            "Yes":
                                $ persistent.america = 1
                                w "Alright."
                                w "Let's send you off... American style."
                                call act1_day2_america from _call_act1_day2_america_1
                            "No":
                                w "Alright."
                                w "I'll send you on your way."
                                call act1_day2_sayo from _call_act1_day2_sayo_1
                    "No":
                        $ persistent.sayori_relation = 1
                        w "Alright."
                        w "I'll send you off."
                        call act1_day2_school from _call_act1_day2_school
            "No (Not Done)":
                w "You're ending the world..."
                w "NOOOO"
                x "This is not the outcome I expected."
                "Broken Masquerade Ending"
    else:
        call act1_day2_school from _call_act1_day2_school_1
    return

label act1_day2_school:
    play music t2
    scene bg bedroom
    with dissolve_scene_full
    "It's a brand new day..."
    "But I should probably head to school..."
    mc "I need to feed myself first."
    scene black
    with wipeleft
    scene bg kitchen
    with wipeleft
    mc "Alright, time to cook something, and head off to school!"
    mc "I'll pack my lunch quickly, and I'll order takeout for my breakfast."
    mc "We have time to kill, so why not?"
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t5
    scene bg kitchen
    mc "That was a great breakfast!"
    mc "I'll head off to school now, to see what other things will happen."
    scene black
    with wipeleft
    scene residential_day
    with wipeleft
    mc "Such a relaxing walk..."
    mc "I do wonder what happened to that girl I saw yesterday though..."
    mc "I hope they're doing okay."
    play music t7
    show natsuki t42 zorder 1 at f11:
        yalign 0.6
    mc "Wait, who are these students here...?"
    mc "And why aren't they at school?"
    menu:
        "Should I go to school, approach the pink haired girl, or approach the purple haired girl?"
        "School":
            mc "Let's just keep going..."
        "Pink haired girl":
            mc "I'll talk with the pink haired girl."
            mc "I hope the teacher doesn't mind though."
        "Purple haired girl":
            mc "I'll talk with the purple haired girl."
            mc "I have to skip class though... I hope the teacher doesn't mind."
    scene black
    with wipeleft
    "This is where the demo ends. We're around 1-2\% done with the mod, so sit tight as the mod develops further!"
    return