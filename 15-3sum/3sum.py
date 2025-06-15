class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        target = 0
        while(i < len(nums)-2):
            j = i+1
            k = len(nums)-1
            while(j < k):
                add = nums[i] + nums[j] + nums[k]
                if add == target:
                    ans.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif add > target:
                    temp = nums[k]
                    while(k > j and nums[k] == temp):
                        k -= 1
                else:
                    temp = nums[j]
                    while(j < k and nums[j] == temp):
                        j += 1
            
            temp = nums[i]
            while(i < len(nums)-2 and nums[i] == temp):
                i += 1
        ans = list(set(ans))
        ans = [list(ele) for ele in ans]
        return ans