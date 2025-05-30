class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = [[-1] * (len(t)+1) for _ in range(len(s)+1)]

        def lcs(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0
            if s[i] == t[j]:
                ans += lcs(i-1, j-1)
            ans += lcs(i-1, j)
            dp[i][j] = ans
            return ans

        return lcs(len(s)-1, len(t)-1)       