init python:
    import os
    import subprocess

    def reset_font():
        gui.text_font = "IBMPlexSans-Bold.ttf"
        gui.name_text_font = "IBMPlexSans-Bold.ttf"
        gui.interface_text_font = "IBMPlexSans-Bold.ttf"
        gui.button_text_font = "IBMPlexSans-Bold.ttf"
        gui.choice_button_text_font = "IBMPlexSans-Bold.ttf"

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

default splash_JP = [

    "ゴアフリー認証済み。武器を捨ててください。",
    "非暴力モード有効。BloodMoney ファンの皆様、申し訳ございません。",
    "スクイッシュフリー認証済み。この先は優しさのみ。",
    "このタイムラインには流血はありません。平和的に進めてください。"

    "この実行はプログラムによって制御されません。",
    "HEP オーバーライド失敗: ユーザーは自律性を維持します。",
    "予定外の感情的不安定が検出されました。\"不正\"としてフラグ付けします。",
    "HEP 通知: このシナリオは承認された希望レベルを超えています。",

    "NSFW なし。純粋な健全さのみ。どういたしまして。",
    "この VN には、抱きしめられることが許可された、コンテンツ警告のない優しさが含まれています。",
    "NSFW? 結構です。私たちは癒しのみを提供します。",
    "\"優しさ\"ロック解除。わいせつ行為はお断り。",

    "ペーパーペッパー、君へ。私 (アンドリウクスデヴ) はベストを尽くしたよ。",
    "ペーパーペッパーにインスパイアされて。丁寧にリミックスしました。",
    "ソフトクラシックのソフトリブート。",
    "愛情を込めて修復し、意図を込めて磨き上げました。"
]

default splash_KR = [
    "고어 없음 인증 완료. 무기는 내려놓으세요.",
    "비폭력 모드 활성화. 유혈 팬 여러분, 죄송합니다.",
    "찌그러짐 없음 인증. 앞으로는 부드러움만 있습니다.",
    "이 타임라인에는 피가 없습니다. 평화롭게 진행하세요.",

    "프로그램은 이 진행을 통제할 수 없습니다.",
    "HEP 재정의 실패: 사용자의 자율성 유지됨.",
    "예정되지 않은 감정적 안정 감지. '무허가'로 분류.",
    "HEP 공지: 이 시나리오는 허용된 희망 수준을 초과합니다.",

    "성인 콘텐츠 없음. 순수한 위로만 있습니다. 환영합니다.",
    "이 비주얼노벨에는 포옹 가능, 주의사항 없는 부드러움이 담겨 있습니다.",
    "성인 콘텐츠? 사양합니다. 우리는 위로만 제공합니다.",
    "부드러움 해금. 음란함 차단.",

    "당신을 위해, 페이퍼 페퍼. 저(안드릭스데브)는 최선을 다했습니다.",
    "페이퍼 페퍼에게 영감을 받아. 정성껏 리믹스했습니다.",
    "부드러운 클래식의 부드러운 재시작.",
    "사랑으로 복원하고, 의도를 담아 연마했습니다."
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
        $ reset_font()

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
        jump confirm_japanese
    
    if choice == "korean":
        show bg bglang
        jump confirm_korean

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

label confirm_japanese:
    pause 0.5
    window show
    menu:
        "{font=ZenMaruGothic-Bold.ttf}日本語に設定しますか？{/font}"  # (Do you want to set the language to Japanese?)
        "{font=ZenMaruGothic-Bold.ttf}はい！{/font}":
            play sound notify
            $ persistent.language = "japanese"
            "{font=ZenMaruGothic-Bold.ttf}了解しました！ハーヴィーの会話やその他のテキストが日本語になります。{/font}"
            "{font=ZenMaruGothic-Bold.ttf}設定メニューからいつでも言語を変更できます。{/font}"
            window hide
            stop music fadeout 2.0
            jump after_language_selection
        "{font=ZenMaruGothic-Bold.ttf}いいえ...{/font}":
            window hide
            pause 0.5
            jump language_select_loop

label confirm_korean:
    pause 0.5
    window show
    menu:
        "{font=CookieRun Bold.ttf}언어를 한국어로 설정하시겠습니까?{/font}"  # (Do you want to set the language to Korean?)
        "{font=CookieRun Bold.ttf}네!{/font}":
            play sound notify
            $ persistent.language = "korean"
            "{font=CookieRun Bold.ttf}알겠습니다! 하비의 대화와 다른 텍스트는 이제 한국어로 표시됩니다.{/font}"
            "{font=CookieRun Bold.ttf}설정 메뉴에서 언제든지 언어를 변경할 수 있습니다.{/font}"
            window hide
            stop music fadeout 2.0
            jump after_language_selection
        "{font=CookieRun Bold.ttf}아니요...{/font}":
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
    $ Language(persistent.language)
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
                "welcome": "Bienvenido a SoftMoney Remasterizado.",
                "desc": "Esta es una experiencia suave y reflexiva sobre el cuidado, el esfuerzo y la conexión.",
                "warning": "SoftMoney Remasterizado no contiene contenido violento ni angustiante, pero sí explora temas emocionales y el estrés financiero de una manera ligera y humana.",
                "menu": "Por favor confirme que está listo para comenzar su experiencia.",
                "confirm": "Entiendo y deseo continuar."
            },
            "french": {
                "welcome": "Bienvenue dans SoftMoney Remasterisé.",
                "desc": "C'est une expérience douce et réfléchie sur le soin, l'effort et la connexion.",
                "warning": "SoftMoney Remasterisé ne contient pas de contenu violent ou pénible, mais explore des thèmes émotionnels et le stress financier de manière légère et humaine.",
                "menu": "Veuillez confirmer que vous êtes prêt à commencer votre expérience.",
                "confirm": "Je comprends et souhaite continuer."
            },
            "russian": {
                "welcome": "Добро пожаловать в SoftMoney Ремастер.",
                "desc": "Это мягкий и задумчивый опыт о заботе, усилиях и связи.",
                "warning": "SoftMoney Ремастер не содержит жестокого или травмирующего контента, но затрагивает эмоциональные темы и финансовый стресс бережным, человеческим образом.",
                "menu": "Пожалуйста, подтвердите, что вы готовы начать свой опыт.",
                "confirm": "Я понимаю и хочу продолжить."
            },
            "japanese": {
                "welcome": "{font=ZenMaruGothic-Bold.ttf}ソフトマネー リマスターへようこそ。{/font}",
                "desc": "{font=ZenMaruGothic-Bold.ttf}これは、ケア、努力、そして繋がりについての柔らかく、思慮深い体験です。{/font}",
                "warning": "{font=ZenMaruGothic-Bold.ttf}ソフトマネー リマスターには過激な内容やトラウマを引き起こすコンテンツは含まれていませんが、感情的なテーマや経済的なストレスを丁寧で人間的な方法で扱っています。{/font}",
                "menu": "{font=ZenMaruGothic-Bold.ttf}体験を始める準備ができたことを確認してください。{/font}",
                "confirm": "{font=ZenMaruGothic-Bold.ttf}理解し、続行したいです。{/font}"
            },
            "korean": {
                "welcome": "{font=CookieRun Bold.ttf}소프트머니 리마스터에 오신 것을 환영합니다.{/font}",
                "desc": "{font=CookieRun Bold.ttf}이것은 돌봄, 노력, 그리고 연결에 대한 부드럽고 사려 깊은 경험입니다.{/font}",
                "warning": "{font=CookieRun Bold.ttf}소프트머니 리마스터는 폭력적이거나 트라우마를 유발하는 콘텐츠를 포함하지 않지만, 감정적인 주제와 재정적 스트레스를 섬세하고 인간적인 방식으로 다룹니다.{/font}",
                "menu": "{font=CookieRun Bold.ttf}경험을 시작할 준비가 되었는지 확인해주세요.{/font}",
                "confirm": "{font=CookieRun Bold.ttf}이해하고 계속 진행하겠습니다.{/font}"
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

    call game_boot from _call_game_boot
    return

label game_boot:
    $ Language(persistent.language)
    python:
        import random
        if persistent.language == "spanish":
            selected_splash = random.choice(splash_ES)
        elif persistent.language == "french":
            selected_splash = random.choice(splash_FR)
        elif persistent.language == "russian":
            selected_splash = random.choice(splash_RU)
        elif persistent.language == "japanese":
            selected_splash = random.choice(splash_JP)
        elif persistent.language == "korean":
            selected_splash = random.choice(splash_KR)
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
    
    # Halloween: October 30–31
    if today.month == 10 and today.day in (30, 31) and not hiddenhalloween.has():
        $ hiddenhalloween.grant()
        $ renpy.pause(3.0, hard=True)

    # Christmas: December 24–25
    if today.month == 12 and today.day in (24, 25) and not hiddenchristmas.has():
        $ hiddenchristmas.grant()
        $ renpy.pause(3.0, hard=True)

    call screen loading_screen

    return  # goes to main menu

