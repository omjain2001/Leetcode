class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = [[-1] * (len(p)+2) for _ in range(len(s)+2)]

        def dfs(i,j):
            if i >= len(s) and j >= len(p):
                dp[i][j] = True
                return dp[i][j]
            if j >= len(p):
                dp[i][j] = False
                return dp[i][j]
            
            if dp[i][j] != -1:
                return dp[i][j]


            # Intuition
            # If it is direct match or '.', move to next characters
            # If not, check if the next character is '*'. In this case, we can either ignore it and 
            # move j by 2 (to next valid character) or consider it and move i to next character (here j still remains at the same character)
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if (j+1) < len(p) and p[j+1] == '*':
                dp[i][j] = dfs(i,j+2) or (match and dfs(i+1,j))
                return dp[i][j]
            
            if match:
                dp[i][j] = dfs(i+1,j+1)
                return dp[i][j]

            # In the case where i == len(s) but j < len(p), the only option for the string to match is all subsequent characters of j
            # should have * after each character. The match condition will be False and the "If" condition determines the result.
            
            dp[i][j] = False
            return dp[i][j]

        return dfs(0,0)
            
        