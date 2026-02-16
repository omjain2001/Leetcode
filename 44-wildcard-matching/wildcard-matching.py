class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = [[-1] * len(p) for _ in range(len(s))]

        def recur(i,j):
            if i < 0 and j < 0:
                return True
            if j < 0 and i >= 0:
                return False
            if i < 0 and j >= 0:
                for k in range(0, j+1):
                    if p[k] != '*':
                        return False
                return True
            
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == p[j] or p[j] == '?':
                dp[i][j] = recur(i-1, j-1)
            elif p[j] == '*':
                dp[i][j] = recur(i-1, j) or recur(i, j-1)
            
            if dp[i][j] == -1:
                dp[i][j] = False
            return dp[i][j]
        
        return recur(len(s)-1, len(p)-1)
        

        