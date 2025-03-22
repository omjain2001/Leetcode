from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])

        visited = [[False] * c for _ in range(r)]
        pacific_cells = []
        atlantic_cells = []

        def bfs_pacific(i,j):
            queue = deque()
            queue.append((i,j))
            visited[i][j] = True
            pacific_cells.append([i,j])

            while(len(queue) > 0):
                x,y = queue.popleft()
                if (x+1) < r and heights[x+1][y] >= heights[x][y] and not visited[x+1][y]:
                    queue.append([x+1,y])
                    visited[x+1][y] = True
                    pacific_cells.append([x+1,y])
                if (y+1) < c and heights[x][y+1] >= heights[x][y] and not visited[x][y+1]:
                    queue.append([x,y+1])
                    visited[x][y+1] = True
                    pacific_cells.append([x,y+1])
                if (x-1) >= 0 and heights[x-1][y] >= heights[x][y] and not visited[x-1][y]:
                    queue.append([x-1,y])
                    visited[x-1][y] = True
                    pacific_cells.append([x-1,y])
                if (y-1) >= 0 and heights[x][y-1] >= heights[x][y] and not visited[x][y-1]:
                    queue.append([x,y-1])
                    visited[x][y-1] = True
                    pacific_cells.append([x,y-1])
            
                
        def bfs_atlantic(i,j):
            queue = deque()
            queue.append((i,j))
            visited[i][j] = True
            atlantic_cells.append([i,j])

            while(len(queue) > 0):
                x,y = queue.popleft()
                if (x+1) < r and heights[x+1][y] >= heights[x][y] and not visited[x+1][y]:
                    queue.append([x+1,y])
                    visited[x+1][y] = True
                    atlantic_cells.append([x+1,y])
                if (y+1) < c and heights[x][y+1] >= heights[x][y] and not visited[x][y+1]:
                    queue.append([x,y+1])
                    visited[x][y+1] = True
                    atlantic_cells.append([x,y+1])
                if (x-1) >= 0 and heights[x-1][y] >= heights[x][y] and not visited[x-1][y]:
                    queue.append([x-1,y])
                    visited[x-1][y] = True
                    atlantic_cells.append([x-1,y])
                if (y-1) >= 0 and heights[x][y-1] >= heights[x][y] and not visited[x][y-1]:
                    queue.append([x,y-1])
                    visited[x][y-1] = True
                    atlantic_cells.append([x,y-1])

        # Pacific ocean is left and top of an island
        for i in range(c):
            if not visited[0][i]:
                bfs_pacific(0,i)
        for i in range(r):
            if not visited[i][0]:
                bfs_pacific(i,0)
        

        visited = [[False]*c for _ in range(r)]

        # Atlantic ocean is right and bottom of an island
        for i in range(c):
            if not visited[r-1][i]:
                bfs_atlantic(r-1,i)
        for i in range(r):
            if not visited[i][c-1]:
                bfs_atlantic(i,c-1)
        
        # Take intersection of both the lists
        print(pacific_cells)
        print(atlantic_cells)
        result = [cord for cord in pacific_cells if cord in atlantic_cells]
        
        return result
        
        