# 4) Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print('Введите целое положительное число:')
number = int(input())
max_digit = 0
while number != 0:
    temp = number % 10
    if temp > max_digit:
        max_digit = temp
    number = number // 10
print(f'Cамая большая цифра в числе: {max_digit}')