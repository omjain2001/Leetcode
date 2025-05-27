class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()

        dp = [1e10] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            dp[i] = 1e10
            
            for c in coins:
                if i - c < 0:
                    break
                
                if dp[i-c] != 1e10:
                    dp[i] = min(dp[i], 1+dp[i-c])

        
        if dp[amount] == 1e10:
            return -1
        return dp[amount]
        

        
            

                

        