# Факториалом числа n называется произведение 1 × 2 × ... × n. 
# Обозначение: n!. По данному натуральному n вычислите значение n!. 
# Пользоваться математической библиотекой math в этой задаче запрещено.

n = int(input('Введите число n'))
nF = 1

for i in range(1,n+1,1):
    nF*= i

print(nF)