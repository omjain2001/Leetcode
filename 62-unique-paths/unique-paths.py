class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1] * (n+1) for j in range(m+1)]

        def recur(i, j):
            if (i == m-1) or (j == n-1):
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = recur(i+1, j) + recur(i, j+1)
            
            return dp[i][j]
        
        return recur(0,0)

        