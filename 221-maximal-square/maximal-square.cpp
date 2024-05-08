class Solution {
public:
    int maxi = 0;
    int recur(vector<vector<char>> &matrix, vector<vector<int>> &dp, int r, int c){
        int rows = matrix.size();
        int cols = matrix[0].size();
        if(r > rows || c > cols) return 0;
        if(dp[r-1][c-1] != -1) return dp[r-1][c-1];
        int right = recur(matrix, dp, r, c+1);
        int down = recur(matrix, dp, r+1, c);
        int diag = recur(matrix, dp, r+1, c+1);
        dp[r-1][c-1] = 0;
        if(matrix[r-1][c-1] == '1'){
            dp[r-1][c-1] = 1 + min({right,down,diag});
        }
        maxi = max(maxi, dp[r-1][c-1]);
        return dp[r-1][c-1];
    }
    int maximalSquare(vector<vector<char>>& matrix) {
        vector<vector<int>> dp(matrix.size(), vector<int>(matrix[0].size(), -1));
        recur(matrix,dp,1,1);
        return maxi * maxi;
    }
};