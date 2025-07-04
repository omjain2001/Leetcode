class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # TC => O(n^2)

        # dp = [1] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(0, i):
        #         if nums[j] < nums[i] and dp[i] < dp[j] + 1:
        #             dp[i] = dp[j] + 1

        # return max(dp)


        # TC => O(nlgn)

        arr = []

        for i in range(len(nums)):
            if (len(arr) == 0) or (nums[i] > arr[-1]):
                arr.append(nums[i])
            else:
                # Binary search
                l = 0
                r = len(arr)-1
                while(l <= r):
                    m = (l + r) // 2
                    if nums[i] > arr[m]:
                        l = m + 1
                    else:
                        r = m - 1
                
                arr[l] = nums[i]
        
        return len(arr)
                
            
        