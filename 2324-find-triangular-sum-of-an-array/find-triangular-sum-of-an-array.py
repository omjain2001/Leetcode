class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        count = len(nums)-1
        while(count):
            for i in range(0, count):
                nums[i] = (nums[i] + nums[i+1]) % 10
            count -= 1
        
        return nums[0]
        