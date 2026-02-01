class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        count = 0
        prev = 0
        i = 0
        while(i < len(arr)):
            missing = arr[i]-prev-1
            if missing > 0:
                if (count + missing) < k:
                    count += missing
                else:
                    break
            prev = arr[i]
            i += 1
        
        if i > 0:
            return arr[i-1]+(k-count)
        else:
            return k
        