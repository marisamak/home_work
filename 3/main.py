from tank import Tank
from tkinter import*
import world

def key_press(event):
    print(f'Нажата клавиша {event.keysym}, код {event.keycode}')

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68

KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37, 39, 38, 40

FPS = 60 # частота кадров

def update():
    player.update()
    enemy.update()
    neutral.update()
    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_sise() // 2,
                        player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_sise() // 2)
    check_collision()
    w.after(1000//FPS, update)

def check_collision():
    player.intersects(enemy)
    enemy.intersects(player)

def key_press(event):
    if event.keycode == KEY_W:
        player.forward()
    if event.keycode == KEY_S:
        player.backvard()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()
    elif event.keycode == KEY_UP:
        world.move_camera(0, -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(0, 5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(-5, 0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(5, 0)
    check_collision()

w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width = world.SCREEN_WIDTH, height = world.SCREEN_HEIGHT, bg = 'alice blue')
canv.pack()
player = Tank(canvas = canv, x = 100, y = 50, ammo = 100, speed = 3, bot = False)

enemy = Tank(canvas = canv, x = 300, y = 300, ammo = 100, speed = 3, bot = True)
enemy.set_target(player)

neutral = Tank(canvas = canv, x = 500, y = 450, ammo = 100, speed = 1, bot = False)
neutral.stop()


w.bind('<KeyPress>', key_press)

update()

w.mainloop()