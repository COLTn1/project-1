import random

print('Це гра "Магічне число"')
print('У тебе 3 спроби,щоб вгадати число від 1 до 100')

bot_number = random.randint(1,100)

for i in range(3):
    user_number = int(input('Введи число:'))

    if bot_number > user_number:
        print('Більше')
    if bot_number < user_number:
        print('Менше')

    if bot_number == user_number:
        print('Ти вгадав(-ла) число!')
        break

print('Спроби закінчились')
print('Гра закінчена')
print(f'Число було: {bot_number}')