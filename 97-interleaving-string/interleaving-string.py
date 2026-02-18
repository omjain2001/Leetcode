class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        dp = [[-1]*len(s2) for _ in range(len(s1))]
        
        def recur(i, j):
            if ((i+j) == len(s3)):
                return True
            if i == len(s1):
                return s2[j:] == s3[i+j:]
            if j == len(s2):
                return s1[i:] == s3[i+j:]

            if dp[i][j] != -1:
                return dp[i][j]
            
            k = i+j
            if s3[k] == s1[i] and s3[k] == s2[j]:
                dp[i][j] = recur(i, j+1) or recur(i+1, j)
            elif s3[k] == s1[i]:
                dp[i][j] = recur(i+1, j)
            elif s3[k] == s2[j]:
                dp[i][j] = recur(i, j+1)
            else:
                dp[i][j] = False
            
            return dp[i][j]
        
        if len(s3) != len(s1) + len(s2):
            return False
        return recur(0, 0)
            
        