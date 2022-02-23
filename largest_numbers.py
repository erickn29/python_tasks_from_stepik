'''
https://stepik.org/lesson/294243/step/13?unit=275922
'''

lst = [int(input()) for i in range(int(input()))]
print(*sorted(lst, reverse=True)[:2], sep='\n')
