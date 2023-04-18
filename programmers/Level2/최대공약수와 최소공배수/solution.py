def solution(n, m):
    a = min(n,m)
    b = max(n,m)
    while b != 0:
        a, b = b, a % b
    b = int(m*n/a)
    return [a,b]