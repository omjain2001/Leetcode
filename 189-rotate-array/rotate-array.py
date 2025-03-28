class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums
        num = k % len(nums)
        temp = nums[len(nums)-num: len(nums)]
        for i in range(len(nums)-num-1, -1, -1):
            nums[i+num] = nums[i]
        for i in range(num):
            nums[i] = temp[i]
        

        