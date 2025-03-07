import sys


def sol():
    s1,s2 = map(str,sys.stdin.read().strip().split())
    print(max(int(''.join([i for i in reversed([e for e in s1])])),int(''.join([i for i in reversed([e for e in s2])]))))


sol()
