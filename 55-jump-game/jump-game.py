class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 0
        for s in nums[:-1]:
            steps -= 1
            steps = max(steps, s)
            if steps == 0:
                return False
        
        if steps >= 0:
            return True
        return False
        