import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = [(grid[0][0], 0, 0)]
        heapify(pq)
        res = 0
        vis = set((0,0))
        m, n = len(grid), len(grid[0])

        while(len(pq) > 0):
            t, x, y = heapq.heappop(pq)
            res = max(res, t)

            if x == m-1 and y == n-1:
                return res

            offset = [[0,1],[0,-1],[1,0],[-1,0]]
            for i,j in offset:
                if (0 <= x+i < m) and (0 <= y+j < n) and (x+i,y+j) not in vis:
                    vis.add((x+i,y+j))
                    heapq.heappush(pq, (grid[x+i][y+j], x+i, y+j))

        return 0
        