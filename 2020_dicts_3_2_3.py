'''
Напишите программу, которая считывает строку с числом nn, которое задаёт количество чисел,
которые нужно считать. Далее считывает n строк с числами x_i , по одному числу в каждой строке.
Итого будет n+1 строк.

При считывании числа x_i программа должна на отдельной строке вывести значение f(x_i). Функция f(x)
уже реализована и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента x. Для того,
чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
'''

n = int(input())
s = dict()
while n > 0:
    x = int(input())
    if x in s:
        print(s[x])
    else:
        s[x] = f(x)
        print(s[x])
    n -= 1