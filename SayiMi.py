# SAYI MI
# ',' ve '.' float sayilar icin
numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.', ','}


def is_digit(text):
    for i in text:
        if i == ' ':
            return False
        if i in str(numbers):
            pass
        else:
            return False
    return True

if is_digit('156, 4'):
    print('SAYI')
else:
    print('TEXT')
