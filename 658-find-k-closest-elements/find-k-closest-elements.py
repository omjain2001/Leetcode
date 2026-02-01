class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # O(nlgn) solution
        # diff_arr = []
        # for ele in arr:
        #     diff_arr.append([abs(x-ele),ele])
        
        # diff_arr.sort(key=lambda x: [x[0],x[1]])

        # result = [ele[1] for ele in diff_arr]
        # result.sort()
        # return result[:k]

        # O(n) solution
        low = 0
        high = len(arr)-1
        while((high-low) >= k):
            if abs(arr[low]-x) > abs(arr[high]-x):
                low += 1
            else:
                high -= 1
        
        result = []
        while(low <= high):
            result.append(arr[low])
            low += 1
        return result
        