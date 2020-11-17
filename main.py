# This program for choosing a movie according to your wishes
# Developer:   Turchinovich Maria

years = input ('Вы хотите фильмы до или после 2000 года?\n')
# film selection up to 2000
if (years.lower() == 'до') or (years.lower() == 'до 2000') or (years.lower() == 'до 2000 года'):
    genre = input ('Какой жанр вы хотите посмотреть (комедию, мелодраму, детектив, боевик, фантастику)?\n')
    if genre.lower() == 'комедию' or genre.lower() == 'комедия':  #comedy selection
        film_1 = input ('Смотрели ли вы фильм "Один дома" (да или нет)?\n')
        if film_1.lower() == 'нет':
            print ('Посмотрите фильм "Один дома"')
        else:
            film_2 = input ('Смотрели ли вы фильм "Тупой и ещё тупее" (да или нет)?\n')
            if film_2.lower() == 'нет':
                print ('Посмотрите фильм "Тупой и ещё тупее"')
            else:
                print ('К сожалению, нам нечего Вам посоветовать.')
    elif genre.lower() == 'мелодраму' or genre.lower() == 'мелодрама':  #choice of melodrama
        film_1 = input ('Смотрели ли вы фильм "Титаник" (да или нет)?\n')
        if film_1.lower() == 'нет':
            print('Посмотрите фильм "Титаник"')
        else:
            film_2 = input ('Смотрели ли вы фильм "Красотка" (да или нет)?\n')
            if film_2.lower() == 'нет':
                print('Посмотрите фильм "Красотка"')
            else:
                print('К сожалению, нам нечего Вам посоветовать.')
    elif genre.lower() == 'детектив':  #detective's choice
        film_1 = input ('Смотрели ли вы фильм "Шерлок Холмс" (да или нет)?\n')
        if film_1.lower() == 'нет':
            print('Посмотрите фильм "Шерлок Холмс"')
        else:
            film_2 = input ('Смотрели ли вы фильм "Подозрительные лица" (да или нет)?\n')
            if film_2.lower() == 'нет':
                print('Посмотрите фильм "Подозрительные лица"')
            else:
                print('К сожалению, нам нечего Вам посоветовать.')
    elif genre.lower() == 'боевик':  #action movie choice
        film_1 = input ('Смотрели ли вы фильм "Трудная мишень" (да или нет)?\n')
        if film_1.lower() == 'нет':
            print('Посмотрите фильм "Трудная мишень"')
        else:
            film_2 = input ('Смотрели ли вы фильм "Отчаянный" (да или нет)?\n')
            if film_2.lower() == 'нет':
                print('Посмотрите фильм "Отчаянный"')
            else:
                print('К сожалению, нам нечего Вам посоветовать.')
    elif (genre.lower() == 'фантастику') or (genre.lower() == 'фантастика'):  #selection of fiction
        film_1 = input ('Смотрели ли вы фильм "Люди в чёрном" (да или нет)?\n')
        if film_1.lower() == 'нет':
            print('Посмотрите фильм "Люди в чёрном"')
        else:
            film_2 = input ('Смотрели ли вы фильм "Звездные войны: Эпизод 1" (да или нет)?\n')
            if film_2.lower() == 'нет':
                print('Посмотрите фильм "Звездные войны: Эпизод 1"')
            else:
                print('К сожалению, нам нечего Вам посоветовать.')

# movie choice after 2000
else:
    genre_after = input ('Какой жанр вы хотите посмотреть (комедию, мелодраму, детектив, боевик, фантастику)?\n')
    if genre_after.lower() == 'комедию' or genre_after.lower() == 'комедия':  #comedy selection
        film_1 = input ('Смотрели ли вы фильм "Холоп" (да или нет)?\n')
        if film_1.lower() == 'нет':
            print ('Посмотрите фильм "Холоп"')
        else:
            film_2 = input ('Смотрели ли вы фильм "Отпетые мошенницы" (да или нет)?\n')
            if film_2.lower() == 'нет':
                print ('Посмотрите фильм "Отпетые мошенницы"')
            else:
                print ('К сожалению, нам нечего Вам посоветовать.')
    elif genre_after.lower() == 'мелодраму' or genre_after.lower() == 'мелодрама':  #choice of melodrama
        film_1 = input ('Смотрели ли вы фильм "Ла-Ла Ленд" (да или нет)?\n')
        if film_1.lower() == 'нет':
            print('Посмотрите фильм "Ла-Ла Ленд"')
        else:
            film_2 = input ('Смотрели ли вы фильм "После" (да или нет)?\n')
            if film_2.lower() == 'нет':
                print('Посмотрите фильм "После"')
            else:
                print('К сожалению, нам нечего Вам посоветовать.')
    elif genre_after.lower() == 'детектив':  #detective's choice
        film_1 = input ('Смотрели ли вы фильм "Загадочное убийство" (да или нет)?\n')
        if film_1.lower() == 'нет':
            print('Посмотрите фильм "Загадочное убийство"')
        else:
            film_2 = input ('Смотрели ли вы фильм "Достать ножи" (да или нет)?\n')
            if film_2.lower() == 'нет':
                print('Посмотрите фильм "Достать ножи"')
            else:
                print('К сожалению, нам нечего Вам посоветовать.')
    elif genre_after.lower() == 'боевик':  #action movie choice
        film_1 = input ('Смотрели ли вы фильм "Мистер и миссис Смит" (да или нет)?\n')
        if film_1.lower() == 'нет':
            print('Посмотрите фильм "Мистер и миссис Смит"')
        else:
            film_2 = input ('Смотрели ли вы фильм "Шпион" (да или нет)?\n')
            if film_2.lower() == 'нет':
                print('Посмотрите фильм "Шпион"')
            else:
                print('К сожалению, нам нечего Вам посоветовать.')
    elif (genre_after.lower() == 'фантастику') or (genre_after.lower() == 'фантастика'):  #selection of fiction
        film_1 = input ('Смотрели ли вы фильм "Аватар" (да или нет)?\n')
        if film_1.lower() == 'нет':
            print('Посмотрите фильм "Аватар"')
        else:
            film_2 = input ('Смотрели ли вы фильм "Мстители: Финал" (да или нет)?\n')
            if film_2.lower() == 'нет':
                print('Посмотрите фильм "Мстители: Финал"')
            else:
                print('К сожалению, нам нечего Вам посоветовать.')