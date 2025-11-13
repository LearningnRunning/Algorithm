from itertools import combinations
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort(reverse=True)

        def dfs(index: int, path: List[int], total: int):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(index, len(candidates)):
                candidate = candidates[i]
                # 같은 인덱스를 넘겨줌: 현재 값 계속 사용 가능
                dfs(i, path + [candidate], total + candidate)

        dfs(0, [], 0)
        return result