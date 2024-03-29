class Solution:
    def validPartition(self, nums):
        dp = [False] * 4
        dp[0] = True
        
        for i in range(len(nums)):
            dp[(i + 1) % 4] = False
            
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                dp[(i + 1) % 4] |= dp[((i + 1) - 2) % 4]
            
            if i - 2 >= 0 and (
                nums[i] == nums[i - 1] == nums[i - 2] or
                nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2
            ):
                dp[(i + 1) % 4] |= dp[((i + 1) - 3) % 4]
        
        return dp[len(nums) % 4]