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

        // Approach 1
        // int num = (int)floor(sqrt(n));
        // vector<vector<int>> dp(num,vector<int>(n, -1));
        // return recur(num,n,dp);

        // Approach 2
        int dp[n + 1];
        for (int i = 0; i <= n; ++i) {
            dp[i] = i;
        }
        int sq = sqrt(n);
        for (int i = 2; i <= sq; ++i) {
            for (int j = i * i; j <= n; ++j) {
                dp[j] = min(dp[j], dp[j - i * i] + 1);
            }
        }
        return dp[n];
    }
};