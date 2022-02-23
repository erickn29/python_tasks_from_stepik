'''
https://stepik.org/lesson/512854/step/8?unit=505068
'''

import string

is_num = lambda x: True if set(x).isdisjoint(set(string.ascii_letters)) and x.count('.') < 2 and x.count('-') < 2 and '-' not in x[1:-1] else False
