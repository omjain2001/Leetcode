class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        MAX = pow(10,5)

        dp = [[MAX] * len(triangle[-1]) for _ in range(len(triangle))]

        def recur(i, j):
            if i == len(triangle):
                return 0
            if j >= len(triangle[i]):
                return pow(10,5)
            
            if dp[i][j] != MAX:
                return dp[i][j]
            
            dp[i][j] = triangle[i][j] + min(recur(i+1,j), recur(i+1, j+1))
            return dp[i][j]

        return recur(0,0)
            
            
            
        