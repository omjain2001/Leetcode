class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        coins.sort()
        dp = [[-1] * (amount+1) for _ in range(len(coins)+1)]

        def recur(i, amt):
            if i < 0:
                return 0
            
            if amt == 0:
                return 1
            
            if dp[i][amt] != -1:
                return dp[i][amt]
            
            dp[i][amt] = 0
            if amt >= coins[i]:
                dp[i][amt] += recur(i, amt - coins[i])

            dp[i][amt] += recur(i-1, amt)

            return dp[i][amt]
        
        return recur(len(coins)-1, amount)
                    