class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        ans = [[]]


        for i in range(1, len(nums)):
            c_nums = [list(c) for c in combinations(nums, i)]
            for c in c_nums:
                c.sort()
                if c not in ans:
                    ans.append(c)
        ans.append(nums)
        return ans