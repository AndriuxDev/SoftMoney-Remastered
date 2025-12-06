# -----------------------
# script-ch1.rpy, may need to be divided in separate files for cleaner look
# -----------------------

#=============================================
# CHECK MONEY TAGS FUNCTION
#=============================================

init python:

    def check_events():

        money = renpy.store.money  # shortcut to the money variable
        s = renpy.store  # shortcut to the interaction flags

        if not s.poke1 and money == 50:
            s.poke1 = True
            renpy.call("poke50")

        if not s.unlock_shop_intro and money == 100:
            s.unlock_shop_intro = True
            renpy.call("shop_intro")

        # --- unlockitem1 (hi5) ---
        if s.unlockitem1 and not s.hifive1 and money == 100:
            s.hifive1 = True
            renpy.call("hi5_A")

        if s.unlockitem1 and not s.hifive2 and money == 200:
            s.hifive2 = True
            renpy.call("hi5_B")

        if s.unlockitem1 and not s.hifive3 and money == 300:
            s.hifive3 = True
            renpy.call("hi5_C")

        if s.unlockitem1 and not s.hifive4 and money == 400:
            s.hifive4 = True
            renpy.call("hi5_A")

        if s.unlockitem1 and not s.hifive5 and money == 500:
            s.hifive5 = True
            renpy.call("hi5_D")

        # --- unlockitem2 (handshakes) ---
        if s.unlockitem2 and not s.hand1 and money == 400:
            s.hand1 = True
            renpy.call("handshake_A")

        if s.unlockitem2 and not s.hand2 and money == 800:
            s.hand2 = True
            renpy.call("handshake_B")

        if s.unlockitem2 and not s.hand3 and money == 1200:
            s.hand3 = True
            renpy.call("handshake_C")

        if s.unlockitem2 and not s.hand4 and money == 1600:
            s.hand4 = True
            renpy.call("handshake_D")

        if s.unlockitem2 and not s.hand5 and money == 2000:
            s.hand5 = True
            renpy.call("handshake_E")

        # --- unlockitem3 (pat heads) ---
        if s.unlockitem3 and not s.pathead1 and money == 1000:
            s.pathead1 = True
            renpy.call("headpat_A")

        if s.unlockitem3 and not s.pathead2 and money == 2000:
            s.pathead2 = True
            renpy.call("headpat_B")

        if s.unlockitem3 and not s.pathead3 and money == 3000:
            s.pathead3 = True
            renpy.call("headpat_C")

        if s.unlockitem3 and not s.pathead4 and money == 4000:
            s.pathead4 = True
            renpy.call("headpat_D")

        if s.unlockitem3 and not s.pathead5 and money == 5000:
            s.pathead5 = True
            renpy.call("headpat_E")

        # --- unlockitem4 (massages) ---
        if s.unlockitem4 and not s.masg1 and money == 2000:
            s.masg1 = True
            renpy.call("massage_A")

        if s.unlockitem4 and not s.masg2 and money == 4000:
            s.masg2 = True
            renpy.call("massage_B")

        if s.unlockitem4 and not s.masg3 and money == 6000:
            s.masg3 = True
            renpy.call("massage_C")

        if s.unlockitem4 and not s.masg4 and money == 8000:
            s.masg4 = True
            renpy.call("massage_D")

        if s.unlockitem4 and not s.masg5 and money == 10000:
            s.masg5 = True
            renpy.call("massage_E")

        # --- unlockitem5 (hugs) ---
        if s.unlockitem5 and not s.hug0 and money == 80:
            s.hug0 = True
            renpy.call("hug_intro")

        if s.unlockitem5 and not s.hug1 and money == 4000:
            s.hug1 = True
            renpy.call("hug_A")

        if s.unlockitem5 and not s.hug2 and money == 8000:
            s.hug2 = True
            renpy.call("hug_B")

        if s.unlockitem5 and not s.hug3 and money == 12000:
            s.hug3 = True
            renpy.call("hug_C")

        if s.unlockitem5 and not s.hug4 and money == 16000:
            s.hug4 = True
            renpy.call("hug_D")

        if s.unlockitem5 and not s.hug5 and money == 20000:
            s.hug5 = True
            renpy.call("hug_E")

        # --- ENDINGS ---

        # Ending 2: Hugs unlocked, but NOT the comb
        if s.unlockitem5 and not s.unlockitem6 and money >= 25000:
            s.endflag2 = True
            return renpy.call("preending2")

        # Ending 1: No hugs (item 5), regardless of other items
        elif not s.unlockitem5 and money >= 25000:
            s.endflag1 = True
            return renpy.call("preending1")


# ============================================
# INITIATION
# ============================================

default clicks = 0
default times = 0
default money = 0
default addmoney = 1        
default unlockitem1 = False # Hi-5 item, unlocked at 100 coins, grants 2 coins per click
default unlockitem2 = False # Handshake item, unlocked at 500 coins, grants 10 coins per click
default unlockitem3 = False # Headpat item, unlocked at 2000 coins, grants 20 coins per click
default unlockitem4 = False # Massage item, unlocked at 5000 coins, grants 40 coins per click
default unlockitem5 = False # Hug item, unlocked at 10000 coins, grants 80 coins per click
default unlockitem6 = False # Comb item, unlocked at 20000 coins, unlocks best ending
default can_click_button = False
default unlock_shop_intro = False

# ============================================
# INTERACTION FLAGS
# ============================================
#===========================================================
default poke1 = False
default hifive1 = False     # 1st hi-five interaction, $100
default hifive2 = False     # 2nd hi-five interaction, $200
default hifive3 = False     # 3rd hi-five interaction, $300
default hifive4 = False     # 4th hi-five interaction, $400
default hifive5 = False     # 5th hi-five interaction, $500
#===========================================================
default hand1 = False       # 1st handshake interaction, $400
default hand2 = False       # 1st handshake interaction, $800
default hand3 = False       # 1st handshake interaction, $1200
default hand4 = False       # 1st handshake interaction, $1600
default hand5 = False       # 1st handshake interaction, $2000
#===========================================================
default pathead1 = False    # 1st headpat interaction, $1000
default pathead2 = False    # 1st headpat interaction, $2000
default pathead3 = False    # 1st headpat interaction, $3000
default pathead4 = False    # 1st headpat interaction, $4000
default pathead5 = False    # 1st headpat interaction, $5000
#===========================================================
default masg1 = False       # 1st massage interaction, $2000
default masg2 = False       # 1st massage interaction, $4000
default masg3 = False       # 1st massage interaction, $6000
default masg4 = False       # 1st massage interaction, $8000
default masg5 = False       # 1st massage interaction, $10000
#===========================================================
default hug0 = False        # 0th hug interaction, $80
default hug1 = False        # 1st hug interaction, $4000
default hug2 = False        # 1st hug interaction, $8000
default hug3 = False        # 1st hug interaction, $12000
default hug4 = False        # 1st hug interaction, $16000
default hug5 = False        # 1st hug interaction, $20000
#===========================================================
default endflag1 = False    # Normal ending
default endflag2 = False    # Sad ending
default endflag3 = False    # Best ending

# ============================================
# INTERACTION LABELS (TEMPLATE)
# ============================================
label template:
    hide screen click_harvey
    window show
    show harvey a4 at tipocenter
    h2 "This is a template!"
    player "Yeah, {w=0.5}, I can definitely see that."
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

# ============================================
# MAIN MINIGAME INTRO
# ============================================

label maingame:
    if not config.developer:
        $ h2.name = "???"
        $ harvey_name = "???"
    else:
        $ h2.name = "Harvey"
        $ harvey_name = "Harvey"

    scene bg bg1
    show harvey a3 at tipocenter
    play music t3

    if config.developer == True:
        window show
        "This is a developer build. Bypassing introduction..."

    else:
        window show
        "As you got into the stall, the man was already waiting for you."
        show harvey a1t at tipocenter
        h2 "Hey there! You must be [player], right?"
        show harvey a1 at tipocenter
        "The man spoke in a friendly tone, trying to ease your nervousness."
        show harvey a3t at tipocenter
        h2 "I\'m Harvey. Thanks for meeting me here."
        show harvey a1 at tipocenter
        player "Harvey?{w=1} That\'s...{w=1} a unique name."
        $ h2.name = "Harvey"
        $ harvey_name = "Harvey"
        show harvey a3t at tipocenter
        h2 "Haha, yeah. I get that a lot."
        show harvey a3 at tipocenter
        "He chuckled softly, his eyes twinkling with amusement."
        player "About your stall..."
        show harvey a2t at tipocenter
        h2 "Oh, right!{w=1} You must be wondering why I\'m here."
        show harvey a1t at tipocenter
        h2 "Every time you click on me, I\'ll give you one dollar."
        show harvey a3t at tipocenter
        h2 "Not a bad deal, right?"
        show harvey a1 at tipocenter
        player "I guess it\'s better than nothing."
        show harvey a1t at tipocenter
        h2 "Here\'s a small tip before you start: I always say clicks are like little spells."
        show harvey a2t at tipocenter
        h2 "The more you believe in them, the more they can give you."
        show harvey a1 at tipocenter
        player "Spells, huh? Interesting way to put it."
        show harvey a3t at tipocenter
        h2 "Trust me, it works!"
        h2 "Just click and see what happens!"
    show harvey a1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

# ------------------------------------------------------------
# SHOP INTRO AND ITEMS
# ------------------------------------------------------------
label shop_intro:
    hide screen click_harvey
    window show
    show harvey a1t at tipocenter
    h2 "Oh, hey!{w=0.5} Look!{w=0.5} See that shop button up top?"
    show harvey a1 at tipocenter
    player "Yeah,{w=0.5} I see it."
    show harvey a1t at tipocenter
    h2 "When it starts glowing yellow,{w=0.5} that means there\'s a cool new item to buy!"
    show harvey a3t at tipocenter
    h2 "Go check it out, buddy!"
    show harvey a3 at tipocenter
    show screen click_harvey
    window hide
    $ ui.interact()
    return

label hi5_intro:
    hide screen click_harvey
    window show
    show harvey a1t at tipocenter
    h2 "A high five?"
    show harvey a1 at tipocenter
    player "Yeah,{w=0.5} I thought it might be fun."
    show harvey a1t at tipocenter
    h2 "Of course,{w=0.5} why not!"
    show harvey a1 at tipocenter
    show screen click_harvey
    window hide
    $ ui.interact()
    return

label handshake_intro:
    hide screen click_harvey
    window show
    show harvey a4 at tipocenter
    h2 "What could be better than a good handshake!"
    player "Exactly! It\'s a classic."
    show harvey a2t at tipocenter
    h2 "Alright then, let\'s shake on it!"
    show harvey a3 at tipocenter
    show screen click_harvey
    window hide
    $ ui.interact()
    return

label headpat_intro:
    show overlay1 with dissolve
    hide screen click_harvey
    window show
    show harvey a4 at tipocenter
    h2 "A pat on the head?"
    player "Yeah, sometimes you just need a little comfort."
    show harvey a2t at tipocenter
    h2 "Well, maybe..."
    h2 "Just be careful with my hair!"
    h2 "Don\'t want to mess it up, you know?"
    show harvey a3 at tipocenter
    show screen click_harvey
    window hide
    $ ui.interact()
    return

label massage_intro:
    hide screen click_harvey
    window show
    show harvey a4 at tipocenter
    h2 "What?"
    h2 "You want to give me a massage?"
    player "Yeah,{w=1} it looked relaxing."
    show harvey a2t at tipocenter
    h2 "Well,{w=1} alright then."
    h2 "Just don\'t go too hard!"
    show harvey a3 at tipocenter
    show screen click_harvey
    window hide
    $ ui.interact()
    return

label hug_preintro:
    hide overlay1 with dissolve
    show overlay2 with dissolve
    hide screen click_harvey
    window show
    show harvey a4 at tipocenter
    h2 "So,{w=1} how are you going to surprise me this time?"
    show harvey a2t at tipocenter
    show screen click_harvey
    window hide
    $ ui.interact()
    return

label hug_intro:
    hide screen click_harvey
    window show
    stop music
    show harvey b1 at tipocenter
    h2 ".{w=1}.{w=1}."
    show harvey c1t at tipocenter
    h2 "You decided to..."
    show harvey c1 at tipocenter
    player "What?{w=1} Is something wrong?"
    show harvey b2 at tipocenter
    h2 "No,{w=1} it\'s just..."
    show harvey c1t at tipocenter
    h2 "That was unexpected..."
    show harvey c1 at tipocenter
    player "I could stop if you want."
    show harvey c2t at tipocenter
    h2 "No,{w=1} it\'s okay."
    h2 "Don\'t think about it,{w=1} just keep going."
    show harvey c1 at tipocenter
    show screen click_harvey
    play music t1
    window hide
    $ ui.interact()
    return

# ------------------------------------------------------------
# Interactions per item
# ------------------------------------------------------------

# No item
label poke50:
    hide screen click_harvey
    window show
    show harvey a1t at tipocenter
    h2 "C\'mon! You can do it!"
    show harvey a3t at tipocenter
    h2 "Every click is a step closer to greatness!"
    show harvey a3 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

# High Five
label hi5_A:
    hide screen click_harvey
    window show
    show harvey a1t at tipocenter
    h2 "Keep going!{w=0.5} You\'re on a roll!"
    show harvey a1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label hi5_B:
    hide screen click_harvey
    window show
    show harvey a1t at tipocenter
    h2 "You\'re making my day with all these clicks!"
    show harvey a1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label hi5_C:
    hide screen click_harvey
    window show
    show harvey a1t at tipocenter
    h2 "You\'ve got the power in your fingertips!"
    show harvey a1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label hi5_D:
    hide screen click_harvey
    window show
    show harvey d2t at tipocenter
    h2 "I think my palm\'s starting to hurt..."
    show harvey a1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

# Handshake
label handshake_A:
    hide screen click_harvey
    window show
    show harvey a4t at tipocenter
    h2 "We should've done this back when we first met, right?"
    show harvey a4 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label handshake_B:
    hide screen click_harvey
    window show
    show harvey a3t at tipocenter
    h2 "You've got quite a strong grip!"
    show harvey a3 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label handshake_C:
    hide screen click_harvey
    window show
    show harvey a2t at tipocenter
    h2 "Handshakes really bring people closer, don't you think?"
    show harvey a1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label handshake_D:
    hide screen click_harvey
    window show
    show harvey a4t at tipocenter
    h2 "Can I..."
    h2 "Can I call you my friend after this?"
    show harvey a4 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label handshake_E:
    hide screen click_harvey
    window show
    show harvey a3t at tipocenter
    h2 "I suppose I can!"
    show harvey a3 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

# Headpat

label headpat_A:
    hide screen click_harvey
    window show
    show harvey a4t at tipocenter
    h2 "This is rather... unusual..."
    show harvey a4 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label headpat_B:
    hide screen click_harvey
    window show
    show harvey a4 at tipocenter
    h2 "You know, it actually feels kind of nice."
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label headpat_C:
    hide screen click_harvey
    window show
    show harvey a2t at tipocenter
    h2 "I hope my hair doesn't look too messy?"
    show harvey a1t at tipocenter
    h2 "My favorite comb broke, so I spent the whole morning fixing it."
    show harvey a1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label headpat_D:
    hide screen click_harvey
    window show
    show harvey a4t at tipocenter
    h2 "I feel like a pet getting petted for being good."
    h2 "That's weird..."
    show harvey a4 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label headpat_E:
    hide screen click_harvey
    window show
    show harvey d2t at tipocenter
    h2 "Let's just forget I said anything about being a pet."
    show harvey d1t at tipocenter
    h2 "Okay?"
    show harvey d1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

# Massage

label massage_A:
    hide screen click_harvey
    window show
    show harvey d2t at tipocenter
    h2 "Thank God my wife isn't seeing this."
    h2 "I'm sure we look incredibly weird from the outside."
    show harvey a1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label massage_B:
    hide screen click_harvey
    window show
    show harvey a4t at tipocenter
    h2 "Maybe we should go back to head pats?"
    show harvey a3t at tipocenter
    h2 "Actually, never mind — keep going."
    show harvey a3 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label massage_C:
    hide screen click_harvey
    window show
    show harvey a1t at tipocenter
    h2 "I usually stand behind this stall all day without a break."
    show harvey a3t at tipocenter
    h2 "I think I really deserved a bit of relaxation!"
    show harvey a3 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label massage_D:
    hide screen click_harvey
    window show
    show harvey a2t at tipocenter
    h2 "Oh, I think my shoulder pain is gone!"
    show harvey a3t at tipocenter
    h2 "Thank you so much!"
    show harvey a3 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label massage_E:
    hide screen click_harvey
    window show
    show harvey a1t at tipocenter
    h2 "You know, you're surprisingly good at this."
    h2 "You wouldn't happen to be a masseur, would you?"
    show harvey a1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

# Hug

label hug_A:
    hide screen click_harvey
    window show
    show harvey c1t at tipocenter
    h2 "I don't get hugs from people very often..."
    show harvey c1 at tipocenter
    player "Really?"
    show harvey c1t at tipocenter
    h2 "Yeah..."
    show harvey c2 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label hug_B:
    hide screen click_harvey
    window show
    show harvey c2t at tipocenter
    h2 "I usually get treated..."
    h2 "...a lot rougher..."
    show harvey c2 at tipocenter
    player "How so?"
    show harvey c1t at tipocenter
    h2 "It's hard to say, honestly..."
    show harvey c1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label hug_C:
    hide screen click_harvey
    window show
    show harvey c1t at tipocenter
    h2 "Sometimes so rough that you can't help but wonder..."
    show harvey c2t at tipocenter
    h2 "As if I'm not a real person..."
    h2 "But just someone's toy..."
    show harvey c2 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label hug_D:
    hide screen click_harvey
    window show
    show harvey d1 at tipocenter
    h2 "..."
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

label hug_E:
    hide screen click_harvey
    window show
    show harvey d2t at tipocenter
    h2 "It's already getting dark — my family's probably waiting for me."
    show harvey d1t at tipocenter
    h2 "Finish up what you're doing and I'll head home."
    show harvey d1 at tipocenter
    show screen click_harvey
    show screen maingame_screen with dissolve
    window hide
    $ ui.interact()
    return

# ------------------------------------------------------------
# ENDINGS
# ------------------------------------------------------------

# Normal ending
label preending1:
    hide screen click_harvey with dissolve
    hide screen maingame_screen with dissolve
    window show
    show harvey a1t at tipocenter
    h2 "Hey, looks like you got the money you need for the surgery!"
    show harvey a1 at tipocenter
    player "Hey, don\'t sweat it. It was your stall here what helped me get the money I need."
    player "[harvey_name], right?"
    show harvey a1t at tipocenter
    h2 "Yes?"
    show harvey a1 at tipocenter
    player "Thank you!"
    h2 "I suppose my job here is done."
    show harvey a3t at tipocenter
    h2 "Another satisfied customer, of course!"
    show harvey a3 at tipocenter
    window hide
    jump ending1
    return

# Sad ending
label preending2:
    hide screen click_harvey with dissolve
    hide screen maingame_screen with dissolve
    window show
    show harvey d1t at tipocenter
    h2 "So... you got the money for the surgery. I\'m glad."
    show harvey d1 at tipocenter
    player "Yeah. I couldn\'t have done it without your stall. It really helped me get what I needed."
    player "[harvey_name], right?"
    show harvey d1t at tipocenter
    h2 "...Yes?"
    show harvey d1 at tipocenter
    player "Thank you. Really."
    h2 "I see. Then... I guess this is where my part ends."
    show harvey d1t at tipocenter
    h2 "Another customer helped... another person moving on..."
    show harvey d2t at tipocenter
    h2 "And in the end... just another customer."
    window hide
    stop music fadeout 1.0
    pause 1.0
    jump ending2
    return

# Best ending
label preending3:
    $ hiddencomb.grant()
    hide screen click_harvey with dissolve
    hide screen maingame_screen with dissolve
    show harvey b1 at tipocenter
    h2 ".{w=1}.{w=1}."
    show harvey b2 at tipocenter
    h2 "I-Is this..."
    h2 "...a gift... for me?"
    show harvey b1 at tipocenter
    player "Yeah. It\'s for you."
    show harvey b2 at tipocenter
    h2 "A new comb...?"
    show harvey c2t at tipocenter
    h2 "But... this was everything you saved for the surgery..."
    show harvey d1t at tipocenter
    h2 "Thank you. I—I don\'t even know what to say."
    show harvey d2t at tipocenter
    h2 "No one\'s ever done something like this for me before."
    h2 "I should head home now, but..."
    show harvey d1t at tipocenter
    h2 "...I can\'t just let things end here."
    show harvey d2t at tipocenter
    h2 "Maybe tomorrow we can meet again and—{p=2.0}{nw}"
    show harvey b2 at tipocenter
    h2 "Wait! Where are you going?!"
    show harvey b1 at tipocenter
    window hide
    pause 1.0
    jump ending3
    return

# ------------------------------------------------------------
# SHOP AND MAIN GAME SCREENS
# ------------------------------------------------------------

screen click_harvey():
    tag harvey

    imagebutton:
        idle hbutton_idle
        hover hbutton_hover
        xalign 0.5
        yalign 0.2
        action [
            SetVariable("money", money + addmoney),
            SetVariable("clicks", clicks + 1),
            Play("sound", audio.money),
            Function(check_events)
        ]

screen maingame_screen():
    tag maingame
    zorder 15

    hbox:
        xpos 0
        ypos 0
        add clks

    hbox:
        xpos 0.79
        ypos 0.155
        spacing 0
        text "{font=ArchiveUkr-Regular.ttf}[clicks]{/font}" size 75 color "#fff"

    hbox:
        xpos 0
        ypos 0
        add coin
    
    hbox:
        xpos 0.79
        ypos 0.025
        spacing 0
        text "{font=ArchiveUkr-Regular.ttf}[money]{/font}" size 75 color "#fff"

    # OPEN SHOP BUTTON
    if money >= 100 and not unlockitem1:
        imagebutton:
            idle shop2_idle
            hover shop2_hover
            xpos 0.0
            ypos 0.0
            action [Show("shop_home"), Show("shop_items"), With(Dissolve(0.5))]
            activate_sound gui.activate_sound
    elif money >= 500 and not unlockitem2:
        imagebutton:
            idle shop2_idle
            hover shop2_hover
            xpos 0.0
            ypos 0.0
            action [Show("shop_home"), Show("shop_items"), With(Dissolve(0.5))]
            activate_sound gui.activate_sound
    elif money >= 2000 and not unlockitem3:
        imagebutton:
            idle shop2_idle
            hover shop2_hover
            xpos 0.0
            ypos 0.0
            action [Show("shop_home"), Show("shop_items"), With(Dissolve(0.5))]
            activate_sound gui.activate_sound
    elif money >= 5000 and not unlockitem4:
        imagebutton:
            idle shop2_idle
            hover shop2_hover
            xpos 0.0
            ypos 0.0
            action [Show("shop_home"), Show("shop_items"), With(Dissolve(0.5))]
            activate_sound gui.activate_sound
    elif money >= 10000 and not unlockitem5:
        imagebutton:
            idle shop2_idle
            hover shop2_hover
            xpos 0.0
            ypos 0.0
            action [Show("shop_home"), Show("shop_items"), With(Dissolve(0.5))]
            activate_sound gui.activate_sound
    elif money >= 20000 and not unlockitem6:
        imagebutton:
            idle shop2_idle
            hover shop2_hover
            xpos 0.0
            ypos 0.0
            action [Show("shop_home"), Show("shop_items"), With(Dissolve(0.5))]
            activate_sound gui.activate_sound
    else:
        imagebutton:
            idle shop1_idle
            hover shop1_hover
            xpos 0.0
            ypos 0.0
            action [Show("shop_home"), Show("shop_items"), With(Dissolve(0.5))]
            activate_sound gui.activate_sound

screen shop_home():
    modal True
    zorder 20
    add Solid("#00000080")  # 50% black overlay
    add shopmenu xpos 0.5 ypos 0.5 anchor (0.5, 0.5)

screen shop_items():
    modal True
    zorder 20
    add shopmenu xpos 0.5 ypos 0.5 anchor (0.5, 0.5)

    # CLOSE SHOP BUTTON
    imagebutton:
        idle shop3_idle
        hover shop3_hover
        xpos 0.0
        ypos 0.0
        action [Hide("shop_items") , Hide("shop_home"), With(Dissolve(0.5))]
        activate_sound gui.activate_sound

    # --- ITEM BUTTONS GRID ---
    vbox:
        xpos 0.5
        ypos 0.75
        xanchor 0.5
        yanchor 0.5
        spacing 25

        # ROW 1 (Hi-5, Handshake, Headpat)
        hbox:
            spacing 40

            # HI-5
            if not unlockitem1:
                imagebutton:
                    if (money >= 100):
                        idle item1_idle
                        hover item1_hover
                        action [SetScreenVariable("can_click_button", True),
                                SetVariable("money", money - 100),
                                SetVariable("unlockitem1", True),
                                SetVariable("addmoney", 2),
                                Play("sound", audio.notify),
                                Hide("shop_items"), Hide("shop_home"), With(Dissolve(0.5)),
                                #Notify("You unlocked the Hi-5! You now earn 2 coins per click!"),
                                Call("hi5_intro")
                                ]                                
                    elif (money >= 100 and unlockitem1 == True):
                        idle item1_insensitive
                        hover item1_insensitive
                        action SetScreenVariable("can_click_button", False)
                    else:
                        idle item1_insensitive
                        hover item1_insensitive
                        action SetScreenVariable("can_click_button", False)
                    insensitive item1_insensitive

            # HANDSHAKE
            if not unlockitem2:
                imagebutton:
                    if (money >= 500):
                        idle item2_idle
                        hover item2_hover
                        action [SetScreenVariable("can_click_button", True),
                                SetVariable("money", money - 500),
                                SetVariable("unlockitem2", True),
                                SetVariable("addmoney", 10),
                                Play("sound", audio.notify),
                                Hide("shop_items"), Hide("shop_home"), With(Dissolve(0.5)),
                                #Notify("You unlocked the Handshake! You now earn 10 coins per click!"),
                                Call("handshake_intro")
                                ]
                    elif (money >= 500 and unlockitem2 == True):
                        idle item2_insensitive
                        hover item2_insensitive
                        action SetScreenVariable("can_click_button", False)
                    else:
                        idle item2_insensitive
                        hover item2_insensitive
                        action SetScreenVariable("can_click_button", False)
                    insensitive item2_insensitive

            # HEADPAT
            if not unlockitem3:
                imagebutton:
                    if (money >= 2000):
                        idle item3_idle
                        hover item3_hover
                        action [SetScreenVariable("can_click_button", True),
                                SetVariable("money", money - 2000),
                                SetVariable("unlockitem3", True),
                                SetVariable("addmoney", 20),
                                Play("sound", audio.notify),
                                Hide("shop_items"), Hide("shop_home"), With(Dissolve(0.5)),
                                #Notify("You unlocked the Headpat! You now earn 20 coins per click!"),
                                Call("headpat_intro")
                                ]
                    elif (money >= 2000 and unlockitem3 == True):
                        idle item3_insensitive
                        hover item3_insensitive
                        action SetScreenVariable("can_click_button", False)
                    else:
                        idle item3_insensitive
                        hover item3_insensitive
                        action SetScreenVariable("can_click_button", False)
                    insensitive item3_insensitive

            # MASSAGE
            if not unlockitem4:
                imagebutton:
                    if (money >= 5000):
                        idle item4_idle
                        hover item4_hover
                        action [SetScreenVariable("can_click_button", True),
                                SetVariable("money", money - 5000),
                                SetVariable("unlockitem4", True),
                                SetVariable("addmoney", 40),
                                Play("sound", audio.notify),
                                Hide("shop_items"), Hide("shop_home"), With(Dissolve(0.5)),
                                #Notify("You unlocked the Massage! You now earn 40 coins per click!"),
                                Call("massage_intro")
                                ]
                    elif (money >= 5000 and unlockitem4 == True):
                        idle item4_insensitive
                        hover item4_insensitive
                        action SetScreenVariable("can_click_button", False)
                    else:
                        idle item4_insensitive
                        hover item4_insensitive
                        action SetScreenVariable("can_click_button", False)
                    insensitive item4_insensitive

            # HUG
            if not unlockitem5:
                imagebutton:
                    if (money >= 10000):
                        idle item5_idle
                        hover item5_hover
                        action [SetScreenVariable("can_click_button", True),
                                SetVariable("money", money - 10000),
                                SetVariable("unlockitem5", True),
                                SetVariable("addmoney", 80),
                                Play("sound", audio.notify),
                                Hide("shop_items"), Hide("shop_home"), With(Dissolve(0.5)),
                                #Notify("You unlocked the Hug! You now earn 80 coins per click!"),
                                Call("hug_preintro")
                                ]
                    elif (money >= 10000 and unlockitem5 == True):
                        idle item5_insensitive
                        hover item5_insensitive
                        action SetScreenVariable("can_click_button", False)
                    else:
                        idle item5_insensitive
                        hover item5_insensitive
                        action SetScreenVariable("can_click_button", False)
                    insensitive item5_insensitive

            # COMB
            if not unlockitem6:
                imagebutton:
                    if (money >= 20000):
                        idle item6_idle
                        hover item6_hover
                        action [SetScreenVariable("can_click_button", True),
                                SetVariable("money", money - 20000),
                                SetVariable("unlockitem6", True),
                                SetVariable("addmoney", 0),
                                Play("sound", audio.notify),
                                Hide("shop_items"), Hide("shop_home"), With(Dissolve(0.5)),
                                #Notify("You unlocked the Comb! You got the best ending!"),
                                Call("preending3")
                                ]
                    elif (money >= 20000 and unlockitem6 == True):
                        idle item6_insensitive
                        hover item6_insensitive
                        action SetScreenVariable("can_click_button", False)
                    else:
                        idle item6_insensitive
                        hover item6_insensitive
                        action SetScreenVariable("can_click_button", False)
                    insensitive item6_insensitive