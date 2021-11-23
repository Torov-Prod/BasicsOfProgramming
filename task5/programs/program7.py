# Последовательность состоит из натуральных чисел и завершается числом 0. 
# Определите, сколько элементов этой последовательности больше предыдущего элемента.
# -- coding: utf-8 --

chain = int(input())
amt = 0
while chain != 0:
    next = int(input())
    if next != 0 and chain < next:
        amt += 1
    chain = next
print(amt)