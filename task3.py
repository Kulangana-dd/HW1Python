# 3) Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.


print('Введите число n:')
n = str(input())
nn = n + n
nnn = nn + n
sum = int(n) + int(nn) + int(nnn)
print(f'{n} + {nn} + {nnn} = {sum}')