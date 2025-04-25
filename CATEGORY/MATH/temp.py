# 소수 채
def prime_numbers(n):
    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    end = int(n ** 0.5)

    for i in range(2, end + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i]]


# 약수 목록 배열 반환
def get_divisors(n):
    if n < 1:
        return []

    small_divisors = []
    large_divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            small_divisors.append(i)
            if i != n // i:
                large_divisors.append(n // i)

    return small_divisors + large_divisors[::-1]


# GCD(최소 공약수 유클리드 호재법)
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


# LCM(최대 공배수) 은 GCD 를 이용
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


import math
from functools import reduce

nums = [12, 18, 24]


def gcd_multiple(numbers):
    return reduce(math.gcd, numbers)


def lcm_two(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_multiple(numbers):
    return reduce(lcm_two, numbers)


print(f"GCD: {gcd_multiple(nums)}")  # 출력: GCD: 6
print(f"LCM: {lcm_multiple(nums)}")  # 출력: LCM: 72
