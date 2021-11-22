# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания.

A = int(input('Введите 1 число'))
B = int(input('Введите 2 число'))
if A%2!=0:
    C = [i for i in range(A,B-1,-2)]
else:
    A-=1
    C = [i for i in range(A,B-1,-2)]

print(C)