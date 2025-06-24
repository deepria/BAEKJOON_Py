def main():
    from sys import stdin
    read = stdin.readlines()
    n = int(read[0])
    for i in range(1, 2 * n, 2):
        d = {k.strip(): int(v) for k, v in (item.strip().split(":") for item in read[i].strip().split(","))}
        c = [group.strip().split('&') for group in read[i + 1].strip().split('|')]
        mn = min(max(d[x] for x in group) for group in c)
        print(mn)


if __name__ == "__main__":
    main()
