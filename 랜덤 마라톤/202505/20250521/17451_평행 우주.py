def main():
    from sys import stdin
    read = [*map(int, stdin.read().strip().split())]
    n, v = read[0], read[1:]
    speed = v[-1]
    for i in range(n - 2, -1, -1):
        speed = v[i] * ((speed + v[i] - 1) // v[i])
    print(speed)

if __name__ == "__main__":
    main()
