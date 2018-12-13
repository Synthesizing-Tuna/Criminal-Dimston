#Возвращение в КИТ
label back2kit:
    $ sms_text = []
    $ sms_on()
    "{#l}{color=#000}Привет! Тебе надо явиться в кит!{/color}"
    "{#r}{color=#FFF}Это ещё зачем?{/color}"
    "{#l}{color=#000}Нет времени объяснять, надо!{/color}"
    "Что за чертощина?"
    $ sms_clear()
    $ sms_off()
    pause 1.0
    "Ебать, что же за хуйня в КИТе, что аж мне написали? Пойду посмотрю ради прикола."
    stop music
    $mp("rain")
    scene bg pidor with dissolve
    "До сих пор угараю с этой хуйни."
    scene bg parking with fade
    "Он опять в КИТе? Да что за чертовщина?!"
    stop music
    scene bg sofa with fade
    "Не буду сдавать одежду в гардероб, пойду так."
    show general
    $cp("general")
    general "Э! Не пущу в одежде и без сменки!"
    menu:
        "Попросить вежливо пропустить":
            $rm += 1
            $ smenka = True
            anon "Ну пожалуста, товарищ Гвардии Майор!"
            general "Э! Шагом марш в гардероб!"
            anon "Окей..."
            stop music
            hide general
            menu:
                "Куда же пойти?"
                "В гардероб":
                    "Да блять, опять стоять очереди в гардеробе."
                    $mp ("noice")
                    scene bg grdr with fade
                    "Сука. Пиздец."
                    scene black with fade
                    centered "Спустя 2 минуты"
                    scene bg sofa
                    "Ебать быстро сдался. Ладно, пойду на пару."
                    jump nn
                "К бахильнику":
                    show bg bahilass with fade
                    menu:
                        "Что бросаем?"
                        "5 рублей":
                            "Похер, брошу пятак."
                            hide bahil
                            "Так, надену эти бахилы, чтобы Маркович отстал."
                            jump nn
                        "Жетон":
                            $ rp -= 10
                            "Наебу дирика и брошу жетончик с пидором."
                            hide bahil
                            "Идеальное преступление. А теперь надену эти бахилы, чтобы Маркович отстал."
                            jump nn

        "Проигнорировать":
            $rm -= 1
            general "Э! Ты куда? А ну-ка стой..."
            stop music
            hide general
            $mp ("run")
            "Ууф, убежал от этого старика. Ладно, сейчас куртку в портфель положу и пойду на пару."
            jump nn
