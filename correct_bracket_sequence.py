'''
https://stepik.org/lesson/334150/step/9?unit=317559
'''

def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return len(text) == 0


txt = input()

print(is_correct_bracket(txt))
