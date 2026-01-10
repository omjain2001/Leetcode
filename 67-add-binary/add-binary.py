class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a)-1
        j = len(b)-1

        res = ""
        carry = 0

        while(i >= 0 and j >= 0):
            total = int(a[i]) + int(b[j]) + carry
            if total <= 1:
                carry = 0
                res = str(total) + res
            elif total == 2:
                carry = 1
                res = "0" + res
            else:
                carry = 1
                res = "1" + res
            
            i -= 1
            j -= 1
        

        while(i >= 0):
            total = int(a[i]) + carry
            if total <= 1:
                carry = 0
                res = str(total) + res
            elif total == 2:
                carry = 1
                res = "0" + res
            i -= 1
        
        while(j >= 0):
            total = int(b[j]) + carry
            if total <= 1:
                carry = 0
                res = str(total) + res
            elif total == 2:
                carry = 1
                res = "0" + res
            j -= 1

        if carry == 1:
            res = str(carry) + res

        return res    
        