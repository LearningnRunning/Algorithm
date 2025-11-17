class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        zero = None
        for one_idx, one in enumerate(numbers):
            if zero == one:
                continue
            else:
                zero = one
            for two_idx, two in enumerate(numbers[one_idx+1:]):
                if target == one + two:
                    return [one_idx+1, one_idx+two_idx+2]

