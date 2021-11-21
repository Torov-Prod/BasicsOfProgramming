# Напишите функцию, которая вычисляет наименьшее из трех чисел и выводит на экран.
# -- coding: utf-8--
a = float(input('введите 1 число :'))
b = float(input('введите 2 число :'))
c = float(input('введите 3 число :'))


def func(a,b,c):
    if a < b:
        if a< c:
            return a
        else: 
            return c
    else:
        if b < c:
            return b
        else:
            return c

print(func(a,b,c))