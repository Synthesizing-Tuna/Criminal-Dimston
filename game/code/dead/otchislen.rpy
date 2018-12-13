#Отчисление после бега от захарки (1 день, начало)
label goout:
    scene bg kabdir
    show snkw akbar at left with easeinleft
    show pidor at right with easeinright
    snkw "Валерий Иванович, я вам тут одного киника привела, отчислите его, он говорил гадости на официальном сайте 'Подслушано в стенах СПбКИТ'"
    pidor "С удовольствием отчислю этого студента."
    scene black with fade
    centered "Спустя 5 минут"
    scene bg kabdir
    show pidor at right
    show snkw akbar at left
    pidor "Приказ напечатан, ты ОТЧИСЛЕЕН! Можешь завтра не приходить!"
    snkw "Иди отсюда, киник! Желаю, чтобы ты сдох от СПИДа."
    scene black with fade
    centered "Вы были отчислены, но вы можете поступить сюда ещё раз!"
    menu:
        "Поступить":
            stop music
            "Что, опять заново?"
            jump nottoday
        "Не поступать":
            scene black with fade
            centered "Мудрое решение."
            centered "КОНЕЦ ИГРЫ!"
            stop music
            return

#Отчисление при истечении бара терпения дирика (1 день, после проёба НН)
label pidorotch:
    show pidor at left with easeinleft
    pidor "Отчислен, можешь даже не приходить завтра. Пошли в кабинет."
    scene kabdir with fade
    show pidor at center with fade
    pidor "Отчислен! Вот твои документы, катись отсюда."
    scene black with fade
    centered "Вы были отчислены за тормознутость."
    pause
    return

#Дирик в сбере отчисляет (1 день, бк)
label sberout:
    sber "А вы собираетесь снимать деньги со счёта?"
    pidor "Нет, только пополнять... Подождите пожалуйста.."
    show pidor at right with easeinleft
    $sp("suddenly")
    pidor "Подслушиваешь? Охуел?"
    pidor "ТЫ ОТЧИСЛЕН! ТЫ ПОНЯЛ? ОТ-ЧИС-ЛЕН!"
    stop music
    scene black with fade
    centered "Вы были отчислены за излишнюю любознательность"
    centered "КОНЕЦ ИГРЫ!"
    pause
    return

#Дирик в трамвае отчисляет (2 день, начало)
label railout:
    show pidor with fade
    anon "Здрастите, Валерий Иванович!{w} А где ваш Солярис?"
    pidor "Ты кто?"
    anon "Я учусь в вашем колледже"
    pidor "Отчислен нах!ОТ-{w}ЧИС-{w}ЛЕН!"
    $mp("sad")
    anon "За что?"
    pidor "Отчислен, можешь не приходить!"
    "Чего блять? Пиздец, я отчислен."
    scene black with fade
    centered "Вы отчислены из-за плохого настроения дирика."
    pause
    return

#Шавлюга отчисляет (3 день, физ-ра)
label delite:
    scene bg kabdir
    show delite at right with easeinright
    show pidor at left with easeinleft
    snkw "Валерий Иванович, он присел на конус, он ненормальный"
    pidor "Ненормальные нам не нужны, отчислен."
    scene black with fade
    centered "Вы были отчислены, но вы можете поступить сюда ещё раз!"
    menu:
        "Поступить":
            stop music
            "Что, опять заново?"
            jump nottoday
        "Не поступать":
            scene black with fade
            centered "Мудрое решение."
            centered "КОНЕЦ ИГРЫ!"
            stop music
            return