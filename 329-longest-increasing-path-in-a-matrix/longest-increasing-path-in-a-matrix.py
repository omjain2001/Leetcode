class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * (n+1) for _ in range(m+1)]

        visited = [[0] * (n+1) for _ in range(m+1)]

        def dfs(i ,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if visited[i][j] == 1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            offset = [(0, 1), (0, -1), (1,0), (-1,0)]
            path = 1
            visited[i][j] = 1
            for x,y in offset:
                if 0 <= (i+x) < m and 0 <= (j+y) < n and visited[i+x][j+y] == 0 and matrix[i+x][j+y] > matrix[i][j]:
                    path = max(path, 1 + dfs(i+x, j+y))
            visited[i][j] = 0
            
            dp[i][j] = path
            return dp[i][j]

        longest_path = 0
        
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i, j))
        
        return longest_path
                
                
        