class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s)-1

        left_string = ""
        right_string = ""

        while(l < r):
            # ignore if it is non-alpha char
            if not s[l].isalpha():
                left_string += s[l]
                l += 1
                continue
            if not s[r].isalpha():
                right_string = s[r] + right_string
                r -= 1
                continue
            
            left_string += s[r]
            right_string = s[l] + right_string

            l += 1
            r -= 1
        
        if l == r:
            left_string += s[l]
        
        return left_string + right_string
            
        

            
        


        