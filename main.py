import math

AB = input("Длина первого катета: ")
AC = input("Длина второго катета: ")

AB = float(AB)
AC = float(AC)

BC = math.sqrt(AB**2 + AC**2)

S = (AB * AC) / 2
P = AB + AC + BC

print("Площадь треугольника: %.2f" % S)
print("Периметр треугольника: %.2f" % P)


'''

#в функции присваиваем переменную и если число меньше 0, то выводим ответ об отрицательных числах
def numeral_count(number):
    if number < 0:
        print('Цифр отриательное')
        return 0
        
#если число больше 0, то проверяем число на кол-во знаков
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


# Запрашиваем 2 цифры
firstTask = int(input('Введите первое число: '))
secondTask = int(input('Введите второе число: '))

#присваиваем переменной значение из функции
firstnumeral = numeral_count(firstTask)
secondnumeral = numeral_count(secondTask)

#основное условия с переменными
if firstnumeral > secondnumeral:
    print('Цифр больше в первом числе')
elif firstnumeral < secondnumeral:
    print('Цифр больше во втором числе')
else:
    print('Разное кол-во чисел!')



level = 50


def mainmenu(): #Текст выбор прокачки скила
    print('1. Прокачать ловкость')
    print('2. Прокачать силу')
    print('3. Прокачать умения')

    print('\nВам доступно:', level, 'едениц') #цикл с выбором скилла
    select = int(input('Выберите навык, который необходимо прокачать: '))
    if select == 1:
        dexterity()
    elif select == 2:
        force()
    elif select == 3:
        skills()
    else:
        print('\nВыберите навык, который необходимо прокачать: ')
#функция прокачки ловкости
def dexterity():
  global level
  dexterityup = int(input('Улучшить навык на: '))
  if level >= dexterityup:
    level -= dexterityup
    print('\nЛовкость прокачена на: ', dexterityup, 'еденицы')
    print('Осталось:', level, 'едениц навыка')
  else:
    print('У вас недостаточно едениц навыка. Осталось:', level, 'еденицы')
  input('\nНажмите на любую кнопку, чтобы вернуться')
  mainmenu()

#функция прокачки силы
def force():
  global level
  forceup = int(input('Улучшить навык на: '))
  if level >= forceup:
    level -= forceup
    print('\nСила прокачена на: ', forceup, 'еденицы')
    print('Осталось:', level, 'едениц навыка')
  else:
    print('У вас недостаточно едениц навыка. Осталось:', level, 'еденицы')
  input('\nНажмите на любую кнопку, чтобы вернуться')
  mainmenu()



import math

def mydistance(x,y):
  distance = math.sqrt(x ** 2 + y ** 2)
  print(distance)

def mybetween(x_1,y_1,x_2,y_2):
  between = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
  print(round(between,4))

chois = int(input('1 - расстояние до точки. 2 - расстояние между точками: '))
if chois == 1:
  x = int(input('Введите координату X: '))
  y = int(input('Введите координату Y: '))
  mydistance(x, y)

elif chois == 2:
  x_1 = int(input('Введите координату первого X: '))
  y_1 = int(input('Введите координату первого Y: '))
  x_2 = int(input('Введите координату второго X: '))
  y_2 = int(input('Введите координату второго Y: '))
  mybetween (x_1,y_1,x_2,y_2)

else:
  print('Ошибка ввода')

  

import math

def func(x):
  if -5 <= x <= 5:
    print('x =', x, 'y =', math.exp(x))
  elif x < -5:
    print('x =', x, 'y =', 2 * abs(x) - 1)
  else:
    print('x =', x, 'y =', 2 * x)

for x in range(-10, 11):
  func(x)

def myadress(name):
  print('Фамилия Хуилова')
  print('Имя', name)
  print('Улица')
  print('Дом')
  print()


myadress('Игорек')
myadress('Василий')
myadress('Песка')

def countFood():
  frukt = int(input('Сколько фруктов? '))
  ovosch = int(input('Сколько овощей? '))
  summ = frukt + ovosch
  print('Всего нужно фрутокв и овощей', summ, 'штук')

print('Жирафы')
countFood()
print('\nСлоны')
countFood()
print('\nПитушары')
countFood()



import math

distance= float(input('Введите расстояние до танка: '))
angle = float(input('Введите угол: '))

angle /= 57.2958

x = math.cos(angle) * distance
y = math.sin(angle) * distance

print('Кординаты танка: ', x, ',' ,y)

import math

x = float(input('Укжите координату X: '))
y = float(input('Укжите координату Y: '))

distance = math.sqrt(x**2 + y**2)
print('Расстояние:', round(distance,2))


while True:
  x = float(input('Укжите координату X: '))
  y = float(input('Укжите координату Y: '))

  if (x and y) < 1:
    xsquart = int(x * 10)
    ysquart = int(y * 10)
    print('Координата:',xsquart,'и', ysquart)
    break
  else:
    print('Введите координаты меньше 1')

height = float(input('Ваш рост: '))
weight = float(input('Ваш вес: '))

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
  print('Недостаточная масса тела')
elif bmi < 25:
  print('Нормальная  масса тела')
elif bmi < 30:
  print('Избытчная масса тела')
else:
  print('Ожирение')

bet = int(input('Сколько ставим?' ))
coof = float(input('Укажите коофициент? '))
win = round(bet * coof,2)
print('Потенциальный выйгрыш:', win)
print(win)


while True: # пока цикл истинен
  for att in range(1, 4): # перебором пробегаемся по 3 попыткам
    pincod = int(input('Введите пинкод: '))# вводим первый пин код
    if pincod == 1234: # и если введеный пинкод равен 1234, то выводим текст
      print('Пинк од верный')
      break #останавлваем цикл
    print('Пин код не верный. Осталось пыпыток', 3 - att) #если пинкод не верный показываем кол-во попыток
  else: # по окончанию цикла(3 попыток выводим текст)
     print('Ваша карта заблокировна')
  print('Следующий клиент')#если цикл пройден, показываем

attem = 3
for att in range(1, 4):
  pincod = int(input('Введите пинкод'))
  if pincod == 1234:
    print('Пинк од верный')
    break
  attem -= 1
  print('Пин код не верный. Осталось пыпыток', 3 - att)
if attem == 0:
  print('Ваша карта заблокировна')

people = int(input('Введите кол-во людей:'))
for hour in range(people + 1):
  print('Идет час:', hour)
1000  for num in range(hour,people):
    print('Номер очереди:', num)
  print()
print('Очередь обслужена')

for row in range(20): #цикл с перебором от 0 до 19
  for cel in range(50): #цикл с перебором от 0 до 49
    if row == 9: # оператор, если переменная(вертикаль) равна 9 то выводим  -
      print('-', end = '')
    elif cel == row + 29:
      print('\\', end = '') 
    elif cel == -row + 19:
      print('/', end = '') 
    elif cel == 24:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()

size = int(input('Введите размер таблицы: ')) #указиываем столбец и строку
for row in range(1, size + 1):
  for cel in range(1, size + 1):
    if row < cel:
      print(0, end = ' ')
    elif row > cel:
      print(2, end = ' ')
    else:
      print (1, end = ' ')
  print()

for row in range(20): #цикл с перебором от 0 до 19
  for cel in range(50): #цикл с перебором от 0 до 49
    if row == 9: # оператор, если переменная(вертикаль) равна 9 то выводим  -
      print('-', end = '')
    elif cel == 24:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()

size = int(input('Введите размер таблицы: ')) #указиываем столбец и строку
for row in range(1, size + 1):
  for cel in range(1, size + 1):
    if row % 2 == 0:
      print(row, end = ' ')
    else:
        print (cel, end = ' ')
  print()

bad = 0
for kids in range (5):
  question = input('Кто написал произведение?')
  if question == 'Пушкин' or question == 'пушкин':
    print('Верно!')
    break
  print('Не правильно!')
  bad += 1
print(bad)

totalpeople = int(input('Сколько солдат? '))
totalrules = int(input('Сколько правил в уставе: '))
push = 0
for solder in range(totalpeople, 0, -4):
  solder_rus = int(input('Солдат, назови колво правил в уставе: '))
  if totalrules != solder_rus:
    print('Не правильно', 10 * solder, 'отжиманий' )
    push += 10 * solder
print('Общее кол-во отжиманий', push)


n = int(input('Введиче число: '))
for number in range(1, n, 2):
  number *= 2 - 1
  print('Прошло часов: ',number, number**2)


totalhours = int(input('Сколько осталось часов? '))
cells = 3
for hour in range(1,totalhours//3 + 1):
  cells *= 2
  print('Прошло часов: ', hour*3)
  print('Сколько клеток?: ', cells)
  print('Сколько часов осталось?: ', totalhours - hour*3)
  print()


n = int(input('Введите  число: '))
for number in range(1, n//2 + 1):
  number *= 2
  print(number, number**3)

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
total = 0
for ku in range(num_1, num_2 + 1):
  total = total+ku
print(total)


tim = int(input('Который час? '))
for ku in range(tim):
  ku = 'Ку-ку'
  print(ku)


monts = int(input('Сколько месяцев будем копить? '))
summ = 0
for mont in range(monts):
  print('Месяц', mont)
  money = int(input('Сколько откладываем денег?'))
  summ += money
print('За', monts,'ты накопишь',summ, 'рублей' )


for num in range(11):
   print(num*3)


cikl = 0
for num in 3,7,5,6,4:
 if num > 0:
   print(num**2, num**3, num**4 )
   cikl += 1

text = 'Pes'
for word in range(5):
  print(text)
  print(word)


a = int(input('Укажите шестизначное число билета: '))
total_a = a//10000 + a//1000%10 + a%1000
total_b = a//100 + a//10%10 + a%10
print(total_a, total_b)



if total_one == total_two:
  print('Билет',number,'счастливый')
  print(a, b)
else:
   print('Билет',number,'не счастливый')
   print(a, b)
   print (a//100 + a//10%10 + a%10)

rate_chek = False
while True:
  active = int(input('Продолжаем работать?'))
  if active ==0:
    print('Приложение закрывается')
    break
  rate = int(input('Поставите оценку?'))
  if rate == 1:
    rate_chek = True
print('Работа завершена')
if rate_chek == True:
   print('Пользователь, продолжает работать')

number = int(input('Укажите число: '))
list_number = 0
while number > 0:
  if number%2 == 0:
    list_number += 1
  print(list_number)

  a = int(input())
k = 0
while a != 0:
   if a % 2 == 0:
       k += 1
   a = int(input())
print("Кол-во четных чисел:", k)


name = input('Укажите ваше имя: ')
credit = int(input('Укажите сумму задолжности: '))
while credit > 0:
  debet = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?: '))
  credit -= debet
  if credit <= 0:
    print ('Отлично,', name,'Вы погасили долг. Спасибо!')
  if credit >= 0:
    print ('Маловато,', name, 'Давайте ещё раз.')


weather = int(input('Сколькл градусов на улице? '))
meters = 0
while weather > 15:
  meters += 20
  weather -= 2
  if weather <= 15:
    break
  meters += 10
  print ('Пройдено метров: ', meters)



number = int(input('Введите число: '))
while number > 1:
  number -= 1
  print(number**3)

number = int(input('Введите число: '))
while number >= 0:
  if number == 3:
    number -= 1
    continue
    print(number)
  number -= 1


bags = int(input('Сколько нужно перенести мешков?'))
totalweigt  = 0
bags_count = 0
while bags_count < bags:
  weigt = int(input('Сколько весит мешок?'))
  totalweigt += weigt
  bags_count += 1
  print('Перенести мешков', bags_count, 'из', bags)
print('Общий вес мешков', totalweigt)

bags = int(input('Сколько нужно перенести мешков?'))
totalweigt  = 0
bags_count = 0
while bags_count < bags:
  weigt = int(input('Сколько весит мешок?'))
  totalweigt += weigt
  bags_count += 1
  print('Перенести мешков', bags_count, 'из', bags)
print('Общий вес мешков', totalweigt)

text = 'Python'
word = 0
while word < 5:
  print(text)
  word += 1





number = int(input('Сколькл градусов на улице? '))
summ = 0
while number != 0:
  las_numb = number%10
  print (las_numb)
  summ += las_numb
  if las_numb == 5:
    print ('Обнаружен разрыв')
    break
  summ + las_num
  number//10
  print ('Сумма:  ', summ)

password = int(input('Введите пароль: '))
while password != 215:
  print ('Не верный пароль')
  password = int(input('Попробуйте еще раз: '))
print ('Пароль верный, добро пожаловать!')

balance = int(input('Сколькл денег пришло? '))
while balance > 5000:
  product = int(input('Введите стоимость товара:  '))
  balance -= product
  print ('Денег неть!')
  print ('Баланс счета: ',balance)

  weather = int(input('Сколькл градусов на улице? '))
meters = 0
while weather > 15:
  meters += 20
  weather -= 2
  if weather <= 15:
    break
  meters += 10
  print ('Пройдено метров: ', meters)
'''
