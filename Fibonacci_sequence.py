'''
https://stepik.org/lesson/294243/step/15?unit=275922
'''

lst = [1, 1]
n = int(input())
for i in range(n - 2):
    if n == 1:
        break
    else:
        lst.append(lst[-1] + lst[-2])
if n == 1:
    print(1)
else:
    print(*lst)
