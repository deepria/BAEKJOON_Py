from itertools import product


def sieve(limit):
    for digits in product('012', repeat=limit):
        if digits[0] == '0':
            continue
        num = int(''.join(digits))
        if num % 3 == 0:
            yield num


n = int(input())
print(len(list(sieve(n))))
