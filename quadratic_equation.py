'''
https://stepik.org/lesson/265110/step/7?unit=246058
'''

from math import *

a, b, c = (float(input()) for i in range(3))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + (sqrt(b ** 2 - 4 * a * c))) / (2 * a)
    x2 = (-b - (sqrt(b ** 2 - 4 * a * c))) / (2 * a)
    print(min(x2, x1), sep='\n')
elif d == 0:
    x1 = (b / (2 * a)) * (-1)
    print(x1)
else:
    print('Нет корней')
