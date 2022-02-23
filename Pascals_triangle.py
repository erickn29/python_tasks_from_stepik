'''
https://stepik.org/lesson/416753/step/10?unit=406261
'''

n = int(input())

def pascal(number):
    n = number + 1
    lst = [list(1 for j in range(1, i + 1)) for i in range(1, n + 1)]
    for x in range(2, n):
        for y in range(1, x):
            lst[x][y] = lst[x - 1][y - 1] + lst[x - 1][y]
    print(lst[n - 1])

pascal(n)
