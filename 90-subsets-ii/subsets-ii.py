class Solution:
    def recur(self, nums, idx, temp, ans):
        ans.append(temp)        
        for start in range(idx, len(nums)):
            if start > idx and nums[start] == nums[start-1]:
                continue
            self.recur(nums, start+1, temp + [nums[start]], ans)
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.recur(nums, 0, [], ans)
        return ans
        