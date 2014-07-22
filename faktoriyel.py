def factorial(n):
    if n < 0:
        return 'Number is negative'
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


print('Result is ', factorial(5))
