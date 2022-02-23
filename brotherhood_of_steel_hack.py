'''
https://stepik.org/lesson/324754/step/8?unit=307930
'''

n = int(input().strip('#'))
lst = [input().rstrip() for i in range(n)]
new_lst = [i[:i.index('#')].rstrip() if i.count('#') > 0 else i for i in lst]
print(*new_lst, sep='\n')
