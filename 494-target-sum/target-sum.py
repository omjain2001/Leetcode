from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        # Recursion and Memoization
        # def recur(i, tgt):

        #     if i >= len(nums):
        #         return (tgt == target)

        #     if (i, tgt) in dp:
        #         return dp[(i, tgt)]
            
        #     dp[(i, tgt)] = recur(i+1, tgt + nums[i]) + recur(i+1, tgt - nums[i])
        #     return dp[(i, tgt)]
        
        # return recur(0, 0)


        # Tabulation
        # dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        # dp[0][0] = 1 # When nums is empty and target is 0, there is only one possible way

        # for i in range(len(nums)):
        #     for curr_sum, count in dp[i].items():
        #         dp[i+1][curr_sum - nums[i]] += count
        #         dp[i+1][curr_sum + nums[i]] += count
        
        # return dp[len(nums)][target]

        # Tabulation (with optimized memory - only previous row is required instead of entire dictionary)
        dp = defaultdict()
        dp[0] = 1

        for i in range(len(nums)):
            new_dp = defaultdict(int)
            for curr_sum, count in dp.items():
                new_dp[curr_sum + nums[i]] += count
                new_dp[curr_sum - nums[i]] += count
            dp = new_dp
        
        return dp[target]
                

            
        