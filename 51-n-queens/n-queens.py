class Solution:
    def isValid(self, board, i, j, n, dp_r, dp_c):
        # Check upper column
        if dp_c[j] == 'Q':
            return False
        
        # Check left
        if dp_r[i] == 'Q':
            return False
        
        # Check left upper diagonal
        r = i
        c = j
        while(r >= 0 and c >= 0):
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        
        r = i
        c = j
        # Check upper right diagonal
        while(r >= 0 and c < n):
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        
        # Valid position
        return True

    def recur(self, board, ans, i, cols, left_dig, right_dig):
        if i == len(board):
            temp = [''.join(ele) for ele in board]
            ans.append(temp)
            return

        for j in range(0, len(board)):
            if j in cols or (i+j) in right_dig or (i-j) in left_dig:
                continue
            cols.add(j)
            right_dig.add(i+j)
            left_dig.add(i-j)
            board[i][j] = 'Q'
            self.recur(board, ans, i+1, cols, left_dig, right_dig)
            board[i][j] = '.'
            left_dig.remove(i-j)
            right_dig.remove(i+j)
            cols.remove(j)
            # for q in range(j, n):
            #     if board[p][q] != 'Q' and self.isValid(board, p, q, n, dp_r, dp_c):
            #         board[p][q] = 'Q'
            #         dp_r[p] = 'Q'
            #         dp_c[q] = 'Q'
            #         self.recur(board, ans, p+1, 0, n, placed + 1, dp_r, dp_c)
            #         board[p][q] = '.'
            #         dp_r[p] = '.'
            #         dp_c[q] = '.'
        

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.']*n for i in range(n)]
        # dp_r = ['.']*n
        # dp_c = ['.']*n
        cols = set()
        left_dig = set()
        right_dig = set()
        self.recur(board, ans, 0, cols, left_dig, right_dig)
        return ans