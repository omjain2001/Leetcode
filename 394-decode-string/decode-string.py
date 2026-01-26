class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                string = ""
                while(len(stack) > 0 and stack[-1] != '['):
                    string = stack.pop() + string
                stack.pop()
                num = ""
                while(len(stack) > 0 and stack[-1].isdigit()):
                    num = stack[-1] + num
                    stack.pop()
                string = string * int(num)
                stack.append(string)
            else:
                stack.append(ch)
        
        string = ""
        while(len(stack) > 0):
            string = stack.pop() + string
        return string
            
        