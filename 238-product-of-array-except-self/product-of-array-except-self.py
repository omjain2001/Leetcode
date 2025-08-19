class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 0:
            return []

        pre = [1] * len(nums)
        suf = [1] * len(nums)

        prod = nums[0]
        for idx in range(1, len(nums)):
            pre[idx] = prod
            prod *= nums[idx]

        prod = nums[-1]
        for idx in range(len(nums)-2, -1, -1):
            suf[idx] = prod
            prod *= nums[idx]

        ans = []
        for idx in range(len(nums)):
            ans.append(pre[idx] * suf[idx])
        
        return ans
        