# Вы можете расположить сценарий своей игры в этом файле.
#config.gamedir - основная директория игры
init python:
    def send_to_file(filename, text):
        with open(config.gamedir + "/" + filename, "w") as o_w:
            o_w.write(text)
        return
    
    

# Определение персонажей игры.
define gachipunk = Character(color="#000000", what_font = "fonts/SlimamifBold.ttf")
define gachipunk_red = Character(color="#000000", what_font = "fonts/SlimamifBold.ttf", what_color="#ff0000", window_background="gui/textboxpass.jpg")
define audio.start_music = "audio/music/start.mp3"
define audio.glitch1 = "audio/sounds/glitch1.mp3"
define audio.glitch2 = "audio/sounds/glitch2.mp3"
define audio.glitch3 = "audio/sounds/glitch3.mp3"





image 8start:
    "/images/8start/8start_1.jpg"
    pause 0.05
    "/images/8start/8start_2.jpg"
    pause 0.05
    "/images/8start/8start_3.jpg"
    pause 0.05
    "/images/8start/8start_4.jpg"
    pause 0.05
    "/images/8start/8start_5.jpg"
    pause 0.05
    "/images/8start/8start_6.jpg"
    pause 0.05
    "/images/8start/8start_7.jpg"
    pause 0.05
    "/images/8start/8start_8.jpg"
    pause 0.05
    "/images/8start/8start_9.jpg"
    pause 0.05
    "/images/8start/8start_10.jpg"
    pause 0.05
    "/images/8start/8start_11.jpg"
    pause 0.05
    "/images/8start/8start_12.jpg"
    pause 0.05
    "/images/8start/8start_13.jpg"
    pause 0.05
    "/images/8start/8start_14.jpg"
    pause 0.05
    "/images/8start/8start_15.jpg"
    pause 0.05
    "/images/8start/8start_16.jpg"
    pause 0.05
    "/images/8start/8start_17.jpg"
    pause 0.05
    "/images/8start/8start_18.jpg"
    pause 0.05
    "/images/8start/8start_19.jpg"
    pause 0.05
    "/images/8start/8start_20.jpg"
    pause 0.05
    "/images/8start/8start_21.jpg"
    pause 0.05
    "/images/8start/8start_22.jpg"
    pause 0.05
    "/images/8start/8start_23.jpg"
    pause 0.05
    "/images/8start/8start_24.jpg"
    pause 0.05
    repeat

image startbook: #возможно лучше добавить больше кадров
    "/images/startbook/startbook_1.jpg"
    pause 0.05
    "/images/startbook/startbook_2.jpg"
    pause 0.05
    "/images/startbook/startbook_3.jpg"
    pause 0.05
    "/images/startbook/startbook_4.jpg"
    pause 0.05
    "/images/startbook/startbook_5.jpg"
    pause 0.05
    "/images/startbook/startbook_6.jpg"
    pause 0.05
    "/images/startbook/startbook_7.jpg"
    pause 0.05
    "/images/startbook/startbook_8.jpg"
    pause 0.05
    "/images/startbook/startbook_9.jpg"
    pause 0.05
    "/images/startbook/startbook_10.jpg"
    pause 0.05
    "/images/startbook/startbook_11.jpg"
    pause 0.05
    "/images/startbook/startbook_12.jpg"
    pause 0.05
    "/images/startbook/startbook_13.jpg"
    pause 0.05
    repeat

image glitch8:
    "8glitch_1"
    pause 0.05
    "8glitch_2"
    pause 0.05
    "8glitch_3"
    pause 0.05
    "8glitch_4"
    pause 0.05
    "8glitch_5"
    pause 0.05
    "8glitch_6"
    pause 0.05
    "8glitch_7"
    pause 0.3

image glitch8_short:
    "8glitch_1"
    pause 0.05
    "8glitch_2"
    pause 0.05
    "8glitch_3"
    pause 0.05
    "8glitch_4"
    pause 0.05

image firestart:
    "/images/firestart/firestart_1.jpg"
    pause 0.05
    "/images/firestart/firestart_2.jpg"
    pause 0.05
    "/images/firestart/firestart_3.jpg"
    pause 0.05
    "/images/firestart/firestart_4.jpg"
    pause 0.05
    "/images/firestart/firestart_5.jpg"
    pause 0.05
    "/images/firestart/firestart_6.jpg"
    pause 0.05
    "/images/firestart/firestart_7.jpg"
    pause 0.05
    "/images/firestart/firestart_8.jpg"
    pause 0.05
    "/images/firestart/firestart_9.jpg"
    pause 0.05
    "/images/firestart/firestart_10.jpg"
    pause 0.05
    "/images/firestart/firestart_11.jpg"
    pause 0.05
    "/images/firestart/firestart_12.jpg"
    pause 0.05
    "/images/firestart/firestart_13.jpg"
    pause 0.05
    "/images/firestart/firestart_14.jpg"
    pause 0.05
    "/images/firestart/firestart_15.jpg"
    pause 0.05
    repeat

image startukrop:
    "images/startukrop/startukrop_1.jpg"
    pause 0.05
    "images/startukrop/startukrop_2.jpg"
    pause 0.05
    "images/startukrop/startukrop_3.jpg"
    pause 0.05
    "images/startukrop/startukrop_4.jpg"
    pause 0.05
    "images/startukrop/startukrop_5.jpg"
    pause 0.05
    "images/startukrop/startukrop_6.jpg"
    pause 0.05
    "images/startukrop/startukrop_7.jpg"
    pause 0.05
    "images/startukrop/startukrop_8.jpg"
    pause 0.05
    "images/startukrop/startukrop_9.jpg"
    pause 0.05
    "images/startukrop/startukrop_10.jpg"
    pause 0.05
    "images/startukrop/startukrop_11.jpg"
    pause 0.05
    "images/startukrop/startukrop_12.jpg"
    pause 0.05
    "images/startukrop/startukrop_13.jpg"
    pause 0.05
    "images/startukrop/startukrop_14.jpg"
    pause 0.05
    "images/startukrop/startukrop_15.jpg"
    pause 0.05
    "images/startukrop/startukrop_16.jpg"
    pause 0.05
    "images/startukrop/startukrop_17.jpg"
    pause 0.05
    "images/startukrop/startukrop_18.jpg"
    pause 0.05
    repeat


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    $ style.say_window = style.window_CUSTOM #активировал первое диалоговое окно
    hide window
    show window
    

    scene black
    

    gachipunk  "{cps=30}Всем привет! {w=1} С вами Гачипанк Димитрик. {w=2} Вы позволите мне протянуть чуть дольше? {/cps}"

    scene start with fade
    play music start_music

    gachipunk  "{cps=30} Всё закончилось... {w=1} грустно. {w=1} И я не знаю, что меня держит. {w=1} Но я знаю, что вы не реальны. {w=2} Или не реален я.{/cps}"
    gachipunk "{cps=30} Это не важно. {w=1} Важно лишь то, что мне до сих пор больно. {w=1} Я достиг своего конца{w=0.5}.{w=0.5}.{w=0.5}. {w} Я достиг своей грани.{w} И только здесь я испытываю что-то кроме боли. {/cps}"
    play sound glitch1
    show 8start
    gachipunk_red "##{nw}" #сделать небольшой глитч текстбокса
    gachipunk "{cps=30}Потому я вас прошу... {w=1} Не закрывайте окно. {w=1} Пожалуйста{w=0.5}.{w=0.5}.{w=0.5}.{/cps}"
    gachipunk "{cps=20} Не закрывайте мою игру разума.{/cps}"
    gachipunk_red "##{nw}"
    
    scene start2
    play sound glitch2
    show glitch8
    pause(0.6)
    hide glitch8
    show firestart
    gachipunk_red "##{nw}"
    gachipunk "{cps=30} Возможно вы здесь за ответами.{/cps}"
    hide firestart
    play sound glitch2
    show glitch8
    pause(0.6)
    hide glitch8
    show startbook
    gachipunk_red "##{nw}"
    gachipunk "{cps=20} Возможно за вопросами.{/cps}"
    hide startbook
    play sound glitch3
    show glitch8_short
    pause(0.3)
    hide glitch8_short
    show startukrop
    gachipunk_red "{cps=200}Ж упчъ п фл фънлф ё{/cps}{nw}" #сунуть глючный текстбокс до конца
    gachipunk "{cps=30} Ведь вам любопытно. {w=1} Тогда не забывайте сохраняться.{/cps}"
    play sound glitch3
    show glitch8_short
    pause(0.3)
    hide glitch8_short
    show startukrop
    gachipunk_red "{cps=200}Флщ упчж ъ улфё{/cps}{nw}"
    gachipunk "{cps=30} Никто не любит повторяться. {w=1} Тогда не забывайте сохраняться.{/cps}"
    play sound glitch3
    show glitch8_short
    pause(0.3)
    hide glitch8_short
    show startukrop
    gachipunk "{cps=30} Игра будет изменяться. {w=1} Тогда не забывайте сохраняться.{/cps}"
    menu:
        gachipunk "Сохраниться???"
        "Конечно!":
            call save_yes
        "Ни за что на свете!":
            call save_no

    
    gachipunk_red "{cps=50} Успехов. {/cps} {w}{cps=100} И да, я знаю, что в моём шрифте 'н' похожа на 'к'.{/cps}{nw}"
    
    $ send_to_file("notes", "https://disk.yandex.ru/d/G6tH94Qjik1Y6g")
        

    return


label save_yes:
    #$ style.say_window = style.window #активировал второе диалоговое окно
    show glitch8_short
    pause(0.3)
    hide glitch8_short
    scene black
    stop music #какую нить бы новую музыку
    
    gachipunk_red "{cps=30} В игре нет автосохранений. {w=1} Сделайте это сами.{/cps}"
    return

label save_no:
    #$ style.say_window = style.window
    show glitch8_short
    pause(0.3)
    hide glitch8_short
    scene black
    stop music
    
    gachipunk_red "{cps=30} Я не буду вас переубеждать. {w=1} Но помните, что в игре нет автосохранений.{/cps}"
    return




    
# для маши всё ярко, для димона всё тускло (пример с парком: маша - яркое живописное место, птички, бабочки, люди, которые выгуливают своих питомцев, димон - бомж на скамейке, мрачно, сыро, холодно, печально, людей нет или люди в тёмных или светлых тонах без лиц)