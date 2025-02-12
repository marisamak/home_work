from tkinter import Canvas, CENTER
import world
import tanks_collection
import missiles_collection

game_paused = False
menu_active = False
menu_index = 0
menu_options = ["Возврат в игру", "Новая игра", "Выход"]
menu_canvas = None


def toggle_pause():
    global game_paused
    game_paused = not game_paused
    tanks_collection.set_game_paused(game_paused)

    if not game_paused and not tanks_collection._menu_active:
        print("Возобновление игрового цикла после паузы")
        tanks_collection.start_update_loop()




#def next_map():
#    global selected_map
#    selected_map = (selected_map + 1) % len(world.map)  # Переход к следующей карте


def restart_game():
    global game_paused, menu_active, menu_canvas

    game_paused = False
    menu_active = False
    if menu_canvas:
        menu_canvas.destroy()
        menu_canvas = None

    world.load_map(world.map)
#    world.load_map(world.map[world.selected_map])  # Загружаем карту
    world.update_map(all=True)  # Обновляем карту
    tanks_collection.reset()  # Пересоздаём танки
    missiles_collection.reset()  # Очищаем ракеты

    tanks_collection.start_update_loop()


def show_menu(root):
    global menu_active, menu_canvas, game_paused
    if menu_active:
        return
    menu_active = True
    game_paused = True

    tanks_collection.set_game_paused(True)  # Останавливаем движение танков
    tanks_collection.set_menu_active(True)

    menu_canvas = Canvas(root, width=300, height=200, bg="gray")
    menu_canvas.place(x=world.SCREEN_WIDTH//2 - 150, y=world.SCREEN_HEIGHT//2 - 100)

    update_menu()


def update_menu():
    global menu_canvas, menu_index

    if not menu_active:
        return

    menu_canvas.delete("all")

    for i, option in enumerate(menu_options):
        if i == menu_index:
            color = "white"  # Выбранная опция
        else:
            color = "black"  # Обычный цвет

        menu_canvas.create_text(150, 50 + i * 50, text=option, fill=color, font=("Arial", 14), anchor=CENTER)


def handle_menu_selection(root):
    global menu_active, game_paused
    if menu_index == 0:  # Возврат в игру
        menu_active = False
        game_paused = False

        tanks_collection.set_game_paused(False)
        tanks_collection.set_menu_active(False)

        if menu_canvas:
            menu_canvas.destroy()

        # Проверяем, идет ли уже игровой цикл, чтобы не запускать его снова
        if not tanks_collection._game_paused and not tanks_collection._menu_active:
            print("Цикл обновления запускается заново после выхода из меню")
            tanks_collection.start_update_loop()


    elif menu_index == 1:  # "Новая игра"
        restart_game()

    elif menu_index == 2:  # "Выход"
        root.quit()


def menu_key_press(event, root):
    global menu_active, menu_index
    if menu_active:
        if event.keycode == 38:  # Стрелка вверх
            menu_index = (menu_index - 1) % len(menu_options)
            update_menu()
        elif event.keycode == 40:  # Стрелка вниз
            menu_index = (menu_index + 1) % len(menu_options)
            update_menu()
        elif event.keycode == 13:  # Enter
            handle_menu_selection(root)
    elif event.keycode == 27:  # Esc
        show_menu(root)
    elif event.keycode == 9:  # Tab
        toggle_pause()