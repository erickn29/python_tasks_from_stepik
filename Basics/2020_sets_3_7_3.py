'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d известных нам слов, после чего на
dd строках указываются эти слова. Затем передаётся количество l строк текста для проверки,
после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
'''

words = set()
phrase = set()
count1 = int(input())
while True:
    x = input().lower()
    if x.isdigit():
        count2 = int(x)
        break
    words.add(x)
z = 0
while z < count2:
    x = input().lower().split()
    for i in x:
        phrase.add(i)
    z += 1
print(*(phrase - words), sep='\n')
