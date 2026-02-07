class Solution:
    def reverse(self, x: int) -> int:

        MAX = pow(2, 31) - 1
        MIN = -pow(2, 31)

        num = 0
        while(x):
            if num > MAX//10 or (num == MAX//10 and int(math.fmod(x,10)) > MAX % 10):
                return 0
            if num < int(MIN/10) or (num == int(MIN/10) and math.fmod(x,10) < math.fmod(MIN,10)):
                return 0
            
            num = num * 10 + int(math.fmod(x, 10))
            x = int(x/10)
        return num
        