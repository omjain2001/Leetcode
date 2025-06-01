class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        dp = [[0] * (len(nums)+2) for _ in range(len(nums)+2)] 

        # def recur(i, j):
        #     if i > j:
        #         return 0
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     for k in range(i, j+1):
        #         dp[i][j] = max(dp[i][j], (arr[k]*arr[i-1]*arr[j+1]) + recur(i, k-1) + recur(k+1, j))
            
        #     return dp[i][j]
        
        # arr = [1] + nums + [1]
        # return recur(1, len(nums))

        arr = [1] + nums + [1]
        for i in range(len(nums), 0, -1):
            for j in range(1, len(nums)+1):
                if i > j:
                    continue
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], (arr[k]*arr[i-1]*arr[j+1]) + dp[i][k-1] + dp[k+1][j])
        
        return dp[1][len(nums)]


            
            
