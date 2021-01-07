total = 0
gross = int(input('Укажите заплату сотрудника в этом месяце: '))
for n in range(1,12):
    if n < 12:
        gross = int(input('Укажите заплату сотрудника в этом месяце: '))
        total+=gross
print(round(total/n))