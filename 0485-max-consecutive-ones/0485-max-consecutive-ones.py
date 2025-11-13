class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max((sum(1 for _ in group) for key, group in groupby(nums) if key == 1), default=0)