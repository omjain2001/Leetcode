class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

        nums = list(hashmap.keys())
        nums.sort(reverse=True)

        result = ""

        i = 0
        while(num > 0):
            n = num // nums[i]
            if n > 0:
                while(n):
                    result += hashmap[nums[i]]
                    num -= nums[i]
                    n -= 1
                print(result)
            i += 1
        
        return result
            
        