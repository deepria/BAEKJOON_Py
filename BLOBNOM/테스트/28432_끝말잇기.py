def main():
    from sys import stdin
    read = lambda: stdin.readline().strip()

    n = int(read())
    if n == 1:
        s, m = read(), int(read())
        if s == '?':
            print(read())
        return

    log = []
    flag = 0
    for i in range(n):
        w = read()
        log.append(w)
        if w == '?':
            flag = i

    a = log[flag - 1][-1] if flag > 0 else ''
    b = log[flag + 1][0] if flag < n - 1 else ''

    m = int(read())
    c = [read() for _ in range(m)]

    for w in c:
        if w in log:
            continue
        if a == '' and w[-1] == b:
            print(w)
            break
        elif b == '' and w[0] == a:
            print(w)
            break
        elif w[0] == a and w[-1] == b:
            print(w)
            break


if __name__ == "__main__":
    main()
