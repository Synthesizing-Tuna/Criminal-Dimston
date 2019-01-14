label poll:
    stop music
    scene bg corridor with fade
    if (pz == True and pb == True and pn == True and pm == True and psh == True and pf == True):
        "Итак, всех опросил, пора, значит, отправляться в Чащу."
        scene bg door with fade
        if rm>=0:
            "Пахом меня там ждёт, главное выпытать из него всю информацию."
        if rub == True:
            "Бахильник дал флешку же как раз, где указывалось что-то про скважину и там было что-то про Чащу как раз."
        if rn>= 0:
            "Локалхост ещё говорила про Кольскую сверхвысокую."
        if medic == True:
            "А медсестра еще о чем-то в курсе, раз мне про бахильник сказала."
            if rub == True:
                "Хорошо, что её послушал."
            else:
                "Жаль, что не послушал и ничего не узнал."
        jump chasha
    else:
        "У кого спрашивать..."
        menu:
            "Бочка":
                "Пойду к бочке!"
                "Он наверное у Матысик."
                stop music
                scene bg foma with fade
                show foma with moveintop
                if pf == False:
                    $pf = True
                    anon "Здрасьтитя!"
                    foma "Здарова! Чо хотел?"
                    anon "Да тут такое дело. {w} Мне надо узнать про Пахома. {w} Мне просто НН-ка сказал узнать про стопмоторную анимацию, а он в ней профи. Во как."
                    foma "Стопмоторная анимация? Щито?"
                    anon "Сам в шоке. {w} Так что, где он?"
                    if rf>0:
                        foma "Да я хз, на самом деле."
                        anon "А примерно где он живет?"
                        foma "Да он на самом деле поехавший. Про поселок Чаща что-то говорил. Что там у него космодром и штаб КПД МП. {w} Я хз, что это."
                        anon "Чаща... Я понял, спасибо!"
                        foma "Да не за что."
                        jump poll
                    else:
                        foma "А?"
                        anon "Так где он?"
                        foma "..."
                        anon "Фома?"
                        foma "А?"
                        "Понятно, хрен я что узнаю. Сука, тогда пойду."
                        jump poll
                else:
                    foma "Тебе что еще надо?"
                    anon "Узнать про Пахома!"
                    foma "А? {w} Что?"
                    "Бля, я же у него был, нахуя я еще раз к нему пошёл."
                    jump poll

            "Захарка":
                scene bg kab302 with dissolve
                if pz == False:
                    $pz = True
                    if rz>=10:
                        show snkw happy with fade
                        snkw "Что тебе, мой программист?"
                        anon "Здравствуйте! {w} Мне бы узнать про Пахомова Д.А. Хочу с ним подготовить проект на СНО про историю процессоров!"
                        snkw "Какие вы молодцы!{w} Вы оба славные программисты!{w} Я так рада, что ты с ним будешь в паре! Он славный философ, программист!"
                        snkw "Творец, не профессионал!"
                        "Полезно, пиздец, погнали дальше."
                        anon "Я тогда пойду его искать, до свидания!"
                        snkw "На СНО жду от вас синквейн!"
                        "Да ты ёбнутая."
                        anon "Хорошо."
                        hide snkw happy
                        jump poll
                    else:
                        show snkw boom with fade
                        snkw "Что тебе надо, киник?!"
                        anon "Здрасте! {w} Мне бы про Пахомо..."
                        snkw "Что тебе надо от этого замечательного человека, мразь! {w} Не то, что тебя, киника, урода, ублюдка!"
                        anon "Да просто узнать, где он жи..."
                        snkw "Пошёл вон!"
                        "Ну нахуй тогда..."
                        hide snkw boom
                        jump poll
                else:
                    "Бля, тут никого нет, да и спрашивал я её."
                    jump poll

            "Дирик":
                jump dirpoll

            "Маркович":
                if pm == False:
                    $pm = True
                    scene bg table4 with fade
                    show general with dissolve
                    general "Чего тебе, э!"
                    anon "Мне бы про Пахома узнать, кто он?"
                    if rm>=0:
                        general "Он истинный патриот! Настоящий солдат нашей Родины! Поддерживает Путина и Армию!"
                        anon "А где он живет?"
                        general "Этого я не знаю."
                        "Сука, полезно!"
                        jump poll
                    else:
                        general "Пшёл вон отсюда!"
                        "Окей..."
                        jump poll
                else:
                    #scene bg marsleep with fade
                    "Лол."
                    anon "РОТА, ПОДЪЕМ"
                    general "Э...Хррррррр...{w} Дай поспать....{w}Хррррррр..."
                    "Ладно, это было жестко."
                    jump poll

            "НН":
                scene bg nn with fade
                show nn with fade
                if pn == False:
                    anon "Здравствуйте. Можно ли у вас узнать про Пахома?"
                    $pn = True
                    if rn>=0:
                        nn "Конечно. Он странный какой-то."
                        nn "Когда я дала задание сделать интернет-магазин, он сделал сайт про Кольскую сверхглубокую скважину. {w} Он его потом попросил скинуть на дискету и отправить Почтой России в посёлок Чаща.{w} Больше ничего не знаю, он поехавший какой-то."
                        anon "Спасибо!"
                        "Хоть зацепка нормальная..."
                        hide nn
                        jump poll
                    else:
                        nn "Иди отсюда!{w} Почему ты плохие вещи пишешь в Подслушано?"
                        "Ой, иди нахуй."
                        jump poll
                else:
                    if rn>=0:
                        nn "Я сказала, что знала."
                        hide nn
                        jump poll
                    else:
                        nn "Я занята, иди отсюда!"
                        hide nn
                        jump poll

            "Бахильник":
                scene bg bahilass with fade
                if pb == False:
                    $pb = True
                    show bahilass
                    "Спрашивать бахильник, дожили."
                    anon "Бахильник, здорова!{w} Что ты знаешь про Пахома?"
                    if rub == True:
                        bahil "Дороу. {w}Забыл уже? Микроволновки защищают от излучения Кольской сверхглубокой! {w} А ещё я слышал, что Пахом управляет Кольской сверхглубокой и хочет запустить Кольскую сверхвысокую для загыебачивания всего мира!"
                        anon "Спасибо!"
                        bahil "Обращайся."
                        "Я просто сошел с ума и меня загыебатили."
                        hide bahilass
                        jump poll
                    else:
                        bahil "Иди нахуй."
                        anon "Сам иди нахуй!"
                        kits "Ты поехавший?"
                        anon "И ты иди нахуй."
                        hide bahilass
                        jump poll
                else:
                    anon "Бахильник!"
                    anon "Эй, блять!"
                    "Спит чтоли? Ну и хуй с ним"
                    jump poll

            "Шавлюга":
                "Пошли к Шавлюге!"
                scene bg sport with fade
                $mp("sport")
                show delite
                anon "Здравствуйте!"
                if psh == False:
                    $psh = True
                    delite "Привет, чего тебе?"
                    anon "Я хочу узнать про Пахома."
                    if rsh>=5:
                        delite "А я знаю про Пахома! Но я хочу за это награду."
                        anon "Какую?"
                        delite "Я хочу, чтобы ты выебал меня, как последнюю шлюху!"
                        "Ну хули делать..."
                        hide delite
                        scene bg delite sex with fade
                        $mp("xxx")
                        pause 10.0
                        anon "О даааааа!"
                        stop music
                        scene bg sport with fade
                        $mp("sport")
                        show delite
                        anon "Так что там про Пахома?"
                        delite "А, аххх. {w} Точно. Он ко мне на пары не приходил, неспортивный он. {w}Ты его с легкостью победишь, зая."
                        "Ебать полезно! Но зато поебался."
                        anon "Я пойду тогда, пока."
                        delite "Пока, милый!"
                        #Звук поцелуя
                        hide delite
                        jump poll
                    else:
                        delite "Ничего не знаю."
                        anon "Ладно..."
                        hide delite
                        jump poll
                else:
                    if rsh>=5:
                        if ebony <3:
                            $ebony +=1
                            delite "Привет, родной!{w} Повторим?"
                            anon "Да!"
                            hide delite
                            scene bg delite sex with fade
                            $mp("xxx")
                            pause 10.0
                            anon "О даааааа, детка!"
                            stop music
                            scene bg sport with fade
                            $mp("sport")
                            show delite
                            hide delite
                            jump poll
                        else:
                            scene bg delite sex with fade
                            $mp("xxx")
                            anon "Уааааааааааа...."
                            scene black with fade
                            $sp ("gta")
                            centered "Вы умерли от обезвоживания."
                            return
                    else:
                        delite "Убирайся отсюда!"
                        hide delite
                        jump poll
