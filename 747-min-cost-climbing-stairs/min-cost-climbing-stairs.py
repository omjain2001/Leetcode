class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = [-1] * (n+1)
        dp[n] = 0

        # # Recursion and memoization
        # def recur(i):
        #     if i > len(cost):
        #         return 1e10
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     dp[i] = cost[i] + min(recur(i+1), recur(i+2))

        #     return dp[i]
        
        # return min(recur(0), recur(1))


        # Tabulation
        dp[n-1] = cost[-1]
        dp[n-2] = cost[-2]

        for i in range(n-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])

        