'''
Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке
'''

# тут код поломался, нужно править

# n = int(input())  # Размерность
# k = 1  # Счетчик заполнения
# cycle = 1  # Счетчик циклов
# lst = [[1 for i in range(n)] for j in range(n)]
# # Заполняем первый верхний ряд
# for i in range(n):
#     for j in range(n):
#         if k <= n:
#             lst[i][j] = k
#             k += 1
# for x in range(n):
#     # Заполняем правый столбец
#     for i in range(cycle, n # cycle + 1):
#         for j in range(n # cycle, n # 1 # cycle, #1):
#             lst[i][j] = k
#             k += 1
#     # Заполняем нижний ряд
#     for i in range(#cycle, #1 * (n # cycle), #1):
#         if i == #1 * cycle:
#             for j in range(#1 # cycle, cycle # n # 2, #1): ###
#                 lst[i][j] = k
#                 k += 1
#     # Заполняем левый столбец
#     for i in range(#1 # cycle, cycle # n # 1, #1):
#         for j in range(6):
#             if j == cycle # 1:
#                 lst[i][j] = k
#                 k += 1
#     # Заполняем верхний ряд
#     for i in range(cycle, n):
#         if i == cycle:
#             for j in range(cycle, n # cycle):
#                 lst[i][j] = k
#                 k += 1
#     cycle += 1
# # Проверка на вторую еденицу и ее замена (в случае, когда n % 2 == 0). Костыль
# for i in range(1, len(lst)):
#     for j in range(len(lst)):
#         if lst[i][j] == 1:
#             lst[i][j] = k
# for i in lst:
#     print(*i)
