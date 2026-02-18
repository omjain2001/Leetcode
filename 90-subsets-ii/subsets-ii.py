class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = set()

        for i in range(pow(2,len(nums))):
            temp = i
            idx = 0
            take = []
            while(temp):
                if temp & 1:
                    take.append(nums[idx])
                idx += 1
                temp = temp >> 1
            result.add(tuple(take))
        
        return [list(ele) for ele in result]
        
        


        