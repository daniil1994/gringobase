k = int(input('Кубик Кости: '))
v = int(input('Кубик владельца: '))
if k >= v:
  print('Сумма: ', k-v)
  print('Костя платит')
else:
  print('Сумма: ', k+v)
  print('Владелец платит')
print('Игра окончена')