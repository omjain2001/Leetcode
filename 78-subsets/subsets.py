class Solution:
    def recur(self, i, nums, temp, ans):
        if i >= len(nums):
            ans.append(temp.copy())
            return
        # Not take
        self.recur(i+1, nums, temp, ans)

        # Take
        temp.append(nums[i])
        self.recur(i+1, nums, temp, ans)
        temp.pop()
        # self.recur(i)
        # for j in range(i, len(nums)):
        #     # Take  
        #     temp.append(nums[j])
        #     self.recur(j+1, nums, temp, ans)
        #     temp.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.recur(0, nums, [], ans)
        return ans