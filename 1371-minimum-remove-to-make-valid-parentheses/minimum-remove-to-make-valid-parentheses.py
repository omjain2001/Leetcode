class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i+1)
            elif ch == ')':
                if len(stack) > 0 and stack[-1] >= 0:
                    stack.pop()
                else:
                    stack.append(-(i+1))
        
        result = ""
        idx = [abs(ele)-1 for ele in stack]
        for i, ch in enumerate(s):
            if i not in idx:
                result += ch
        
        return result
            
        