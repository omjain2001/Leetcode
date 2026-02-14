class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) == 0:
            return ""
        if numRows == 1 or numRows >= len(s):
            return s
        
        result = ""
        for i in range(numRows):
            result += s[i]
            bottom = 2 * (numRows-i-1)
            top = i*2

            temp = i
            while(temp < len(s)):
                temp += bottom
                if bottom > 0 and temp < len(s):
                    result += s[temp]
                temp += top
                if top > 0 and temp < len(s):
                    result += s[temp]
        
        return result
        
        