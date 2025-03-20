import sys
input = sys.stdin.readline

def main():
    s = input().rstrip()
    bomb = list(input().rstrip())
    n, k = len(bomb), bomb[-1]
    ans = []

    for c in s:
        ans.append(c)
        if c == k and ans[-n:] == bomb:
            del ans[-n:]

    print(''.join(ans) if ans else "FRULA")
