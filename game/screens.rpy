################################################################################
## Initialization
################################################################################

default debug_tab = "general"

init offset = -1

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -501 screen name_input(message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]
    
    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30
        label _(message):
            style "confirm_prompt"
            xalign 0.5
        input default "" value VariableInputValue("player") length 20 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" textalign 0.5
        
        hbox:
            xalign 0.5
            spacing 100
            textbutton _("Start Game") action ok_action hover_sound gui.hover_sound activate_sound gui.activate_sound
            textbutton _("Cancel") action Hide("name_input") hover_sound gui.hover_sound activate_sound gui.activate_sound

init python:
    def reset_data():
        ## deletes all persistent data use with caution
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswith("_"):
                setattr(persistent, attr, None)

        # Set the window title manually
        setattr(config, "window_title", "SoftMoney Remastered")

        ## deletes all save games use with caution!
        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)

        ## a Ren'Py relaunch is nessesary
        renpy.quit(relaunch=True)

init python:
    # English display names for your languages
    LANGUAGE_LABELS = {
        "english": "English",
        "spanish": "Spanish",
        "french": "French",
        "japanese": "Japanese",
        "russian": "Russian",
        "korean": "Korean"
        # Add all languages you support
    }

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on
    ## the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action:
                activate_sound gui.activate_sound
                hover_sound gui.hover_sound


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-
## game menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            #textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("Auto") action Preference("auto-forward", "toggle")
            #textbutton _("Save") action ShowMenu('save')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")

screen ok_screen(message):
    modal True
    zorder 100

    # Dark transparent overlay behind the frame
    add Solid("#00000080")  # 50% black overlay

    frame:
        align (0.5, 0.5)
        padding (40, 30)
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
        xmaximum 600
        yminimum 200

        vbox:
            spacing 20
            xalign 0.5

            text message:
                xalign 0.5
                size 28
                text_align 0.5

            textbutton _("OK"):
                xalign 0.5
                # Plays a hover sound and a click sound, then hides the screen
                action Hide("ok_screen")
                activate_sound gui.activate_sound
                hover_sound gui.hover_sound
                text_align 0.5

screen error_screen(message):
    modal True
    zorder 100

    # Play the sound when the screen shows
    on "show" action Play("sound", "audio/SFX_Error.mp3")

    # Dark transparent overlay behind the frame
    add Solid("#00000080")  # 50% black overlay

    frame:
        align (0.5, 0.5)
        padding (40, 30)
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
        xmaximum 600
        yminimum 200

        vbox:
            spacing 20
            xalign 0.5

            text message:
                xalign 0.5
                size 28
                text_align 0.5

            textbutton _("OK"):
                xalign 0.5
                action Hide("error_screen")
                activate_sound gui.activate_sound
                hover_sound gui.hover_sound
                text_align 0.5




################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

init -1 python:
    def FinishEnterName():
        if not player:
            return

        persistent.playername = player

        renpy.save_persistent()
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos

        yalign 0.65

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start"):
                action If(persistent.playername, true=[Start('start')], false=Show(screen="name_input", message="What's your name?", ok_action=Function(FinishEnterName)))
                activate_sound gui.start_game_sound

        else:

            textbutton _("History") action ShowMenu("history")

            #textbutton _("Save") action ShowMenu("save")

        #textbutton _("Load") action ShowMenu("load")

        textbutton _("Achievements") action ShowMenu("achievement_gallery")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("Language") action ShowMenu("menu_lang")

        if main_menu:
            textbutton _("More Games") action ShowMenu("moregames")

        textbutton _("About") action ShowMenu("about")

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")
        
        if config.developer and not main_menu:
            textbutton "Debug Menu" action ShowMenu("debug_menu")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm="not main_menu")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"
        add gui.char_menu
        add gui.main_menu_logo zoom 0.7 xalign 0.0 yalign 0.0

    ## Auto-set language from persistent.language when main menu opens.
    ## Uses the Language action (same as the Language buttons elsewhere).
    if persistent.language:
        # Small delay so the action runs after the screen is shown.
        timer 0.01 action Language(persistent.language)
    else:
        timer 0.01 action Language(renpy.get_language())

    imagebutton:
        idle "gui/cat.png"
        hover "gui/catH.png"
        xalign 0.03
        yalign 0.97
        action OpenURL("https://github.com/AndriuxDev/SoftMoney-Remastered")
        hover_sound gui.hover_sound
        activate_sound gui.activate_sound

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"
            
            if "1." not in config.version:
                text "DEV BUILD":
                    style "outline_text"
                    size 50
                    xalign 1.0  # align the whole vbox to the right
                    xmaximum 800  # optional: max width for alignment

            #text "[config.name!t]":
            #     style "main_menu_title"

            text "Version [config.version]":
                style "outline_text"
                size 30
                xalign 1.0  # align the whole vbox to the right
                xmaximum 800  # optional: max width for alignment


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style outline_text:
    color "#FFFFFF"
    outlines [(3, "#000000", 0, 0)]


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("preferences")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            if "1." not in config.version:
                text _("Version [config.version!t] - DEV BUILD\n") color "#999999"
            else:
                text _("Version [config.version!t]\n") color "#999999"

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n" color "#999999"
            
            text _("Inspiration by ShroomyChrist's \"BloodyMoney\". Flags made by {a=https://uiflags.app/}UI Flags{/a}. Fanmade Klingon and High Valyrian flags made by AndriuxDev.") color "#999999"
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") color "#999999"


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of
            ## the buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better
## suit themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if not renpy.variant("mobile"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window"):
                            action Preference("display", "window")
                            activate_sound gui.radio_sound
                            hover_sound gui.hover_sound
                        textbutton _("Fullscreen"):
                            action Preference("display", "fullscreen")
                            activate_sound gui.radio_sound
                            hover_sound gui.hover_sound

                    
                    if preferences.fullscreen == False:

                        vbox:
                            style_prefix "radio"
                            label _("Window Size")
                            textbutton _("1920×1080"):
                                action Preference("display", (1.0))
                                activate_sound gui.radio_sound
                                hover_sound gui.hover_sound

                            textbutton _("1440×810"):
                                action Preference("display", 0.75)
                                activate_sound gui.radio_sound
                                hover_sound gui.hover_sound

                            textbutton _("960×540"):
                                action Preference("display", 0.5)
                                activate_sound gui.radio_sound
                                hover_sound gui.hover_sound

                            textbutton _("480×270"):
                                action Preference("display", 0.25)
                                activate_sound gui.radio_sound
                                hover_sound gui.hover_sound

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text"):
                        action Preference("skip", "toggle")
                        activate_sound gui.radio_sound
                        hover_sound gui.hover_sound
                    textbutton _("After Choices"):
                        action Preference("after choices", "toggle")
                        activate_sound gui.radio_sound
                        hover_sound gui.hover_sound
                    textbutton _("Transitions"):
                        action InvertSelected(Preference("transitions", "toggle"))
                        activate_sound gui.radio_sound
                        hover_sound gui.hover_sound

                ## Additional vboxes of type "radio_pref" or "check_pref" can
                ## be added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            activate_sound gui.activate_sound
                            hover_sound gui.hover_sound
                            style "mute_all_button"

                vbox:
                    if main_menu:
                        label _("Game Data")
        
                        hbox:
                            textbutton _("Reset Progress"):
                                activate_sound gui.activate_sound
                                hover_sound gui.hover_sound
                                text_hover_color "#FF0000"
                                action [Play("music", "audio/Neutral Ending.ogg"), Show("del_confirm1")]

screen del_confirm1():
    modal True
    zorder 200
    add Solid("#00000040")  # 50% black overlay
    frame:
        style "confirm_frame"

        vbox:
            spacing 15
            text _("Delete all data in [config.name]?"):
                style "confirm_label"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100
                textbutton _("No"):
                    action [Hide("del_confirm1"), Play("music", "audio/MainMenu.mp3")]
                    activate_sound gui.activate_sound
                    hover_sound gui.hover_sound
                textbutton _("Yes"):
                    action [Hide("del_confirm1"), Show("del_confirm2")]
                    activate_sound gui.activate_sound
                    hover_sound gui.hover_sound

screen del_confirm2():
    modal True
    zorder 200
    add Solid("#00000080")  # 50% black overlay
    frame:
        style "confirm_frame"

        vbox:
            spacing 15
            text _("Are you sure about that?\nHarvey might not be happy about it."):
                style "confirm_label"
                text_align 0.5
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100
                textbutton _("No, don't."):
                    action [Hide("del_confirm2"), Play("music", "audio/MainMenu.mp3")]
                    activate_sound gui.activate_sound
                    hover_sound gui.hover_sound
                textbutton _("Yes, delete it."):
                    action [Hide("del_confirm2"), Show("del_confirm3"), Play("audio","audio/SFX_Error.mp3")]
                    activate_sound gui.activate_sound
                    hover_sound gui.hover_sound

screen del_confirm3():
    modal True
    zorder 200
    add Solid("#000000ff")  # 50% black overlay
    #add "delgrad" xsize config.screen_width ysize config.screen_height
    frame:
        style "confirm_frame"

        vbox:
            spacing 15
            text _("This action can't be undone. No regrets?"):
                style "confirm_label"
                text_align 0.5
                xalign 0.5
                size 64
            text _("All achievements, progress, and language settings will be permanently cleared.") style "confirm_text" xalign 0.5 text_align 0.5
            text _("{color=#FF0000}Proceeding will restart the game with no memory of your past actions.{/color}") style "confirm_text" xalign 0.5 text_align 0.5


            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Don't delete!"):
                    action [Hide("del_confirm3"), Play("music", "audio/MainMenu.mp3")]
                    activate_sound gui.activate_sound
                    hover_sound gui.hover_sound
                textbutton _("No regrets!"):
                    action [Hide("del_confirm3"), Achievement.reset(), Function(reset_data)]
                    activate_sound gui.activate_sound
                    hover_sound gui.hover_sound
                    text_hover_color "#FF0000"

screen moregames():
    tag menu

    use game_menu(_("More Games"), scroll="viewport"):

        frame:
            background "#00000080"   # optional semi-transparent backdrop
            xfill True

            hbox:
                spacing 20

                # Game Icon
                add Transform("icon-bm", zoom=0.3)

                # Text Info
                vbox:
                    spacing 5

                    text _("BloodMoney!") color "#FFFFFF" size 32
                    text _("Author: ShroomyChrist") color "#CCCCCC"
                    text _("A dark horror clicker where you earn cash for a life-saving operation by clicking and inflicting pain on a mysterious, pastel-colored man. How far will you go for $25,000?") color "#BBBBBB"

                    textbutton _("Download Game!") xalign 0.5 action OpenURL("https://shroomychrist-studios.itch.io/bloodmoney") hover_sound gui.hover_sound activate_sound gui.activate_sound

        frame:
            background "#00000080"   # optional semi-transparent backdrop
            xfill True

            hbox:
                spacing 20

                # Game Icon
                add Transform("icon-hep", zoom=0.3)

                # Text Info
                vbox:
                    spacing 5

                    text _("BloodMoney: Human Expenditure Program") color "#FFFFFF" size 32
                    text _("Author: ShroomyChrist") color "#CCCCCC"
                    text _("The official sequel to BloodMoney! Experience a psychological horror sim where you are tasked with the chilling care and maintenance of Harvey Harvington. Monitor his vitals and follow the rules, or face the consequences of the Program.") color "#BBBBBB"

                    textbutton _("Download Game!") xalign 0.5 action OpenURL("https://shroomychrist-studios.itch.io/human-expenditure-program") hover_sound gui.hover_sound activate_sound gui.activate_sound

        frame:
            background "#00000080"   # optional semi-transparent backdrop
            xfill True

            hbox:
                spacing 20

                # Game Icon
                add Transform("icon-lm", zoom=0.3)

                # Text Info
                vbox:
                    spacing 5

                    text _("LoveMoney!") color "#FFFFFF" size 32
                    text _("Author: buwu3") color "#CCCCCC"
                    text _("Forget the hammers and needles—it's time for hugs and kisses! This fan-made spin-off lets you shower Harvey Harvington with love to earn the $25,000 you need. A romantic, spicy journey to steal a man's heart, one compliment at a time!") color "#BBBBBB"

                    textbutton _("Download Game!") xalign 0.5:
                        hover_sound gui.hover_sound activate_sound gui.activate_sound
                        action Show(
                            screen="confirm",
                            message="This game contains {color=#AA0000}NSFW themes{/color}.\nThe material shown in this game may not be suitable for all audiences.\nAre you sure you want to proceed anyway?",
                            yes_action=[Hide("confirm"), OpenURL("https://buwu3.itch.io/llllollll")],           # what to do if user selects YES
                            no_action=[Hide("confirm")]  # what to do if NO
                        )

        frame:
            background "#00000080"   # optional semi-transparent backdrop
            xfill True

            hbox:
                spacing 20

                # Game Icon
                add Transform("icon-sm", zoom=0.3)

                # Text Info
                vbox:
                    spacing 5

                    text _("SoftMoney (Original)") color "#FFFFFF" size 32
                    text _("Author: paper pepper") color "#CCCCCC"
                    text _("Tired of seeing Harvey suffer again and again? Think he deserves better? Then this game is for you! Same $25,000 operation, same roadside stall, same $1 per click—but with one big change: Harvey doesn't suffer anymore.") color "#BBBBBB"

                    textbutton _("Download Game!") xalign 0.5:
                        hover_sound gui.hover_sound activate_sound gui.activate_sound
                        action Show(
                            screen="confirm",
                            message="This game contains... {color=#AA00AA}wholesome themes{/color}.\nIt could be too much cuteness for you.\nAre you sure you have what it takes to proceed?",
                            yes_action=[Hide("confirm"), OpenURL("https://paper-pepper.itch.io/softmoney")],           # what to do if user selects YES
                            no_action=[Hide("confirm")]  # what to do if NO
                        )



style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character,
                        ## if set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes"):
                    action yes_action
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                textbutton _("No"):
                    action no_action
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound

    ## Right-click and escape answer "no".
    key "game_menu":
        action no_action
        activate_sound gui.activate_sound


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Language selection screens ###################################################
##
## These screens indicate selecting a language, duh.

screen menu_lang():
    tag menu

    use game_menu(_("Language"), scroll="viewport"):
        vbox:
            spacing 10
            text _("Select your preferred language:")

            for lang in renpy.known_languages():

                $ key = "language_" + lang
                $ lang_name = renpy.translate_string(key, key)

                textbutton lang_name:
                    action [
                        Language(lang),
                        Function(lambda l=lang: setattr(persistent, "language", l)),
                        Function(renpy.save_persistent)
                    ]
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound

screen language_select_screen():

    tag menu
    modal True
    add "bg bglang"
    # Full-screen frame background
    add "gui/frame.png" xsize 700 ysize 700 xalign 0.5 yalign 0.5

    fixed:
        at default_transition
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 40
            xalign 0.5
            yalign 0.5

            # Title
            text "Choose your language!" size 50 xalign 0.5

            # Scrollable buttons
            frame:
                background None
                padding (25, 25)
                xalign 0.5
                yalign 0.5

                viewport:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    xysize (500, 400)
                    xalign 0.5
                    yalign 0.5

                    vbox:
                        spacing 20
                        xalign 0.5

                        # Main languages
                        for lang in [("English","flag_EN","english"),
                                    ("Español","flag_SP","spanish"),
                                    ("Français","flag_FR","french"),
                                    ("Русский","flag_RU","russian"),
                                    ("{font=ZenMaruGothic-Bold.ttf}日本語{/font}","flag_JP","japanese"),
                                    ("{font=CookieRun Bold.ttf}한국인{/font}","flag_KR","korean")]:

                            $ text_label, flag_image, return_val = lang

                            button:
                                action Return(return_val)
                                xalign 0.5
                                hover_sound gui.hover_sound
                                activate_sound gui.activate_sound
                                hbox:
                                    spacing 10
                                    add flag_image
                                    text text_label size 30 color "#FFFFFF" hover_color "#FFFF00"

                        # “Other Languages” button
                        button:
                            action Return("other_languages")
                            xalign 0.5
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound
                            hbox:
                                spacing 10
                                add "flag_UNK"
                                text "Other Languages" size 30 color "#FFFFFF" hover_color "#FFFF00"

            text "Scroll to see more" size 22 xalign 0.5

screen other_languages_screen():

    tag menu
    modal True
    add "bg bglang"
    # Full-screen frame background
    add "gui/frame.png" xsize 700 ysize 700 xalign 0.5 yalign 0.5

    fixed:
        at default_transition
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 40
            xalign 0.5
            yalign 0.5

            # Title
            text "Other Languages" size 50 xalign 0.5

            # Scrollable joke languages
            frame:
                background None
                padding (25, 25)
                xalign 0.5
                yalign 0.5

                viewport:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    xysize (500, 400)
                    xalign 0.5
                    yalign 0.5

                    vbox:
                        spacing 20
                        xalign 0.5

                        # Joke languages
                        for lang in [("High Valyrian","flag_HV","valyrian"),
                                    ("Klingon","flag_TLH","klingon")]:

                            $ text_label, flag_image, return_val = lang

                            button:
                                action Return(return_val)
                                xalign 0.5
                                hover_sound gui.hover_sound
                                activate_sound gui.activate_sound
                                hbox:
                                    spacing 10
                                    add flag_image
                                    text text_label size 30 color "#FFFFFF" hover_color "#FFFF00"

                        # Back button
                        button:
                            action Return("back")
                            xalign 0.5
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound
                            hbox:
                                spacing 10
                                text "Back" size 30 color "#FFFFFF" hover_color "#FFFF00"

            text "Scroll to see more" size 22 xalign 0.5

## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly
        ## if config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed
## at once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using
## speech bubbles. The bubble screen takes the same parameters as the say
## screen, must create a displayable with the id of "what", and can create
## displayables with the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            #textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu("preferences")


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

############################################################
# TABBED DEBUG MENU
############################################################

screen debug_menu():

    tag menu
    modal True

    use game_menu(_("Debug Menu")):

        vbox:
            spacing 20

            # ------------------------------------------------------------
            # TABS
            # ------------------------------------------------------------
            hbox:
                spacing 10

                textbutton "General" action SetVariable("debug_tab", "general")
                textbutton "Unlocks" action SetVariable("debug_tab", "unlocks")
                textbutton "Interactions" action SetVariable("debug_tab", "interactions")
                textbutton "Endings" action SetVariable("debug_tab", "endings")

            null height 20

            # ------------------------------------------------------------
            # TAB CONTENT
            # ------------------------------------------------------------
            if debug_tab == "general":

                text "General Controls" size 32

                hbox:
                    spacing 10
                    text "Money: [money]" size 26
                    textbutton "+100" action SetVariable("money", money + 100)
                    textbutton "+1000" action SetVariable("money", money + 1000)
                    textbutton "Reset" action SetVariable("money", 0)

                null height 15

                text "Quick Flags" size 28

                vbox:
                    hbox:
                        text "poke1: [poke1]"
                        textbutton "Toggle" action ToggleVariable("poke1")


            elif debug_tab == "unlocks":

                text "Unlockable Items" size 32

                grid 2 6 spacing 10:

                    text "Hi-5 (item1): [unlockitem1]"
                    textbutton "Toggle" action ToggleVariable("unlockitem1")

                    text "Handshake (item2): [unlockitem2]"
                    textbutton "Toggle" action ToggleVariable("unlockitem2")

                    text "Headpat (item3): [unlockitem3]"
                    textbutton "Toggle" action ToggleVariable("unlockitem3")

                    text "Massage (item4): [unlockitem4]"
                    textbutton "Toggle" action ToggleVariable("unlockitem4")

                    text "Hug (item5): [unlockitem5]"
                    textbutton "Toggle" action ToggleVariable("unlockitem5")

                    text "Comb (item6): [unlockitem6]"
                    textbutton "Toggle" action ToggleVariable("unlockitem6")


            elif debug_tab == "interactions":

                text "Interaction Flags" size 32

                viewport:
                    mousewheel True
                    draggable True
                    scrollbars "vertical"

                    vbox:
                        spacing 20

                        # Hi-Fives
                        text "--- Hi-Fives ---" size 26
                        for n in range(1, 6):
                            hbox:
                                text f"hifive{n}: [{globals()[f'hifive{n}']}]"
                                textbutton "Toggle" action ToggleVariable(f"hifive{n}")

                        # Handshakes
                        text "--- Handshakes ---" size 26
                        for n in range(1, 6):
                            hbox:
                                text f"hand{n}: [{globals()[f'hand{n}']}]"
                                textbutton "Toggle" action ToggleVariable(f"hand{n}")

                        # Headpats
                        text "--- Headpats ---" size 26
                        for n in range(1, 6):
                            hbox:
                                text f"pathead{n}: [{globals()[f'pathead{n}']}]"
                                textbutton "Toggle" action ToggleVariable(f"pathead{n}")

                        # Massages
                        text "--- Massages ---" size 26
                        for n in range(1, 6):
                            hbox:
                                text f"masg{n}: [{globals()[f'masg{n}']}]"
                                textbutton "Toggle" action ToggleVariable(f"masg{n}")

                        # Hugs
                        text "--- Hugs ---" size 26
                        for n in range(0, 6):
                            hbox:
                                text f"hug{n}: [{globals()[f'hug{n}']}]"
                                textbutton "Toggle" action ToggleVariable(f"hug{n}")


            elif debug_tab == "endings":

                text "Ending Flags" size 32

                vbox:
                    spacing 10
                    for n in range(1, 4):
                        hbox:
                            text f"endflag{n}: [{globals()[f'endflag{n}']}]"
                            textbutton "Toggle" action ToggleVariable(f"endflag{n}")

            null height 40
    
default loading_progress = 0.0

screen loading_screen():
    modal True
    zorder 200

    # Semi-transparent overlay
    add Solid("#00000040")

    # Timer to animate the progress
    timer 0.07 repeat True action If(
        loading_progress < 1.0,
        SetVariable("loading_progress", loading_progress + 0.01),
        [Hide("loading_screen"), Return()]
    )

    text "{font=ArchiveUkr-Regular.ttf}Please wait...{/font}":
        xalign 0.5
        yalign 0.3
        size 60
        color "#FFFFFF"
        outlines [(2, "#000000", 0, 0)]

    # Percentage text
    text "{font=ArchiveUkr-Regular.ttf}[int(loading_progress * 100)]%{/font}":
        xalign 0.5
        yalign 0.5
        size 256
        color "#FFFFFF"
        outlines [(2, "#000000", 0, 0)]

    add "gui/presplash_background2.png" xalign 0.5 yalign 0.8
    # Cropped fill bar using tuple-based Crop
    add Crop((0, 0, int(loading_progress * 400), 50), "gui/presplash_background.png"):
        xpos 760
        yalign 0.8


    # Frame overlay
    add "gui/presplash_foreground.png" xalign 0.5 yalign 0.8

