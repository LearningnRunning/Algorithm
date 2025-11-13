class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_l,y_l = nums[:n], nums[n:]
        ans = []
        for x, y in zip(x_l,y_l):
            ans.extend([x,y])
        return ans
        

        