import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)

        for i in nums:
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, i)
            elif len(maxHeap) == k and maxHeap[0] < i:
                heapq.heappushpop(maxHeap, i)
        
        return maxHeap[0]