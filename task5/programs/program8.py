# Дана последовательность натуральных чисел, завершающаяся числом 0. 
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
# -- coding: utf-8 --

chain = int(input())
amt = 0
while chain != 0:
    next = int(input())
    if next != 0 and chain == next:
        amt += 1
    chain = next
print(amt)