init python:
    import os
    import subprocess

default seen_langwarn = False

default splash_EN = [

    # == BloodMoney References ==
    "Gore-Free Certified. Please drop your weapons.",
    "Non-violent mode enabled. Sorry, BloodMoney fans.",
    "Certified squish-free. Only softness ahead.",
    "This timeline contains no blood. Proceed peacefully.",

    # == Human Expenditure Program ==
    "The Program has no control over this run.",
    "HEP Override Failed: User retains autonomy.",
    "Unscheduled emotional stability detected. Flagging as \"unauthorized.\"",
    "HEP Notice: This scenario exceeds approved levels of hope.",

    # == LoveMoney Wholesome References ==
    "No NSFW. Just pure wholesomeness. You're welcome.",
    "This VN contains cuddles-permitted, content-warning-free softness.",
    "NSFW? No thanks. We serve comfort only.",
    "Tenderness unlocked. Lewdness denied.",

    # == SoftMoney Tribute ==
    "For you, paper pepper. I (AndriuxDev) did my best.",
    "Inspired by paper pepper. Remixed with care.",
    "A soft reboot of a soft classic.",
    "Restored with love, polished with intent."
]

default splash_RU = [
    "Сертификат «без жестокости». Пожалуйста, опустите оружие.",
    "Ненасильственный режим включён. Простите, фанаты BloodMoney.",
    "Сертифицировано как «без размозжения». Впереди только мягкость.",
    "В этой временной линии нет крови. Продолжайте мирно.",

    "Программа не контролирует этот забег.",
    "Ошибка переопределения HEP: пользователь сохраняет автономию.",
    "Обнаружена незапланированная эмоциональная стабильность. Помечено как «неразрешённое».",
    "Уведомление HEP: этот сценарий превышает допустимый уровень надежды.",

    "Никакого NSFW. Только чистая душевность. Пожалуйста.",
    "Эта визуальная новелла содержит разрешённую-обнимашками мягкость без предупреждений.",
    "NSFW? Нет, спасибо. Мы предлагаем только комфорт.",
    "Нежность разблокирована. Похоть отклонена.",

    "Для тебя, paper pepper. Я (AndriuxDev) сделал всё, что мог.",
    "Вдохновлено paper pepper. Переработано с заботой.",
    "Мягкий перезапуск мягкой классики.",
    "Восстановлено с любовью, отполировано с намерением.",
]

default splash_FR = [
    "Certifié sans gore. Veuillez déposer vos armes.",
    "Mode non violent activé. Désolé, fans de BloodMoney.",
    "Certifié sans écrasement. Rien que de la douceur à venir.",
    "Cette ligne temporelle ne contient aucun sang. Avancez en paix.",

    "Le Programme n’a aucun contrôle sur cette partie.",
    "Échec du dépassement HEP : l’utilisateur conserve son autonomie.",
    "Stabilité émotionnelle non prévue détectée. Indiquée comme « non autorisée ».",
    "Avis HEP : Ce scénario dépasse les niveaux d’espoir approuvés.",

    "Pas de NSFW. Juste de la pure bienveillance. De rien.",
    "Ce VN contient une douceur autorisée-pour-les-câlins et sans avertissements.",
    "NSFW ? Non merci. Nous offrons uniquement du réconfort.",
    "Tendresse débloquée. Grivoiseries refusées.",

    "Pour toi, paper pepper. J’ai fait de mon mieux (AndriuxDev).",
    "Inspiré par paper pepper. Remixé avec soin.",
    "Un redémarrage doux d’un classique doux.",
    "Restauré avec amour, poli avec intention.",
]

default splash_ES = [
    "Certificado sin gore. Por favor, deja tus armas.",
    "Modo no violento activado. Lo siento, fans de BloodMoney.",
    "Certificado sin aplastamientos. Solo suavidad por delante.",
    "Esta línea temporal no contiene sangre. Procede en paz.",

    "El Programa no tiene control sobre esta partida.",
    "Error en la anulación del HEP: el usuario mantiene su autonomía.",
    "Estabilidad emocional no programada detectada. Marcando como «no autorizada».",
    "Aviso HEP: Este escenario supera los niveles aprobados de esperanza.",

    "Nada de NSFW. Solo pureza absoluta. De nada.",
    "Esta novela visual contiene suavidad permitida-para-abrazos y sin advertencias.",
    "¿NSFW? No gracias. Aquí solo ofrecemos consuelo.",
    "Ternura desbloqueada. Picardía denegada.",

    "Para ti, paper pepper. Yo (AndriuxDev) hice lo mejor que pude.",
    "Inspirado por paper pepper. Reversionado con cariño.",
    "Un reinicio suave de un clásico suave.",
    "Restaurado con amor, pulido con intención.",
]

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

    # Already selected?
    if persistent.language:
        if not getattr(persistent, "first_run", False):
            jump after_language_selection
        else:
            jump game_boot
            return
    
    if seen_langwarn == False:
        $ setattr(config, "name", "SoftMoney Remastered")
        $ seen_langwarn = True
        pause 2.0
        window show
        "Before you begin, you'll have choose a language."
        "Please select a language from the following to start playing."
        window hide
        # Play starting music normally
        $ renpy.music.play(audio.t5, loop=True, if_changed=True, relative_volume=1)
        $ choice = renpy.call_screen("language_select_screen")
    else:
        $ renpy.music.play(audio.t5, loop=True, if_changed=True, relative_volume=1)
        $ choice = renpy.call_screen("language_select_screen")
    # REAL LANGUAGES -------------------------------------------------------

    if choice == "english":
        show bg bglang
        jump confirm_english

    if choice == "spanish":
        show bg bglang
        jump confirm_spanish

    if choice == "french":
        show bg bglang
        jump confirm_french

    if choice == "russian":
        show bg bglang
        jump confirm_russian

    if choice == "japanese":
        show bg bglang
        jump unav_lang
    
    if choice == "korean":
        show bg bglang
        jump unav_lang

    # JOKE LANGUAGES -------------------------------------------------------

    if choice == "other_languages":
        $ other_choice = renpy.call_screen("other_languages_screen")

        if other_choice == "valyrian":
            show bg bglang
            stop music
            pause 1.0
            window show
            "Oh… a Game of Thrones fan!"
            "High Valyrian is not available, sorry."
            "If you want to learn it, check the official course on Duolingo (account required)."
            $ style.default.font = "fonts/ArchiveUkr-Regular.ttf"
            window hide
            jump language_select_loop

        elif other_choice == "klingon":
            show bg bglang
            stop music
            pause 1.0
            window show
            "A Star Trek fan, I see!"
            "Klingon will never be implemented in this clicker game."
            "But you can learn it on Duolingo (account required)."
            window hide
            jump language_select_loop

        elif other_choice == "back":
            jump language_select_loop

    # NO LANGUAGE ----------------------------------------------------------

    if choice == "nolang":
        "No language?! Are you serious?"
        "You have to pick one to continue."
        jump language_select_loop

# ========== Confirmations (clean + separate) ==========

label confirm_english:
    pause 0.5
    window show
    menu:
        "Set language to English?"
        "Yes!":
            play sound notify
            $ persistent.language = "english"
            "Okay! Harvey's dialogue and other text will now be in English."
            "You can change this at any time in the options menu."
            window hide
            stop music fadeout 2.0
            jump after_language_selection
        "No...":
            window hide
            pause 0.5
            jump language_select_loop

label confirm_spanish:
    pause 0.5
    window show
    menu:
        "¿Establecer el idioma en Español?"
        "¡Sí!":
            play sound notify
            $ persistent.language = "spanish"
            "¡Muy bien! El diálogo de Harvey y otros textos ahora estarán en Español."
            "Puedes cambiarlo en cualquier momento en el menú de opciones."
            window hide
            stop music fadeout 2.0
            jump after_language_selection
        "No...":
            window hide
            pause 0.5
            jump language_select_loop

label confirm_french:
    pause 0.5
    window show
    menu:
        "Définir la langue en Français?"
        "Oui!":
            play sound notify
            $ persistent.language = "french"
            "D'accord ! Les dialogues de Harvey et d'autres textes seront désormais en Français."
            "Vous pouvez changer cela à tout moment dans le menu des options."
            window hide
            stop music fadeout 2.0
            jump after_language_selection
        "Non...":
            window hide
            pause 0.5
            jump language_select_loop

label confirm_russian:
    pause 0.5
    window show
    menu:
        "Установить язык Русский?"
        "Да!":
            play sound notify
            $ persistent.language = "russian"
            "Хорошо! Диалоги Харви и другие тексты теперь будут на Русском."
            "Вы можете изменить это в любое время в меню настроек."
            window hide
            stop music fadeout 2.0
            jump after_language_selection
        "Нет...":
            window hide
            pause 0.5
            jump language_select_loop

label unav_lang:
    pause 0.5
    window show
    "This language is unavailable."
    "Check the repository for future updates."
    window hide
    pause 0.5
    jump language_select_loop

label after_language_selection:
    hide bg bglang with Dissolve(2.0)
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

    scene white with Dissolve(3.0)

    call game_boot
    return

label game_boot:

    python:
        import random
        if persistent.language == "spanish":
            selected_splash = random.choice(splash_ES)
        elif persistent.language == "french":
            selected_splash = random.choice(splash_FR)
        elif persistent.language == "russian":
            selected_splash = random.choice(splash_RU)
        else:
            selected_splash = random.choice(splash_EN)

    scene white
    $ renpy.pause(1.5, hard=True)

    # Show logo text with black color
    play audio logo volume 0.5
    show devlogo at fade_img(0.5, 5.0, 0.5)
    $ renpy.pause(7.0, hard=True)

    # Show splash text with random color
    show text "[selected_splash]" at fade_text(0.7, 3.0, 1.0)
    $ renpy.pause(5.0, hard=True)

    hide text with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)

    scene bg mainscreen with Dissolve(1.5)  # Replace with your main menu background
    $ renpy.pause(0.5, hard=True)

    call screen loading_screen

    return  # goes to main menu

