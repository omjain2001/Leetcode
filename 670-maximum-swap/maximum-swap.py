class Solution:
    def maximumSwap(self, num: int) -> int:

        arr = list(str(num))
        n = len(arr)
        suffix_arr = [0] * n
        suffix_arr[n-1] = n-1

        for i in range(n-2, -1, -1):
            if int(arr[i]) <= int(arr[suffix_arr[i+1]]):
                suffix_arr[i] = suffix_arr[i+1]
            else:
                suffix_arr[i] = i
        
        for i in range(len(arr)):
            if int(arr[i]) < int(arr[suffix_arr[i]]):
                arr[i], arr[suffix_arr[i]] = arr[suffix_arr[i]], arr[i]
                break
        
        return int(''.join(arr))
        

        