class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        visited = [[False]*c for _ in range(r)]
        count = 0
        
        def dfs(i,j):
            if (i < 0 or i == r) or (j < 0 or j == c) or (visited[i][j]) or (grid[i][j] == '0'):
                return
            visited[i][j] = True
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i-1,j)
            dfs(i,j-1)
            return

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i,j) 

        return count      