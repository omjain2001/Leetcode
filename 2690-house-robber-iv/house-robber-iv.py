class Solution:

    def count_houses_with_capability(self, c, nums):
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] <= c:
                count += 1
                i += 1
            i += 1
        return count

    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = 1, max(nums)

        while l <= r:
            c = (l + r) // 2
            if self.count_houses_with_capability(c, nums) >= k:
                r = c - 1
            else:
                l = c + 1

        return l