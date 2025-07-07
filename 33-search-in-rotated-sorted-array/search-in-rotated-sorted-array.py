class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        n = len(nums)

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
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

        return -1