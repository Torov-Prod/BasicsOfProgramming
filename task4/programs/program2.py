# Дана строка, состоящая из слов, разделенных пробелами. 
# Определите, сколько в ней слов. Используйте для решения задачи метод count
# -- coding: utf-8 --

line = str(input('введите строку: '))
def func(line):
    print(line.count(' ') + 1)

func(line)