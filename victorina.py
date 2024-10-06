from random import choice

student = input('Представьтесь пожалуйста: ')

try:
    level=int(input('Выберите уровень сложности 1-3: '))
except:
    level=1
if level < 1 or level > 3:
    level = 1

print(f'Установлен {level} уровень сложности')
print(f"Хорошо, {student}, тебе вопросы:")

points=0

questions={
    1:[("Какой материк самый большой по площади?", "Евразия"), ("Какая столица у России", "Москва"), ("Какой океан самый большой?", "Тихий")],
    2:[("Какая столица у Италии?", "Рим"), ("Какая столица у Казахстана?", "Астана"), ("Какой материк самый маленький?", "Австралия")],
    3:[("Какая страна в Европе самая маленькая?", "Ватикан"), ("Какой отсров самый большой в мире?", "Гренландия"), ("Самый высокая гора в мире", "Эверест")]}

for i in range(3):
    question, corect_answer = choice(questions[level])
    print(f'{student}, {question}')
    student_answer = input().lower()
    if student_answer == corect_answer.lower():
        points = points + 1
        print("Молодец, правильно!")
    else:
        print(f"Не правильно! Правильный ответ: {corect_answer}")

if points == 3:
    print(f'{student}, молодец, всё правильно!')
elif points == 2:
    print(f"{student}, хорошо, но можно и лучше")
else:
    print(f"{student}, ты плохо знаешь географию!")