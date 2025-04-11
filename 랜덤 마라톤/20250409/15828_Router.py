from sys import stdin
from collections import deque

n = int(stdin.readline())
queue = deque()

while True:
    packet = int(stdin.readline())
    if packet == -1:
        break
    elif packet == 0:
        if queue:
            queue.popleft()
    elif len(queue) < n:
        queue.append(packet)

if queue:
    print(*queue)
else:
    print("empty")
