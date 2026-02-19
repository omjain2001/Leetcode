class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[[-1]*3 for _ in range(2)]  for _ in range(len(prices))]


        def recur(i, buy, count):
            
            # Base conditions
            if i == len(prices) or count == 0:
                return 0
            
            if dp[i][buy][count] != -1:
                return dp[i][buy][count]
            
            # Buy
            if buy:
                dp[i][buy][count] = max((-prices[i] + recur(i+1, 0, count)), recur(i+1, buy, count))
            else:
                dp[i][buy][count] = max((prices[i] + recur(i+1, 1, count-1)), recur(i+1, buy, count))
            
            return dp[i][buy][count]

        return recur(0, 1, 2)    
        