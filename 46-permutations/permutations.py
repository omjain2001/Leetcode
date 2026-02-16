class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def recur(ptr):
            if ptr == len(nums)-1:
                result.append([ele for ele in nums])
                return
            
            for i in range(ptr, len(nums)):
                nums[ptr], nums[i] = nums[i], nums[ptr]
                recur(ptr+1)
                nums[i], nums[ptr] = nums[ptr], nums[i]
        
        recur(0)
        return result
        