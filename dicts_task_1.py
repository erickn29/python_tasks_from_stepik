'''
https://stepik.org/lesson/446696/step/11?unit=437002
'''

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
for key1 in dict1.keys():
    for key2 in dict2.keys():
        if key1 == key2:
            result[key1] = dict1[key1] + dict2[key2]
            break
        elif key2 not in result:
            result[key2] = dict2[key2]
        else:
            result[key1] = dict1[key1]
