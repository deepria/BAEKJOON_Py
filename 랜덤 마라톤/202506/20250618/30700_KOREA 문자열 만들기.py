s = input()
sq = ['K', 'O', 'R', 'E', 'A']
idx, l = 0, 0
for c in s:
    tmp = sq[idx]
    if c == tmp and idx < 4:
        l += 1
        idx += 1
    elif c == tmp and idx >= 4:
        l += 1
        idx = 0
print(l)
