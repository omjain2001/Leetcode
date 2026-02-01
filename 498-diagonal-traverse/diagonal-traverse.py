class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if not mat or not mat[0]:
            return []
        
        n,m = len(mat), len(mat[0])

        result, intermediate = [], []

        for d in range(0, n+m-1):

            r = 0 if d < m else d-m+1
            c = d if d < m else m-1

            while r < n and c >= 0:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

            intermediate.clear() 
        
        return result
        