class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[-1] * 2 for _ in range(len(prices))]

        def recur(i, buy):
            if i >= len(prices):
                return 0
            
            if dp[i][buy] != -1:
                return dp[i][buy]
            
            if buy:
                dp[i][buy] = max(-prices[i] + recur(i+1, not buy), recur(i+1, buy))
            else:
                dp[i][buy] = max(prices[i] + recur(i+2, not buy), recur(i+1, buy))
            
            return dp[i][buy]
        
        return recur(0, 1)
        




        