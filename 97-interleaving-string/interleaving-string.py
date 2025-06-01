from collections import Counter
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        if len(s3) != (n1+n2):
            return False

        dp = [[False] * (n2+1) for _ in range(n1+1)]

        def recur(i, j):
            if n1 == 0:
                return s3 == s2
            if n2 == 0:
                return s3 == s1
            if i >= n1 and j >= n2:
                return True

            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = (int)((i < n1 and s1[i] == s3[i+j] and recur(i+1, j)) or (j < n2 and s2[j] == s3[i+j] and recur(i, j+1)))
            return dp[i][j]

        # ans = recur(0, 0)
        # if ans == 1:
        #     return True
        # return False

        dp[n1][n2] = True

        for i in range(n2-1, -1, -1):
            dp[n1][i] = (s3[n1+i] == s2[i]) and dp[n1][i+1]
        
        for i in range(n1-1, -1, -1):
            dp[i][n2] = (s3[i+n2] == s1[i]) and dp[i+1][n2]

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                dp[i][j] = (int)((s1[i] == s3[i+j] and dp[i+1][j]) or (s2[j] == s3[i+j] and dp[i][j+1]))
        
        return dp[0][0]
                