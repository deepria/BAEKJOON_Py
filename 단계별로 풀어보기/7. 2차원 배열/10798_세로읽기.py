import sys


def sol():
    arr = sys.stdin.read().strip().split('\n')
    i, m = 1, 0

    while i != m:
        for s in arr:
            l = len(s)
            if l > i:
                i = l
            if m < l:
                sys.stdout.write(s[m])
        m += 1


sol()
