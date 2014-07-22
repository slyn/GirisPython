# Prime Number


def is_prime(no):
    if no > 2:
        for i in range(2, no):
            if no % i == 0:
                return '{0} is not a prime number'.format(no)
        return '{0} is a prime number'.format(no)
    elif no == 2:
        # Two is a prime number
        return '2 is a prime number'
    else:
        return '{0} is not a prime number'.format(no)


def is_prime_bool(no): # if 'no' is a prime, methods return True else methods return False
    if no > 2:
        for i in range(2, no):
            if no % i == 0:
                return False
        return True
    elif no == 2:
        # Two is a prime number
        return True
    else:
        return False


def prime_list(no1=1, no2=10):  # method has initial values for parameters(no1=1, no2=10)
    if no1 == no2:
        print('Your number is Equal ')
        return False
    elif no1 > no2:
        no1, no2 = no2, no1  # Value swapping
        list_prime = list()  # empty list for prime number
    for i in range(no1, no2):
        if is_prime_bool(i):
            list_prime.append(i)
    return list_prime


a = int(input('Please Enter Number..: '))
print(is_prime(a))


x, y = 21, 54
c, d = 54, 21
print(prime_list())  # method has initial values for parameters
print(prime_list(x, y))  # method calculates prime number between to numbers
print(prime_list(c, d))
