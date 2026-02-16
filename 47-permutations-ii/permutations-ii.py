class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = set()
        
        def recur(ptr):
            if ptr == len(nums)-1:
                result.add(tuple(nums))
                return
            for i in range(ptr, len(nums)):
                nums[ptr], nums[i] = nums[i], nums[ptr]
                recur(ptr+1)
                nums[i], nums[ptr] = nums[ptr], nums[i]
        
        recur(0)
        ans = [list(ele) for ele in result]
        return ans
        