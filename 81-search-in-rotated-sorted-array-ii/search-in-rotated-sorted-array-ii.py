class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        n = len(nums)

        while l <= r:
            
            while l < r and nums[l+1] == nums[l]:
                l += 1
            
            while r > l and nums[r] == nums[r-1]:
                r -= 1

            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[0] <= nums[m]:
                if nums[0] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[n - 1]:
                    l = m + 1
                else:
                    r = m - 1

        return False