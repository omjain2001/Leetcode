class Solution:
    def climbStairs(self, n: int) -> int:

        # dp = [-1] * (n+1)
        # dp[n] = 1

        # def recur(n, i):
        #     if i > n:
        #         return 0

        #     if dp[i] != -1:
        #         return dp[i]
            
        #     dp[i] = recur(n, i+1) + recur(n, i+2)
            
        #     return dp[i]
        
        # Tabulation method
        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[n] = 1
        dp[n-1] = 1

        for i in range(n-2, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        
        # return recur(n, 0)
        return dp[0]
        