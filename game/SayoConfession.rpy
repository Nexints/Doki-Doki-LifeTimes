label sayodepression:
    show sayori 1l zorder 1 at f11:
        yalign 0.7
    s "But yeah, there is something on my mind."
    play music t9
    s "Ever since I've met you, I've just felt... different."
    s "You've made me feel something I've never felt before."
    s "I'm still trying to figure things out, but I think I might be falling in love with you."
    show sayori 1k zorder 1 at f11:
        yalign 0.7
    s "Do you accept my confession?"
    scene black
    with wipeleft
    menu:
        "Do I accept Sayori's confession?"
        "Yes":
            scene bg residential_day
            with wipeleft
            show sayori 1k zorder 1 at t11:
                yalign 0.7
            mc "I've liked you as well for a long time, but I wouldn't be able to tell you."
            mc "I think this goes without saying. I love you, Sayori."
            show sayori 3y zorder 1 at f11:
                yalign 0.7
            s "I love you too, [player]."
            scene black
            with wipeleft
            "It feels as if the only people around are me and Sayori."
            "Like I could spend this moment with her forever."
            mc "Soo, are we officially dating?"
            s "I'll have to think about it~"
            mc "Alright."
            scene bg residential_day
            with wipeleft
            show sayori 1y zorder 1 at t11:
                yalign 0.7
            mc "I'll probably head home though, as I do have a lot of work to do."
            "That was a partial lie, as I need to sort out my emotions."
            "But I do have a lot of work to do..."
            show sayori 1l zorder 1 at f11:
                yalign 0.7
            s "I have lots of work to do as well..."
            show sayori 1x zorder 1 at f11:
                yalign 0.7
            s "But do you want to hang out tomorrow?~"
            show sayori 1a zorder 1 at t11:
                yalign 0.7
            mc "Sure! I'll be available for you whenever you need."
            show sayori 1x zorder 1 at f11:
                yalign 0.7
            s "Alright! I do have to head home though, so see you later!"
            show sayori 1a zorder 1 at t11:
                yalign 0.7
            mc "See you, Sayo!"
            show sayori at thide:
                yalign 0.7
            mc "Welp, I guess I'm dating now...?"
            mc "But I'm not sure if any of this is real."
            mc "I can make it real though, I just have to try hard enough."
            scene black
            with wipeleft
        "No":
            scene bg residential_day
            with wipeleft
            mc "I just don't feel that way towards you..."
            mc "I'm sorry."
            show sayori 3u zorder 1 at f11:
                yalign 0.7
            s "It's alright... I'll just leave you be then."
            show sayori 3u at thide:
                yalign 0.7
            mc "Wait!"
            "..."
            mc "Well, she's long gone..."
            mc "Maybe things would've turned out differently in an alternate lifetime."
            mc "I'll just head home for now... I have tons of work to do."
            scene black
            with wipeleft