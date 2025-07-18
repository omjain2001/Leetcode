import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # if n == 1:
        #     return 1 if k == 1 else -1
        # if n == 2:
        #     return k if k <= 2 else -1
        # i = 1
        # fac = []
        # while(i <= math.ceil(math.sqrt(n))):
        #     if n % i == 0:
        #         fac.append(i)
        #         if i != (n // i):
        #             fac.append(n // i)
        #     i += 1
        
        # fac.sort()
        # if len(fac) < k:
        #     return -1
        # return fac[k-1]

        fac = []
        for i in range(1, n+1):
            if n % i == 0:
                fac.append(i)
        
        if len(fac) < k:
            return -1
        return fac[k-1]
        
        

        