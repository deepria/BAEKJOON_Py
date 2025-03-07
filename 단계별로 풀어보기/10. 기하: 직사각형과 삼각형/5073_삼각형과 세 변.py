import sys


def sol():
    read = list(map(int, sys.stdin.read().split()))
    arr = [read[i:i + 3] for i in range(0, len(read) - 3, 3)]
    for i in arr:
        a, b, c = i[0], i[1], i[2]
        if a + b <= c or a + c <= b or b + c <= a:
            result = 'Invalid'
        elif a == b == c:
            result = 'Equilateral'
        elif a == b or a == c or b == c:
            result = 'Isosceles'
        else:
            result = 'Scalene'
        print(result)


sol()
