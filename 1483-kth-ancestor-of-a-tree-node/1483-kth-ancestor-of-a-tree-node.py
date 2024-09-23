class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.log = 20  # log2(5 * 10^4) ≈ 15.6, 여유있게 20으로 설정
        self.dp = [parent] + [[-1] * n for _ in range(self.log - 1)]
        
        for i in range(1, self.log):
            for node in range(n):
                if self.dp[i-1][node] != -1:
                    self.dp[i][node] = self.dp[i-1][self.dp[i-1][node]]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.log):
            if k & (1 << i):
                node = self.dp[i][node]
                if node == -1:
                    return -1
        return node
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)