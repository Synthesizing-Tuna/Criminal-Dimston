# Этот файл публично доступен. Модифицируйте его под свои собственные экраны.

##############################################################################
# Say
#
# Экран отображения ADV-диалога.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Умолчания для side_image и two_window
    default side_image = None
    default two_window = False

    # Решаем, нужен ли нам двухоконный или однооконный вариант.
    if not two_window:

        # Вариант с одним окном.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # Вариант с двумя окнами.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # Если есть изображение, отобразить его над текстом.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0




##############################################################################
# Choice
#
# Экран для отображения внутриигровых меню.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Экран для отображения renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

##############################################################################
# Nvl
#
# Экран для NVL-диалога и меню.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Отображать диалог.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Отображать меню, если есть.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0


##############################################################################
# Main Menu
# Сделан через координаты по причине лени и, когда он делался, неопытности и не знанию про imagebutton. Сделан 19 числа ещё днём.

screen main_menu:
    tag menu

    imagemap:
            ground "gui/main.png" #Главное меню без фокуса на кнопках
            hover "gui/main2.png" #С фокусом
            alpha True

            hotspot (917, 342, 200, 190) action Start()
            hotspot (1118, 344, 200, 190) action ShowMenu("load")
            hotspot (1120, 543, 200, 190) action Quit(confirm=True)
            hotspot (923, 534, 200, 190) action ShowMenu("preferences")


##############################################################################
# Navigation
#
# Экран, включаемый в другие экраны для отображения навигации и фона.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # Фон игрового меню.
    window:
        style "gm_root"

    # Кнопки.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Назад") action Return()
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Сохранить игру") action ShowMenu("save")
        textbutton _("Загрузить игру") action ShowMenu("load")
        textbutton _("Главное меню") action MainMenu()
        textbutton _("Выход") action Quit()

##############################################################################
# Save, Load
#
# Экраны для сохранения и загрузки игры.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Ибо сохранение и загрузка очень похожи, мы совмещаем их в один экран,
# file_picker. Потом мы используем его из экранов
# загрузки и сохранения.

screen file_picker:

    frame:
        style "file_picker_frame"

        $ columns = 2
        $ rows = 5

        # Отобразить сетку файловых слотов.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Отобразить 10 слотов, с номерами от 1 до 10.
            for i in range(1, columns * rows + 1):

                # Каждый из них — кнопка.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Добавить скриншот.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Здесь может быть ваша реклама."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # Это заменяет другие меню.
    tag menu

    use navigation
    use file_picker

screen load:

    # Это заменяет другие меню.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)



##############################################################################
# Preferences
#
#Тут уже imagebutton-ы и разные состояния. Часть сделана 20 октября в 4 утра. Кек.

screen preferences:

    tag menu
    add 'gui/settings.png'

    if renpy.game.preferences.transitions:
        imagebutton idle "gui/anim.png" xpos 1169 ypos 502 action Preference('transitions', 'none')
    else:
        imagebutton idle "gui/noanim.png" xpos 1169 ypos 502 action Preference('transitions', 'all')

    if renpy.game.preferences.fullscreen:
        imagebutton idle "gui/fullscreen.png" xpos 1007 ypos 502 action Preference('display', 'window')
    else:
        imagebutton idle "gui/window.png" xpos 1007 ypos 502 action Preference('display', 'fullscreen')

    bar xpos 300 ypos 300 value Preference("music volume") style "pref_vslider"

    bar xpos 65 ypos 300 value Preference("sound volume") style "pref_vslider"

    bar xpos 545 ypos 300 value Preference("text speed") style "pref_vslider"

    key "game_menu" action Return()


init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0

    style.pref_vslider.left_bar = "gui/slideroff.png" # весь слайдер окрашенный в цвет, что слева от бегунка
    style.pref_vslider.right_bar = "gui/slider.png" # весь слайдер окрашенный в цвет, что справа от бегунка
    style.pref_vslider.xmaximum = 40 # ширина слайдера (ширина картинок bar_left.png и bar_right.png)
    style.pref_vslider.ymaximum = 200 # высота слайдера
    style.pref_vslider.thumb = "gui/toggle.png" # рисунок бегунка
    style.pref_vslider.thumb_offset = 20

##############################################################################
# Yes/No Prompt
#
# Экран, спрашивающий у пользователя вопрос да/нет.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True
    add 'gui/exit.png'

    imagebutton idle "gui/yes.png" xpos 100 ypos 250 action yes_action
    imagebutton idle "gui/no.png" xpos 390 ypos 250 action no_action

    # Правый щелчок и escape отвечают "нет".
    key "game_menu" action no_action

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.layout = "subtitle"


##############################################################################
# Quick Menu
#
# Экран, входящий в экран save и дающий некоторые полезные функции

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
