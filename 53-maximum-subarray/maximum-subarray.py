class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        ans = -1e10
        for num in nums:
            temp += num
            ans = max(ans, temp)
            temp = max(temp, 0)
        return ans 
        