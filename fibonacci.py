def fibonacci(n):
    if n < 0:
        return 'Number is negative'
    if n == 0 or n == 1:
        return 1
    else:
        return n+fibonacci(n-1)

print('Result is ', fibonacci(2))