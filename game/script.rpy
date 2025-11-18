# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define petr = Character('Петя', color='#007bff')
define maxim = Character('Макс', color='#1c6f00')
define elena = Character('Лена', color='#ff1e7f')
define denis = Character('Денис', color='#44009d')
define irina = Character('Ирина', color='#eb3a3a')
define maria = Character('Маша', color='#ffa544')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Переменные

define balance = 0
define frontend = 0
define backend = 0

# Игра начинается здесь:
label start:

    scene scene_prev
    with fade

    show petr

    "Это Петя, он только закончил бакалавриат по направлению программная инженерия в Уральском Федеральном и каким-то чудом его взяли стажером в Яндекс. Петя очень рад!"

    jump scene_1

label scene_1:

    scene scene_1
    with fade

    show maxim
    maxim "Новый день — новый код. Привет, Петя. Готов стать full stack разработчиком?"
    hide maxim

    show petr
    petr "Если честно, я до конца не понимаю, чем именно он занимается…"
    hide petr

    show maxim
    maxim "Значит, будешь понимать и фронт, и бэк. То, что видит пользователь, и то, что остается за сценой."
    hide maxim

    show petr
    petr "Как дирижёр в оркестре?"
    hide petr

    show maxim
    maxim "Ну типо того. Только вместо музыкантов — баги, дедлайны и бесконечные билды."
    hide maxim

    show petr
    petr "Звучит круто! Правда немного страшно от неизвестности..."
    hide petr

    show maxim
    maxim "Поверь мне - будет интересно!"
    menu:
        maxim "Готов начать свой путь в fullstack разработку?"
        "Конечно!":
            menu:
                "С чего хочешь начать?"
                "Хочу видеть всю систему целиком.":
                    $ balance += 1
                    jump scene_2
                "Начну с интерфейса, люблю визуальную часть.":
                    $ frontend += 1
                    jump scene_2
                "Хочу ковыряться в логике и данных.":
                    $ backend += 1
                    jump scene_2
        "Что-то уже расхотелось...":
            jump scene_whynot

label scene_whynot:

    show maxim
    maxim "Петя, ну так дела не делаются. Мы же взяли тебя на стажировку, мы верим в тебя"
    hide maxim

    show petr
    petr "Да, действительно, что-то я немного растроился. Давайте работать!"
    hide petr

    show maxim
    menu:
        maxim "С чего хочешь начать?"
        "Хочу видеть всю систему целиком.":
            $ balance += 1
            jump scene_2
        "Начну с интерфейса, люблю визуальную часть.":
            $ frontend += 1
            jump scene_2
        "Хочу ковыряться в логике и данных.":
            $ backend += 1
            jump scene_2

label scene_2:

    scene scene_2
    with fade

    show elena    
    elena "Ты Петя? Ну, добро пожаловать в мир пикселей и вечной борьбы с CSS."
    hide elena
    
    show petr
    petr "Красиво выглядит. Это React?"
    hide petr

    show elena
    elena "Да, и ещё несколько важных библиотек. Но главное — UX. Пользователь не должен задумываться, как всё работает."

    menu:
        elena "Что для тебя важно?"
        "Важен баланс: и удобно, и надежно.":
            $ balance += 1
            jump scene_3
        "Хочу, чтобы интерфейс вызывал восторг.":
            $ frontend += 1
            elena "Тогда запомни: фронтенд — это не только верстка, это коммуникация с пользователем."
            jump scene_3
        "Главное, чтобы всё работало стабильно.":
            $ backend += 1
            jump scene_3

    return


label scene_3:

    scene scene_3
    with fade

    show denis
    denis "Тихо. Сервер думает..."
    hide denis

    show petr
    petr "Он что, живой?"
    hide petr

    show denis
    denis "Конечно живой, а ты как думал! Здесь мы пишем наши проекты на Node.js, для базы данных используем PostgreSQL. Стабильность, безопасность, четкие API."
    
    menu:
        denis "Что тебе по душе?"
        "Мне важно понимать весь путь данных: от клика до базы данных.":
            $ balance += 1
            denis "Хорошо сказано. Настоящий full stack разработчик должен видеть связи, а не только код."
            jump scene_4
        "Интересно, как потом это показывается пользователю.":
            $ frontend += 1
            jump scene_4
        "Хочу понять, как данные текут по системе.":
            $ backend += 1
            jump scene_4


label scene_4:

    scene scene_4
    with fade

    show maxim
    maxim "Нужно реализовать регистрацию. Лена делает форму, Денис — базу с пользователями. Ты связываешь всё это."
    hide maxim

    show elena
    elena "Вот мокап формы. Сделай, чтобы при нажатии “Отправить” всё шло на сервер."
    hide elena

    show denis
    denis "И чтобы сервер не упал, как в прошлый раз."
    hide denis

    show maxim
    menu:
        maxim "Что будешь делать?"
        "Сделаю схему: фронт → сервер → база.":
            $ balance += 1
            maxim "Вот и отличия между “кодером” и “инженером”: первый пишет, второй — понимает."
            jump scene_5
        "Добавлю плавные переходы и валидацию на фронте.":
            $ frontend += 1
            jump scene_5
        "Сначала протестирую API-запрос.":
            $ backend += 1
            jump scene_5


label scene_5:

    scene scene_5
    with fade

    show petr
    petr "Почему сервер не принимает запрос?!"
    hide petr

    show elena
    elena "Ты случайно не забыл поставить Content-Type?"
    hide elena

    show denis
    denis "И не перепутал метод GET и POST?"
    hide denis

    show maxim
    menu:
        maxim "Что будешь делать?"
        "Сверю формат JSON между клиентом и сервером.":
            $ balance += 1
            maxim "Отлично! Видишь? Ошибки — это инструмент, не враг."
            jump scene_6
        "Посмотрю, правильно ли форма отправляет данные.":
            $ frontend += 1
            maxim "Отлично! Видишь? Ошибки — это инструмент, не враг."
            jump scene_6
        "Проверю логи сервера и сетевой трафик.":
            $ backend += 1
            maxim "Отлично! Видишь? Ошибки — это инструмент, не враг."
            jump scene_6


label scene_6:

    scene scene_6
    with fade

    show irina
    irina "Клиенты хотят загружать видео напрямую. Что будем делать?"
    hide irina

    show elena
    elena "Вставим плеер YouTube — просто и быстро."
    hide elena

    show denis
    denis "Нет, внешние ссылки ломаются. Надо хранить у себя."
    hide denis

        
    show maxim
    menu:
        maxim "Петя, а ты как думаешь?"
        "Разделим: фронт, API, CDN, S3 — чтобы система масштабировалась.":
            $ balance += 1
            maxim "Мудро. С архитектурой спешить нельзя, а то потом будет больно."
            jump scene_7
        "Главное, чтобы пользователям было удобно.":
            $ frontend += 1
            jump scene_7
        "Сделаем надёжное файловое хранилище.":
            $ backend += 1
            jump scene_7


label scene_7:

    scene scene_7
    with fade

    show maria
    maria "В Safari падает регистрация!"
    hide maria

    show elena
    elena "Опять CORS?"
    hide elena

    show petr
    petr "В Chrome всё работает…"
    hide petr

    show maria
    menu:
        maria "Что будешь делать?"
        "Сравню заголовки — у нас расхождение.":
            $ balance += 1
            maria "Отлично, ты не паникуешь. Из тебя выйдет толковый инженер."
            jump scene_8
        "Проверю, как фронт делает запросы.":
            $ frontend += 1
            maria "Отлично, ты не паникуешь. Из тебя выйдет толковый инженер."
            jump scene_8
        "Проверю CORS-настройки на сервере.":
            $ backend += 1
            maria "Отлично, ты не паникуешь. Из тебя выйдет толковый инженер."
            jump scene_8


label scene_8:

    scene scene_8
    with fade

    show elena
    elena "Денис опять поменял формат API! Всё сломалось!"
    hide elena

    show denis
    denis "Зато стало правильно."
    hide denis

    show maxim
    maxim "Так, спор потом!"
    menu:
        maxim "Петя, а ты как думаешь?"
        "Создам общую документацию и тесты для API.":
            $ balance += 1
            maxim "Именно. Full stack разработчик часто становится медиатором."
            jump scene_9
        "Сделаем адаптер на фронте, чтобы не зависеть от формата.":
            $ frontend += 1
            jump scene_9
        "Пропишем спецификацию и больше не будем менять без согласования.":
            $ backend += 1
            jump scene_9


label scene_9:

    scene scene_9
    with fade

    show maxim
    maxim "Сейчас самое страшное — выкладывать в прод."
    hide maxim

    show petr
    petr "Что может пойти не так?"
    hide petr

    show elena
    elena "Всё!"
    hide elena

    show maxim
    menu:
        maxim "Что будешь делать?"
        "Сделаю CI/CD, чтобы не повторять это руками.":
            $ balance += 1
            maxim "Запомни: хороший разработчик не боится деплоя. Он всегда готов к нему!"
            jump scene_10
        "Проверю, что сборка фронта работает в проде.":
            $ frontend += 1
            maxim "Запомни: хороший разработчик не боится деплоя. Он всегда готов к нему!"
            jump scene_10
        "Настрою окружение и базы данных.":
            $ backend += 1
            maxim "Запомни: хороший разработчик не боится деплоя. Он всегда готов к нему!"
            jump scene_10


label scene_10:

    scene scene_10
    with fade

    show irina
    irina "Пользователи довольны! Всё работает. Петя, чему научился?"

    if (frontend > backend) & (frontend > balance):
        show petr
        petr "Я понял, что важно думать о людях, а не только о коде. Хороший интерфейс — это мост между пользователем и продуктом."
        hide petr

        show elena
        elena "Добро пожаловать в наш клуб перфекционистов!"
        hide elena

    elif (backend > frontend) & (backend > balance):
        show petr
        petr "Я осознал, что стабильность и логика — основа всего. Фронт можно поменять, но архитектура должна быть прочной."
        hide petr

        show denis
        denis "Тогда ты мой человек!"
        hide denis

    else:
        show petr
        petr "Full stack — это видеть связи. Фронт, бэк, тесты, архитектура — всё часть одной системы."
        hide petr

        show maxim
        maxim "Поздравляю. Ты не просто пишешь код — ты строишь решения."
        hide maxim

    window hide
    scene poster1 with fade
    pause
    "Конец."

    $ persistent.scene_10 = True





    
