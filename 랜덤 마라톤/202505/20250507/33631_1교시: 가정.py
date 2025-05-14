def main():
    from sys import stdin, stdout
    read = lambda: stdin.readline().strip()
    f, c, e, b = map(int, read().split())
    f_, c_, e_, b_ = map(int, read().split())
    q = int(read())
    cookie = 0
    for _ in range(q):
        cmd, i = map(int, read().split())
        match cmd:
            case 1:
                if f_ * i <= f and c_ * i <= c and e_ * i <= e and b_ * i <= b:
                    f -= f_ * i
                    c -= c_ * i
                    e -= e_ * i
                    b -= b_ * i
                    cookie += i
                    stdout.write(str(cookie) + '\n')
                else:
                    stdout.write('Hello, siumii\n')
            case 2:
                f += i
                stdout.write(str(f) + '\n')
            case 3:
                c += i
                stdout.write(str(c) + '\n')
            case 4:
                e += i
                stdout.write(str(e) + '\n')
            case 5:
                b += i
                stdout.write(str(b) + '\n')


if __name__ == "__main__":
    main()
