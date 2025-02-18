import sys
from collections import deque


def sol():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        commands = sys.stdin.readline().strip()
        n = int(sys.stdin.readline().strip())
        data = sys.stdin.readline().strip()
        if n == 0:
            numbers = deque()
        else:
            numbers = deque(map(int, data[1:-1].split(',')))
        run(commands, numbers)


def run(commands, numbers):
    reverse_flag = False
    for e in commands:
        if e == "D":
            if numbers:
                if reverse_flag:
                    numbers.pop()
                else:
                    numbers.popleft()
            else:
                print("error")
                return
        elif e == "R":
            reverse_flag = not reverse_flag
    if reverse_flag:
        numbers.reverse()

    print("[" + ",".join(map(str, numbers)) + "]")


sol()
