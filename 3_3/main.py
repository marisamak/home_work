from tank import Tank
from tkinter import*
import world
import tanks_collection
import texture


def key_press(event):
    print(f'Нажата клавиша {event.keysym}, код {event.keycode}')


def update():
    tanks_collection.update()
    player=tanks_collection.get_player()
    world.set_camera_xy(player.get_x()-world.SCREEN_WIDTH//2+player.get_size()//2,
                        player.get_y()-world.SCREEN_HEIGHT//2+player.get_size()//2)
    world.update_map()
    w.after(1000//FPS,update)


def key_press(event):
    player=tanks_collection.get_player()
    if event.keycode == KEY_W:
        player.forward()
    if event.keycode == KEY_S:
        player.backward()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()
    if event.keycode == 32:
        tanks_collection.spawn()


def load_textures():
    texture.load('tank_up','../img/tankT34_up.png')
    texture.load("tank_down",'../img/tankT34_down.png')
    texture.load("tank_left",'../img/tankT34_left.png')
    texture.load("tank_right",'../img/tankT34_right.png')

    texture.load('tank_up_player','../img/tank_up_player.png')
    texture.load('tank_down_player','../img/tank_down_player.png')
    texture.load('tank_left_player','../img/tank_left_player.png')
    texture.load('tank_right_player','../img/tank_right_player.png')

    texture.load(world.BRICK, "../img/brick.png")
    texture.load(world.WATER, "../img/water.png")
    texture.load(world.CONCRETE, "../img/wall.png")
    texture.load(world.MISSLE, "../img/bonus.png")


KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37,39,38,40

KEY_W=87
KEY_S=83
KEY_A=65
KEY_D=68
FPS=60

w=Tk()
load_textures()
w.title('Танки на минималках 2.0')
canv=Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg='#8ccb5e')
canv.pack()
world.initialaze(canv)
tanks_collection.initialize(canv)
w.bind('<KeyPress>', key_press)
update()
w.mainloop()