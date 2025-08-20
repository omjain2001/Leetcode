class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        maxi = 0
        for p in range(1,len(prices)):
            total += prices[p]-prices[p-1]
            maxi = max(maxi, total)
            if total < 0:
                total = 0
        return maxi
        