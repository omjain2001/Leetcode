class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        prefix = [1e7] * len(seats)
        for i in range(len(seats)):
            if seats[i] == 1:
                prefix[i] = 0
            else:
                if i > 0:
                    prefix[i] = prefix[i-1] + 1
        
        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                prefix[i] = 0
            else:
                if i < len(seats)-1:
                    prefix[i] = min(prefix[i], prefix[i+1]+1)
        
        return max(prefix)
        