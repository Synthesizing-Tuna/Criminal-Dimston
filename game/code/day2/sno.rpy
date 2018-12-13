#Столовка
label eat:
    $mp ("table")
    show bg table2 with fade
    "Сука, макароны с лобковыми волосами!"
    "Заебало уже!"
    show bg table3 with dissolve
    show snkw happy
    snkw "Ребята, на следующей паре у нас СНО!{w} Ждём вас всех!"
    if rz>=0:
        snkw "[anon], я тебя особенно жду, мой программист!"
    else:
        snkw "[anon], не придёшь, я скажу директору!"
    "Блядское СНО!{w} Заебало уже нахуй."
    "Может, свалить? А то потом не выпустят."
    menu:
        "Валим?"
        "Да":
            $rz -=10
            "Да, точно, надо отсюда валить. Надеюсь, Маркович ещё не успел встать."
            stop music
            scene bg door with fade
            show general
            $cp("general")
            "Блять, встал, как теперь выйти?"
            anon "А можно выйти покурить?"
            if rm>=1:
                general "Да, конечно, проходи."
                kit "Эй, как он выше..."
                "Вот это да.{w} Из этого следует мудрая мысль - перед Марковичем надо покупать бахилы."
                stop music
                jump homeday2
            else:
                general "Э!{w} Нет! Не выпущу!{w} Пошёл на СНО!"
                "Надеюсь, Захарка не видела..."
                stop music
                $mp ("noice")
                if rz>=-10:
                    $sp("suddenly")
                    show snkw boom at left with moveinright
                    snkw "Ах ты киник! Я тебе верила, а ты меня предал!{w} Мразь!{w} Урод!{w} Сволочь!{w} Ублюдок!{w} Разве я заслужила такого отношения?"
                    "Вспомнишь говно, вот и оно.{w} Теперь ещё и испортил отношения с Захаркой. Ну йобана.{w} И всё равно идти на СНО..."
                    jump sno
                else:
                    "Блять, Захарка идёт, лучше на СНО пойду, пока она не увидела, а то к дирику поведёт."
                    $sp("suddenly")
                    show snkw boom at right with moveinright
                    show pidor at left with moveinleft
                    snkw "Свалить хотел?"
                    pidor "Отвечай!"
                    anon "Я на СНО шёл! Я просто был в столовой, сами видели!"
                    snkw "Ну хорошо. Но если свалишь - пеняй на себя!"
                    pidor "Отчислю тебя!"
                    "Ох, сколько я уже должен быть отчислен..."
                    scene black
                    centered "Через 10 минут."
                    jump sno
        "Нет":
            "Потушу пердак. Вдруг Маркович не выпустит или Захарка заметит.{w} Узнал бы раньше..."
            stop music
            jump sno

#СНО
label sno:
    scene bg akt with fade
    show snkw happy
    snkw "Здравствуйте, дорогие студенты!{w} Рада приветствовать вас на 13 ежегодном межгалактическом студентческом обществе!"
    $ sp ("cotton")
    snkw "Представляю вам Алексея Гусельникова, выпускника нашего колледжа!{w} Он стал рок-звездой и руководит группой Yeblo!"
    goose "Yllo!"
    snkw "Прости меня, зайчик! Да, группа Yllo, аплодисменты!"
    stop sound
    menu:
        "Валим?"
        "Да":
            $rz =-5
            "Ну нахуй это ебучее СНО и ебучего гуся."
            jump hardhome
        "Нет":
            play movie "videos/nepman.webm"
            $renpy.pause(10, hard=True)
            pause 10
            stop movie
            snkw "Отличное выступление! Следующий - Русская Зима!"
            $ sp ("cotton")
            "Бляяять, мне уже гуся хватило... Может всё же свалить?"
            stop sound
            menu:
                "Валим?"
                "Да":
                    $rz =-3
                    "Ну нахуй это ебучее СНО и ебучую русскую зиму!"
                    jump hardhome
                "Нет":
                    play movie "videos/russian_winter.webm"
                    $renpy.pause(10, hard=True)
                    pause 10
                    stop movie
                    $ sp ("cotton")
                    snkw "Это было замечательно!{w} Хорошее выступление!"
                    snkw "И последнее - МС Кит! Хороший репер, уважающий наше заведение!"
                    stop sound
                    menu:
                        "Может сейчас валить?"
                        "Да":
                            "Я просто уже в ахуе, нахуй надо. {w}Валить, только валить!"
                            jump hardhome
                        "Нет":
                            play movie "videos/rap.webm"
                            $renpy.pause(10, hard=True)
                            pause 10
                            stop movie
                            "Ох, ну и СНО... Надеюсь, это всё?"
                            $ sp ("call")
                            $rz=+5
                            snkw "На этом 13 ежегодное межгалактическое СНО закончена! Всем спасибо!"
                            $ sp ("cotton")
                            "Я выдержал, охуеть!"
                            "Ладно, ну нахер, надо идти домой."
                            stop sound
                            jump easyhome
#Свалинг домой с шарадами
label hardhome:
    scene bg door with dissolve
    "Хорошо, что никого в гардеробе не было, изи куртку взял."
    show general
    $cp ("general")
    general "Э!{w} Куда пошёл?"
    anon "Домой."
    if rm>=1:
        general "Ладно, иди! Только тихо, э!"
        anon "Спасибо!"
        stop music
        jump homeday2
    else:
        general "Выпущу, если отгадаешь мои загадки!"
        "О, шарады я последнее время полюбил."
        anon "Давайте."
        general "Какой самый известный самолёт на тихоокеанском театре военных действий?"
        menu:
            "Тигр":
                general "Идиот, блядь.{w} Скотина блядь.{w} Это знать надо, если ты учился в шестом училище!{w} Это классика, блядь!"
                general "Чай неси!"
                "Похоже, не знаю я этих шарад. Ладно, пойду чай принесу."
                stop music
                $mp("table")
                scene bg table2 with dissolve
                "О!{w} Спизжу этот чай!"
                kit "Чай сука спиздили!"
                scene bg door with dissolve
                stop music
                $cp ("general")
                show general
                anon "Вот!"
                general "Ладно, проходи. Марш отсюда!"
                "С радостью!"
                stop music
                jump homeday2
            "Американский В29 и японский Zero":
                $rm +=5
                general "Правильно.{w} Проходи"
                "Это было просто. Ну и хорошо, норм способ свалить домой."
                stop music
                jump homeday2
            "Тандерболт":
                general "Отец твой тандерболт, а мамка твоя лайтнинг. Не правильно! Это знать надо!"
                general "Постоишь, не развалишься."
                $renpy.pause(20, hard=True)
                stop music
                $ sp ("call")
                general "Все, иди уже."
                anon "Спасибо."
                jump homeday2

#Легкий свалинг домой без загадок
label easyhome:
    scene bg grdr with fade
    $("noice")
    "Ну и ебучее это СНО было!{w} То Гусь, то русская зима, то репер! Да я лучше реп зачитаю!"
    "Ну ладно, хоть Захарку не обидил."
    if rz>=0:
        "И даже улучшил отношение!"
    scene bg door with dissolve
    "Прощай, шарага ебанная! Я иду домой нахуй."
    jump homeday2
