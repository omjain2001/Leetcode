class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Replace all negative numbers with 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # Mark elements at (indices = nums[i]) as negative
        # Note that nums[i] can be negative if previous element has already marked it
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -(len(nums)+1)
        
        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i
        
        return len(nums)+1
        