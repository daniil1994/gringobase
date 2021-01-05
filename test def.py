number = int(input('Введите число: '))
quantity = 0
while number > 0:
    number//= 10
    quantity +=1

print(quantity)