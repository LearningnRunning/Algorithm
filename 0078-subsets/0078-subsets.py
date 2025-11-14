class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        ans = [[]]


        for i in range(1, len(nums)):
            c_nums = [list(c) for c in combinations(nums, i)]
            ans.extend(c_nums)
        ans.append(nums)

        return ans