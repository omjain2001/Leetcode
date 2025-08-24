class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        l = 0
        r = m*n - 1

        while(l <= r):
            mid = (l+r)//2
            row = mid//n
            col = mid%n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid+1
            else:
                r = mid-1       
        return False
        