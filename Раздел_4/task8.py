hours = int(input('Количество отработанных часов: '))
credit = int(input('Остаток по кредиту: '))
food = int(input('Количество денег на еду: '))
wage = ((200 * hours)/ (2**3)) + hours
expenses = food + credit
if wage > expenses:
  print('Часов хватает. Можно отдохнуть')
else:
  print('Часов не хватает. Придётся работать!')