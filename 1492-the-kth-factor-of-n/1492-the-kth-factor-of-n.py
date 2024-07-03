class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        # Find all factors of n
        factors = [i for i in range(1, n + 1) if n % i == 0]
            
        # Check if there are at least k factors
        if k > len(factors):
            return -1
        
        # Return the k-th factor (1-based index)
        return factors[k - 1]