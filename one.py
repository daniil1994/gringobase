# Две функции: 1. Принимает число и находит сумму всех чисел.
# 2. Считает кол-во цифр в числе. В ответе выводит разность суммы

# глобальные переменные
number_one = 0
number_two = 0
result = 0


# Функция считает кол-во цифр в числе.
def one(number):
    global number_one
    while number > 0:
        number //= 10
        number_one += 1
    return number_one

# Функция разбирает каждое число из числа и складывает друг с другом
def two(number):
    global number_two
    while (number != 0):
        number_two = number_two + number % 10
        number = number // 10
    return number_two


number = int(input('Введите число: '))
totalnumeral_one = one(number)
totalnumeral_two = two(number)

result = totalnumeral_two - totalnumeral_one

print('Сумму чисел: ', totalnumeral_two)
print('Кол-во цифр в числе: ', totalnumeral_one)
print('Разность суммы и кол-ва цифр: ', result)

