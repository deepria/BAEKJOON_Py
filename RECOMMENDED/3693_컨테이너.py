import sys, math

def cal(s):
    best_l, best_w, best_area = float('inf'), float('inf'), float('inf')

    max_r = int(math.sqrt(s)) + 2
    for r in range(1, max_r):
        c = math.ceil(s / r)
        for rows, cols in [(r, c), (c, r)]:
            l = 44 * cols + 4
            w = 10 * rows + 2
            area = l * w
            diff = abs(l - w)
            if area < best_area or (area == best_area and diff < abs(best_l - best_w)):
                best_l, best_w, best_area = l, w, area

    if best_l < best_w:
        best_l, best_w = best_w, best_l

    return best_l, best_w, best_area

def sol():
    read = list(map(int, sys.stdin.read().strip().split()))
    con = [math.ceil(n / 5) for n in read[1:]]
    for c in con:
        l, w, area = cal(c)
        sys.stdout.write(f'{l} X {w} = {area}\n')

sol()