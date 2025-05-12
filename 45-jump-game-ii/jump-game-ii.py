class Solution:
    def jump(self, nums: List[int]) -> int:

        # DP Approach (O(n^2))

        # dp = [1e10] * len(nums)

        # def recur(i):
        #     if i >= len(nums):
        #         return 1e10
        #     if i >= len(nums)-1:
        #         return 0
        #     if dp[i] != 1e10:
        #         return dp[i]

        #     mini = 1e10
        #     for j in range(i+1, i+nums[i]+1):
        #         mini = min(mini, 1 + recur(j))
        #     dp[i] = mini
        #     return dp[i]
        
        # ans = recur(0)
        # return ans


        # Linear Approach (O(n))
        jumps = l = r = 0
        while(r < len(nums)-1):
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            jumps += 1
        return jumps

        