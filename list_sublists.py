'''
https://stepik.org/lesson/416753/step/14?unit=406261
'''

def chunked(string):
    string = string.split()
    lst = [[i] for i in string]
    lst.insert(0,[])
    for i in range(2, len(string) + 1):
        for j in range(len(string) + 1):
            if list(string[j:i]) not in lst:
                lst.append(list(string[j:i]))
    print(sorted(lst, key=len))


chunked(input())
