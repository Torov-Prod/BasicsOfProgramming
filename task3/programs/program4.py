# Дано несколько чисел. Вычислите их сумму. 
# Сначала вводите количество чисел N, затем вводится ровно N целых чисел. 
# Постройте решение так, чтобы использовалось минимальное количество переменных.

N = int(input('Введите кол-во чисел'))
x = [int(input()) for _ in range(N)]

def func(N,x):
    a = 0
    for i in range(N):
        a = a + x[i]
        if i == x[N-2]:
            return a
            

print(func(N,x))