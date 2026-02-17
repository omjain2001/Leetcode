class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        k = len(nums)-1

        j = 0
        while(j <= k):
            if nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            elif nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            else:
                j += 1
        
        