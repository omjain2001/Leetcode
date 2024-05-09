class Solution {
public:
    int recur(int n, int target, vector<vector<int>> &dp){
        if(target == 0) return 0;
        if(n == 1) return target;
        if(dp[n-1][target-1] != -1) return dp[n-1][target-1];
        int ans1 = 0;
        if(n*n <= target){
            ans1 = 1 + recur((int)floor(sqrt(target-n*n)), target-n*n, dp);
        }
        return dp[n-1][target-1] = min(ans1, recur(n-1,target,dp));
    }
    int numSquares(int n) {
        int num = (int)floor(sqrt(n));
        vector<vector<int>> dp(num,vector<int>(n, -1));
        return recur(num,n,dp);
    }
};