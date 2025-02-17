def fw(n, graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    for row in graph:
        print(*row)


def fw_detail(n, graph):
    for k in range(n):
        print(f'k : {k}\n')
        for i in range(n):
            print(f'    i : {i}\n')
            for j in range(n):
                print(f'        j : {j}\n')
                print(f'         [i][k] and [k][j] ? {graph[i][k] and graph[k][j]}\n')
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
                    print(f'\n            [{i}][{j}] = 1\n')
    for row in graph:
        print(*row)

# 비트 마스크 최적화 (n <= 32 일때 유효)
def fw_opt_bit_mask(n, arr):
    adj = [0] * n

    for i in range(n):
        for j in range(n):
            if arr[i * n + j]:
                adj[i] |= 1 << j

    for k in range(n):
        for i in range(n):
            if adj[i] & (1 << k):
                adj[i] |= adj[k]

    for i in range(n):
        row = ['1' if adj[i] & (1 << j) else '0' for j in range(n)]
        print(' '.join(row))


def sol():
    n, *arr = map(int, open(0).read().split())
    graph = [arr[i * n:(i + 1) * n] for i in range(n)]
    # fw(n, graph)
    fw_detail(n, graph)
    # fw_opt_bit_mask(n, arr)


sol()
