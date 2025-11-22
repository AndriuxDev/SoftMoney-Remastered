## Music
define audio.t0a = "audio/MainMenu.mp3"
define audio.t0b = "audio/TitleSMB.mp3"
define audio.t1 = "audio/Dune.mp3"
define audio.t2 = "audio/Intro.ogg"
define audio.t3 = "audio/Music Normal.ogg"
define audio.t4 = "audio/Neutral Ending.ogg"
define audio.t5 = "audio/LangSelect.mp3"
define audio.t6 = "audio/ROMVerify.mp3"

## Sound Effects
define audio.button = "audio/SFX_Button.ogg"
define audio.decision = "audio/SFX_Decision.ogg"
define audio.hbeep = "audio/SFX_Hospital.ogg"
define audio.money = "audio/SFX_Money.ogg"
define audio.notify = "audio/SFX_Notification.ogg"
define audio.birbs = "audio/birds.ogg"
define audio.doorbell = "audio/bell.ogg"
define audio.error = "audio/SFX_Error.mp3"

## Backgrounds
image bg end1 = "images/end1.png"
image bg end2 = "images/end2.png"
#image bg end3 = "images/end3.png"
image bg end4 = "images/end4.png"
image bg end5 = "images/end5.png"
#image bg end6 = "images/end6.png"
image bg end7 = "images/end7.png"

image bg intro1 = "images/intro1.png"
image bg intro2 = "images/intro2.png"

image bg mainscreen = "images/menu.png"
image bg thx = "images/thanks.png"

image bg bg1 = "images/bg 1.png"

# Shop UI Images
define hbutton_idle = "images/harvbutt.png"
define hbutton_hover = "images/harvbutth.png"

define coin = "images/money.png"
define clks = "images/clicks.png"
image overlay1 = "images/over1.png" # Sunset overlay
image overlay2 = "images/over2.png" # Night overlay
define shopmenu = "images/shop.png" # Shop main menu

# Shop Category Buttons
define shop1_idle = "images/s1.png" # Home button
define shop1_hover = "images/s1h.png" # Home button hover

define shop2_idle = "images/s2.png" # Available Items button
define shop2_hover = "images/s2h.png" # Available Items button hover

define shop3_idle = "images/s3.png" # Close button
define shop3_hover = "images/s3h.png" # Close button hover

# Shop Items
define item1_idle = "shopbuttons/hi5.png" # High five button
define item1_hover = "shopbuttons/hi5-hover.png" # High five button hover
define item1_insensitive = "shopbuttons/hi5-insensitive.png" # High five button insensitive

define item2_idle = "shopbuttons/handshake.png" # Handshake button
define item2_hover = "shopbuttons/handshake-hover.png" # Handshake button hover
define item2_insensitive = "shopbuttons/handshake-insensitive.png" # Handshake button insensitive

define item3_idle = "shopbuttons/headpat.png" # Headpat button
define item3_hover = "shopbuttons/headpat-hover.png" # Headpat button hover
define item3_insensitive = "shopbuttons/headpat-insensitive.png" # Headpat button insensitive

define item4_idle = "shopbuttons/massage.png" # Massage button
define item4_hover = "shopbuttons/massage-hover.png" # Massage button hover
define item4_insensitive = "shopbuttons/massage-insensitive.png" # Massage button insensitive

define item5_idle = "shopbuttons/hug.png" # Hug button
define item5_hover = "shopbuttons/hug-hover.png" # Hug button hover
define item5_insensitive = "shopbuttons/hug-insensitive.png" # Hug button insensitive

define item6_idle = "shopbuttons/comb.png" # Comb button
define item6_hover = "shopbuttons/comb-hover.png" # Comb button hover
define item6_insensitive = "shopbuttons/comb-insensitive.png" # Comb button insensitive

# ----------------------------------------------------
# Character Definitions
# ----------------------------------------------------

# ---------- Names ----------
default harvey_name = "???"

# ---------- Characters ----------
define h = DynamicCharacter(
    "[harvey_name]",
    image="harvey",
    what_prefix='"',
    what_suffix='"',
    ctc="ctc",
    ctc_position="fixed"
)

define h2 = Character("Harvey")

# ----------------------------------------------------
# Harvey Sprite Definitions
# ----------------------------------------------------
# Organized by sets, grouped cleanly
# All images use the tag "harvey" so attributes work with:  h a1t "..."
# ----------------------------------------------------

# --- Set A ---
image harvey a1 = "images/a1.png"       # Normal
image harvey a1t = "images/a1t.png"     # Normal, talk
image harvey a2t = "images/a2t.png"     # Looking right, talk
image harvey a3 = "images/a3.png"       # Closed happy eyes
image harvey a3t = "images/a3t.png"     # Closed happy eyes, talk
image harvey a4 = "images/a4.png"       # Looking left
image harvey a4t = "images/a4t.png"     # Looking left, talk

# --- Set B ---
image harvey b1 = "images/b1.png"       # Shocked
image harvey b2 = "images/b2.png"       # Shocked, talk

# --- Set C ---
image harvey c1 = "images/c1.png"       # Sad
image harvey c1t = "images/c1t.png"     # Sad, talk
image harvey c2 = "images/c2.png"       # Looking left sad
image harvey c2t = "images/c2t.png"     # Looking left sad, talk

# --- Set D ---
image harvey d1 = "images/d1.png"       # Melancholic
image harvey d1t = "images/d1t.png"     # Melancholic, talk
image harvey d2 = "images/d2.png"       # Looking left melancholic
image harvey d2t = "images/d2t.png"     # Looking left melancholic

# --- Set 2A, sunset overlay ---
image harvey 2a1 = "images/2a1.png"
image harvey 2a2 = "images/2a2.png"
image harvey 2a3 = "images/2a3.png"
image harvey 2a3h = "images/2a3h.png"

# --- Set 3, night overlay ---
image harvey 3a1 = "images/3a1.png"
image harvey 3c1 = "images/3c1.png"
image harvey 3c2 = "images/3c2.png"
image harvey 3d1 = "images/3d1.png"
image harvey 3d1h = "images/3d1h.png"


## Persistent file
default persistent.playername = ""
default player = persistent.playername
default persistent.first_run = False
default persistent.language = None
image ctc = "gui/ctc.png"  # Make sure the file exists
