import sys


def sol():
    a, b, c = map(int, sys.stdin.read().strip().split())
    result = ''
    if a+b+c != 180:
        result = 'Error'
    elif a == b == c:
        result = 'Equilateral'
    elif a == b or a == c or b == c:
        result = 'Isosceles'
    else:
        result = 'Scalene'
    print(result)

sol()
