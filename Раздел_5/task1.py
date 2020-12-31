experience = int(input('Введите количество опыта: '))
if experience < 1000:
  print('Ваш уровень 1')
elif experience <= 2500:
  print('Ваш уровень 2')
else:
  print('Ваш уровень 3')