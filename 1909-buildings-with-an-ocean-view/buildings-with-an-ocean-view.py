class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        n = len(heights)
        suffix = [0] * n
        result = []

        if n == 0:
            return []

        suffix[n-1] = heights[n-1]
        result.append(n-1)

        for i in range(n-2, -1, -1):
            if heights[i] > suffix[i+1]:
                result.append(i)
            
            suffix[i] = max(suffix[i+1], heights[i])
        
        return result[::-1]
        