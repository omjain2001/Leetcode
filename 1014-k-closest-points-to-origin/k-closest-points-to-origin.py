import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        for x, y in points:
            dist = (x**2 + y**2)**0.5
            if len(maxHeap) == k:
                if -maxHeap[0][0] > dist:
                    heapq.heappushpop(maxHeap, (-dist, x, y))
            else:
                heapq.heappush(maxHeap, (-dist,x,y))
        
        result = []
        while(len(maxHeap)):
            dist, x, y = heapq.heappop(maxHeap)
            result.append([x,y])
        
        return result
                