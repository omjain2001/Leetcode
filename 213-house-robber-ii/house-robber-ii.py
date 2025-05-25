class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        dp = [-1] * (n+1)
        dp[n] = 0

        # # Recursion and memoization
        # def recur(i, arr):
        #     if i >= n-1:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     dp[i] = max(arr[i] + recur(i+2, arr), recur(i+1, arr))

        #     return dp[i]
        
        # arr = nums[:-1]
        # ans1 = recur(0, arr)

        # dp = [-1] * (n+1)
        # dp[n] = 0
        # arr = nums[1:]
        # ans2 = recur(0, arr)
        # return max(ans1, ans2)


        # Tabulation
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        ans1 = dp[0]

        dp = [0] * (n+2)
        for i in range(n-1, 0, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        ans2 = dp[1]

        return max(ans1, ans2)


        