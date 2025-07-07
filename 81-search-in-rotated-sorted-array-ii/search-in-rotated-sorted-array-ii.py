class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        n = len(nums)

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif (nums[m] == nums[l]) and (nums[m] == nums[r]):
                l += 1
                r -= 1
                continue
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False