def main():
    from sys import stdin
    read = stdin.read().splitlines()
    n = int(read[0])
    arr = [tuple(map(int, read[i].split())) for i in range(1, n + 1)]

    min_diff = float('inf')

    for bit in range(1 << n):
        s_m, b_s = 1, 0
        picked = False

        for i in range(n):
            if bit & (1 << i):
                s, b = arr[i]
                s_m *= s
                b_s += b
                picked = True

        if picked:
            min_diff = min(min_diff, abs(s_m - b_s))

    print(min_diff)


if __name__ == "__main__":
    main()

'''
1
3 10

7

2
3 8
5 8

1

4
1 7
2 6
3 8
4 9

1
'''
