MOD = 10 ** 9 + 9

n = int(input())
dp = [0, 0, 0]

for d in [1, 2]:
    dp[d % 3] += 1

for _ in range(n - 1):
    new_dp = [0, 0, 0]
    for mod in range(3):
        for d in [0, 1, 2]:
            new_mod = (mod + d) % 3
            new_dp[new_mod] = (new_dp[new_mod] + dp[mod]) % MOD
    dp = new_dp
print(dp[0])
