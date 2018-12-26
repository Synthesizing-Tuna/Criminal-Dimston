init python:
    def mp(mname, fin=0, fout=0.5):
        renpy.play("sounds/music/" + mname + ".mp3", channel="music", loop=True, fadein=fin, fadeout=fout)
    def sp(mname, fin=0, fout=0):
        renpy.play("sounds/sound/" + mname + ".mp3", channel="sound", loop=False, fadein=fin, fadeout=fout)
    def cp(mname, fin=0, fout=0):
        renpy.play("sounds/music/characters/" + mname + ".mp3", channel="music", loop=True, fadein=fin, fadeout=fout)

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # Устанавливает постепенное появление и исчезновение бара и требуется только один раз в скрипте

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.7 xmaximum 300 at alpha_dissolve

init:
    $ timer_range = 0
    $ timer_jump = 0

#Бекграунды

#Начало
image bg molotok = "posters/poster1.jpg"

#Столовка
image bg dream = "bg/bahil_factory.jpg"
image bg table = "bg/hell_1.png"
image bg table2 = "bg/hell_2.png"
image bg table3 = "bg/hell_3.jpg"
image bg table4 = "bg/hell_4.png"
image bg table5 = "bg/hell_5.jpg"

#Улица
image bg parking = "bg/solaris_1.png"
image bg zagrebsky = "bg/zagrebsky.png"
image bg solarisbk = "bg/solaris_2.png"
image bg moonkit = "bg/moon_kit.png"
image bg moonkupchino = "bg/moon_kupchino.png"
image bg mkupchino = "bg/metro_enter.png"
image bg train snkw = "bg/metro.jpg"
image bg mdybenko = "bg/dybenko.jpg"
image bg pidor = "bg/graffity.png"
image bg dirrail = "bg/rail.png"

#кит
image bg grdr = "bg/wardrobe_1.jpg"
image bg door = "bg/kordon.png"
image bg kabdir = "bg/kabdir.png"
image bg sofa = "bg/sofa.png"
image bg nn = "bg/408.png"
image bg zapor = "bg/wstair_1.jpg"
#image bg stairs = ""
#image bg fourhall = ""
image bg firestairs = "bg/fire.jpg"
image bg grdrnokits = "bg/wardrobe_2.png"
image bg bahilass = "bg/bahil_1.png"
image bg kab302 = "bg/kab302.png"
image bg floor3 = "bg/floor3.png"
image bg ceilingcrash = "bg/ceilingcrash.jpg"
image bg sport = "bg/sport.png"
image bg akt = "bg/akt.png"
image bg pahom = "bg/pahom.jpg"
image bg foma = "bg/seva.jpg"
image bg corridor = "bg/corridor.jpg"
#image bg marsleep = "bg/sleep.jpg"

#БК
image bg bk = "bg/bk.jpg"
image bg dirsber = "bg/sberbank.jpg"

#Дом
image bg kitchen = "bg/kitchen_night.JPG"
image bg room = "bg/home_night.png"
image bg morning = "bg/alarm.png"

#Скрины экрана
image bg moodle1 = "bg/moodle_1.jpg"
image bg moodle2 = "bg/moodle_2.jpg"
image bg yasmi = "bg/yandex.png"
image bg kolsk1 = "bg/kolsk_proof_1.jpg"
image bg kolsk2 = "bg/kolsk_proof_2.jpg"
image bg kolsk3 = "bg/kolsk_proof_3.jpg"
image bg kolsk4 = "bg/kolsk_proof_4.jpg"
image bg kolskalt1 = "bg/kolsk_proof_alt1.jpg"
image bg kolskalt2 = "bg/kolsk_proof_alt2.jpg"


#Изображения персонажей

#Пахомы
image dp10 dream = "characters/dp/hitler.png"
image dp10 = "characters/dp/idle.png"

#Захарка
image snkw boom = "characters/zaharka/angry.png"
image snkw happy = "characters/zaharka/idle.png"
image snkw box = "characters/zaharka/box_closed.png"
image snkw boxopen = "characters/zaharka/box_open.png"
image snkw ball = "characters/zaharka/ball.png"
image snkw akbar = "characters/zaharka/very_angry.png"

#Пидор дирик
image pidor = "characters/pidor/idle.png"

#Маркович
image general = "characters/markovich/idle.png"

#Локалхост
image nn = "characters/nn/idle.png"

#Рустэм
image zver = "characters/rustam/idle.png"

#Бахильник
image bahil = "characters/staff/bahil.png"
image bahilass = "characters/staff/bahil_alive.png"

#ТЕЛЕВИЗОР, ДА
image tv anim = Animation("characters/news/spb.png", 1.5,
                        "characters/news/ny.png", 1.5,
                        "characters/news/paris.png", 1.5,
                        "characters/news/sidney.png", 1.5,
                        "characters/news/msk.png", 1.5,
                        "characters/news/toronto.png", 1.5)
image tv kisel = "characters/news/kisel.png"
image tv off = "characters/news/tv_off.png"

#Фома
image foma = "characters/foma/barrel.png"

#Шавлюга
image delite = "characters/delite/idle.png"
image delite xxx = "characters/delite/xxx.png"
image bg delite sex = "bg/shavluga_sex.jpg"

#Конус
image con = "characters/staff/conidle.png"
image con shit = "characters/staff/conshit.png"


#Определение персонажей игры.
define anon = Character("[anon]", color="#c8ffc8")
define dp10 = Character('Пахомов ДП-10', color="#ff0000")
define snkw = Character('Захарова', color="#F7D3E9")
define hz = Character('???')
define kit = Character('Какой-то китёнок')
define kits = Character('Китята')
define pidor = Character('Ильин В.И.')
define bk = Character('Работник БК')
define general = Character('Гвардии-майор Борис Маркович')
define nn = Character('Наталья Николаевна')
define zver = Character('Рустэм')
define bahil = Character('Бахильник')
define sber = Character('Работник Сбера')
define medkit = Character('Медсестра КИТа')
define human = Character('Неизвестный человек')
define mom = Character('Мама')
define dad = Character('Папа')
define TV = Character('Телек')
define foma = Character('Фомин')
define delite = Character('Шавлюга')
define con = Character('Конус')
define goose = Character('Гусельников')
define table = Character('Буфетчица')

#Счётчики
define rz = 0 #Увожение Захаровой
define rp = 0 #Увожение пидора
define rn = 0 #Увожение локалхоста
define rm = 0 #Увожение марковича
define rsh = 0 #Увожение шавлюги
define rf = 0 #Увожение фомы
define pidorsber = False #Видел ли анон пидора в сбере, только в первом дне, выводит в отчисление
define smenka = False #Сдавал ли ты сменку, важно для Марковича
define cellyou = False #Дал свой номер захарке
define cellparents = False #Дал номер родаков захарке
define rub = False #В бахильник загрузил 5 рублей - трулио получил
define hardmoodle = False #Разозлил захарку - труднее сдать мудл
define moodle = 0 #Счетчик мудла, зависит оценка
define dop = 0 #Счетчик составления синквейна
define cons = False #Не надо садиться на конус, будет подсказка
define medic = False #Медик тоже в курсе
define ebony = 0 #Сколько раз ебали шавлюгу, когда был опрос Пахома

#Счетчик опроса
define  pz= False #ответ Захаровой
define  pb= False #ответ бахильника
define  pn= False #ответ локалхоста
define  pm= False #ответ марковича
define  psh= False #ответ шавлюги
define  pf= False #ответ фомы
