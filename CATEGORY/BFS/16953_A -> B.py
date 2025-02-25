import sys
from collections import deque


def bfs(start, end):
    queue = deque([(start, 1)])

    while queue:
        node, depth = queue.popleft()

        if node == end:
            return depth
        next1 = int(str(node) + '1')
        next2 = 2 * node

        if next1 <= end:
            queue.append((next1, depth + 1))
        if next2 <= end:
            queue.append((next2, depth + 1))

    return -1


def sol():
    a, b = map(int, sys.stdin.read().strip().split())
    print(bfs(a, b))


sol()
