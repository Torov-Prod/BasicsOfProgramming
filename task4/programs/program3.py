# Дана строка. Разрежьте ее на две равные части (если длина строки — четная, 
# а если длина строки нечетная, то длина первой части должна быть на один символ больше). 
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран. 
# Решение задачи должно быть выполнено без использования конструкции if и ей подобных.
# -- coding: utf-8 --

line = str(input('введите строку: '))

def func(line):
    print(line[(len(line) + 1) // 2:] + line[:(len(line) + 1) // 2])

func(line)