bank = int(input('Сколько внести на вклад? '))
procent = int(input('Ежегодный процент по вкладу: '))

sum_bank = bank + ((bank/100) * procent)
total_period = sum_bank + sum_bank
print(total_period)