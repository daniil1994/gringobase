number = int(input('Укажите шестизначное число билета: '))
a = number//1000
b = number%1000
if a == b:
  print('Билет',number,'счастливый')
  print(a, b)
else:
   print('Билет',number,'не счастливый')
   print(a, b)
