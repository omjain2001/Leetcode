class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                if left >= 0:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            else:
                if left == -1:
                    left = i
        