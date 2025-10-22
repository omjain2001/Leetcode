import math
class Solution:
    def reverse(self, x: int) -> int:

        num = 0
        MAX = 2**31-1
        MIN = -(2**31)

        while(x):
            digit = int(math.fmod(x, 10))
            if (num > (MAX // 10)) or ((num == (MAX // 10)) and digit > (MAX % 10)):
                return 0
            elif (num < MIN // 10) or (num == MIN // 10 and digit < MIN % 10):
                return 0
            
            num = num * 10 + digit
            x = int(x / 10)
        
        return num

        