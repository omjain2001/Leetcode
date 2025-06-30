class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while(l <= r):
            mid = (l + r) // 2

            # Compute hours
            count = 0
            for i in piles:
                count += ceil(i / mid)
            
            if count <= h:
                r = mid - 1
            else:
                l = mid + 1
            
        return l
        