class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        r = len(grid)
        c = len(grid[0])
        maxi = 0
        print(maxi)
        
        def dfs(i,j):
            nonlocal maxi
            if i < 0 or i == r or j < 0 or j == c or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1 + dfs(i,j+1) + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j-1)
            maxi = max(maxi, area)
            return area
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    dfs(i,j)
        
        return maxi
        