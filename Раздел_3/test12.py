'''
Реализуйте программу, которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке. 
'''
a = int(input('Введите число: '))
one = a%10
two = int((a%100)/10)
three = int((a%1000)/100)
four = int((a%10000)/1000)
print(one,two,three,four)