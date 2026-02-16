class Solution:
    def jump(self, nums: List[int]) -> int:

        l = r = 0
        count = 0
        while(l <= r and r < len(nums)-1):
            temp = r
            for i in range(l, r+1):
                temp = max(temp, i + nums[i])
            count += 1
            l = r + 1
            r = temp
        
        if r >= len(nums)-1:
            return count
        return -1
        