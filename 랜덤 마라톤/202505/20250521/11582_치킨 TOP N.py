def main():
    import sys
    read = sys.stdin.read
    data = read().split()

    n = int(data[0])
    a = list(map(int, data[1:n + 1]))
    k = int(data[n + 1])

    size = n // k
    result = []

    for i in range(0, n, size):
        group = a[i:i + size]
        group.sort()
        result.extend(group)

    print(*result)


if __name__ == "__main__":
    main()
