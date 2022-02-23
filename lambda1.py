'''
https://stepik.org/lesson/512854/step/7?unit=505068
'''

import string

is_non_negative_num = lambda x: float(x) >= 0 if set(x).isdisjoint(set(string.ascii_letters)) and x.count('.') < 2 else False
