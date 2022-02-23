'''
https://stepik.org/lesson/334150/step/10?unit=317559
'''

def convert_to_python_case(text):
    for c in text:
        if c == c.upper() and not c.isdigit():
            text = text.replace(c, '_' + c.lower())
    return text[1:]


txt = input()

print(convert_to_python_case(txt))
