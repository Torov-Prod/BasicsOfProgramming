# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. 
# Выведите показатель степени и саму степень. Операцией возведения в степень пользоваться нельзя!
# -- coding: utf-8 --

N = int(input('Введите целое число: '))
degree = 2
power = 1
while degree <= N:
    degree *= 2
    power += 1
print(power - 1, degree // 2)
