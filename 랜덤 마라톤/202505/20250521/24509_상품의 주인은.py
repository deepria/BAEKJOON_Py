def main():
    from sys import stdin
    next_line = stdin.readline
    n = int(next_line())
    students = [tuple(map(int, next_line().split())) for _ in range(n)]
    winners = set()
    result = []
    for subj in range(1, 5):
        sorted_list = sorted(students, key=lambda s: (-s[subj], s[0]))
        for sid, *scores in sorted_list:
            if sid not in winners:
                winners.add(sid)
                result.append(sid)
                break
    print(*result)


if __name__ == "__main__":
    main()
