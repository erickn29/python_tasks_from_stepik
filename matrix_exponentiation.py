'''
https://stepik.org/lesson/416756/step/11?unit=406264
'''

import numpy as np

n = int(input())
m1 = np.array([list(map(int, input().split())) for i in range(n)])
pow = int(input())
res = np.linalg.matrix_power(m1, pow)
for c in res:
    print(*c)
