from collections import defaultdict
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Intuition comes if we can generate the formula
        # Formula - 
        # Max freq = Initial count of k - Number of k in subarray (as they will be increased or decreased in that operation) + Number of m (element with largest freq in that subarray)

        # Simplifying this, we will get....
        # Max freq = initial count + (number of m in subarray - number of k in subarray)
        # The value in the paranthesis can be solved with kadane's algorithm

        initial_count = nums.count(k)
        maxi = 0

        for m in range(1, 51):
            if m == k:
                continue
            curr_sum = 0
            max_sum = 0
            for n in nums:
                if n == m:
                    curr_sum += 1
                elif n == k:
                    curr_sum -= 1

                # curr_sum += 1 if (n == m) else (-1 if (n == k) else 0)
                max_sum = max(max_sum, curr_sum)
                if curr_sum < 0:
                    curr_sum = 0
            maxi = max(maxi, max_sum)
        
        return (initial_count + maxi)

        