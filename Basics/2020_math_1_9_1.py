'''
Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы AA часов в сутки,
но пересыпать тоже вредно и не стоит спать более BB часов. Сейчас Аня спит HH часов в сутки.
Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
Если Аня спит менее AA часов, выведите “Недосып”, если же более BB часов, то выведите “Пересып”.

Получаемое число AA всегда меньше либо равно BB.

На вход программе в три строки подаются переменные в следующем порядке: AA, BB, HH.
'''

norma = int(input())
perespal = int(input())
spit = int(input())
if spit <= perespal and spit >= norma:
    print("Это нормально")
elif spit < norma:
    print("Недосып")
elif spit > perespal:
    print("Пересып")