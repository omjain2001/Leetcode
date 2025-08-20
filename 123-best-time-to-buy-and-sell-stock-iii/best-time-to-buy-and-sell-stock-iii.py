class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[[-1] * 3 for _ in range(2)] for _ in range(len(prices)+1)]

        def recur(i, buy, count):
            if i >= len(prices) or count == 0:
                return 0

            if dp[i][buy][count] != -1:
                return dp[i][buy][count]
            
            ans = 0
            if buy:
                ans = max(-prices[i] + recur(i+1, 0, count), 0 + recur(i+1, 1, count))
            else:
                ans = max(prices[i] + recur(i+1, 1, count - 1), 0 + recur(i+1, 0, count))
            
            dp[i][buy][count] = ans

            return ans
        
        result = recur(0, 1, 2)
        return result
        


            
        