class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[-1] * (amount + 1) for i in range(len(coins)+1)]
        # for i in range(len(coins) + 1):
        #     dp[i][0] = 0
        # for i in range(amount + 1):
        #     dp[0][i] = 0
        

        def recur(i, rem):

            if rem == 0:
                return 0

            if i == (len(coins) - 1):
                if rem % coins[i] == 0:
                    return rem // coins[i]
                return 1e10
            
            if dp[i][rem] != -1:
                return dp[i][rem]

            take = 1e10
            if rem >= coins[i]:
                take = min(1 + recur(i, rem - coins[i]), 1e10)
            not_take = recur(i+1, rem)
            
            dp[i][rem] = min(take, not_take)
            return dp[i][rem]
        
        
        ans = recur(0, amount)
        if ans == 1e10:
            return -1
        return ans
        

        
            

                

        