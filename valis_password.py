'''
https://stepik.org/lesson/334150/step/8?unit=317559
'''

def is_valid_password(password):
    psw = password.split(':')
    if len(psw) != 3:
        return False
    if psw[0] != psw[0][::-1]:
        return False
    for i in range(2, (int(psw[1]) // 2) + 1):
        if int(psw[1]) % i == 0:
            return False
    if int(psw[2]) % 2 != 0:
        return False
    return True


psw = input()

print(is_valid_password(psw))
