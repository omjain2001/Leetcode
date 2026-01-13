class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums)-1

        mini = 0
        maxi = len(nums)-1

        # Find minimum
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            
        mini = left

        left = 0
        right = len(nums)-1

        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        maxi = right

        if mini == len(nums) or maxi == -1 or nums[mini] != target or nums[maxi] != target:
            return [-1,-1]

        return [mini, maxi]
        