class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while(l <= r):
            mid = (l+r)//2
            
            hours = 0
            for ele in piles:
                hours += (ceil(ele/mid))
            
            if hours <= h:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
            
        