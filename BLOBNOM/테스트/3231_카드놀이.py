def main():
    from sys import stdin
    data = list(map(int, stdin.read().split()))
    n = data[0]
    arr = data[1:]
    pos = [0] * (n + 1)
    for i, num in enumerate(arr):
        pos[num] = i
    prev = -1
    clap = 0
    for i in range(1, n + 1):
        if pos[i] < prev:
            clap += 1
        prev = pos[i]
    print(clap)

if __name__ == "__main__":
    main()