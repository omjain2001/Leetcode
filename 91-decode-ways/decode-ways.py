class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [-1] * (n+1)
        dp[n] = 1
        dp[n-1] = (int)(1 <= int(s[n-1]) <= 9)

        def recur(i):
            if i == len(s):
                return 1

            if dp[i] != -1:
                return dp[i]
            
            ans1 = ans2 = 0
            if 1 <= int(s[i]) <= 26:
                ans1 = recur(i+1)
            
            if 10 <= int(s[i:i+2]) <= 26:
                ans2 = recur(i+2)
            
            dp[i] = ans1 + ans2
            return dp[i]
        
        return recur(0)
        