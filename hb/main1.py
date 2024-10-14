from hitbox import Hitbox

hb1 = Hitbox(50, 0, 100, 100)
hb2 = Hitbox(150, 100, 100, 100)
hb3 = Hitbox(200, 200, 100, 100)

print(' ')
print(f'верхняя граница hb1: {hb1.top}, верхняя граница hb2: {hb2.top}, верхняя граница hb3: {hb3.top}')
print(f'нижняя граница hb1: {hb1.bottom}, нижняя граница hb2: {hb2.bottom}, нижняя граница hb3: {hb3.bottom}')
print(f'левая граница hb1: {hb1.left}, левая граница hb2: {hb2.left}, левая граница hb3: {hb3.left}')
print(f'правая граница hb1: {hb1.right}, правая граница hb2: {hb2.right}, правая граница hb3: {hb3.right}')
print(' ')

intesection_1 = hb1.intersects(hb2)
intersection_2 = hb1.intersects(hb3)
intersection_3 = hb2.intersects(hb3)

print(f'Первый со вторым - {intesection_1}, первый с третьим - {intersection_2}, '
      f'второй с третьим - {intersection_3}.')