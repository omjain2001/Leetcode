class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:

        MAX = float('inf')

        def solve(target):
            arr = [ele for ele in nums]
            count = 0
            for i in range(len(arr)-1):
                if arr[i] != target:
                    count += 1
                    arr[i] = -arr[i]
                    arr[i+1] = -arr[i+1]
            
            if arr[len(arr)-1] == target:
                return count
            return MAX
        
        return (solve(1) <= k or solve(-1) <= k)
        