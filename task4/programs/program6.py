# Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения. 
# Если буква f в данной строке встречается только один раз, выведите число -1, 
# а если не встречается ни разу, выведите число -2.
# -- coding: utf-8 --

line = str(input('Введите строку: '))

def func(arg):
   return arg.find('f', arg.find('f') + 1)

print(func(line))