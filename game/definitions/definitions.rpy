## definitions.rpy

# This file defines important stuff for DDLC and your mod!

# This variable declares if the mod is a demo or not.
# Leftover from DDLC.
define persistent.demo = False

# This variable declares whether the mod is in the 'steamapps' folder.
define persistent.steam = ("steamapps" in config.basedir.lower())

# This variable declares whether Developer Mode is on or off in the mod.
define config.developer = False

# This python statement starts singleton to make sure only one copy of the mod
# is running.
python early:
    import singleton
    me = singleton.SingleInstance()

init -3 python:
    ## Dynamic Super Position (DSP)
    # DSP is a feature in where the game upscales the positions of assets 
    # with higher resolutions (1080p).
    # This is just simple division from Adobe, implemented in Python.
    def dsp(orig_val):
        ceil = False if isinstance(orig_val, float) else True
        dsp_scale = config.screen_width / 1280.0
        if ceil: return math.ceil(orig_val * dsp_scale)
        else: return orig_val * dsp_scale

    ## Dynamic Super Resolution
    # DSR is a feature in where the game upscales asset sizes to higher
    # resolutions (1080p) and sends back a modified transform.
    # (Recommend that you just make higher res assets than upscale lower res ones)
    class DSR:
        def __call__(self, path):
            img_bounds = renpy.image_size(path)
            return Transform(path, size=(dsp(img_bounds[0]), dsp(img_bounds[1])))

    dsr = DSR()

# This init python statement sets up the functions, keymaps and channels
# for the game.
init python:
    # These variable declarations adjusts the mapping for certain actions in-game.
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []

    # This variable declaration registers the music poem channel for the poem sharing music.
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    
    # This function gets the postition of the music playing in a given channel.
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    # This function deletes all the saves made in the mod.
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    # This function deletes a given character name from the characters folder.
    def delete_character(name):
        if renpy.android:
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/characters/" + name + ".chr")
            except: pass
        else:
            try: os.remove(config.basedir + "/characters/" + name + ".chr")
            except: pass

    # These functions restores all the character CHR files to the characters folder 
    # given the playthrough number in the mod and list of characters to restore.
    def restore_character(names):
        if not isinstance(names, list):
            raise Exception("'names' parameter must be a list. Example: [\"monika\", \"sayori\"].")

        for x in names:
            if renpy.android:
                try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/characters/" + x + ".chr")
                except: open(os.environ['ANDROID_PUBLIC'] + "/characters/" + x + ".chr", "wb").write(renpy.file("chrs/" + x + ".chr").read())
            else:
                try: renpy.file(config.basedir + "/characters/" + x + ".chr")
                except: open(config.basedir + "/characters/" + x + ".chr", "wb").write(renpy.file("chrs/" + x + ".chr").read())

    def restore_all_characters():
        if persistent.playthrough == 0:
            restore_character(["monika", "sayori", "natsuki", "yuri"])
        elif persistent.playthrough == 1 or persistent.playthrough == 2:
            restore_character(["monika", "natsuki", "yuri"])
        elif persistent.playthrough == 3:
            restore_character(["monika"])
        else:
            restore_character(["sayori", "natsuki", "yuri"])
    
    # This function is obsolete as all characters now restores only
    # relevant characters to the characters folder.
    def restore_relevant_characters():
        restore_all_characters()

    # This function pauses the time for a certain amount of time or indefinite.
    def pause(time=None):
        global _windows_hidden

        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False

## Music
# This section declares the music available to be played in the mod.
# Syntax:
#   audio. - This tells Ren'Py this is a audio variable.
#   t1 - This tells Ren'Py the label of the music/sound file being declared.
#   <loop 22.073> - This tells Ren'Py to loop the music/sound to this position when the song completes.
#   "bgm/1.ogg" - This tells Ren'Py the path of the music/sound file to use.
# Example: 
#   define audio.t2 = "bgm/2.ogg"

define audio.t1 = "<loop 22.073>bgm/1.ogg" # Doki Doki Literature Club! - Main Theme
define audio.t2 = "<loop 4.499>bgm/2.ogg" # Ohayou Sayori! - Sayori Theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg" # Main Theme - In Game 
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg" # Dreams of Love and Literature - Poem Game Theme
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg" # Okay Everyone! - Sharing Poems Theme

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" # Okay Everyone! (Monika)
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" # Okay Everyone! (Sayori)
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" # Okay Everyone! (Natsuki)
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" # Okay Everyone! (Yuri)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg" # Play With Me - Yuri/Natsuki Theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg" # Poem Panic - Argument Theme
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg" # Daijoubu! - Argument Resolved Theme
define audio.t9 = "<loop 3.172>bgm/9.ogg" # My Feelings - Emotional Theme
define audio.t9g = "<loop 1.532>bgm/9g.ogg" # My Feelings but 207% Speed
define audio.t10 = "<loop 5.861>bgm/10.ogg" # My Confession - Sayori Confession Theme
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg" # Just Monika. - Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" # I Still Love You - Monika Post-Delete Theme

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

## Backgrounds
# This section declares the backgrounds available to be shown in the mod.
# To define a new color background, declare a new image statement like in this example:
#     image blue = "X" where X is your color hex i.e. '#158353'
# To define a new background, declare a new image statement like this instead:
#     image bg bathroom = "mod_assets/bathroom.png" 

image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image sayopov = "#0d4662ff"
image mcpov = "#505005ff"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"

image bg residential_day = "bg/residential.png" # Start of DDLC BG
image bg class_day = "bg/class.png" # The classroom BG
image bg corridor = "bg/corridor.png" # The hallway BG
image bg club_day = "bg/club.png" # The club BG
image bg main_home = "bg/house.jpg"
image bg club_day2: # Glitched Club BG
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"

image bg closet = "bg/closet.png" # The closet BG
image bg bedroom = "bg/bedroom.png" # MC's Room BG
image bg sayori_bedroom = "bg/sayori_bedroom.png" # Sayori's Room BG
image bg house = "bg/house.png" # Sayori's House BG
image bg kitchen = "bg/kitchen.png" # MC's Kitchen BG

image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook-glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

# This image shows a glitched screen during Act 2 poem sharing with Yuri.
image bg glitch = LiveTile("bg/glitch.jpg")

# This image transform shows a glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0

# This image transform shows another glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0

# Characters
# This is where the characters bodies and faces are defined in the mod.
# They are defined by a left half, a right half and their head.
# To define a new image, declare a new image statement like in this example:
#     image sayori 1ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1cl.png", (0, 0), "mod_assets/sayori/1cr.png", (0, 0), "sayori/a.png")

# Sayori's Character Definitions
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

# Sayori in her Casual Outfit [Day 4]
image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

# This image shows a glitched Sayori sprite during Act 2.
image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki's Character Definitions
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")

# Natsuki in her casual outfit [Day 4 - Natsuki Route]
image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# These image definitions are left-overs of certain Natsuki expressions 
# found in the original 1.0 release of DDLC.
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

# This image shows the realistic mouth on Natsuki on a random playthrough
# of Act 2.
image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

# This image shows black rectangles on Natsuki on a random playthrough
# of Act 2.
image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

# This image transform makes the realistic mouth move on Natsuki's face
# on a random playthrough of Act 2.
image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

# These images show the Natsuki ghost sprite shown in the poemgame of 
# Act 2.
image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"

# This image makes Natsuki's sprite glitch up for a bit before
# returning to normal.
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

# These images declare alterative eyes for Natsuki on a random playthrough of
# Act 2.
image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri's Character Definitions
# Note: Sprites with a 'y' in the middle are Yuri's Yandere Sprites.
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

# Yuri in her casual outfit [Day 4 - Yuri Route]
image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

# This image shows the looping Yuri glitched head in Act 2.
image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

# These images shows Yuri stabbing herself at the end of Act 2 in six stages.
image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

# This image transform animates Yuri's eyes on her 6th stabbing in Act 2.
image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15

# These images shows Yuri with a offcenter right eye moving slowing away
# from her face.
image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

# These images show a glitched Yuri during Act 2.
image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

# These image declarations show Yuri's moving eyes in Act 2.
image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

# This image shows the base of Yuri's sprite as her eyes move.
image yuri eyes_base = "yuri/eyes1.png"

# This image shows Yuri's realistic moving eyes during Act 2.
image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

# This image shows another glitched Yuri from Act 2. 
image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

# Monika's Character Definitions
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

# This image transform shows a glitched Monika during a special poem.
image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

# This image transform shows Monika being glitched as she is 
# deleted in Act 3.
image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

## Character Variables
# This is where the characters are declared in the mod.
# To define a new character with assets, declare a character variable like in this example:
#   define e = DynamicCharacter('e_name', image='eileen', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
# To define a new character without assets, declare a character variable like this instead:
#   define en = Character('Eileen & Nat', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', image='mainchar', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define f = DynamicCharacter('f_name', image='femc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define w = DynamicCharacter('w_name', image='wallace', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define x = DynamicCharacter('x_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define guy_1 = DynamicCharacter('guy1_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define guy_2 = DynamicCharacter('guy2_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define guy_3 = DynamicCharacter('guy3_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define rc = DynamicCharacter('rc_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# This variable determines whether to allow the player to dismiss pauses.
# By default this is set by config.developer which is normally set to false
# once you packaged your mod.
define _dismiss_pause = config.developer

## [BETA] Pronoun Variables
# This section adds the feature to use player pronouns within the game text easily.
# To use this feature, simply ask the user for their pronoun and use it here.
# For capitalization, use heC, himC, areC and hesC
default persistent.he = ""
default persistent.him = ""
default persistent.are = ""
default persistent.hes = ""
default he = persistent.he
default him = persistent.him
default are = persistent.are
default hes = persistent.hes
default he_capital = he.capitalize()
default him_capital = him.capitalize()
default are_capital = are.capitalize()
default hes_capital = hes.capitalize()

## Extra Settings Variables
# This section controls whether the mod is censored or is in let's play mode.
default persistent.uncensored_mode = False
default persistent.lets_play = False

## Variables
# This section declares variables when the mod runs for the first time on all saves.
# To make a new persistent variable, make a new variable with the 'persistent.' in it's name
# like in this example:
#   default persistent.monika = 1
# To make a non-persistent variable, make a new variable like this instead:
#   default cookies = False
# To make sure a variable is set to a given condition use 'define' rather than 'default'.

default persistent.playername = ""
default player = persistent.playername
default currentuser = "Player"
default persistent.current_user = ""
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None

default persistent.wallace_gone = 0
default persistent.sayori_dead = 0
default persistent.america = 0
default persistent.sayori_relation = 0
default persistent.lsayo = 0

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

# Default Name Variables
# To define a default name make a character name variable like in this example:
#   default e_name = "Eileen"

default f_name = "FeMC"
default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default x_name = "Nexint"
default w_name = "Wallace"
default guy1_name = "Dev 1"
default guy2_name = "Dev 2"
default guy3_name = "Dev 3"
default rc_name = "RainClouds"

# Poem Variables
# This section records how much each character likes your poem in-game.
# Syntax:
#   -1 - Bad
#   0 - Neutral
#   1 - Good
# To add a new poem person, make a poem array like in this example:
#   default e_poemappeal = [0, 0, 0]

default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# This variable keeps tracks on which person won the poem session after each day.
default poemwinner = ['sayori', 'sayori', 'sayori']

# These variables keep track on who has read your poem during poem sharing
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# This variable keeps track on how many people have read your poem.
default poemsread = 0

# These variables store the appeal a character has to your poem
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# These variables control if we have seen Natsuki's or Yuri's exclusive scenes
default n_exclusivewatched = False
default y_exclusivewatched = False

# These variables track whether we gave Yuri our poem in Act 2 and if she
# ran away during Act 2 poem sharing.
default y_gave = False
default y_ranaway = False

# These variables track whether we read Natsuki's or Yuri's 3rd poem in poem sharing.
default n_read3 = False
default y_read3 = False

# This variable tracks which person we sided with in Day 2 of the game.
default ch1_choice = "sayori"

# This variable tracks if we gave Natsuki our poem first during poem sharing.
default n_poemearly = False

# These variables track whether we tried to help Monika or Sayori during Day 3's ending.
default help_sayori = None
default help_monika = None

# These variables track which route Day 4 will play and who is their name.
default ch4_scene = "yuri"
default ch4_name = "Yuri"

# This variable tracks whether we accepted Sayori's confession or not.
default sayori_confess = True

# This variable tracks whether we read Natsuki's 3rd poem in Act 2.
default natsuki_23 = None

################################################################################################
#Additional Definitions

#Happy Sayori hugging MC CG
image s_cg4:
    "mod_assets/cg/s_cg4.png"                                   #CREDIT: Malukah Maker#2907

#Monika Spaceroom #####################
image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1

image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image room_glitch = "images/cg/monika/monika_bg_glitch.png"
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
######################################


# Original Background Variants
image bedroom_night = "mod_assets/bg/bedroom_n.jpg"             #CREDIT: noah.rpy#1267 / nsmythddyas#5245
image class_sunset = "mod_assets/bg/class_s.jpg"                #CREDIT: Gorosona#8350
image class_night = "mod_assets/bg/class_n.jpg"                 #CREDIT: Alex [ORG]#9077
image club_sunset = "mod_assets/bg/club_s.jpg"                  #CREDIT: Gorosona#8350
image club_night = "mod_assets/bg/club_n.jpg"                   #CREDIT: Alex [ORG]#9077
image corridor_sunset = "mod_assets/bg/corridor_s.jpg"          #CREDIT: WAHnika (Current)#9757
image corridor_night = "mod_assets/bg/corridor_n.png"           #CREDIT: Alex [ORG]#9077
image corridor_rainy = "mod_asets/bg/corridor_r.png"            #CREDIT: Alex [ORG]#9077
image house_sunset = "mod_assets/bg/house_s.png"                #CREDIT: Crashpunk#0025
image house_night = "mod_assets/bg/house_n.jpg"                 #CREDIT: POBAWsiezmna#1550
image residential_sunset = "mod_assets/bg/residential_s.png"    #CREDIT: Crashpunk#0025
image residential_night = "mod_assets/bg/residential_n.png"     #CREDIT: TsunKrAZy#2862
image residential_rainy = "mod_asets/bg/residential_r.jpg"      #CREDIT: Astro Space#9989
image spaceroom_night = "mod_assets/bg/spaceroom_n.jpg"         #CREDIT: Alex [ORG]#9077

#House Backgrounds
image balcony = "mod_assets/bg/balcony.jpg"                     #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image bedroom_desk = "mod_assets/bg/bedroom_d.jpg"              #CREDIT: Akame#8940
image bedroom_2 = "mod_assets/bg/bedroom_2.jpg"                 #CREDIT osumashi
image dorm = "mod_assets/bg/dorm.jpg"                           #CREDIT osumashi
image dorm_sunset = "mod_assets/bg/dorm_s.jpg"                  #CREDIT osumashi
image dorm_night = "mod_assets/bg/dorm_n.jpg"                   #CREDIT osumashi
image entrance = "mod_assets/bg/entrance.jpg"                   #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image entrance_night = "mod_assets/bg/entrance_n.jpg"           #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image house_hallway = "mod_assets/bg/house_hallway.jpg"         #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image living_room = "mod_assets/bg/living_room.jpg"             #CREDIT: Nuxill#7870
image living_room_sunset = "mod_assets/bg/living_room_s.jpg"    #CREDIT: Nuxill#7870
image living_room_night = "mod_assets/bg/living_room_n.jpg"     #CREDIT: Nuxill#7870

image room = "mod_assets/bg/room.jpg"                           #CREDIT: Kimagure After
image room_sunset = "mod_assets/bg/room_s.jpg"                  #CREDIT: Kimagure After
image room_night = "mod_assets/bg/room_n.jpg"                   #CREDIT: Kimagure After
image moving_room = "mod_assets/bg/moving_room.jpg"             #CREDIT: Kimagure After
image moving_room_sunset = "mod_assets/bg/moving_room_s.jpg"    #CREDIT: Kimagure After
image moving_room_night = "mod_assets/bg/moving_room_n.jpg"     #CREDIT: Kimagure After

image monika_bedroom = "mod_assets/bg/monika_bedroom.jpg"       #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image monika_books = "mod_assets/bg/monika_room.jpg"             #CREDIT: Kimagure After
image monika_books = "mod_assets/bg/monika_room_s.jpg"    #CREDIT: Kimagure After
image monika_books = "mod_assets/bg/monika_room_n.jpg"     #CREDIT: Kimagure After

image natsuki_bedroom = "mod_assets/bg/natsuki_bedroom.jpg"             #CREDIT: Kimagure After
image natsuki_bedroom_sunset = "mod_assets/bg/natsuki_bedroom_s.jpg"    #CREDIT: Kimagure After
image natsuki_bedroom_night = "mod_assets/bg/natsuki_bedroom_n.jpg"     #CREDIT: Kimagure After
image natsuki_bedroom_midnight = "mod_assets/bg/natsuki_bedroom_m.jpg"  #CREDIT: Kimagure After

image yuri_bedroom = "mod_assets/bg/yuri_bedroom.jpg"           #CREDIT: Minikle / QQQnoQno   edited by Nuxill#7870
image yuri_room = "mod_assets/bg/yuri_room.jpg"                 #CREDIT: Kimagure After
image yuri_room_sunset = "mod_assets/bg/yuri_room_s.jpg"        #CREDIT: Kimagure After
image yuri_room_night = "mod_assets/bg/yuri_room_n.jpg"         #CREDIT: Kimagure After
image yuri_room_midnight = "mod_assets/bg/yuri_room_m.jpg"      #CREDIT: Kimagure After

#Residential Backgrounds
image building = "mod_assets/bg/building.jpg"                   #CREDIT: Kimagure After
image building_sunset = "mod_assets/bg/building_s.jpg"          #CREDIT: Kimagure After
image building_night = "mod_assets/bg/building_n.jpg"           #CREDIT: Kimagure After
image building_midnight = "mod_assets/bg/building_m.jpg"        #CREDIT: Kimagure After
image building_rainy = "mod_assets/bg/building_r.jpg"           #CREDIT: Kimagure After
image garden = "mod_assets/bg/garden.jpg"                       #CREDIT: Kimagure After
image monika_house = "mod_assets/bg/monika_house.jpg"           #DDLC
image natsuki_house = "mod_assets/bg/natsuki_house.jpg"                 #CREDIT: Kimagure After
image natsuki_house_sunset = "mod_assets/bg/natsuki_house_s.jpg"        #CREDIT: Kimagure After
image natsuki_house_night = "mod_assets/bg/natsuki_house_n.jpg"         #CREDIT: Kimagure After

image park = "mod_assets/bg/park.jpg"                           #CREDIT: Creative Freaks
image park_sunset = "mod_assets/bg/park_s.jpg"                  #CREDIT: Creative Freaks
image park_night = "mod_assets/bg/park_n.jpg"                   #CREDIT: Creative Freaks
image park_overlook = "mod_assets/bg/park_overlook.jpg"         #CREDIT Cyrke#8043
image park_entrance = "mod_assets/bg/park_entrance.jpg"                 #CREDIT: Kimagure After
image park_entrance_sunset = "mod_assets/bg/park_entrance_s.jgp"        #CREDIT: Kimagure After
image park_entrance_night = "mod_assets/bg/park_entrance_n.jpg"         #CREDIT: Kimagure After
image pathway = "mod_assets/bg/pathway.jpg"                     #CREDIT: Kimagure After
image pathway_sunset = "mod_assets/bg/pathway_s.jpg"            #CREDIT: Kimagure After
image pathway_night = "mod_assets/bg/pathway_n.jpg"             #CREDIT: Kimagure After
image sidewalk = "mod_assets/bg/sidewalk.jpg"                   #CREDIT: Uncle Mugen

#City Backgrounds
image alley = "mod_assets/bg/alley.jpg"                         #CREDIT osumashi
image alley_2 = "mod_assets/bg/alley_2.jpg"                     #CREDIT osumashi
image intersection = "mod_assets/bg/intersection.jpg"                   #CREDIT: Kimagure After
image intersection_sunset = "mod_assets/bg/intersection_s.jpg"          #CREDIT: Kimagure After
image intersection_night = "mod_assets/bg/intersection_n.jpg"           #CREDIT: Kimagure After
image intersection_midnight = "mod_assets/bg/intersection_m.jpg"        #CREDIT: Kimagure After
image intersection_rainy = "mod_assets/bg/intersection_r.jpg"           #CREDIT: Kimagure After
        
image shops = "mod_assets/bg/shops.jpg"                         #CREDIT: (c) 安野譲 (Vanishing Point)
image shops_sunset = "mod_assets/bg/shops_s.jpg"                #CREDIT: (c) 安野譲 (Vanishing Point)
image shops_night = "mod_assets/bg/shops_n.jpg"                 #CREDIT: (c) 安野譲 (Vanishing Point)
image shops_midnight = "mod_assets/bg/shops_m.jpg"              #CREDIT: (c) 安野譲 (Vanishing Point)
image restaurant = "mod_assets/bg/restaurant.jpg"               #CREDIT: yagamirai10#7046
image public_library = "mod_assets/bg/public_library.jpg"       #CREDIT: Yukito

image street = "mod_assets/bg/street.jpg"                       #CREDIT: Kimagure After
image street_sunset = "mod_assets/bg/street_s.jpg"              #CREDIT: Kimagure After
image street_night = "mod_assets/bg/street_n.jpg"               #CREDIT: Kimagure After
image street_midnight = "mod_assets/bg/street_m.jpg"            #CREDIT: Kimagure After
image street_rainy = "mod_assets/bg/street_r.jpg"               #CREDIT: Kimagure After

image train = "mod_assets/bg/train.jpg"                         #CREDIT: Kimagure After
image train_sunset = "mod_assets/bg/train_s.jpg"                #CREDIT: Kimagure After
image train_night = "mod_assets/bg/train_n.jpg"                 #CREDIT: Kimagure After

#School Backgrounds
image bathroom = "mod_assets/bg/bathroom.jpg"                   #CREDIT: u/AFewSecondsToLive
image board = "mod_assets/bg/board.jpg"                         #CREDIT: Cyrke#8043
image chalkboard = "mod_assets/bg/chalkboard.png"               #CREDIT yagamirai10#7046
image chalkboard_graffiti = "mod_assets/bg/chalkboard_g.png"    #CREDIT yagamirai10#7046
image classroom = "mod_assets/bg/class.jpg"                     #CREDIT: Kimagure After
image classroom_sunset = "mod_assets/bg/class_s.jpg"            #CREDIT: Kimagure After
image classroom_night = "mod_assets/bg/class_n.jpg"             #CREDIT: Kimagure After
image classroom_2 = "mod_assets/bg/classroom_2.jpg"             #CREDIT: Yukito
image club_desks = "mod_assets/bg/club_desks.jpg"               #CREDIT: Wheatley#3103, edited by Malukah Maker#2907
image empty_classroom = "mod_assets/bg/empty_classroom.jpg"             #CREDIT: Kimagure After
image empty_classroom_sunset = "mod_assets/bg/empty_classroom.jpg"      #CREDIT: Kimagure After
image empty_classroom_night = "mod_assets/bg/empty_classroom.jpg"       #CREDIT: Kimagure After
image lecture = "mod_assets/bg/lecture.jpg"                     #CREDIT: Kimagure After
image lecture_sunset = "mod_assets/bg/lecture_s.jpg"            #CREDIT: Kimagure After
image lecture_night = "mod_assets/bg/lecture_n.jpg"             #CREDIT: Kimagure After
image lecture_2 = "mod_assets/bg/lecture_2.jpg"                 #CREDIT: Yukito
image school = "mod_assets/bg/school.jpg"                       #CREDIT: Kimagure After
image school_sunset = "mod_assets/bg/school_s.jpg"              #CREDIT: Kimagure After
image school_night = "mod_assets/bg/school_n.jpg"               #CREDIT: Kimagure After

image hallway = "mod_assets/bg/hallway.jpg"                     #CREDIT: Kimagure After
image hallway_sunset = "mod_assets/bg/hallway_s.jpg"            #CREDIT: Kimagure After
image hallway_night = "mod_assets/bg/hallway_n.jpg"             #CREDIT: Kimagure After
image hallway_midnight = "mod_assets/bg/hallway_m.jpg"          #CREDIT: Kimagure After
image main_hall = "mod_assets/bg/main_hall.jpg"                 #CREDIT: Kimagure After
image main_hall_sunset = "mod_assets/bg/main_hall_s.jpg"        #CREDIT: Kimagure After
image main_hall_night = "mod_assets/bg/main_hall_n.jpg"         #CREDIT: Kimagure After
image main_hall_midnight = "mod_assets/bg/main_hall_m.jpg"      #CREDIT: Kimagure After

image ground_floor = "mod_assets/bg/ground.jpg"                 #CREDIT: Kimagure After
image ground_floor_sunset = "mod_assets/bg/ground_s.jpg"        #CREDIT: Kimagure After
image ground_floor_night = "mod_assets/bg/ground_n.jpg"         #CREDIT: Kimagure After
image second_floor = "mod_assets/bg/s_floor.jpg"                #CREDIT: Kimagure After
image second_floor_sunset = "mod_assets/bg/s_floor_s.jpg"       #CREDIT: Kimagure After
image second_floor_night = "mod_assets/bg/s_floor_n.jpg"        #CREDIT: Kimagure After
image stairway = "mod_assets/bg/stairway.jpg"                   #CREDIT: Kimagure After
image stairway_sunset = "mod_assets/bg/stairway_s.jpg"          #CREDIT: Kimagure After
image stairway_night = "mod_assets/bg/stairway_n.jpg"           #CREDIT: Kimagure After

image gate = "mod_assets/bg/gate.jpg"                           #CREDIT: Kimagure After
image gate_sunset = "mod_assets/bg/gate_s.jpg"                  #CREDIT: Kimagure After
image gate_night = "mod_assets/bg/gate_n.jpg"                   #CREDIT: Kimagure After
image gate_midnight = "mod_assets/bg/gate_m.jpg"                #CREDIT: Kimagure After
image gate_rainy = "mod_assets/bg/gate_r.jpg"                   #CREDIT: Kimagure After
image outside = "mod_assets/bg/outside.jpg"                     #CREDIT: Kimagure After
image outside_sunset = "mod_assets/bg/outside_s.jpg"            #CREDIT: Kimagure After
image outside_night = "mod_assets/bg/outside_n.jpg"             #CREDIT: Kimagure After

image computers = "mod_assets/bg/computers.jpg"                 #CREDIT: Kimagure After
image computers_night = "mod_assets/bg/computers_n.jpg"         #CREDIT: Kimagure After
image office = "mod_assets/bg/office.jpg"                       #CREDIT: Kimagure After
image office_sunset = "mod_assets/bg/office_s.jpg"              #CREDIT: Kimagure After
image office_night = "mod_assets/bg/office_n.jpg"               #CREDIT: Kimagure After
image storage = "mod_assets/bg/storage.jpg"                     #CREDIT: Kimagure After
image storage_sunset = "mod_assets/bg/storage_s.jpg"            #CREDIT: Kimagure After
image storage_night = "mod_assets/bg/storage_n.jpg"             #CREDIT: Kimagure After

image art = "mod_assets/bg/art.jpg"                             #CREDIT: Kimagure After
image art_sunset = "mod_assets/bg/art_s.jpg"                    #CREDIT: Kimagure After
image art_night = "mod_assets/bg/art_n.jpg"                     #CREDIT: Kimagure After
image artroom = "mod_assets/bg/artroom.jpg"                     #CREDIT: Kimagure After
image artroom_sunset = "mod_assets/bg/artroom_s.jpg"            #CREDIT: Kimagure After
image artroom_night = "mod_assets/bg/artroom_n.jpg"             #CREDIT: Kimagure After
image art_empty = "mod_assets/bg/art_empty.jpg"                 #CREDIT: Kimagure After
image art_empty_sunset = "mod_assets/bg/art_empty_s.jpg"        #CREDIT: Kimagure After
image art_empty_night = "mod_assets/bg/art_empty_n.jpg"         #CREDIT: Kimagure After
image piano_room = "mod_assets/bg/piano.jpg"                    #CREDIT: Yukito
image piano_room_full = "mod_assets/bg/piano_full.jpg"          #CREDIT: Yukito

image gym = "mod_assets/bg/gym.jpg"                             #CREDIT: (c) 安野譲 (Vanishing Point)
image gym_sunset = "mod_assets/bg/gym_s.jpg"                    #CREDIT: (c) 安野譲 (Vanishing Point)
image gym_night = "mod_assets/bg/gym_n.jpg"                     #CREDIT: (c) 安野譲 (Vanishing Point)
image gym_midnight = "mod_assets/bg/gym_m.jpg"                  #CREDIT: (c) 安野譲 (Vanishing Point)
image pool = "mod_assets/bg/pool.jpg"
image pool_sunset = "mod_assets/bg/pool_s.jpg"                  #CREDIT: Kimagure After
image pool_night = "mod_assets/bg/pool_n.jpg"                   #CREDIT: Kimagure After
image pool_rainy = "mod_assets/bg/pool_r.jpg"                   #CREDIT: Kimagure After
image lockers = "mod_assets/bg/lockers.jpg"                     #CREDIT: Kimagure After
image lockers_sunset = "mod_assets/bg/lockers_s.jpg"            #CREDIT: Kimagure After
image lockers_night = "mod_assets/bg/lockers_n.jpg"             #CREDIT: Kimagure After

image library = "mod_assets/bg/library.jpg"                     #CREDIT: Kimagure After
image library_sunset = "mod_assets/bg/library_s.jpg"            #CREDIT: Kimagure After
image library_night = "mod_assets/bg/library_n.jpg"             #CREDIT: Kimagure After
image medical = "mod_assets/bg/medical.jpg"                     #CREDIT: Kimagure After
image medical_sunset = "mod_assets/bg/medical_s.jpg"            #CREDIT: Kimagure After
image medical_night = "mod_assets/bg/medical_n.jpg"             #CREDIT: Kimagure After
image staff_room = "mod_assets/bg/staff_room.jpg"               #CREDIT: Yukito

image roof = "mod_assets/bg/roof.jpg"                           #CREDIT: Kimagure After
image roof_sunset = "mod_assets/bg/roof_s.jpg"                  #CREDIT: Kimagure After
image roof_night = "mod_assets/bg/roof_n.jpg"                   #CREDIT: Kimagure After
image roof_rainy = "mod_assets/bg/roof_r.jpg"                   #CREDIT: Kimagure After
image yard = "mod_assets/bg/yard.jpg"                           #CREDIT: (c) 安野譲 (Vanishing Point)
image yard_sunset = "mod_assets/bg/yard_s.jpg"                  #CREDIT: (c) 安野譲 (Vanishing Point)
image yard_night = "mod_assets/bg/yard_n.jpg"                   #CREDIT: (c) 安野譲 (Vanishing Point)
image yard_midnight = "mod_assets/bg/yard_m.jpg"                #CREDIT: (c) 安野譲 (Vanishing Point)

#Misc Backgrounds
image breakdown = "mod_assets/bg/breakdown.jpg"                 #CREDIT: Trueloverofmonika#5084



# Sayori
image sayori 1z = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/z.png")         #HEAD CREDIT: SpringingTraps#5243
image sayori 1za = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/za.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 1zb = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zb.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 1zc = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zc.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 1zd = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zd.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 1ze = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/ze.png")       #HEAD CREDIT: LeoDeCraprio#4239

image sayori 1bz = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/z.png")      #HEAD CREDIT: SpringingTraps#5243
image sayori 1bza = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/za.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 1bzb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zb.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 1bzc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zc.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 1bzd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zd.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 1bze = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/ze.png")    #HEAD CREDIT: LeoDeCraprio#4239

image sayori 2z = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/z.png")         #HEAD CREDIT: SpringingTraps#5243
image sayori 2za = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/za.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 2zb = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zb.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 2zc = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zc.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 2zd = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zd.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 2ze = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/ze.png")       #HEAD CREDIT: LeoDeCraprio#4239

image sayori 2bz = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/z.png")      #HEAD CREDIT: SpringingTraps#5243
image sayori 2bza = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/za.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 2bzb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zb.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 2bzc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zc.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 2bzd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zd.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 2bze = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/ze.png")    #HEAD CREDIT: LeoDeCraprio#4239

image sayori 3z = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/z.png")         #HEAD CREDIT: SpringingTraps#5243
image sayori 3za = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/za.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 3zb = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zb.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 3zc = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zc.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 3zd = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/zd.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 3ze = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori/ze.png")       #HEAD CREDIT: LeoDeCraprio#4239

image sayori 3bz = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/z.png")      #HEAD CREDIT: SpringingTraps#5243
image sayori 3bza = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/za.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 3bzb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zb.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 3bzc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zc.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 3bzd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/zd.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 3bze = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sayori/ze.png")    #HEAD CREDIT: LeoDeCraprio#4239

image sayori 4z = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/z.png")         #HEAD CREDIT: SpringingTraps#5243
image sayori 4za = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/za.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 4zb = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zb.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 4zc = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zc.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 4zd = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/zd.png")       #HEAD CREDIT: u/NormallyAverage
image sayori 4ze = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sayori/ze.png")       #HEAD CREDIT: LeoDeCraprio#4239

image sayori 4bz = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/z.png")      #HEAD CREDIT: SpringingTraps#5243
image sayori 4bza = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/za.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 4bzb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zb.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 4bzc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zc.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 4bzd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/zd.png")    #HEAD CREDIT: u/NormallyAverage
image sayori 4bze = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sayori/ze.png")    #HEAD CREDIT: LeoDeCraprio#4239

#BODY CREDIT: u/NormallyAverage##########
image sayori 6a = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/a.png")
image sayori 6b = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/b.png")
image sayori 6c = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/c.png")
image sayori 6d = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/d.png")
image sayori 6e = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/e.png")
image sayori 6f = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/f.png")
image sayori 6g = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/g.png")
image sayori 6h = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/h.png")
image sayori 6i = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/i.png")
image sayori 6j = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/j.png")
image sayori 6k = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/k.png")
image sayori 6l = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/l.png")
image sayori 6m = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/m.png")
image sayori 6n = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/n.png")
image sayori 6o = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/o.png")
image sayori 6p = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/p.png")
image sayori 6q = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/q.png")
image sayori 6r = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/r.png")
image sayori 6s = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/s.png")
image sayori 6t = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/t.png")
image sayori 6u = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/u.png")
image sayori 6v = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/v.png")
image sayori 6w = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/w.png")
image sayori 6x = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/x.png")
image sayori 6y = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "sayori/y.png")
image sayori 6z = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/z.png")   #HEAD CREDIT: SpringingTraps#5243
image sayori 6za = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/za.png") #HEAD CREDIT: u/NormallyAverage
image sayori 6zb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/zb.png") #HEAD CREDIT: u/NormallyAverage
image sayori 6zc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/zc.png") #HEAD CREDIT: u/NormallyAverage
image sayori 6zd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/zd.png") #HEAD CREDIT: u/NormallyAverage
image sayori 6ze = im.Composite((960, 960), (0, 0), "mod_assets/sayori/4l.png", (0, 0), "mod_assets/sayori/4r.png", (0, 0), "mod_assets/sayori/ze.png") #HEAD CREDIT: LeoDeCraprio#4239
########################################

#Natsuki
image natsuki 1za = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/za.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1zb = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zb.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1zc = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zc.png")           #DDLC
image natsuki 1zd = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zd.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1ze = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/ze.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 1zf = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zf.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 1zg = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zg.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 1zh = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zh.png")           #HEAD CREDIT: u/DeliRoxeD

image natsuki 1bza = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/za.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1bzb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zb.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1bzc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zc.png")        #DDLC 
image natsuki 1bzd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zd.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 1bze = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/ze.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 1bzf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zf.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 1bzg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zg.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 1bzh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zh.png")        #HEAD CREDIT: u/DeliRoxeD

image natsuki 2za = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/za.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2zb = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zb.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2zc = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zc.png")           #DDLC 
image natsuki 2zd = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zd.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2ze = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/ze.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 2zf = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zf.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 2zg = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zg.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 2zh = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zh.png")           #HEAD CREDIT: u/DeliRoxeD

image natsuki 2bza = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/za.png")         #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2bzb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zb.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2bzc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zc.png")        #DDLC 
image natsuki 2bzd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zd.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 2bze = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/ze.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 2bzf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zf.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 2bzg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zg.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 2bzh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zh.png")        #HEAD CREDIT: u/DeliRoxeD

image natsuki 3za = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/za.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3zb = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zb.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3zc = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zc.png")           #DDLC 
image natsuki 3zd = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zd.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3ze = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/ze.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 3zf = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zf.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 3zg = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zg.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 3zh = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/zh.png")           #HEAD CREDIT: u/DeliRoxeD

image natsuki 3bza = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/za.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3bzb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zb.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3bzc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zc.png")        #DDLC 
image natsuki 3bzd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zd.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 3bze = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/ze.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 3bzf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zf.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 3bzg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zg.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 3bzh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/zh.png")        #HEAD CREDIT: u/DeliRoxeD

image natsuki 4za = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/za.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4zb = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zb.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4zc = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zc.png")           #DDLC 
image natsuki 4zd = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zd.png")           #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4ze = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/ze.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 4zf = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zf.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 4zg = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zg.png")           #HEAD CREDIT: u/DeliRoxeD
image natsuki 4zh = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/zh.png")           #HEAD CREDIT: u/DeliRoxeD

image natsuki 4bza = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/za.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4bzb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zb.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4bzc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zc.png")        #DDLC 
image natsuki 4bzd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zd.png")        #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 4bze = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/ze.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 4bzf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zf.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 4bzg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zg.png")        #HEAD CREDIT: u/DeliRoxeD
image natsuki 4bzh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/zh.png")        #HEAD CREDIT: u/DeliRoxeD

image natsuki 5za = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/za.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5zb = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zb.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5zc = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zc.png", (0, 0), "natsuki/3.png")            #DDLC 
image natsuki 5zd = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zd.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5ze = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/ze.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: u/DeliRoxeD
image natsuki 5zf = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zf.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: u/DeliRoxeD
image natsuki 5zg = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zg.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: u/DeliRoxeD
image natsuki 5zh = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zh.png", (0, 0), "natsuki/3.png")            #HEAD CREDIT: u/DeliRoxeD

image natsuki 5bza = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/za.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5bzb = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zb.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5bzc = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zc.png", (0, 0), "natsuki/3b.png")          #DDLC 
image natsuki 5bzd = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zd.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 5bze = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/ze.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: u/DeliRoxeD
image natsuki 5bzf = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zf.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: u/DeliRoxeD
image natsuki 5bzg = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zg.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: u/DeliRoxeD
image natsuki 5bzh = im.Composite((960, 960), (18, 22), "mod_assets/natsuki/zh.png", (0, 0), "natsuki/3b.png")          #HEAD CREDIT: u/DeliRoxeD


#BODY CREDIT: u/NormallyAverage##########
image natsuki 61 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/1t.png")
image natsuki 6a = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/a.png")
image natsuki 6b = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/b.png")
image natsuki 6c = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/c.png")
image natsuki 6d = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/d.png")
image natsuki 6e = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/e.png")
image natsuki 6f = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/f.png")
image natsuki 6g = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/g.png")
image natsuki 6h = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/h.png")
image natsuki 6i = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/i.png")
image natsuki 6j = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/j.png")
image natsuki 6k = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/k.png")
image natsuki 6l = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/l.png")
image natsuki 6m = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/m.png")
image natsuki 6n = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/n.png")
image natsuki 6o = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/o.png")
image natsuki 6p = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/p.png")
image natsuki 6q = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/q.png")
image natsuki 6r = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/r.png")
image natsuki 6s = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/s.png")
image natsuki 6t = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/t.png")
image natsuki 6u = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/u.png")
image natsuki 6v = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/v.png")
image natsuki 6w = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/w.png")
image natsuki 6x = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/x.png")
image natsuki 6y = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/y.png")
image natsuki 6z = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "natsuki/z.png")
image natsuki 6za = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/za.png")     #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 6zb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zb.png")     #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 6zc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zc.png")     #DDLC 
image natsuki 6zd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zd.png")     #HEAD CREDIT: alykait { 𝓓𝓜 }#1259
image natsuki 6ze = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/ze.png")     #HEAD CREDIT: u/DeliRoxeD
image natsuki 6zf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zf.png")     #HEAD CREDIT: u/DeliRoxeD
image natsuki 6zg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zg.png")     #HEAD CREDIT: u/DeliRoxeD
image natsuki 6zh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/4l.png", (0, 0), "mod_assets/natsuki/4r.png", (0, 0), "mod_assets/natsuki/zh.png")     #HEAD CREDIT: u/DeliRoxeD
########################################

image natsuki 7a2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/5.png", (0, 0), "mod_assets/natsuki/a2.png")    #DDLC


# Yuri
image yuri 1x = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/x.png")         #HEAD CREDIT: u/NormallyAverage
image yuri 1y = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/y.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1z = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/z.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1za = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/za.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1zb = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zb.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1zc = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zc.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zd = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zd.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1ze = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/ze.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zf = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zf.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zg = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zg.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zh = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zh.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zi = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zi.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zj = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zj.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zk = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zk.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zl = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zl.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zm = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zm.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 1zn = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yuri/zn.png")       #HEAD CREDIT: yagamirai10#7046

image yuri 1y8 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y8.png")
image yuri 1y9 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y9.png")
image yuri 1y10 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y10.png")
image yuri 1y11 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y11.png")

image yuri 1bx = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/x.png")      #HEAD CREDIT: u/NormallyAverage
image yuri 1by = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/y.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1bz = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/z.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1bza = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/za.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1bzb = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zb.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 1bzc = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zc.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzd = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zd.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bze = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/ze.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzf = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zf.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzg = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zg.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzh = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zh.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzi = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zi.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzj = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zj.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzk = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zk.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzl = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zl.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzm = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zm.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 1bzn = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png", (0, 0), "mod_assets/yuri/zn.png")    #HEAD CREDIT: yagamirai10#7046

image yuri 2x = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/x.png")         #HEAD CREDIT: u/NormallyAverage
image yuri 2y = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/y.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2z = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/z.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2za = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/za.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2zb = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zb.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2zc = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zc.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zd = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zd.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2ze = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/ze.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zf = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zf.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zg = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zg.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zh = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zh.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zi = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zi.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zj = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zj.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zk = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zk.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zl = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zl.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zm = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zm.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 2zn = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zn.png")       #HEAD CREDIT: yagamirai10#7046

image yuri 2y8 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y8.png")
image yuri 2y9 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y9.png")
image yuri 2y10 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y10.png")
image yuri 2y11 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y11.png")

image yuri 2bx = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/x.png")      #HEAD CREDIT: u/NormallyAverage
image yuri 2by = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/y.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2bz = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/z.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2bza = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/za.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2bzb = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zb.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 2bzc = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zc.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzd = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zd.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bze = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/ze.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzf = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zf.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzg = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zg.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzh = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zh.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzi = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zi.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzj = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zj.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzk = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zk.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzl = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zl.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzm = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zm.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 2bzn = im.Composite((960, 960), (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zn.png")    #HEAD CREDIT: yagamirai10#7046

image yuri 3x = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/x.png")         #HEAD CREDIT: u/NormallyAverage
image yuri 3y = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/y.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3z = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/z.png")         #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3za = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/za.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3zb = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zb.png")       #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3zc = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zc.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zd = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zd.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3ze = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/ze.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zf = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zf.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zg = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zg.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zh = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zh.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zi = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zi.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zj = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zj.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zk = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zk.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zl = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zl.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zm = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zm.png")       #HEAD CREDIT: u/NormallyAverage
image yuri 3zn = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yuri/zn.png")       #HEAD CREDIT: yagamirai10#7046

image yuri 3y8 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y8.png")
image yuri 3y9 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y9.png")
image yuri 3y10 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y10.png")
image yuri 3y11 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y11.png")

image yuri 3bx = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/x.png")      #HEAD CREDIT: u/NormallyAverage
image yuri 3by = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/y.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3bz = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/z.png")      #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3bza = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/za.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3bzb = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zb.png")    #HEAD CREDIT: LeoDeCraprio#4239
image yuri 3bzc = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zc.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzd = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zd.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bze = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/ze.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzf = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zf.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzg = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zg.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzh = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zh.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzi = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zi.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzj = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zj.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzk = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zk.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzl = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zl.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzm = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zm.png")    #HEAD CREDIT: u/NormallyAverage
image yuri 3bzn = im.Composite((960, 960), (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png", (0, 0), "mod_assets/yuri/zn.png")    #HEAD CREDIT: yagamirai10#7046

image yuri 4f = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "mod_assets/yuri/f2.png")
image yuri 4g = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "mod_assets/yuri/g2.png")

# Monika
image monika 1s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/s.png")         #HEAD CREDIT: u/NormallyAverage
image monika 1t = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/t.png")         #HEAD CREDIT: greenbean01#6360
image monika 1u = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/u.png")         #HEAD CREDIT: greenbean01#6360
image monika 1v = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/v.png")         #HEAD CREDIT: u/NormallyAverage
image monika 1w = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/w.png")         #HEAD CREDIT: TsunKrAZy#2862
image monika 1x = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/x.png")         #HEAD CREDIT: yagamirai10#7046
image monika 1y = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/y.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 1z = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/z.png")         #HEAD CREDIT: yagamirai10#7046
image monika 1za = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/za.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 1zb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zb.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 1zc = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zc.png")       #HEAD CREDIT: u/NormallyAverage
image monika 1zd = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zd.png")       #HEAD CREDIT: yagamirai10#7046
image monika 1ze = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/ze.png")       #HEAD CREDIT: u/NormallyAverage

image monika 2s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/s.png")         #HEAD CREDIT: u/NormallyAverage
image monika 2t = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/t.png")         #HEAD CREDIT: greenbean01#6360
image monika 2u = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/u.png")         #HEAD CREDIT: greenbean01#6360
image monika 2v = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/v.png")         #HEAD CREDIT: u/NormallyAverage
image monika 2w = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/w.png")         #HEAD CREDIT: TsunKrAZy#2862
image monika 2x = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/x.png")         #HEAD CREDIT: yagamirai10#7046
image monika 2y = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/y.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 2z = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/z.png")         #HEAD CREDIT: yagamirai10#7046
image monika 2za = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/za.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 2zb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zb.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 2zc = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zc.png")       #HEAD CREDIT: u/NormallyAverage
image monika 2zd = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zd.png")       #HEAD CREDIT: yagamirai10#7046
image monika 2ze = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/ze.png")       #HEAD CREDIT: u/NormallyAverage

image monika 3s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/s.png")         #HEAD CREDIT: u/NormallyAverage
image monika 3t = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/t.png")         #HEAD CREDIT: greenbean01#6360
image monika 3u = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/u.png")         #HEAD CREDIT: greenbean01#6360
image monika 3v = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/v.png")         #HEAD CREDIT: u/NormallyAverage
image monika 3w = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/w.png")         #HEAD CREDIT: TsunKrAZy#2862
image monika 3x = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/x.png")         #HEAD CREDIT: yagamirai10#7046
image monika 3y = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/y.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 3z = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/z.png")         #HEAD CREDIT: yagamirai10#7046
image monika 3za = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/za.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 3zb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zb.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 3zc = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zc.png")       #HEAD CREDIT: u/NormallyAverage
image monika 3zd = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/zd.png")       #HEAD CREDIT: yagamirai10#7046
image monika 3ze = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/ze.png")       #HEAD CREDIT: u/NormallyAverage

image monika 4s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/s.png")         #HEAD CREDIT: u/NormallyAverage
image monika 4t = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/t.png")         #HEAD CREDIT: greenbean01#6360
image monika 4u = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/u.png")         #HEAD CREDIT: greenbean01#6360
image monika 4v = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/v.png")         #HEAD CREDIT: u/NormallyAverage
image monika 4w = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/w.png")         #HEAD CREDIT: TsunKrAZy#2862
image monika 4x = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/x.png")         #HEAD CREDIT: yagamirai10#7046
image monika 4y = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/y.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 4z = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/z.png")         #HEAD CREDIT: yagamirai10#7046
image monika 4za = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/za.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 4zb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zb.png")       #HEAD CREDIT: JaxxHunter#3435
image monika 4zc = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zc.png")       #HEAD CREDIT: u/NormallyAverage
image monika 4zd = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/zd.png")       #HEAD CREDIT: yagamirai10#7046
image monika 4ze = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/ze.png")       #HEAD CREDIT: u/NormallyAverage

#BODY CREDIT: u/NormallyAverage##########
image monika 6a = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/a.png")
image monika 6b = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/b.png")
image monika 6c = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/c.png")
image monika 6d = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/d.png")
image monika 6e = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/e.png")
image monika 6f = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/f.png")
image monika 6g = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/g.png")
image monika 6h = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/h.png")
image monika 6i = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/i.png")
image monika 6j = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/j.png")
image monika 6k = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/k.png")
image monika 6l = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/l.png")
image monika 6m = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/m.png")
image monika 6n = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/n.png")
image monika 6o = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/o.png")
image monika 6p = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/p.png")
image monika 6q = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/q.png")
image monika 6r = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/r.png")
image monika 6s = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/s.png")           #HEAD CREDIT: u/NormallyAverage
image monika 6t = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/t.png")           #HEAD CREDIT: greenbean01#6360
image monika 6u = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/u.png")           #HEAD CREDIT: greenbean01#6360
image monika 6v = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/v.png")           #HEAD CREDIT: u/NormallyAverage
image monika 6w = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/w.png")           #HEAD CREDIT: TsunKrAZy#2862
image monika 6x = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/x.png")           #HEAD CREDIT: yagamirai10#7046
image monika 6y = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/y.png")           #HEAD CREDIT: JaxxHunter#3435
image monika 6z = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/z.png")           #HEAD CREDIT: yagamirai10#7046
image monika 6za = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/za.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 6zb = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/zb.png")         #HEAD CREDIT: JaxxHunter#3435
image monika 6zc = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/zc.png")         #HEAD CREDIT: u/NormallyAverage
image monika 6zd = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/zd.png")         #HEAD CREDIT: yagamirai10#7046
image monika 6ze = im.Composite((960, 960), (0, 0), "mod_assets/monika/4l.png", (0, 0), "mod_assets/monika/4r.png", (0, 0), "mod_assets/monika/ze.png")         #HEAD CREDIT: u/NormallyAverage
########################################

image wallace 1ba = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/a.png")
image wallace 1bb = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/b.png")
image wallace 1bc = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/c.png")
image wallace 1bd = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/d.png")
image wallace 1be = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/e.png")
image wallace 1bf = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/f.png")
image wallace 1bg = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/g.png")
image wallace 1bh = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/h.png")
image wallace 1bi = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/i.png")
image wallace 1bj = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/j.png")
image wallace 1bk = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/k.png")
image wallace 1bl = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/l.png")
image wallace 1bm = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/m.png")
image wallace 1bn = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/n.png")
image wallace 1bo = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/o.png")
image wallace 1bp = im.Composite((960, 960), (0, 0), "mod_assets/wallace/1bl.png", (0, 0), "mod_assets/wallace/1br.png", (0, 0), "mod_assets/wallace/p.png")

image wallace 2ba = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/a.png")
image wallace 2bb = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/b.png")
image wallace 2bc = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/c.png")
image wallace 2bd = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/d.png")
image wallace 2be = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/e.png")
image wallace 2bf = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/f.png")
image wallace 2bg = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/g.png")
image wallace 2bh = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/h.png")
image wallace 2bi = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/i.png")
image wallace 2bj = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/j.png")
image wallace 2bk = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/k.png")
image wallace 2bl = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/l.png")
image wallace 2bm = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/m.png")
image wallace 2bn = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/n.png")
image wallace 2bo = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/o.png")
image wallace 2bp = im.Composite((960, 960), (0, 0), "mod_assets/wallace/2bl.png", (0, 0), "mod_assets/wallace/2br.png", (0, 0), "mod_assets/wallace/p.png")

image femc 1k = im.Composite((960, 960), (0, 0), "mod_assets/blonde_femc/1l.png", (0, 0), "mod_assets/blonde_femc/1r.png", (0, 0), "mod_assets/blonde_femc/k.png")

image mainchar 1a = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/a.png")
image mainchar 1b = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/b.png")
image mainchar 1c = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/c.png")
image mainchar 1d = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/d.png")
image mainchar 1e = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/e.png")
image mainchar 1f = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/f.png")
image mainchar 1g = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/g.png")
image mainchar 1h = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/h.png")
image mainchar 1i = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/i.png")
image mainchar 1j = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/j.png")
image mainchar 1k = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/k.png")
image mainchar 1l = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/l.png")
image mainchar 1m = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/m.png")
image mainchar 1n = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/n.png")
image mainchar 1o = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/o.png")
image mainchar 1p = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/p.png")
image mainchar 1q = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/q.png")
image mainchar 1r = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/r.png")
image mainchar 1s = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/s.png")
image mainchar 1t = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/t.png")
image mainchar 1u = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/u.png")
image mainchar 1v = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/v.png")
image mainchar 1w = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/w.png")
image mainchar 1x = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/x.png")
image mainchar 1y = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/y.png")
image mainchar 1z = im.Composite((960, 960), (0, 0), "mod_assets/player/1l.png", (0, 0), "mod_assets/player/1r.png", (0, 0), "mod_assets/player/z.png")