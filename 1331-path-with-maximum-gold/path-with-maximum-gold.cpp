class Solution {
public:
    int solve(vector<vector<int>> &grid, vector<vector<int>> &vis, vector<vector<int>> &dp, int i, int j){
        int m = grid.size();
        int n = grid[0].size();
        if(i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0 || vis[i][j] == 1) return 0;
        // if(dp[i][j] != -1) return dp[i][j];
        vis[i][j] = 1;
        dp[i][j] = grid[i][j] + max({solve(grid,vis,dp,i+1,j), solve(grid,vis,dp,i-1,j), solve(grid,vis,dp,i,j+1), solve(grid,vis,dp,i,j-1)});
        vis[i][j] = 0;
        return dp[i][j];
    }
    int getMaximumGold(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> vis(m, vector<int>(n, 0));
        vector<vector<int>> dp(m, vector<int>(n, -1));
        int maxi = INT_MIN;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                maxi = max(maxi, solve(grid,vis,dp,i,j));
            }
        }
        return maxi;
    }
};