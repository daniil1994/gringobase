nar = 0

for n in range(30,35 + 1):
    if n == 30:
        people = int(input('Какое кол-во людей в секторе 30: '))
    elif n == 31:
            people = int(input('Какое кол-во людей в секторе 31: '))
    elif n == 32:
            people = int(input('Какое кол-во людей в секторе 32: '))
    elif n == 33:
            people = int(input('Какое кол-во людей в секторе 33: '))
    elif n == 34:
            people = int(input('Какое кол-во людей в секторе 34: '))
    elif n == 35:
        people = int(input('Какое кол-во людей в секторе 35: '))


    if people > 10:
            nar+= 1
            print('Нарушение! Слишком много людей в секторе!')
    else:
            print('Все спокойно.')
print('Обнаружено:', nar, 'нарушений')
