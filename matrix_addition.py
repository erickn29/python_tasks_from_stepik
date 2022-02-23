'''
https://stepik.org/lesson/416756/step/9?unit=406264
'''

import numpy as np

n, m = map(int, input().split())
m1 = np.array([list(map(int, input().split())) for i in range(n)])
sp = input()
m2 = np.array([list(map(int, input().split())) for i in range(n)])
tmp = m1 + m2
for c in tmp:
    print(*c)
