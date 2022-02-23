'''
https://stepik.org/lesson/313439/step/6?unit=295959
'''

import string

n, str, az = int(input()), list(input()), list(string.ascii_lowercase)
for c in str:
    for b in az:
        if c == b:
            print(az[(az.index(b) - n)], end='')
