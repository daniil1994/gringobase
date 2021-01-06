number = int(input('Угадай число: '))
i = 0

while number != 265:
    print('Число меньше, чем нужно. Попробуйте ещё раз!')
    number = int(input('Угадай число: '))
    i += 1

print('Вы угадали! Число попыток: ', i)

