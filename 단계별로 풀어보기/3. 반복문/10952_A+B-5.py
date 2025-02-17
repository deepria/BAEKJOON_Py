import sys


def sol():
    a, b = map(int, sys.stdin.readline().rstrip().split())
    while a != 0 and b != 0:
        print(a + b)
        a, b = map(int, sys.stdin.readline().rstrip().split())



def sol_opt():
    while True:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if a == 0 and b == 0:  # 종료 조건
            break
        print(a + b)


sol()
