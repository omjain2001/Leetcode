class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        i = 0
        j = len(height)-1

        while(i < j):
            maxi = max(maxi, min(height[i], height[j]) * (j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        
        return maxi
        