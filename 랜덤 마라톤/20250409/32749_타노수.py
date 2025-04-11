n, t = map(int, input().split())
x = input()

len_final = 1 << (n - t)
gap = len(x) // (1 << t)

best = x[:len_final]
for i in range(1, 1 << t):
    start = i * gap
    candidate = x[start:start + len_final]
    if candidate > best:
        best = candidate

print(int(best))