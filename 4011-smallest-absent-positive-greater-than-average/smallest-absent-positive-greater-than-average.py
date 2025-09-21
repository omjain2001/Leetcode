class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:

        # Calculate average
        avg = sum(nums) / len(nums)

        # Insert elements in the set
        unique_elements = set(nums)

        # Start with the next greater positive integer of an average and check if it 
        # is present in the set or not. If not present, that is the answer

        next_integer = max(floor(avg)+1,1)
        while(True):
            if next_integer in unique_elements:
                next_integer += 1
            else:
                return next_integer


        