'''
Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное),
выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того,
чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает
все случаи, как минимум до 1000 человек.
'''

x = int(input())  #Получаем число

if x < 10:
    last_int = x
    if x == 0:
        print(x, 'программистов')
    elif x == 1:
        print(x, 'программист')
    elif 5 > x > 1:
        print(x, 'программиста')
    else:
        print(x, 'программистов')
elif 99 > x > 9:
    if 20 > x > 9:
        print(x, 'программистов')
    else:
        last_int = x % 10
        if last_int == 0 or last_int > 4 and last_int <= 9:
            print(x, 'программистов')
        elif last_int == 1:
            print(x, 'программист')
        else:
            print(x, 'программиста')
else:
    last_int = x % 10
    double_int = x % 100
    if 10 < double_int < 20:
        print(x, 'программистов')
        quit()
    if last_int == 0 or last_int > 4 and last_int <= 9:
        print(x, 'программистов')
    elif last_int == 1:
        print(x, 'программист')
    else:
        print(x, 'программиста')