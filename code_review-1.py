'''
https://stepik.org/lesson/311433/step/3?unit=293861
'''

count = 0
product = 1
for i in range(0, 10):
    x = int(input())
    if x >= 0:
        product *= x
        count += 1
if count > 0:
    print(count)
    print(product)
else:
    print('NO')
