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


'''

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