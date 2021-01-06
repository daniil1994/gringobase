i = 0
m = 0

number = int(input('Введите число: '))

while number != 0:
    if number > 0:
        i += 1
        number = int(input('Введите число: '))
    elif number < 0:
        m += 1
        number = int(input('Введите число: '))
    else:
        break

print(i,m)