def solution(brown, yellow):
    ttl = brown + yellow
    for i in range(3, int(ttl**0.5) + 1):
        if (ttl % (i) == 0) & ((i - 2) * ((ttl // i) - 2) == yellow):
            # 조건1. i가 총합의 약수이다
            # 조건2. i의 짝약수와 -2씩 뺀 뒤 곱했을 때 yellowd인 값
            return [ttl // i, i]
