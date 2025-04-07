import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        heapq.heapify(self.minHeap)
        for i in nums:
            if len(self.minHeap) == k:
                if i > self.minHeap[0]:
                    heapq.heappushpop(self.minHeap, i)
            else:
                heapq.heappush(self.minHeap, i)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        else:
            if self.minHeap[0] < val:
                heapq.heappushpop(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)