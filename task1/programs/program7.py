# Проверьте является ли значение в переменной number - четным.
# -- coding: utf-8--


number = int(input('Введите значение '))
#  % - остаток от деления
if number % 2 == 0:
    print('значение четное')
else:
    print('значение нечетное')