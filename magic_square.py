'''
https://stepik.org/lesson/416755/step/9?unit=406263
'''

lst, flag, count = [list(map(int, input().split())) for i in range(int(input()))], True, 0
new_lst = [list(i) for i in zip(*lst)]
max_num = max(sum(lst, []))
for i in range(1, max(sum(lst, [])) + 1):
    if i not in sum(lst, []) or 0 in sum(lst, []):
        flag = False
        break
for row in lst:
    if sum(row) != sum(lst[0]):
        flag = False
        break
for row in new_lst:
    if sum(row) != sum(lst[0]):
        flag = False
        break
for i in range(len(lst)):
        count += lst[i][i]
if count != sum(lst[0]):
    flag = False
count = 0
for i in range(-1, -len(lst) - 1, -1):
        count += lst[i][i]
if count != sum(lst[0]):
    flag = False
print('YES' if flag else 'NO')
