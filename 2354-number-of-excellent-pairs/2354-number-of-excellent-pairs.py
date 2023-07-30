from collections import Counter

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # Create a counter to store the count of set bits for each unique number in the array.
        count = Counter(map(int.bit_count, set(nums)))
        
        # Initialize the result variable to store the count of excellent pairs.
        result = 0
        
        # Iterate through all possible pairs of set bit counts and calculate the number of excellent pairs.
        for i in count:
            for j in count:
                if i + j >= k:
                    result += count[i] * count[j]
        
        return result