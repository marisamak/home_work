from random import randint
from tank import Tank
import world

_tanks = []
_canvas = None

def initialize(canv):
    global _canvas
    _canvas = canv

    spawn(False)
    for i in range(5):
        spawn(True).set_target(get_player())

    print(_tanks)

def get_player():
    return _tanks[0]

def update():
    for tank in _tanks:
        tank.update()
        check_collision(tank)

def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.inersects(other_tank):
            return True
    return False

def spawn(is_bot=True):
    cols = world.get_cols()
    rows = world.get_rows()

    while True:
        col = randint(1, cols-1)
        row = randint(1, rows-1)

        if world.get_block(row, cols) != world.GROUND:
            continue

        t = Tank(_canvas, x = col*world.BLOCK_SIZE, y = row*world.BLOCK_SIZE, speed=2, bot=is_bot)
        if not check_collision(t):
            _tanks.append(t)
            return t
