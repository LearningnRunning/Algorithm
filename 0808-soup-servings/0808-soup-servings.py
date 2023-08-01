class Solution:
    def soupServings(self, n: int) -> float:
        # Helper function to calculate the probability recursively
        def serve(a, b, memo):
            if a <= 0 and b <= 0:  # Base case: both soups are empty
                return 0.5
            if a <= 0:  # Base case: soup A is empty
                return 1.0
            if b <= 0:  # Base case: soup B is empty
                return 0.0
            if (a, b) in memo:
                return memo[(a, b)]
            
            # Calculate the probability for each operation
            prob = 0.25 * (
                serve(a - 100, b, memo) +
                serve(a - 75, b - 25, memo) +
                serve(a - 50, b - 50, memo) +
                serve(a - 25, b - 75, memo)
            )
            
            memo[(a, b)] = prob
            return prob

        # Check the edge case where n is larger than the maximum allowed value
        if n >= 5000:
            return 1.0

        memo = {}
        return serve(n, n, memo)