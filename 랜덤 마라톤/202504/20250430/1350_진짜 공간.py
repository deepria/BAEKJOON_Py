def main():
    from sys import stdin
    from math import ceil
    read = [*map(int, stdin.read().rstrip().split())]
    n, files, cl = read[0], read[1:-1], read[-1]
    s = 0
    for f in files:
        s += ceil(f / cl)
    print(s*cl)


if __name__ == "__main__":
    main()
