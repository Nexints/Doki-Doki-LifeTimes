# Day 1
label prologue_0:
    stop music fadeout 0.5
    scene black
    "Act 0, Day 1 (2025)."
    "Prologue and Pre-lore."
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me."
    $ s_name = "Sayori"
    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    $ pause(1.0)
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    $ pause(1.0)
    $ gtext = glitchtext(48)
    stop music
    scene black with trueblack
    mc "What's happening???"
    $ w_name = "Boss"
    w "Wake Up. NOW."
    $ consolehistory = []
    $ run_input(input="music.play(\"music/monika.ogg\")", output="Activated music.")
    play music m1
    $ run_input(input="player.snap(\"reality\")", output="Snapped to reality.")
    show monika_room
    with dissolve_scene_half
    show wallace 1bc zorder 2 at f11
    hide screen console_screen
    w "What were you possibly dreaming about?"
    show wallace 1be zorder 2 at f11
    w "Why did you go to sleep ON THE JOB-"
    show wallace 1bf zorder 2 at f11
    w "Remember, we're working on VM3, not napping on the job."
    show wallace 1bf zorder 2 at t11
    mc "So I can't sleep on the job...?"
    show wallace 2bj zorder 2 at f11
    w "WHAT ARE YOU THINKING? GET OUT OF MY OFFICE-"
    show wallace 2bi zorder 2 at t11
    mc "Okay, jeez man, you don't have to do this..."
    scene corridor
    with wipeleft
    stop music fadeout 0.5
    w "This lead developer sucks."
    mc "You suck more, Wallace."
    scene black
    with wipeleft
    scene office_sunset
    with wipeleft
    play music t8
    mc "This job is super exhausting. Let's just go home."
    guy_1 "I agree. I personally despise the \"Boss\" of this project."
    guy_2 "Same. This \"Boss\" makes things so complicated, I just wanna have fun!"
    mc "Wasn't his name \"Wallace\"?"
    mc "This \"Wallace\" kid, claiming hes the boss of the team."
    mc "I already hate him."
    mc "I'm the lead developer of VM3, promoted above him, and he still claims to be the boss."
    mc "Progress will continue."
    mc "I'll go home and continue work on VM3. You should get some rest too."
    $ guy1_name = "Joe (Dev 1)"
    $ guy2_name = "Patrick (Dev 2)"
    $ guy3_name = "Charles (Dev 3)"
    guy_1 "Farewell. I wish all the best for you, [player]."
    guy_2 "Alright, best of luck!"
    guy_3 "See ya."
    scene corridor_night
    with wipeleft
    stop music fadeout 0.5
    scene hallway_night
    with wipeleft
    play music t10
    mc "Just let me out of here..."
    scene house_night
    with wipeleft
    mc "This went quite badly."
    mc "However, we're almost done VM3!"
    mc "I've also been promoted above Wallace, but I shouldn't tell him yet."
    mc "Let's head inside."
    scene bedroom_night
    with wipeleft
    mc "I'm tired now... I need to start sleeping."
    mc "I guess I'll have to finish VM3 tomorrow."
    stop music fadeout 1.5
    scene black
    with dissolve_scene_full

    # Day 2
    "Act 0, Day 2. (2025)"
    # Insert transition here.
    scene office
    with dissolve_scene_half
    play music t2
    mc "It's the final day of development."
    mc "I just have to apply a few commands, and it's done."
    stop music fadeout 0.5
    scene computers
    with wipeleft
    play music t4
    $ console_history = []
    $ run_input(input="renpy.createchr(\"Monika\")", output="Created Monika")
    $ run_input(input="renpy.createchr(\"Natsuki\")", output="Created Natsuki.")
    $ run_input(input="renpy.createchr(\"Yuri\")", output="Created Yuri.")
    $ run_input(input="renpy.createchr(\"Sayori\")", output="Created Sayori.")
    mc "Got the main characters of the VM."
    mc "NPC's can be auto-generated at a later point."
    mc "Now for the backgrounds..."
    scene computers
    $ run_input(input="renpy.createbg(\"City_Park\")", output="Created Background.")
    $ run_input(input="renpy.createbg(\"City_Area\")", output="Created Background.")
    $ run_input(input="renpy.createbg(\"Country_Roads\")", output="Created Background.")
    $ run_input(input="renpy.createbg(\"Classroom\")", output="Created Background.")
    $ run_input(input="renpy.createbg(\"Club_room\")", output="Created Background.")
    $ run_input(input="renpy.createbg(\"Country_Side\")", output="Created Background.")
    mc "Houses too..."
    scene computers
    $ run_input(input="renpy.createhouse(\"[persistent.playername]House\")", output="Created House.")
    $ run_input(input="renpy.createhouse(\"NatsukiHouse\")", output="Created House.")
    $ run_input(input="renpy.createhouse(\"MonikaHouse\")", output="Created House.")
    $ run_input(input="renpy.createhouse(\"SayoriHouse\")", output="Created House.")
    $ run_input(input="renpy.createhouse(\"YuriHouse\")", output="Created House.")
    mc "We should be done with backgrounds."
    mc "I'll just quickly add this."
    scene computers
    $ run_input(input="renpy.createchr(\"[persistent.playername]\")", output="Created [persistent.playername].")
    mc "And remove this..."
    scene computers
    $ run_input(input="os.delete(\"Wallace.chr\")", output="Access Denied.")
    play music t7
    mc "What? Access denied???"
    scene computers
    $ run_input(input="os.elevateAccess([player])", output="Access Elevated.")
    play music t4
    mc "Finally. Let's get that stinking \"boss\" out of there, and while we're at it, remove Monika's permissions."
    mc "We don't want another VM1 again.."
    scene computers
    $ run_input(input="os.delete(\"Wallace\")", output="Deleted Wallace.chr")
    $ run_input(input="renpy.removePermission(\"Monika\")", output="Removed Permissions from Monika.")
    $ run_input(input="renpy.addPermission(\"[persistent.playername]\")", output="Added Permissions for [persistent.playername].")
    mc "For security sake, we should de-elevate permissions."
    scene computers
    $ run_input(input="os.resetPermission()", output="Access Permissions Reset.")
    play music t5
    mc "Should be done now! We'll be able to add things as the VM plays out."
    scene computers
    hide screen console_screen
    scene office
    with wipeleft
    $ w_name = "Wallace"
    mc "Ahh, finally..."
    play music t7
    show wallace 2bj zorder 2 at f11
    w "What do you think you are doing??"
    show wallace 2bi zorder 2 at t11
    mc "You can't stop me anymore."
    show wallace 2bm zorder 2 at f11
    w "Oh, I can."
    $ run_input(input="renpy.creatchr(\"Wallace\")", output="Access Denied.")
    show wallace 1bo zorder 2 at f11
    w "WHAT?"
    hide screen console_screen
    show wallace 2bj zorder 2 at f11
    w "I'll get you back for this. You can't do this, YOU PIECE OF-!"
    show wallace 2bi zorder 2 at t11
    mc "Okay then. I'd like to see you try."
    show wallace 2bj zorder 2 at f11
    w "I'm the boss of the entire project."
    show wallace 2bi zorder 2 at t11
    mc "Well, haven't you heard? I've been promoted above you, Wallace."
    show wallace 2bj zorder 2 at f11
    w "SCREW YOU."
    w "I WILL GET IN THE VM."
    show wallace 2bi zorder 2 at f11
    menu:
        "Should I delete him from real life?"
        "Yes":
            $ persistent.wallace_gone = 1
            call prologue_1 from _call_prologue_1
        "No":
            $ persistent.wallace_gone = 0
            call prologue_2 from _call_prologue_2
        "Break His Legs":
            $ persistent.wallace_gone = 1
            "Alright."
            mc "I'LL BREAK YOUR LEGS-"
            show wallace 2bi zorder 2 at t11
            w "I'd rather delete myself first."
            stop music fadeout 0.5
            $ console_history = []
            $ run_input(input="delete(\"Wallace\")", output="Wallace (\"Boss\") Deleted.")
            scene office
            play music t8
            mc "Dang... He got deleted first"
            hide screen console_screen
            mc "NOOOO I CANT BREAK WALLACE'S LEGS"
            mc "Welp... It was fun while it lasted."
    play music t5
    mc "Anyway, are you all ready to launch VM3?"
    $ guy1_name = "Joe"
    $ guy2_name = "Patrick"
    $ guy3_name = "Charles"
    if persistent.wallace_gone == 0:
        show wallace 2bj zorder 2 at t11
        w "No."
        show wallace 2bi zorder 2 at t11
        guy_1 "I'd say start the virtual machine."
        guy_2 "We're ready!"
        guy_3 "Just do it. I don't care."
        mc "4 against 1. You can't stop us now. Remember, I got promoted above you!"
        show wallace 2bp zorder 2 at t11
        w "Fine..."
        scene office
    else:
        guy_1 "Feel free to go ahead."
        guy_2 "Let's do this!"
        guy_3 "Just get this over with."
    mc "Time to launch the VM!"
    mc "Our entire lives have worked up to this point, so let's pray it works."
    stop music fadeout 0.5
    scene black
    with wipeleft
    scene office_sunset
    with wipeleft
    play music t3
    mc "Welp, that went well!"
    guy_1 "VM3's currently stable. Let's see what happens."
    guy_2 "It's amazing! I can do whatever I want now!"
    guy_3 "Finally, all this is over."
    mc "You bet."
    if persistent.wallace_gone == 0:
        guy_1 "Wait... Why isn't Wallace here?"
        mc "I'm not sure... Maybe he went home early?"
    play music t7
    mc "Wait, how are we going to connect to VM3?"
    guy_1 "We could always use a memory dump?"
    guy_3 "Memory dumps aren't consistent enough. Just screw it."
    mc "I *did* code in a [persistent.playername] character... but I'm not sure."
    guy_2 "We could use that!"
    guy_1 "Yeah, we could."
    guy_3 "Hey, [player]?"
    mc "Yeah?"
    guy_3 "You're going to have to enter VM3."
    guy_3 "I'm not asking you."
    guy_2 "We'll work out a way to get you out, don't worry!"
    mc "Do I have a choice..."
    mc "Alright. I'll get in the VM. I just need to go home for now."
    guy_1 "Alright, see you later."
    stop music fadeout 0.5
    scene corridor_night
    with wipeleft
    play music t3
    scene hallway_night
    with wipeleft
    scene house_night
    with wipeleft
    scene bedroom_night
    with wipeleft
    mc "This went well!"
    mc "We've just launched VM3, and it seems to be going smoothly."
    mc "It's currently set in 2012."
    mc "Welp, I'll see what happens tomorrow, I guess..."
    stop music fadeout 1.5
    scene black
    with dissolve_scene_full
    call day3 from _call_day3
    return

label prologue_1:
    $ console_history = []
    $ run_input(input="delete(\"Wallace\")", output="Wallace (\"Boss\") Deleted.")
    scene office
    play music t8
    mc "Get this \"Wallace\" out of here. Screw Wallace."
    hide screen console_screen
    mc "Did I made the right choice?"
    mc "Only time will tell..."
    return

label prologue_2:
    mc "I probably shouldn't. That's too harsh... right?"
    mc "Maybe, maybe not. Let's see..."
    return

label day3:
    "Act 0, Day 3 (2025)"
    scene bg bedroom
    with dissolve_scene_half
    play music t2
    mc "Ahh, good morning!"
    mc "I'm going to try to get into the VM."
    mc "It's going to be painful, but I think I know how to."
    mc "I can use my player script that I coded in!"
    play music t7
    mc "Wait, I should probably eat something!"
    mc "I need to go... Fast..."
    scene black
    with wipeleft
    scene bg kitchen
    with wipeleft
    mc "What shall I cook..."
    mc "I'm feeling lazy right now, so I'lll order some takeout instead..."
    play music t3
    mc "This is going to be interesting."
    scene black
    with wipeleft
    scene living_room
    with wipeleft
    mc "It's time to wait..."
    scene black
    with wipeleft
    $ pause(1)
    scene living_room
    with wipeleft
    mc "Food's here!"
    mc "Just got some pizza, nothing much."
    scene black
    with wipeleft
    "*nom*"
    scene living_room
    with wipeleft
    mc "That was some amazing pizza!"
    mc "I guess I'd better go to the office."
    mc "I'd rather not be late..."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t5
    scene office
    with wipeleft
    "We're here."
    "It's time to bring up the plan I had."
    mc "I think I might have a way to get in."
    mc "Team, follow me..."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t4
    scene ground_floor
    with wipeleft
    if persistent.wallace_gone == 0:
        mc "Team, are you sure about this?"
        show wallace 1bf zorder 2 at f11
        w "Just get in, [player]. I don't care about you."
        show wallace 1bc zorder 2 at t11
        guy_1 "Absolutely. Might as well try."
        guy_2 "We're sure!"
        guy_3 "Just get this built man."
        show wallace zorder 2 at thide
        mc "Alright then."
        mc "Here's how you do it..."
    else:
        mc "Team, are you sure about this?"
        guy_1 "We're sure."
        guy_2 "Let's get this built!"
        guy_3 "Yeah. Besides, we're forcing you in, it's not like you had a choice."
        mc "Alright then."
        mc "Let's see how to build this..."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t8
    scene ground_floor
    with wipeleft
    mc "And that's the entire project done!"
    guy_1 "That wasn't so complicated after all."
    mc "I'll hop in now. Wish me luck!"
    guy_2 "Good luck!"
    $ console_history = []
    $ run_input(input="os.merge(\"[persistent.playername]\", \"[player]\")", output="Merged [player] with [persistent.playername]")
    stop music fadeout 0.5
    scene black
    with dissolve_scene_full
    hide screen console_screen
    return