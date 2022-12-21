# 12번 문제를 틀렸고 호환성에서도 문제였다.
def solution(n, works):
    if sum(works) <= n:
        return 0
    while n != 0:
        works.sort(reverse=True)
        if works[0] - 1 <= 0:
            works.pop(0)
        else:
            works[0] = works[0] - 1
            n -= 1

    return sum([i**2 for i in works])


# 자동 정렬되는 heap
from heapq import heapify, heappop, heappush


def solutionHeapq(n, works):
    if sum(works) <= n:
        return 0
    works = [-x for x in works]
    heapify(works)
    while n != 0:
        if works[0] - 1 >= 0:
            heappop(works)
        else:
            tmp = heappop(works)
            n -= 1
            tmp += 1
            heappush(works, tmp)

    return sum([i**2 for i in works])


n = 4
works = [4, 3, 3]


solutionHeapq(n, works)
solution(n, works)
