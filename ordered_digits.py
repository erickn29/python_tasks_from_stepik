'''
https://stepik.org/lesson/265122/step/10?unit=246071
'''

n = [int(i) for i in input()]
flag = True
for i in range(-1, -len(n), -1):
    if n[i] > n[i - 1]:
        flag = False
print('NO' if flag is False else 'YES')
