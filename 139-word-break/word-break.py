class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)

        dp = [-1] * (len(s) + 1)

        def recur(idx):

            if idx == len(s):
                return True
            
            if dp[idx] != -1:
                return dp[idx]
            
            temp = ""

            for i in range(idx, len(s)):
                temp += s[i]
                if temp in words:
                    if recur(i+1):
                        dp[i] = 1
                        return True
            
            dp[idx] = 0
            return False
        

        return recur(0)
        