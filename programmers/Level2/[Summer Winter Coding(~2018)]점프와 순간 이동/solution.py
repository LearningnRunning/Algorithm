def solution(n):
    ans = 1
    while n != 1:
        if n % 2 != 0:
            ans += 1
            n -= n % 2
        else:
            n = int(n / 2)

    return ans


def solution2(n):
    return bin(n).count("1")


n = 5000
solution(n)
solution2(n)
