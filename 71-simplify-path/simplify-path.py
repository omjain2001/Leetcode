class Solution:
    def simplifyPath(self, path: str) -> str:

        # split the path with '/'
        arr = path.split('/')

        # create a stack and filter the results with empty content
        stack = []
        for ele in arr:
            if ele == "" or ele == ".":
                continue
            elif ele == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(ele)
        
        final_path = '/'.join(stack)

        return '/' + final_path