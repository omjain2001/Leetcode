import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Maintain the minheap of k large elements
        pq = []
        heapq.heapify(pq)

        for i in nums:
            if len(pq) < k:
                heapq.heappush(pq, i)
            elif i > pq[0]:
                heapq.heappushpop(pq, i)
        
        return pq[0]
            

        