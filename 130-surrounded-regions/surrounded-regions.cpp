class Solution {
public:
    void dfs(vector<vector<char>> &board, int i, int j, vector<vector<int>> &visited){
        if(i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] == '~') return;
        board[i][j] = '~';
        if(i < board.size()-1 && board[i+1][j] == 'O') dfs(board, i+1, j, visited);
        if(i > 0 && board[i-1][j] == 'O') dfs(board, i-1,j,visited);
        if(j < board[0].size()-1 && board[i][j+1] == 'O') dfs(board, i, j+1, visited);
        if(j > 0 && board[i][j-1] == 'O') dfs(board, i, j-1, visited);
    }
    bool recur(vector<vector<char>> &board, int i, int j, vector<vector<int>> &visited){
        if(i == 0 || i == board.size()-1 || j == 0 || j == board[0].size()-1) return false;
        bool result = true;
        board[i][j] = '-';
        if(board[i][j-1] != 'X' && board[i][j-1] != '-') result &= recur(board, i, j-1, visited);
        if(board[i][j+1] != 'X' && board[i][j+1] != '-') result &= recur(board, i, j+1, visited);
        if(board[i-1][j] != 'X' && board[i-1][j] != '-') result &= recur(board, i-1,j, visited);
        if(board[i+1][j] != 'X' && board[i+1][j] != '-') result &= recur(board, i+1, j, visited);
        if(result) board[i][j] = '~';
        else {
            board[i][j] = 'O';
            visited[i][j] = 1;
        }
        return result;
    }
    bool check(vector<vector<char>> &board, int i, int j){
        if(board[i-1][j] == 'O' || board[i+1][j] == 'O' || board[i][j-1] == 'O' || board[i][j+1] == 'O') return false;
        return true;
    }
    void solve(vector<vector<char>>& board) {
        vector<vector<int>> visited(board.size(), vector<int>(board[0].size(), 0));
    //    for(int i=0; i<board.size(); i++){
    //     for(int j=0; j<board[0].size(); j++){
    //         if(visited[i][j] == 0 && board[i][j] == 'O'){
    //             recur(board, i, j, visited);
    //         } else if(board[i][j] == '~' && check(board, i, j)){
    //             if(check(board,i,j)) board[i][j] = 'X';
    //             else board[i][j] = 'O';
    //         }
    //     }
    //    }
        for (int i=0; i<board[0].size(); i++){
            if(board[0][i] == 'O') dfs(board,0,i,visited);
            if(board[board.size()-1][i] == 'O') dfs(board, board.size()-1,i,visited);
        } 

        for(int i=0; i<board.size(); i++){
            if(board[i][0] == 'O') dfs(board,i,0,visited);
            if(board[i][board[0].size()-1] == 'O') dfs(board,i,board[0].size()-1,visited);
        }

        for(int i=0; i<board.size(); i++){
            for(int j=0; j<board[0].size(); j++){
                if(board[i][j] == '~') board[i][j] = 'O';
                else if(board[i][j] == 'O') board[i][j] = 'X';
            }
        }
    }
};