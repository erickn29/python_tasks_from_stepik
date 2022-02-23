'''
https://stepik.org/lesson/331754/step/13?unit=315133
'''

def quick_merge(lst):
    lst.sort()
    return lst

nums = [int(c) for _ in range(int(input())) for c in input().split()]
print(*quick_merge(nums))
