class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # Two choices
        # 1. Add open paranthesis if open < n
        # 2. Add close paranthesis if close < open

        result = []

        def recur(open, close, ans):
            if close == n:
                result.append(ans)
                return
            
            if open < n:
                recur(open+1, close, ans + '(')
            if close < open:
                recur(open, close+1, ans + ')')
        
        recur(0,0,"")
        return result