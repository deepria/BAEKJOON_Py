import os

def sol_opt():
    *a,=map(int,open(0))
    m=max(a)
    print(m,a.index(m)+1)

def sol():
    tokens = map(int, iter(os.read(0, os.stat(0).st_size).split()))
    a = -100
    cnt, i = 0, 0

    for x in tokens:
        cnt += 1
        if x > a:
            a = x
            i = cnt

    os.write(1, (str(a) + '\n' + str(i)).encode())
    os._exit(0)


sol()
