from sys import stdin


def sol():
    arr = sorted(map(int, stdin.read().split()))
    total = sum(arr)
    for i in range(9):
        for j in range(i + 1, 9):
            if total - arr[i] - arr[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(arr[k])
                return


sol()
