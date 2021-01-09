result = 0
counter = 0
a = int(input('Введите число: '))
b = int(input('Введите число: '))
for n in range(a, b + 1):
    if n%3 == 0:
        counter+=1
        result += n
print('Среднее арифметическое: ', result // counter)