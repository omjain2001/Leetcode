class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        lsb = prices[0]
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx-1]:
                maxi = maxi + prices[idx] - prices[idx-1]
            
        return maxi
        