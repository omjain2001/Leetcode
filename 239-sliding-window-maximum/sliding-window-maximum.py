import heapq
from typing import List

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_heap = []
        heapq.heapify(max_heap)

        ans = []

        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            if i >= k-1:
                ans.append(-max_heap[0][0])
                left = i - k + 1
                while(len(max_heap) > 0 and max_heap[0][1] <= left):
                    heapq.heappop(max_heap)
        
        return ans


        