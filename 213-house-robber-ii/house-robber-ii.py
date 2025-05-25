class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]
        
        dp = [-1] * (n+1)
        dp[n] = 0

        # Recursion and memoization
        def recur(i, arr):
            if i >= n-1:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = max(arr[i] + recur(i+2, arr), recur(i+1, arr))

            return dp[i]
        
        arr = nums[:-1]
        ans1 = recur(0, arr)

        dp = [-1] * (n+1)
        dp[n] = 0
        arr = nums[1:]
        ans2 = recur(0, arr)
        return max(ans1, ans2)
        