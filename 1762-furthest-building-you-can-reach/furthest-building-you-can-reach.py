import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        if len(heights) == 0:
            return -1

        pq = []
        heapq.heapify(pq)
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if len(pq) < ladders:
                    heapq.heappush(pq, diff)
                else:
                    heapq.heappush(pq, diff)
                    new_diff = heapq.heappop(pq)
                    bricks -= new_diff
                    if bricks < 0:
                        return i
        
        return len(heights)-1