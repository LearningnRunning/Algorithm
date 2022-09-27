from collections import deque


def solution(s):
    answer = True
    x = 0
    que = deque(s)
    while que:
        que_tmp = que.popleft()
        if que_tmp == "(":
            x += 1
        else:
            x -= 1
        if x < 0:
            answer = False
            break
    if x > 0:
        answer = False
    return answer
