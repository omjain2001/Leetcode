class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = len(nums) * (1 + len(nums)) // 2
        sum2 = sum(nums)

        return (sum1 - sum2)
        