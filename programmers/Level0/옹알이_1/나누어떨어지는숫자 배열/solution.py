def solution(a, d):
    answer = []
    for i in a:
        if i % d == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        answer.sort()
        return answer