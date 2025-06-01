class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[-1] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word2)+1):
            dp[0][i] = i
        
        for i in range(len(word1)+1):
            dp[i][0] = i

        def lcs(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i-1] == word2[j-1]:
                dp[i][j] = lcs(i-1, j-1)
            else:
                dp[i][j] = 1 + min(lcs(i-1, j), lcs(i, j-1), lcs(i-1, j-1))
            
            return dp[i][j]
        
        count = lcs(len(word1), len(word2))

        return count
        
        