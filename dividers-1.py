'''
https://stepik.org/lesson/298796/step/3?unit=280623
'''

divisors, count, summ, a, b = {}, 0, 0, int(input()), int(input())
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            count += i
            divisors[j] = count
    count = 0
s_divs = sorted(divisors, key=divisors.get)
for k in range(1, s_divs[-1] + 1):
    if s_divs[-1] % k == 0:
        summ += k
print(s_divs[-1], summ)
