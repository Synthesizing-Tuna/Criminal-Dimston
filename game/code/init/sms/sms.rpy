# sms.rpy by Руслан barsunduk Небыков
# 10.04.2016 (доработано 19.06.2017) лизензия: CC0
init:
    transform _a(alpha=0.0):
        alpha alpha

init python:
    sms_text = []
    what2 = ""
    # заголовок можно менять в любой момент, меняя эту переменную
    pp = 10
    # изъять текст смс из текстбокса и закинуть в экран смс
    def sms(txt):
        global what2
        what2 = txt
        if ("{#l}" in txt) or ("{#r}" in txt):
            sms_text.append(txt)
            what2 = ""
        # разные звуки для сообщений
        if ("{#l}" in txt):
            renpy.music.play("code/init/sms/send.mp3", channel="sound", loop=False, fadein=0, fadeout=0)
        if ("{#r}" in txt):
            renpy.music.play("code/init/sms/send.mp3", channel="sound", loop=False, fadein=0, fadeout=0)
    SMS = renpy.curry(sms) # функцию в Action
    # показать экран смс
    def sms_on(effect=dissolve):
        renpy.show_screen("sms_screen", _layer="master")
        renpy.with_statement(effect)
    # спрятать экран смс
    def sms_off(effect=dissolve):
        renpy.hide_screen("sms_screen", layer="master")
        renpy.with_statement(effect)
    # очистить экран смс
    def sms_clear(effect=dissolve):
        global sms_text
        sms_text = []
        renpy.restart_interaction()

# экран с смсками
screen sms_screen:
    frame:
        # изображение пустого экрана
        background "code/init/sms/smsbg.png"
        align(.85, .0)
        yfill True
        # ширина
        xminimum 600
        xmaximum 600
        # отступ сообщений от верха
        top_padding 115
        # контейнер для пузырьков с сообщениями
        vbox:
            xfill True
            yanchor 1.0
            yalign 0.3
            for i in sms_text:
                # пузырьки с сообщениями
                textbutton _("{size=20}{font=code/init/sms/SFRegular.ttf}" + i + "{/font}{/size}"):
                    xminimum 60
                    yminimum 60
                    top_padding pp
                    bottom_padding pp
                    left_padding pp*4
                    right_padding pp*4
                    if "{#r}" in i:
                        xalign 0.55
                        background Frame("code/init/sms/smsright.png", 60, 38)
                    else:
                        xalign 0.0
                        background Frame("code/init/sms/smsleft.png", 60, 38)
                    action []
            # это чтобы первые сообщения появлялись сверху
            frame:
                yfill True
                background None
        # заголовочная часть интерфейса, прячет верхние сообщения
        add "code/init/sms/smscaption.png" align(-.045, .0) yoffset -115

# копия стандартного экрана say, с небольшими изменениями,
# которые позволяют скрыть основное окно, если в тексте есть теги для смс
screen say:
    default side_image = None
    default two_window = False
    on "show" action SMS(what) # сначала обрабатываем наши теги для СМС
    on "replace" action SMS(what)
    if not two_window:
        window:
            id "window"
            if not what2:
                background None
            vbox:
                style "say_vbox"
                if who:
                    text who id "who"
                text what id "what":
                    if not what2:
                        at _a(0)
    else:
        vbox:
            style "say_two_window_vbox"
            if who and what2:
                window:
                    style "say_who_window"
                    if not what2:
                        background None
                    text who:
                        id "who"
                        if not what2:
                            at _a(0)
            window:
                id "window"
                if not what2:
                    background None
                vbox:
                    style "say_vbox"
                    text what id "what"
                    if not what2:
                        at _a(0)
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0
