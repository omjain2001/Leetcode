class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = 10**10
        dp = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def recur(i, t):

            # Base case
            if t == 0:
                return 0
            if dp[i][t] != -1:
                return dp[i][t]
            if i == 0:
                if t % coins[i] == 0:
                    dp[i][t] = t // coins[i]
                else:
                    dp[i][t] = MAX
                return dp[i][t]

            # Two options
            ans = MAX
            if t >= coins[i]:
                ans = min(ans, 1 + recur(i, t - coins[i]))
            ans = min(ans, recur(i - 1, t))
            dp[i][t] = ans
            return ans

        result = recur(len(coins) - 1, amount)
        if result == MAX:
            return -1
        return result