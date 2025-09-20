class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        
        # Steps
        # 1. Remove duplicate elements
        # 2. Sort the list in descending order
        # 3. Take first k elements as the answer

        # Step 1
        distinct_elements = list(set(nums))
        
        # Step 2
        distinct_elements.sort(reverse = True)

        # Step 3
        return distinct_elements[:k]