class Solution:
    def maxArea(self, height: List[int]) -> int:

        if not height:
            return 0
        
        # Brute force: Compare every pair of lines (O(n^2))

        # Optimal solution
        left = 0
        right = len(height)-1

        maxi = 0

        while(left < right):
            maxi = max(maxi, (right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxi
        
        