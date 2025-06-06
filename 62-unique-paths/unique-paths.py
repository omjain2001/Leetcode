class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1] * (n+1) for j in range(m+1)]

        # def recur(i, j):
        #     if (i == m-1) or (j == n-1):
        #         return 1
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     dp[i][j] = recur(i+1, j) + recur(i, j+1)
            
        #     return dp[i][j]
        
        # return recur(0,0)

        # Tabulation

        for i in range(m):
            dp[i][n-1] = 1
        
        for j in range(n):
            dp[m-1][j] = 1
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]


        