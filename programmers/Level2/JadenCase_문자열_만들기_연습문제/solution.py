from collections import deque


def solution(s):
    answer = s[0].upper()
    for i in range(1, len(s)):
        if ord(s[i - 1]) == 32:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer
