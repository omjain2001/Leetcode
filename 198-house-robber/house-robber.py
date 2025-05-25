class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * (n+1)
        dp[n] = 0

        # Recursion and memoization
        def recur(i):
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = max(nums[i] + recur(i+2), recur(i+1))

            return dp[i]
        
        return recur(0)
    
        