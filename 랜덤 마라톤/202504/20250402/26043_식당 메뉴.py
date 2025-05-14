from sys import stdin
from collections import deque


def out(arr):
    print(*sorted(arr) if arr else ['None'])


n = int(stdin.readline())
stu, a, b, c = deque(), [], [], []
for _ in range(n):
    cmd = list(map(int, stdin.readline().split()))
    if cmd[0] == 1:
        stu.append(cmd[1:])
    else:
        s = stu.popleft()
        if cmd[1] == s[1]:
            a.append(s[0])
        else:
            b.append(s[0])
while stu:
    s = stu.popleft()
    c.append(s[0])

out(a)
out(b)
out(c)
