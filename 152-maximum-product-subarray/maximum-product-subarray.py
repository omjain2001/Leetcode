class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        prod = 1
        max_prod = nums[0]

        for i in range(len(nums)):
            prod *= nums[i]
            max_prod = max(max_prod, prod)

            if prod == 0:
                prod = 1
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            max_prod = max(max_prod, prod)

            if prod == 0:
                prod = 1
        
        return max_prod
        