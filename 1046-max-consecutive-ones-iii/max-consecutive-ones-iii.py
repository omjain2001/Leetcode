class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        countZ = 0
        maxi = 0
        while(r < len(nums)):
            if nums[r] == 0:
                countZ += 1
                while l <= r and countZ > k:
                    if nums[l] == 0:
                        countZ -= 1
                    l += 1
            maxi = max(maxi, r-l+1)
            r += 1
        return maxi
        