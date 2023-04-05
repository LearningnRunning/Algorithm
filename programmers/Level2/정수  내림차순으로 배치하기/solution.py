def solution(n):
    n = sorted(list(str(n)))
    n = ''.join(reversed(n))
    return int(n)