class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(i,j):
            nonlocal board
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if board[i][j] == '$' or board[i][j] == 'X':
                return
            board[i][j] = '$'
            offset = [(0,1), (0,-1), (1,0), (-1,0)]
            for of in offset:
                dfs(i+of[0], j+of[1])

        # Check the edges
        for i in range(n):
            if board[0][i] == 'O':
                dfs(0,i)
            if board[m-1][i] == 'O':
                dfs(m-1,i)
        
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '$':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        