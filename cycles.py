# 1 example with FOR:
stroka = input('Это программа выводит из строки с различными символами только буквы. Введите строку: ')
for i in stroka:
    if i.isalpha():
        print(i, end = ' ')

# 2 example with FOR:
animals = ['dog', 'cat', 'cow', 'horse']
for i in range(len(animals)):
    print(i, animals[i])

# 3 example with FOR:
a = int(input('Эта программа может вывести все числа в заданном диапозоне. Введите число: '))
for i in range(a):
    print(i+1, end = ' ')


# 1 example with WHILE:
while True:
    print('Этот цикл будет выполняться бесконечно. Нажмите Ctrl+C для остановки')

# 2 example with WHILE:
word = input('Введите слово, которое будет повторяться: ')
kol = int(input('Введите сколько повторений этого слова: '))
def print_word(word, kol):
    a = 0
    while a < kol:
        print(word, end = ' ')
        a = a + 1
print_word(word, kol)

# 3 example with WHILE:
word_ = input('Это игра - "Угадай слово". Введите что-нибудь: ')
while word_ != 'стоп':
    if word_ != 'стоп':
        word_ = input('Не угадал( Попробуй еще раз! Введите что-нибудь: ')
        if word_ == 'стоп':
            print('Ура! Ты выиграл!')