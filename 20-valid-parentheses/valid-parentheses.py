from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for ch in s:
            if ch in ('(','[','{'):
                q.append(ch)
            else:
                if (len(q) > 0) and ((ch == ')' and q[-1] == '(') or (ch == ']' and q[-1] == '[') or (ch == '}' and q[-1] == '{')):
                    q.pop()
                else:
                    return False
        
        if len(q) > 0:
            return False
        return True
                