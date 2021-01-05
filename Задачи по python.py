import math

num = 0
one = float(input('Введите первое число: '))
n2 = 0

result = one//1 #целое
remainder = one - result #остаток

#Переворачиваем числа

while result > 0:
    # находим остаток - последнюю цифру
    digit = result % 10
    # делим нацело - удаляем последнюю цифру
    result = result // 10
    # увеличиваем разрядность второго числа
    n2 = n2 * 10
    # добавляем очередную цифру
    n2 = n2 + digit

print('"Обратное" ему число:', n2)
print(int(result))
print(round(remainder, 2))


'''
one//10
one%10

#У вас есть массив чисел. Напишите три функции, которые вычисляют сумму этих чисел: с for-циклом, с while-циклом, с рекурсией.

list = [1,2,3,4,5]
list_total = 0

#Решаем через for
def one(list):
    global list_total
    for l in list:
        list_total += l

result = one(list) # присваиваем переменной результат функции

print(list_total)

#Напишите функцию, которая создаёт комбинацию двух списков таким образом

l_total = []'''
