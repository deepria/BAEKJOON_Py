import sys


def sol():
    read = sys.stdin.read().strip().split()[1:]
    cnt = 0

    for s in read:
        seen = set()
        prev = None
        is_group_word = True

        for c in s:
            if prev != c:
                if c in seen:
                    is_group_word = False
                    break
                seen.add(c)
            prev = c

        if is_group_word:
            cnt += 1

    print(cnt)


sol()
