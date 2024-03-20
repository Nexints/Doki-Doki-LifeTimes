# Sayori's Route, part 1
# Complex feelings.

label sayo_route:
    "A couple of days later..."
    scene sayopov
    $ pause(0.01)
    scene black
    with dissolve_cg
    play music t9
    scene bg sayori_bedroom
    with wipeleft
    "I'm awoken by the sun for a brand new day."
    rc "But do you really belong here?"
    rc "[player] doesn't care about you."
    rc "He's not going to be there in the morning."
    "But he's been so nice to me..."
    "I have to get up, as [player] will get worried."
    "Besides, I have to keep my lie of being this \"cute girl\" alive."
    rc "The facade will fall, just like you."
    play music t7
    s "Wait, I'm late???"
    "I'll have to come up with an excuse for that one."
    play music t8
    s "I'll head off to school now!~"
    "Sayori's Mom" "You're late again?"
    s "Yeah... But I'm not going to be late again!"
    "I know that's a lie."
    "Sayori's Mom" "Alright. I'm just warning you."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t2
    scene bg residential_day
    with wipeleft
    "Just don't get [player] worried."
    s "Heyy!"
    play music t7
    "But [player] isn't here."
    rc "I told you. You're nothing to him."
    s "I'll just head to school on my own..."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t9
    scene bg class_day
    with wipeleft
    "I haven't seen [player] at all..."
    "Does he even care about me?"
    if persistent.lsayo == 0:
        call sayo_route_2 from _call_sayo_route_2
    else:
        call sayo_route_3 from _call_sayo_route_3
    return

label sayo_route_2:
    "I guess not-"
    mc "Sayo, are you here?"
    # Implement Rainclouds
    rc "[player] shouldn't care about you."
    rc "You're not good enough for [player]."
    "I'll deal with these rainclouds later."
    "I'll just go to sle-"
    "*MC Bursts through the door*"
    show mainchar 1b zorder 1 at t11:
        ypos 1.25
    s "Uwaa-"
    s "Heyy [player]!"
    play music t7
    show mainchar 1i zorder 1 at f11:
        ypos 1.25
    mc "Why were you here?"
    show mainchar 1b zorder 1 at t11:
        ypos 1.25
    s "I just come here to think sometimes..."
    s "But everything's alright! See?~"
    "I flash a bright smile to discourage [player] from finding out."
    show mainchar 1e zorder 1 at f11:
        ypos 1.25
    mc "I know something's off. Do you want to talk about it?"
    show mainchar 1s zorder 1 at f11:
        ypos 1.25
    mc "It's written all over you."
    show mainchar 1s zorder 1 at t11:
        ypos 1.25
    rc "See? Your little lies have fallen."
    "I'll still try to keep the lie..."
    s "I'm alright! I promise-"
    rc "Now you're just lying to the one person that showed sympathy for you."
    "At least he doesn't have to worry."
    show mainchar 1c zorder 1 at f11:
        ypos 1.25
    mc "Alright, if you say so. I'll see you at lunch!"
    mc "Just let me know if anything's wrong."
    stop music fadeout 0.5
    scene black
    with wipeleft
    "That lie... barely worked."
    "But at least [player] doesnt know exactly what I feel."
    "It's for the best. At least he doesn't have to worry-"
    play music t2
    scene bg class_day
    with wipeleft
    "Bell" "\"RIING!\""
    s "Welp, it's time to go."
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t5
    scene bg corridor
    with wipeleft
    "This gives me tons of time to contemplate my feelings for [player]."
    "Do I really like [player]? It's only been a couple of days since meeting him."
    "And yet, he's the only one whos actually cared."
    rc "He probably cares about other people more than you."
    "Yeah... I assumed so."
    "This is so confusing... I don't know what to feel."
    play music t8
    show mainchar 1t zorder 1 at f11:
        ypos 1.25
    mc "Earth to Sayori, are you there?"
    show mainchar 1t zorder 1 at t11:
        ypos 1.25
    s "I'm here! Don't worry~"
    show mainchar 1y zorder 1 at f11:
        ypos 1.25
    mc "Why were you just standing there?"
    show mainchar 1t zorder 1 at t11:
        ypos 1.25
    s "I'm just going to my typical lunch spot!"
    "I'm not really lying, but I'm also not telling the truth either..."
    show mainchar 1k zorder 1 at f11:
        ypos 1.25
    mc "Makes sense. Do you mind if I have a look?"
    show mainchar 1k zorder 1 at t11:
        ypos 1.25
    rc "[player]'s just being nice. He doesn't actually care."
    "But he's been so nice to me..."
    rc "Because he's nice to everyone that he meets. It's pretty clear, knowing from his attitude."
    s "Ehe~ Alright!"
    stop music fadeout 0.5
    scene black
    with wipeleft
    play music t3
    scene club_desks
    with wipeleft
    s "Here it is!~"
    show mainchar 1i zorder 1 at f11:
        ypos 1.25
    mc "Woah-"
    show mainchar 1c zorder 1 at f11:
        ypos 1.25
    mc "Nice place you got there."
    show mainchar 1a zorder 1 at t11:
        ypos 1.25
    s "It's quite cozy here!"
    s "I just like to sit here and eat with myself."
    show mainchar 1j zorder 1 at f11:
        ypos 1.25
    mc "Won't that make you a little isolated?"
    show mainchar 1h zorder 1 at t11:
        ypos 1.25
    s "And that's where I have to ask..."
    show mainchar 1i zorder 1 at t11:
        ypos 1.25
    s "Do you wanna sit with me?"
    rc "There's no way [player] says yes."
    rc "He doesn't really care about you, he's just nice to everyone."
    show mainchar 1k zorder 1 at f11:
        ypos 1.25
    mc "Sure, I don't mind."
    show mainchar 1f zorder 1 at f11:
        ypos 1.25
    mc "I mean, I don't know where else to sit, so might as well."
    show mainchar 1d zorder 1 at t11:
        ypos 1.25
    rc "You're still nothing to him. He's just being nice because he's nice to everyone else."
    rc "You aren't good enough for [player]."
    "But I can still try to make him feel included..."
    s "You're always welcome to sit here! Ehe~"
    show mainchar 1c zorder 1 at f11:
        ypos 1.25
    mc "Thanks, Sayo."
    scene black
    with wipeleft
    "It seems like he actually does care about me...?"
    "I'm not sure though what I feel about [player]. I've met him 2 days ago, and yet, he's been so caring towards me."
    rc "He doesn't care. [player]'s just nice to you because he is."
    "Honestly, I think [player] could be the one for me. I'd like to ask him out eventually, but I'm scared he'll deny a ditzy girl like myself."
    rc "He's more into other girls. He'd pick Monika over you any day of the week."
    rc "She is the class star. There's no way [player] will not accept Monika."
    "It's still worth a shot."
    rc "I'm just saying, [player] doesn't care at all about you."
    rc "You can try, but there's no way he accepts you."
    rc "I'm just the voice of reason."
    # Expand more on this segment.
    call sayo_route_4 from _call_sayo_route_4
    return

label sayo_route_3:
    scene black
    with wipeleft
    x "This is where this route for Doki Doki LifeTimes ends for now."
    x "We're around ~2\% done with this mod, and this route will get more work done on it!"
    x "There's so much more I want to add to this mod, so check out the github repository!"
    return