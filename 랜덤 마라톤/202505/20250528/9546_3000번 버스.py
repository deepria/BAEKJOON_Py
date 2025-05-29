def main():
    from sys import stdin
    read = [*map(int, stdin.read().rstrip().split())]
    n, arr = read[0], read[1:]
    for a in arr:
        c = 0
        for i in range(a):
            c += 0.5
            c *= 2
        print(int(c))


if __name__ == "__main__":
    main()
