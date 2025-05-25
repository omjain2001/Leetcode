class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n+1)
        dp[n] = 1

        def recur(n, i):
            if i > n:
                return 0

            if dp[i] != -1:
                return dp[i]
            
            dp[i] = recur(n, i+1) + recur(n, i+2)
            
            return dp[i]
        
        return recur(n,0)
        