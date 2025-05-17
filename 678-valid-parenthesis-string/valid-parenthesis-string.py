class Solution:
    def checkValidString(self, s: str) -> bool:
        mini = 0
        maxi = 0
        for ch in s:
            if ch == '(':
                mini += 1
                maxi += 1
            elif ch == ')':
                mini = max(0, mini-1)
                if maxi == 0:
                    return False
                maxi -= 1
            else:
                mini = max(0, mini-1)
                maxi += 1
        
        if mini == 0:
            return True
        return False
        