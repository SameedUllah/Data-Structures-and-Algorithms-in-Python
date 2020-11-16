# Factorial
# import sys
# sys.setrecursionlimit(10000)

x = 10

def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be a positve integer only'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(x))
endl