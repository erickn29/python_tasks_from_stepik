'''
Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке.
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка
[c;d][c;d].

Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a ≤ b, c ≤ d.
'''

a, b, c, d = int(input()), int(input()), int(input()), int(input())
for j in range(c, d + 1):
    print('\t', j, end='')
print()
for i in range(a, b + 1):
    print(i, '\t', end='')
    for x in range(c, d + 1):
        print(i * x, '\t', end='')
        x += 1
    i += 1
    print()
