import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        else:
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))
            

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()