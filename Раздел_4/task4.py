chair_1 = int(input('Стоимость студа 1: '))
chair_2 = int(input('Стоимость студа 2: '))
chair_3 = int(input('Стоимость студа 3: '))
summ = chair_1 + chair_2 + chair_3
if summ > 10000:
  print('Итоговая сумма:', summ - (summ*0.1))
else:
  print('Итоговая сумма:',summ)
