from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1

        r = len(grid)
        c = len(grid[0])

        queue = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append((i,j))
        time = 0

        while(len(queue) > 0):
            count = len(queue)
            isFresh = False
            while(count):
                i,j = queue.popleft()
                if i > 0 and grid[i-1][j] == 1:
                    queue.append((i-1,j))
                    grid[i-1][j] = 2
                    isFresh = True
                if i < r-1 and grid[i+1][j] == 1:
                    queue.append((i+1,j))
                    grid[i+1][j] = 2
                    isFresh = True
                if j > 0 and grid[i][j-1] == 1:
                    queue.append((i,j-1))
                    grid[i][j-1] = 2
                    isFresh = True
                if j < c-1 and grid[i][j+1] == 1:
                    queue.append((i,j+1))
                    grid[i][j+1] = 2
                    isFresh = True
                count -= 1
            if isFresh:
                time += 1
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1
        return time
                
                
        