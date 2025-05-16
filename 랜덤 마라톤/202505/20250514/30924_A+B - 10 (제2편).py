def main():
    from random import shuffle
    is_a, is_b = False, False
    a, b = 0, 0
    pool = list(range(1, 10001))
    shuffle(pool)
    for n in pool:
        if not is_a:
            print("? A", n, flush=True)
            res_a = int(input())
            if res_a == 1:
                is_a = True
                a = n
        if not is_b:
            print("? B", n, flush=True)
            res_b = int(input())
            if res_b == 1:
                is_b = True
                b = n
        if is_a and is_b:
            print("!", a + b)
            break


if __name__ == "__main__":
    main()

# def simulation():
#     import random
#     tries = []
#     for _ in range(1000):
#         pool = list(range(1, 10001))
#         random.shuffle(pool)
#         A = random.choice(pool)
#         B = random.choice(pool)
#         while B == A:
#             B = random.choice(pool)
#
#         count = 0
#         found_a = False
#         found_b = False
#         for x in pool:
#             count += 1
#             if x == A or x == B:
#                 if x == A:
#                     found_a = True
#                 if x == B:
#                     found_b = True
#             if found_a and found_b:
#                 break
#         tries.append(count)
#
#     print(sum(tries) / len(tries))
