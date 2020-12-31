a = int(input('Первое число - '))
b = int(input('Второе число - '))
c = int(input('Третье число - '))
if a == b == c:
    print ('Совпадают все числа')
elif a == b or a == c or b == c:
    print ('Совпадает 2 числа')
else:
    print ('Совпадает 0  чисел')