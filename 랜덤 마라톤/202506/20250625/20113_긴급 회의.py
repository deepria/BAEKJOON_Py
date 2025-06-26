def main():
    from sys import stdin
    read = stdin.readlines()
    n = int(read[0])
    arr = [*map(int, read[1].split())]
    ca = [0] * (n + 1)
    for a in arr:
        ca[a] += 1
    mx = ca.index(max(ca))
    flag = mx == 0
    if flag:
        ca = ca[1:]
        mx = ca.index(max(ca))
    try:
        _ = ca[mx + 1:].index(ca[mx])
    except ValueError:
        print(mx + 1 if flag else mx)
        exit()
    print('skipped')


if __name__ == "__main__":
    main()