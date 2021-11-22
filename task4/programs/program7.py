# Дана строка, в которой буква h встречается минимум два раза. 
# Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
# -- coding: utf-8 --

line = str(input('Введите строку: '))

def func(line):
    line = line[:line.find('h')] +line[line.rfind('h') + 1:]
    return line

print(func(line))