uj = list(map(int, input().split()))
sl = list(map(int, input().split()))
scored_first, lost = False, False
uj_point, sl_point = 0, 0
for i in range(9):
    uj_point += uj[i]
    if uj_point > sl_point:
        scored_first = True
    sl_point += sl[i]
    if uj_point < sl_point:
        lost = True
    else:
        lost = False
print('Yes' if scored_first and lost else 'No')
