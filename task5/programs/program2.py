# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
# -- coding: utf-8 --

N = int(input('Введите целое число: '))
i = 2
while N % i != 0:
    i += 1
print(i)