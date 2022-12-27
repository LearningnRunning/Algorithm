from  heapq import heappop,heappush,heapify
def solution(scoville, K):
    ans = 0
    heapify(scoville)
    # 가장 작은 수 scoville[0] 
    # min(scoville) 을 쓰면 효율성에서 걸린다
    while scoville[0] < K:
        # 가장 작은 수와 그 다음 작은 수
        heappush(scoville,heappop(scoville) +(heappop(scoville)*2))
        ans += 1
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return ans

scoville = [1, 2, 3, 9, 10, 12]
K = 7
solution(scoville,K)