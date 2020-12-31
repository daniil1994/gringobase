name = input('Укажите ваше имя: ')
credit = int(input('Укажите сумму задолжности: '))
while credit > 0:
  debet = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?: '))
  credit -= debet
  if credit <= 0:
    print ('Отлично,', name,'Вы погасили долг. Спасибо!')
  if credit >= 0:
    print ('Маловато,', name, 'Давайте ещё раз.')