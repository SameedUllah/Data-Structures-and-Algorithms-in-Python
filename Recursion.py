# Factorial
import sys
sys.setrecursionlimit(10000)

x = 3

def factorial(n):
    print(n)
    return n * factorial(n-1)
factorial(x)