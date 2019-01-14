label chasha:
    scene black with fade
    centered "И засели мы в электрон..."
    "Ну почему мне везёт на пидора?"
    scene bg electron1 with fade
    "Хочется приключений? {w} Доебаться до дирика бы надо..."
    menu:
        "Доебемся?"
        "Да":
            jump electron_d
        "Да пошёл он нахуй, уйду в другой вагон":
            #block of code to run

    return
