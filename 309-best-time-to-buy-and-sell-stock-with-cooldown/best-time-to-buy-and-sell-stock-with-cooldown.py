class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 2 for _ in range(len(prices)+1)]

        def recur(i, buy):
            if i >= len(prices):
                return 0

            if dp[i][buy] != -1:
                return dp[i][buy]
            
            ans = 0
            if buy:
                ans = max(-prices[i] + recur(i+1, 0), 0 + recur(i+1, 1))
            else:
                ans = max(prices[i] + recur(i+2, 1), 0 + recur(i+1, 0))
            
            dp[i][buy] = ans

            return ans
        
        result = recur(0, 1)
        return result
        