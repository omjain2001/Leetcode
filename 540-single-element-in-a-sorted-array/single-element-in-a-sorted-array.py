class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        while(l <= r):
            mid = (l+r)//2
            if (mid+1) < len(nums) and nums[mid] == nums[mid+1]:
                if mid % 2 == 0:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if mid % 2 == 1:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return nums[l]

        