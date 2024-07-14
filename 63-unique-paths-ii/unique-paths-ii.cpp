class Solution {
public:
    int recur(vector<vector<int>> &obstacleGrid, vector<vector<int>> &dp, int i, int j){
        if(i >= obstacleGrid.size() || j >= obstacleGrid[0].size()) return 0;
        if(dp[i][j] != -1) return dp[i][j];
        if(obstacleGrid[i][j] == 1) return dp[i][j] = 0;
        if(i == obstacleGrid.size()-1 && j == obstacleGrid[0].size()-1) return 1;
        return dp[i][j] = recur(obstacleGrid, dp, i+1, j) + recur(obstacleGrid, dp, i, j+1);
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        vector<vector<int>> dp(obstacleGrid.size(), vector<int>(obstacleGrid[0].size(), -1));
        return recur(obstacleGrid, dp, 0, 0);
    }
};