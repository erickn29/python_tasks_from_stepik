'''
https://stepik.org/lesson/311433/step/6?unit=293861
'''

n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n //= 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)
