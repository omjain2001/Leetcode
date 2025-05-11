class Solution:
    def isValid(self, board, i, j, n, dp_r, dp_c):
        # Check upper column
        if dp_c[j] == 'Q':
            return False
        # for r in range(i, -1, -1):
        #     if board[r][j] == 'Q':
        #         return False
        
        # Check left
        if dp_r[i] == 'Q':
            return False
        # for c in range(j, -1, -1):
        #     if board[i][c] == 'Q':
        #         return False
        
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

    def recur(self, board, ans, i, j, n, placed, dp_r, dp_c):
        if placed == n:
            temp = [''.join(ele) for ele in board]
            # for r in range(n):
            #     item = ""
            #     for c in board[r]:
            #         item += c
            #     temp.append(item)
            ans.append(temp)
            return
        
        if i < 0 or i >= n or j < 0 or j >= n:
            return

        for p in range(i, n):
            for q in range(j, n):
                if board[p][q] != 'Q' and self.isValid(board, p, q, n, dp_r, dp_c):
                    board[p][q] = 'Q'
                    dp_r[p] = 'Q'
                    dp_c[q] = 'Q'
                    self.recur(board, ans, p+1, 0, n, placed + 1, dp_r, dp_c)
                    board[p][q] = '.'
                    dp_r[p] = '.'
                    dp_c[q] = '.'
        

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.']*n for i in range(n)]
        dp_r = ['.']*n
        dp_c = ['.']*n
        self.recur(board, ans, 0, 0, n, 0, dp_r, dp_c)
        return ans