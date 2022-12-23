from collections import *
import heapq
def solution(n, k, enemy):
    ans = 0
    dq = deque(enemy)
    hq = []
    while n>=0 and dq:
        pop = dq.popleft()
        n-=pop
        heapq.heappush(hq,-pop)
        if n >= 0:
            ans+=1
        elif k>0:
            n-=heapq.heappop(hq)
            k-=1
            ans +=1

    return ans