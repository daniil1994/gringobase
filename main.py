name = input('Укажите ваше имя: ')
credit = int(input('Укажите сумму задолжности: '))
while credit > 0:
  debet = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?: '))
  credit -= debet
  if credit <= 0:
    print ('Отлично,', name,'Вы погасили долг. Спасибо!')
  if credit >= 0:
    print ('Маловато,', name, 'Давайте ещё раз.')
  



'''
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