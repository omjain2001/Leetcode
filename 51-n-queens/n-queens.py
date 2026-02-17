class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        rows = [0] * n
        cols = [0] * n

        grid = [['.']*n for _ in range(n)]

        def can_place(i, j):
            if rows[i] == 1 or cols[j] == 1:
                return False
            
            # Check upper left diagonal
            r = i
            c = j
            while(r >= 0 and c >= 0):
                if grid[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            
            r = i
            c = j
            while(r >= 0 and c < n):
                if grid[r][c] == 'Q':
                    return False
                r -= 1
                c += 1
            
            return True

        result = []        

        def recur(row, count):

            # Base condition
            if count == 0:
                result.append([''.join(ele) for ele in grid])
                return
            if row == n:
                return

            for j in range(n):
                if can_place(row, j):
                    rows[row] = 1
                    cols[j] = 1
                    grid[row][j] = 'Q'
                    recur(row+1, count-1)
                    grid[row][j] = '.'
                    rows[row] = 0
                    cols[j] = 0
        
        recur(0, n)
        return result
            
            
        