# Строка хранит число n. Посчитайте и выведите на экран результат выражения n + n^2 + n^3 + n^4 + n^5
# -- coding: utf-8--

n = str(input('Введите число: '))
# преобразуем строку в число
number = int(n)

print(number + number**2 + number**3 + number**4 + number**5)