'''
https://stepik.org/lesson/334150/step/5?unit=317559
'''

def is_password_good(pas):
    al = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)]
    for c in pas:
        if c not in al:
            return False
    return False if len(pas) < 8 or pas.isdigit() or pas.isalpha() or pas.islower() or pas.isupper() else True


txt = input()

print(is_password_good(txt))
