import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 1e7
        minspeed = -1

        while(left <= right):
            mid = (left + right) // 2

            total = 0
            for i in range(len(dist)):
                if i < len(dist)-1:
                    total += math.ceil(dist[i]/mid)
                else:
                    total += dist[i]/mid
            
            if total > hour:
                left = mid + 1
            else:
                minspeed = mid
                right = mid - 1
        
        # if left < len(dist):
        #     return left
        # return -1
        return int(minspeed)
             
        