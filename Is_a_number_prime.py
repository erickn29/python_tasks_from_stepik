'''
https://stepik.org/lesson/334150/step/3?unit=317559
'''

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    else:
        return True

n = int(input())

print(is_prime(n))
