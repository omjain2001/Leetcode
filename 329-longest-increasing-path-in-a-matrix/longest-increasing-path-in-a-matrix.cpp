class Solution {
public:
    int solve(vector<vector<int>> &matrix, int i, int j, int par, vector<vector<int>> &dp){
        int m = matrix.size();
        int n = matrix[0].size();
        if(i < 0 || i >= m || j < 0 || j >= n) return 0;
        if(matrix[i][j] <= par) return 0;
        if(dp[i][j] != -1) return dp[i][j];
        // vis[i][j] = 1;
        dp[i][j] = 1 + max({solve(matrix, i, j+1, matrix[i][j], dp), solve(matrix, i, j-1, matrix[i][j], dp), solve(matrix, i+1, j, matrix[i][j], dp), solve(matrix, i-1, j, matrix[i][j], dp)});
        // vis[i][j] = 0;
        return dp[i][j];
    }
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int maxi = INT_MIN;
        vector<vector<int>> dp(m, vector<int>(n, -1));
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                // if(i == 1 && j == n-1) cout<<dp[i][j]<<endl;
                // vector<vector<int>> vis(m, vector<int>(n, 0));
                maxi = max(maxi, solve(matrix, i, j, -1, dp));
                // if(i == 1 && j == n-1) cout<<dp[i][j]<<endl;
            }
        }
        return maxi;
    }
};