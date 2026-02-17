class Solution:
    def canJump(self, nums: List[int]) -> bool:

        l = 0
        r = 0
        i = 0
        while(l <= r and r < len(nums)-1):
            i = l
            temp = 0
            while(i <= r):
                temp = max(temp, i + nums[i])
                i += 1
            l = r + 1
            r = temp
        
        if r < len(nums)-1:
            return False
        return True
            
                
        