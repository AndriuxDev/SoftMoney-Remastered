## Music
define audio.t0 = "audio/TitleSMB.mp3"
define audio.t1 = "audio/Dune.mp3"
define audio.t2 = "audio/Intro.ogg"
define audio.t3 = "audio/Music Normal.ogg"
define audio.t4 = "audio/Neutral Ending.ogg"
define audio.t5 = "audio/Music Normal.ogg"
define audio.t6 = "audio/ROMVerify.mp3"

## Sound Effects
define audio.button = "audio/SFX_Button.ogg"
define audio.decision = "audio/SFX_Decision.ogg"
define audio.hbeep = "audio/SFX_Hsopital.ogg"
define audio.money = "audio/SFX_Money.ogg"
define audio.notif = "audio/SFX_Notification.ogg"

## Harvey's sprites

default h_name = "Harvey"

define h = DynamicCharacter('h_name', image='harvey', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# Harvey - Set A
image harvey a1 = Composite((654,886), (0,0), "images/a1.png")
image harvey a1h = Composite((654,886), (0,0), "images/a1h.png")
image harvey a1t = Composite((654,886), (0,0), "images/a1t.png")
image harvey a2t = Composite((654,886), (0,0), "images/a2t.png")
image harvey a3 = Composite((654,886), (0,0), "images/a3.png")
image harvey a3h = Composite((654,886), (0,0), "images/a3h.png")
image harvey a3t = Composite((654,886), (0,0), "images/a3t.png")
image harvey a4 = Composite((654,886), (0,0), "images/a4.png")
image harvey a4h = Composite((654,886), (0,0), "images/a4h.png")
image harvey a4t = Composite((654,886), (0,0), "images/a4t.png")

# Harvey - Set B
image harvey b1 = Composite((654,886), (0,0), "images/b1.png")
image harvey b2 = Composite((654,886), (0,0), "images/b2.png")

# Harvey - Set C
image harvey c1 = Composite((654,886), (0,0), "images/c1.png")
image harvey c1h = Composite((654,886), (0,0), "images/c1h.png")
image harvey c1t = Composite((654,886), (0,0), "images/c1t.png")
image harvey c2 = Composite((654,886), (0,0), "images/c2.png")
image harvey c2h = Composite((654,886), (0,0), "images/c2h.png")
image harvey c2t = Composite((654,886), (0,0), "images/c2t.png")

# Harvey - Set D
image harvey d1 = Composite((654,886), (0,0), "images/d1.png")
image harvey d1h = Composite((654,886), (0,0), "images/d1h.png")
image harvey d1t = Composite((654,886), (0,0), "images/d1t.png")
image harvey d2 = Composite((654,886), (0,0), "images/d2.png")
image harvey d2h = Composite((654,886), (0,0), "images/d2h.png")
image harvey d2t = Composite((654,886), (0,0), "images/d2t.png")

# Harvey - Set 2A
image harvey 2a1 = Composite((654,886), (0,0), "images/2a1.png")
image harvey 2a1h = Composite((654,886), (0,0), "images/2a1h.png")
image harvey 2a2 = Composite((654,886), (0,0), "images/2a2.png")
image harvey 2a2h = Composite((654,886), (0,0), "images/2a2h.png")
image harvey 2a3 = Composite((654,886), (0,0), "images/2a3.png")
image harvey 2a3h = Composite((654,886), (0,0), "images/2a3h.png")

# Harvey - Set 3
image harvey 3a1 = Composite((654,886), (0,0), "images/3a1.png")
image harvey 3a1h = Composite((654,886), (0,0), "images/3a1h.png")
image harvey 3c1 = Composite((654,886), (0,0), "images/3c1.png")
image harvey 3c1h = Composite((654,886), (0,0), "images/3c1h.png")
image harvey 3c2 = Composite((654,886), (0,0), "images/3c2.png")
image harvey 3c2h = Composite((654,886), (0,0), "images/3c2h.png")
image harvey 3d1 = Composite((654,886), (0,0), "images/3d1.png")
image harvey 3d1h = Composite((654,886), (0,0), "images/3d1h.png")

## Backgrounds
image bg end1 = "images/end1.png"
image bg end2 = "images/end2.png"
image bg end3 = "images/end3.png"
image bg end4 = "images/end4.png"
image bg end5 = "images/end5.png"
image bg end6 = "images/end6.png"
image bg end7 = "images/end7.png"

image bg intro1 = "images/intro1.png"
image bg intro2 = "images/intro2.png"

image bg mainscreen = "images/menu.png"
image bg thx = "images/thanks.png"

image bg1 = "images/bg 1.png"

## Persistent file

default persistent.playername = ""
default player = persistent.playername
default persistent.first_run = False
default persistent.language = None