import sys

def sol():
    paper = [[0] * 100 for _ in range(100)]
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                paper[i][j] = 1
    black_area = sum(sum(row) for row in paper)
    print(black_area)

sol()