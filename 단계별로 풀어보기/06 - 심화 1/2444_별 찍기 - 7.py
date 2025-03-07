import sys

n = int(sys.stdin.read().strip())
l = 2 * n - 1
for i in range(1, n + 1):
    side = (l - (2 * i - 1)) // 2
    sys.stdout.write(' ' * side + '*' * (2 * i - 1) + '\n')
for i in range(n - 1, 0, -1):
    side = (l - (2 * i - 1)) // 2
    sys.stdout.write(' ' * side + '*' * (2 * i - 1) + '\n')
