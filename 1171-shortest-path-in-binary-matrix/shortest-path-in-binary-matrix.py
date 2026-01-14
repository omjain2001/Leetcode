from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # BFS
        m,n = len(grid), len(grid[0])

        if m > 0 and n > 0 and (grid[0][0] != 0 or grid[m-1][n-1] != 0):
            return -1

        queue = deque()
        queue.append((0,0,1))

        grid[0][0] = -1

        while(len(queue) > 0):
            i,j,v = queue.popleft()
            
            if i == m-1 and j == n-1:
                return v
            
            offsets = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

            for of in offsets:
                x = i + of[0]
                y = j + of[1]

                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = -1
                    queue.append((x,y,v+1))
        
        return -1



        