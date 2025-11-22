# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Doctor")

# The game starts here.

label start:

    if config.developer == True:
        scene black with dissolve
        stop music fadeout 1.0
        pause 1.0
        "This is a developer build. Bypassing pre-introduction..."
        "TESTING OTHER MENUS..."
        menu:
            "What menu/scene to test?"

            "Ending 1":
                jump ending1
            "Ending 2":
                jump ending2
            "Ending 3":
                jump ending3
            "Main Game":
                jump maingame
            "None":
                return
    else:
        scene black with dissolve
        stop music fadeout 1.0
        pause 1.0

        play music hbeep

        pause 3.0

        "The hospital felt heavier than usual—air thick with worry, every hallway echoing with muted fear."
        "Some patients were climbing their way back to life,{w=0.5} others were quietly slipping toward their final moments."
        "And you?{w=0.5} You were trapped in a nightmare—one that demanded a price you could never hope to afford."

        play music t2

        scene bg intro1

        d "Your condition is critical, [player].{w=1.5} Without surgery… you won’t make it. The procedure will cost $25,000."

        "Your stomach drops.{w=0.5} The words hit harder than any diagnosis ever could.{w=0.5} Twenty-five thousand… how could anyone raise that in time?"
        "Every tick of the clock feels like another thread snapping beneath you—another breath stolen."
        "And death?{w=0.25} {cps=10}DEATH WAS THE LAST THING{/cps} you were willing to accept."

        scene bg intro2 with dissolve

        "You try to outrun the dread clawing at your chest,{w=0.5} so you go for a drive—anything to clear your mind."
        "But along the road, something unusual catches your eye: a small, curious stall… and a man who smiles as though he’s been expecting you."
        "Against your better judgment,{w=0.5} you pull over."

        scene black
        stop music fadeout 5.0
        pause 2.0

    pause 2.0

    return

