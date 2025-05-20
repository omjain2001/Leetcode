class Solution:
    def countBits(self, n: int) -> List[int]:

        # O(nlgn)
        # ans = []
        # for i in range(0, n+1):
        #     count = 0
        #     while(i):
        #         if i & 1:
        #             count += 1
        #         i = i >> 1
        #     ans.append(count)
        # return ans

        # O(n)
        dp = [0] * (n+1)
        for ele in range(n+1):
            dp[ele] = dp[ele >> 1] + (ele & 1)
        return dp
        
        