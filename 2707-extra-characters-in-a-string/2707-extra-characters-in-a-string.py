class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] + [float('inf')] * n
        
        for i in range(1, n + 1):
            dp[i] = dp[i-1] + 1  # 현재 문자를 사용하지 않는 경우
            
            for word in dictionary:
                if s.find(word, max(0, i - len(word)), i) != -1:
                    dp[i] = min(dp[i], dp[i - len(word)])
        
        return dp[n]