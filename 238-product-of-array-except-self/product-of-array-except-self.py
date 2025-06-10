class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zc = 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                zc += 1
        
        ans = [0] * len(nums)

        if zc > 1:
            return ans
        elif zc == 1:
            ans[nums.index(0)] = prod
            return ans
        else:
            lp = [0] * len(nums)
            rp = [0] * len(nums)
            lp[0] = 1
            rp[len(nums)-1] = 1
            
            for i in range(1, len(nums)):
                lp[i] = lp[i-1] * nums[i-1]
            for i in range(len(nums)-2, -1, -1):
                rp[i] = rp[i+1] * nums[i+1]
            for i in range(len(nums)):
                ans[i] = lp[i] * rp[i]
            return ans