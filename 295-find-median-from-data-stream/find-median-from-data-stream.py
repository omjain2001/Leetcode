import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        heapq.heapify(self.max_heap)
        self.min_heap = []
        heapq.heapify(self.min_heap)
        

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        n1 = len(self.max_heap)
        n2 = len(self.min_heap)
        if (n1+n2) % 2 == 0:
            return (self.min_heap[0]-self.max_heap[0]) / 2
        return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()