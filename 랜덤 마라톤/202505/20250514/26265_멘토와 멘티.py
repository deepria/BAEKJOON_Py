def main():
    from sys import stdin, stdout
    read = lambda: stdin.readline().strip()
    n = int(read())
    arr = []
    for _ in range(n):
        arr.append(read().split())
    arr.sort(key=lambda x: x[1], reverse=True)
    arr.sort(key=lambda x: x[0])
    for a in arr:
        stdout.write(f'{a[0]} {a[1]}\n')


if __name__ == "__main__":
    main()
