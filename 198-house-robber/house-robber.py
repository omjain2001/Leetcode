class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * (n+2)
        dp[n] = 0
        dp[n+1] = 0

        # # Recursion and memoization
        # def recur(i):
        #     if i >= n:
        #         return 0
            
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     dp[i] = max(nums[i] + recur(i+2), recur(i+1))

        #     return dp[i]
        
        # return recur(0)

        # Tabulation
        for i in range(n-1, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        return dp[0]
    
        