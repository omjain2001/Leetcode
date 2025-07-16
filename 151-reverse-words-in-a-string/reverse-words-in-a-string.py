class Solution:
    def reverseWords(self, s: str) -> str:

        n = len(s)
        i = n-1
        result = ""
        temp = ""

        while(i >= 0 and s[i].isspace()):
            i -= 1
        
        while(i >= 0):
            if s[i].isalnum():
                temp = s[i] + temp
                i -= 1
            else:
                result += temp + " "
                temp = ""
                i -= 1
                while(i >= 0 and s[i].isspace()):
                    i -= 1
        
        if len(temp) > 0:
            result += temp + " "
        return result[:-1]
            
        
        