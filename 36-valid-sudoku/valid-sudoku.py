class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rows = [[0] * n for _ in range(m)]
        cols = [[0] * n for _ in range(m)]
        mat = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j].isdigit():
                    num = int(board[i][j]) - 1

                    k = i//3 * 3 + j//3
                    if rows[i][num] or cols[j][num] or mat[k][num]:
                        return False
                    
                    rows[i][num] = cols[j][num] = mat[k][num] = 1
        
        return True

        