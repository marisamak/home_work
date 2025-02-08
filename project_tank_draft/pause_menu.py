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
    print("Пауза включена" if game_paused else "Игра продолжается")

def restart_game():
    pass

def show_menu(root):
    global menu_active, menu_canvas
    if menu_active:
        return
    menu_active = True
    menu_canvas = Canvas(root, width=300, height=200, bg="gray")
    menu_canvas.place(x=world.SCREEN_WIDTH//2 - 150, y=world.SCREEN_HEIGHT//2 - 100)
    update_menu()

def update_menu():
    global menu_canvas, menu_index
    if not menu_active:
        return
    menu_canvas.delete("all")
    for i, option in enumerate(menu_options):
        color = "white" if i == menu_index else "black"
        menu_canvas.create_text(150, 50 + i * 50, text=option, fill=color, font=("Arial", 14), anchor=CENTER)

def handle_menu_selection(root):
    global menu_active, menu_index, menu_canvas
    if menu_index == 0:
        menu_active = False
        if menu_canvas:
            menu_canvas.destroy()
    elif menu_index == 1:
        restart_game()
    elif menu_index == 2:
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