from collections import Counter, deque
def solution(k, tangerine):
    ans = 0
    tmp = deque(Counter(tangerine).most_common())
    while k > 0:
        k -= tmp.popleft()[1]
        ans += 1
    return ans