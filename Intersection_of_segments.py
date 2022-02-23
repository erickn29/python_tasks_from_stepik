'''
Задание:
https://stepik.org/lesson/265082/step/11?unit=246030
'''

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
l1, l2 = set(i for i in range(a1, b1 + 1)), set(i for i in range(a2, b2 + 1))
if not l1.isdisjoint(l2):
    if list(sorted(l1 & l2))[0] != list(sorted(l1 & l2))[-1]:
        print(list(sorted(l1 & l2))[0], list(sorted(l1 & l2))[-1])
    else:
        print(list(sorted(l1 & l2))[0])
else:
    print('пустое множество')
