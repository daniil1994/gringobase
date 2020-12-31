mileage = int(input('Укажи пробег: '))
day = int(input('Номер дня: '))
one = mileage%10
two = int((mileage%100)/10)
three = int((mileage%1000)/100)
summ = one + two + three
if summ < day:
  print('Сброс')
  print ('Пробег: ',mileage - mileage,'км')
else:
  print('Сегодня не сломался')
  print ('Пробег: ',mileage,'км')