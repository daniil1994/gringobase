'''
Реализуйте программу, которая получает на вход четырёхзначное число и выводит на экран каждую его цифру отдельно
'''
a = int(input('Введите число: '))
one = a%10
two = int((a%100)/10)
three = int((a%1000)/100)
four = int((a%10000)/1000)
print(four,three,two,one)
