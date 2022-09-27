def solution(n):
    if n >= 2:
        answer = solution(n - 2) + solution(n - 1)
    else:
        answer = n
    return answer
