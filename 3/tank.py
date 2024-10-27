from tkinter import *
from hitbox import Hitbox
from random import randint

class Tank:

    __count=0 # счетчик танков

    def __init__(self, canvas, x, y, model = 'T-14 Армата', ammo = 100, speed = 5,
                 file_up = '../img/tankT34_up.png',
                 file_down = '../img/tankT34_down.png',
                 file_left = '../img/tankT34_left.png',
                 file_right = '../img/tankT34_right.png',
                 bot = True):

        self.__bot = bot

        self.__target = None # цель для стрельбы

        self.__skin_up = PhotoImage(file = file_up)
        self.__skin_down = PhotoImage(file = file_down)
        self.__skin_left = PhotoImage(file = file_left)
        self.__skin_right = PhotoImage(file = file_right)

        Tank.__count += 1

        self.__hitbox = Hitbox(x, y, self.get_sise(), self.get_sise(), padding=1)

        self.__canvas = canvas
        self.__model = model # модель
        self.__hp = 100 # здоровье
        self.__dx = 0
        self.__dy = 0
        self.__xp = 0 # опыт
        self.__ammo = ammo # боеприпасы
        self.__fuel = 1000
        self.__speed = speed
        self.__x = x
        self.__y = y

        self.__vx = 0
        self.__vy = 0

        if self.__x < 0:
            self.__x = 0
        if self.__y < 0:
            self.__y = 0

        self.__create()
        #self.right()

    def set_target(self, target):
        self.__target = target

    def __AI_goto_target(self):
        if randint(1, 2) == 1:
            if self.__target.get_x() > self.get_x():
                self.left()
            else:
                self.right()
        else:
            if self.__target.get_y() < self.get_y():
                self.backvard()
            else:
                self.forward()

    def __AI(self): # алгоритм для бота
        if randint(1,30) == 1: # поворот в случайном направлении с частотой 30 кадров
            if randint(1, 10) < 9 and self.__target is not None:
                self.__AI_goto_target()
            else:
                self.__AI_change_orientation()

    def __AI_change_orientation(self):
        rand = randint(0, 3)
        if rand == 0:
            self.left()
        if rand == 1:
            self.right()
        if rand == 2:
            self.forward()
        if rand == 3:
            self.backvard()

    def fire(self):
        if self.__ammo > 0:
            self.__ammo -= 1
            print('Стреляю')

    def forward(self): # назад
        if self.__fuel > 0:
            self.__vx = 0
            self.__vy = 1
            self.__canvas.itemconfig(self.__id, image = self.__skin_down)
            #self.__repaint()

    def backvard(self): # вперёд
        if self.__fuel > 0:
            self.__vx = 0
            self.__vy = -1
            self.__canvas.itemconfig(self.__id, image = self.__skin_up)
            #self.__repaint()

    def left(self):
        if self.__fuel > 0:
            self.__vx = -1
            self.__vy = 0
            self.__canvas.itemconfig(self.__id, image = self.__skin_left)
            self.__repaint()

    def right(self):
        if self.__fuel > 0:
            self.__vx = 1
            self.__vy = 0
            self.__canvas.itemconfig(self.__id, image = self.__skin_right)
            self.__repaint()

    def update(self):
        if self.__fuel > self.__speed:
            if self.__bot:
                self.__AI()

            self.__dx = self.__vx * self.__speed
            self.__dy = self.__vy * self.__speed
            self.__x += self.__dx
            self.__y += self.__dy
            self.__update_hitbox()
            self.__repaint()

    def __create(self):
        self.__id = self.__canvas.create_image(self.__x, self.__y, image = self.__skin_up, anchor = 'nw')

    def __repaint(self):
        self.__canvas.moveto(self.__id, x = self.__x, y = self.__y)

    def __update_hitbox(self): # метод движения хитбокса
        self.__hitbox.moveto(self.__x, self.__y)

    def __undo_move(self): # метод возврата танка на место после столкновения
        if self.__dx == 0 and self.__dy == 0:
            return
        self.__x -= self.__dx
        self.__y -= self.__dy
        self.__fuel += self.__speed
        self.__update_hitbox()
        self.__repaint()
        self.__dx = 0
        self.__dy = 0

    def intersects(self, other_tank):
        value = self.__hitbox.intersects(other_tank.__hitbox)
        if value:
            self.__undo_move()
            if self.__bot:
                self.__AI_change_orientation()
        return value

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_ammo(self):
        return self.__ammo

    def get_model(self):
        return self.__model

    def get_hp(self):
        return self.__hp

    def get_xp(self):
        return self.__xp

    def get_fuel(self):
        return self.__fuel

    def get_speed(self):
        return self.__speed

    @staticmethod
    def get_quantity():
        return Tank.__count

    # @staticmethod
    def get_sise(self):
        return self.__skin_up.width()

    def __str__(self):
        return (f'Модель: {self.__model}, Здоровье: {self.__hp}, Опыт: {self.__xp}, Боеприпасы: {self.__ammo}, Координаты: ({self.__x}, {self.__y})')