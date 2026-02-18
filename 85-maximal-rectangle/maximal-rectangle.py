class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def find_largest_rectangle(heights):
            n = len(heights)
            nle = [0] * n
            ple = [0] * n

            stack = []
            for i in range(n):
                while(len(stack) > 0 and heights[stack[-1]] >= heights[i]):
                    stack.pop()
                if len(stack) == 0:
                    ple[i] = -1
                else:
                    ple[i] = stack[-1]
                stack.append(i)
            

            stack = []
            for i in range(n-1, -1, -1):
                while(len(stack) > 0 and heights[stack[-1]] >= heights[i]):
                    stack.pop()
                if len(stack) == 0:
                    nle[i] = n
                else:
                    nle[i] = stack[-1]
                stack.append(i)

            maxHeight = 0

            for i in range(n):
                maxHeight = max(maxHeight, heights[i]*(nle[i]-ple[i]-1))
            
            return maxHeight
        
        n = len(matrix[0])
        hist = [0]*n

        maxRec = 0

        for i in range(len(matrix)):
            for j in range(n):
                if matrix[i][j] == "0":
                    hist[j] = 0
                else:
                    hist[j] += 1 if j > 0 else 1
            
            maxRec = max(maxRec, find_largest_rectangle(hist))
        
        return maxRec
        
        