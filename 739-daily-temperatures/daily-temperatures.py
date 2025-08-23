class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nle = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while(stack and temperatures[stack[-1]] <= temperatures[i]):
                stack.pop()
            if not stack:
                nle[i] = 0
            else:
                nle[i] = stack[-1] - i
            
            stack.append(i)
        
        return nle