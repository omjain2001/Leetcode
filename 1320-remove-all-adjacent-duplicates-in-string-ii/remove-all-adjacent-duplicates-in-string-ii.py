class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        # Use stack and store (char, count) in stack
        stack = []
        for ele in s:
            if len(stack) > 0 and stack[-1][0] == ele:
                _, count = stack.pop()
                count += 1
                if count < k:
                    stack.append((ele, count))
            else:
                stack.append((ele,1))
        
        result = ""
        for ele in stack:
            result += ele[0] * ele[1]
        return result
        