# Пользователь вводит число N с клавиатуры - количество чисел из ряда Фибоначчи. Посчитайте сумму этих чисел.

fib1 = fib2 = 1

n = int(input('Номер элемента ряда Фибоначчи: '))

fibSum = fib1+fib2
while n > 0:
    fib1,fib2 = fib2, fib1+fib2
    n-=1
    fibSum += fib2

print("Сумма элементов введеных чисел Фибоначии: ", fibSum)