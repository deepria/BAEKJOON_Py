def main():
    from sys import stdin, stdout
    read = lambda: stdin.readline().strip()
    while True:
        n, m = map(int, read().split())
        if n == m == 0:
            break
        stdout.write(str(n + m) + '\n')


if __name__ == "__main__":
    main()
