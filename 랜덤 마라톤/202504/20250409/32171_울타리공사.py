from sys import stdin

read = lambda: stdin.readline().rstrip()
n = int(read())
w1, w2, h1, h2 = 11, -11, 11, -11
for _ in range(n):
    x1, y1, x2, y2 = map(int, read().split())
    w1 = min(w1,x1)
    w2 = max(w2,x2)
    h1 = min(h1,y1)
    h2 = max(h2,y2)
    print(2*(w2-w1)+2*(h2-h1))
