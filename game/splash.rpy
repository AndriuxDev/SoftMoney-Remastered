init python:
    import os
    import subprocess

label splashscreen:

    python:
        process_list = []
        currentuser = ""

        if renpy.windows:
            try:
                output = subprocess.check_output("wmic process get Description", shell=True)
                process_list = output.decode(errors="ignore").lower().splitlines()
            except Exception:
                process_list = []

            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
                        break
            except Exception:
                currentuser = ""

    # Handle first-run setup
    python:
        firstrun_path = os.path.join(config.basedir, "game", "firstrun")
        firstrun = ""

        try:
            if os.path.exists(firstrun_path):
                with open(firstrun_path, "r") as f:
                    firstrun = f.read(1)
            else:
                with open(firstrun_path, "w") as f:
                    f.write("")
        except Exception:
            firstrun = ""

    # First launch / restore behavior
    if not firstrun:
        if getattr(persistent, "first_run", False) and os.path.exists(os.path.join(renpy.config.basedir, "saves")):
            $ quick_menu = False

            scene black

            menu:
                "Previous SoftMoney data was found. Would you like to start fresh?"

                "Yes, reset my data and begin again.":
                    "Clearing save data...{nw}"

                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        persistent.first_run = False
                        renpy.save_persistent()
                        renpy.full_restart()

                "No, keep my progress.":
                    pass

        python:
            try:
                with open(firstrun_path, "w") as f:
                    f.write("1")
            except Exception:
                if renpy.has_label("readonly"):
                    renpy.jump("readonly")
                else:
                    renpy.quit()

    # If this is the first run ever (persistent flag not set)
    if not getattr(persistent, "first_run", False):

        $ quick_menu = False
        $ persistent.language = getattr(persistent, "language", None)

        jump language_select_loop

label language_select_loop:
    $ renpy.music.play(audio.t5, loop=True, if_changed=True, relative_volume=0.3)

    # Si ya hay un idioma guardado...
    if persistent.language:

        # Solo mostrar el disclaimer si aún no se ha mostrado antes
        if not getattr(persistent, "first_run", False):
            jump after_language_selection
        else:
            # Ya se mostró el disclaimer antes, continuar al juego o menú principal
            return

    # Si no hay idioma elegido aún, mostrar menú de selección
    menu:
        "Choose your language! / ¡Elige tu idioma! / Choisissez votre langue! / Выберите язык!"

        "English":
            menu:
                "Set language to English?"
                
                "Yes":
                    play sound notify
                    $ persistent.language = "english"
                    "Okay! Harvey's dialogue and other text will now be in English."
                    "You can change this at any time in the options menu."
                    "More languages may be added in the future!"
                    stop music fadeout 2.0
                "No":
                    jump language_select_loop

        "Español":
            menu:
                "¿Establecer el idioma en Español?"
                
                "Sí":
                    play sound notify
                    $ persistent.language = "spanish"
                    "¡Muy bien! El diálogo de Harvey y otros textos ahora estarán en Español."
                    "Puedes cambiarlo en cualquier momento en el menú de opciones."
                    "¡Es posible que se agreguen más idiomas en el futuro!"
                    stop music fadeout 2.0
                "No":
                    jump language_select_loop

        "Français":
            menu:
                "Définir la langue en Français?"
                
                "Oui":
                    play sound notify
                    $ persistent.language = "french"
                    "D'accord ! Les dialogues de Harvey et d'autres textes seront désormais en Français."
                    "Vous pouvez changer cela à tout moment dans le menu des options."
                    "D'autres langues pourraient être ajoutées à l'avenir !"
                    stop music fadeout 2.0
                "Non":
                    jump language_select_loop

        "Русский":
            menu:
                "Установить язык Русский?"

                "Да":
                    play sound notify
                    $ persistent.language = "russian"
                    "Хорошо! Диалоги Харви и другие тексты теперь будут на Русском."
                    "Вы можете изменить это в любое время в меню настроек."
                    "В будущем могут быть добавлены другие языки!"
                    stop music fadeout 2.0
                "Нет":
                    jump language_select_loop

        "Continue without choosing":
            "No language?! Are you serious?"
            "You must choose a language to proceed."
            "Please pick one of the available options."
            jump language_select_loop


label after_language_selection:
    
    pause 1.0
    scene white with Dissolve(2.0)
    pause 1.0

    #play music t6 fadein 1.0

    scene white
    pause 0.5

    scene sm_tos
    with Dissolve(1.0)

    pause 1.0

    python:
        lang = getattr(persistent, "language", "english") or "english"
        lang = lang.lower()

        translations = {
            "english": {
                "welcome": "Welcome to SoftMoney Remastered.",
                "desc": "This is a gentle and reflective experience about care, effort, and connection.",
                "warning": "SoftMoney Remastered has no violent or distressing content, but it does explore emotional themes and financial stress in a light, human way.",
                "menu": "Please confirm that you're ready to begin your experience.",
                "confirm": "I understand and wish to continue."
            },
            "spanish": {
                "welcome": "Bienvenido a SoftMoney Remastered.",
                "desc": "Esta es una experiencia suave y reflexiva sobre el cuidado, el esfuerzo y la conexión.",
                "warning": "SoftMoney Remastered no contiene contenido violento ni angustiante, pero sí explora temas emocionales y el estrés financiero de una manera ligera y humana.",
                "menu": "Por favor confirme que está listo para comenzar su experiencia.",
                "confirm": "Entiendo y deseo continuar."
            },
            "french": {
                "welcome": "Bienvenue dans SoftMoney Remastered.",
                "desc": "C'est une expérience douce et réfléchie sur le soin, l'effort et la connexion.",
                "warning": "SoftMoney Remastered ne contient pas de contenu violent ou pénible, mais explore des thèmes émotionnels et le stress financier de manière légère et humaine.",
                "menu": "Veuillez confirmer que vous êtes prêt à commencer votre expérience.",
                "confirm": "Je comprends et souhaite continuer."
            },
            "russian": {
                "welcome": "Добро пожаловать в SoftMoney Remastered.",
                "desc": "Это мягкий и задумчивый опыт о заботе, усилиях и связи.",
                "warning": "SoftMoney Remastered не содержит жестокого или травмирующего контента, но затрагивает эмоциональные темы и финансовый стресс бережным, человеческим образом.",
                "menu": "Пожалуйста, подтвердите, что вы готовы начать свой опыт.",
                "confirm": "Я понимаю и хочу продолжить."
            }
        }

        t = translations.get(lang, translations["english"])

    "[t['welcome']]"
    "[t['desc']]"
    "[t['warning']]"

    menu:
        "[t['menu']]"

        "[t['confirm']]":
            pass

    $ persistent.first_run = True
    $ renpy.save_persistent()

    scene sm_tos2
    with Dissolve(1.5)

    pause 1.0

    scene white
    #stop music fadeout 1.0
    with Dissolve(3.0)

    ## This line was causing trouble with the main menu!
    #show screen main_menu with Dissolve(2.0)

    return
