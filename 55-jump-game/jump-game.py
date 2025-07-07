class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # steps = 0
        # for s in nums[:-1]:
        #     steps -= 1
        #     steps = max(steps, s)
        #     if steps == 0:
        #         return False
        
        # if steps >= 0:
        #     return True
        # return False

        jumps = nums[0]
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return True
            jumps -= 1
            jumps = max(jumps, nums[i])
            if jumps == 0:
                break

        return False
        