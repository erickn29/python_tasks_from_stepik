'''
https://stepik.org/lesson/311433/step/4?unit=293861
'''

max = -(10**6)
sum = 0
for i in range(10):
    x = int(input())
    if x < 0:
        sum += x
    if x >= max and x < 0:
        max = x
if sum < 0:
    print(sum)
    print(max)
else:
    print('NO')
