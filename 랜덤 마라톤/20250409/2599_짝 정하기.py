def main():
    n = int(input())
    a_m, a_f = map(int, input().split())
    b_m, b_f = map(int, input().split())
    c_m, c_f = map(int, input().split())

    for a in range(a_m + 1):
        d = a_m - a
        e = c_f - d
        b = b_m - e
        c = a_f - b
        f = c_m - c

        if all(x >= 0 for x in [a, b, c, d, e, f]):
            print(1)
            print(f"{a} {d}")
            print(f"{b} {e}")
            print(f"{c} {f}")
            return
    print(0)

main()