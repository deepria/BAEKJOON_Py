import sys

def sol():
    read = list(map(int,sys.stdin.read().strip().split()))
    t = read[0]
    cases = [e for e in read[1::2]]
    print(*cases)

sol()