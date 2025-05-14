def main():
    from sys import stdin, stdout
    read = stdin.read().splitlines()
    n = int(read[0])
    n, m = map(int, read[0])

    read = lambda: stdin.readline().strip()
    n, m = map(int, read().split())

    read = [*map(int, stdin.read().rstrip().split())]
    n, arr = read[0], read[1:]

if __name__ == "__main__":
    main()

n = 10 ** 9
visited = bytearray(n // 8 + 1)


def visit(i):
    visited[i // 8] |= (1 << (i % 8))


def un_visit(i):
    visited[i // 8] &= ~(1 << (i % 8))


def is_visited(i):
    return (visited[i // 8] >> (i % 8)) & 1


import time

start = time.time()

# your simulation here...

print("실행 시간:", time.time() - start)
