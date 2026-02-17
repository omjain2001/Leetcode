class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if len(word1) < len(word2):
            self.minDistance(word2, word1)

        dp = [[-1]*len(word2) for _ in range(len(word1))]

        def recur(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            elif i == len(word1):
                return len(word2)-j
            elif j == len(word2):
                return len(word1)-i

            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = recur(i+1, j+1)
            else:
                dp[i][j] = 1 + min(recur(i, j+1), recur(i+1, j), recur(i+1, j+1))
            
            return dp[i][j]
        
        return recur(0, 0)

        