'''
https://stepik.org/lesson/328948/step/7?unit=312239
'''

lst = [input() for i in range(int(input()))]
n = int(input())
words = [input() for i in range(n)]
count = 0
for c in lst:
    for k in words:
        if k.lower() in c.lower():
            count += 1
        if count == n:
            print(c)
    count = 0
