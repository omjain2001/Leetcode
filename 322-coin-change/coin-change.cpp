class Solution {
public:
    int recur(vector<int> &coins, int amount, int i, vector<vector<long>> &dp){
        if(i == 0 || amount < 0) return INT_MAX - 2;
        if(amount == 0) return 0;
        if(dp[i][amount] != -1) return dp[i][amount];
        return dp[i][amount] = min(1 + recur(coins, amount - coins[i-1], i, dp), recur(coins, amount, i-1, dp));
    }
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<vector<long>> dp(n+1, vector<long>(amount+1, -1));
        fill(dp[0].begin(), dp[0].end(), 0);
        for(int i=0; i<=n; i++){
            dp[i][0] = 1;
        }
        long ans = recur(coins, amount, n, dp);
        if(ans == INT_MAX - 2) return -1;
        return ans;
    }
};