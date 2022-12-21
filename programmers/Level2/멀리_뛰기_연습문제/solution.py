from itertools import product


def solution(n):
    anw = 1
    for i in range(1, n):
        nums = [1, 2]
        anw += len([c for c in list(product(nums, repeat=i)) if sum(c) == n]) % 1234567
    return anw


# 경우의 수로 구하기(피보나치수열)
def solution(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567
    return dp[n]


n = 4
solution(n)
