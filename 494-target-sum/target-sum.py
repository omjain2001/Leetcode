class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def recur(i, tgt):

            if i >= len(nums):
                return (tgt == target)

            if (i, tgt) in dp:
                return dp[(i, tgt)]
            
            dp[(i, tgt)] = recur(i+1, tgt + nums[i]) + recur(i+1, tgt - nums[i])
            return dp[(i, tgt)]
        
        return recur(0, 0)
            
        