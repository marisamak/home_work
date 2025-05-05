from tkinter import *
import missiles_collection
import world
import tanks_collection
import texture
import pause_menu  # Импортируем меню паузы
import os

KEY_UP, KEY_DOWN = 38, 40
KEY_W, KEY_S, KEY_A, KEY_D = 87, 83, 65, 68
SPACE = 32
PLUS = 187
ESC = 27
TAB = 9

FPS = 60

def key_press(event):
    player = tanks_collection.get_player()
    if player.is_destroyed() or pause_menu.menu_active:
        pause_menu.menu_key_press(event, w)  # Позволяем управлять меню
        return

    if not pause_menu.menu_active:  # Если меню не активно, управляем танком
        if event.keycode == KEY_W:
            player.forward()
        elif event.keycode == KEY_S:
            player.backward()
        elif event.keycode == KEY_A:
            player.left()
        elif event.keycode == KEY_D:
            player.right()
        elif event.keycode == SPACE:
            player.fire()
        elif event.keycode == PLUS:
            tanks_collection.spawn()
        elif event.keycode == ESC:  # Клавиша Esc
            pause_menu.show_menu(w)  # Передаем главное окно в функцию
        elif event.keycode == TAB:
            pause_menu.toggle_pause()

def update():
    player = tanks_collection.get_player()
    if player.is_destroyed():
        pause_menu.show_menu(w)  # Показываем меню, если игрок погиб
        return

    if not pause_menu.game_paused and not pause_menu.menu_active:
        tanks_collection.update()
        missiles_collection.update()
        world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_size() // 2,
                            player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_size() // 2)
        world.update_map()
    w.after(1000 // FPS, update)

def load_textures():
    # Используйте абсолютные пути или правильные относительные пути
    base_path = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_path, 'img')

    texture.load('tank_down', os.path.join(img_path, 'tank_down.png'))
    texture.load('tank_up', os.path.join(img_path, 'tank_up.png'))
    texture.load('tank_left', os.path.join(img_path, 'tank_left.png'))
    texture.load('tank_right', os.path.join(img_path, 'tank_right.png'))
    texture.load('tank_down_player', os.path.join(img_path, 'tank_down_player.png'))
    texture.load('tank_up_player', os.path.join(img_path, 'tank_up_player.png'))
    texture.load('tank_left_player', os.path.join(img_path, 'tank_left_player.png'))
    texture.load('tank_right_player', os.path.join(img_path, 'tank_right_player.png'))

    texture.load(world.BRICK, os.path.join(img_path, 'brick.png'))
    texture.load(world.WATER, os.path.join(img_path, 'water.png'))
    texture.load(world.CONCRETE, os.path.join(img_path, 'wall.png'))
    texture.load(world.MISSILE, os.path.join(img_path, 'bonus.png'))

    texture.load('missile_up', os.path.join(img_path, 'missile_up.png'))
    texture.load('missile_down', os.path.join(img_path, 'missile_down.png'))
    texture.load('missile_left', os.path.join(img_path, 'missile_left.png'))
    texture.load('missile_right', os.path.join(img_path, 'missile_right.png'))
    texture.load('tank_destroy', os.path.join(img_path, 'tank_destroy.png'))

w = Tk()
load_textures()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg='#8ccb5e')
canv.pack()
world.initialize(canv)
tanks_collection.initialize(canv)
missiles_collection.initialize(canv)

w.bind('<KeyPress>', key_press)
update()
w.mainloop()
