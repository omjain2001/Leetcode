class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 1:
            return 1

        def recur(x, num):

            if num == 0:
                return 1
            
            if num == 1:
                return x
            
            total = 1
            if num % 2 == 0:
                total = recur(x, num // 2)
                return total * total
            else:
                total = recur(x, (num-1) // 2)
                return x * (total * total)
        
        ans = 0
        if n < 0:
            ans = recur(x, abs(n))
            return 1 / ans
        else:
            ans = recur(x,n)
            return ans

        