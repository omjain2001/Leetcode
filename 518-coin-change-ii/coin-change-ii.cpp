class Solution {
public:
    int recur(vector<int> &coins, int amount, int i, vector<vector<int>> &dp){
        if(i < 0 || amount < 0) return 0;
        if(amount == 0) return 1;
        if(i == 0){
            if(amount % coins[i] == 0) return 1;
            return 0;
        }
        if(dp[i][amount] != -1) return dp[i][amount];
        return dp[i][amount] = recur(coins, amount - coins[i], i, dp) + recur(coins, amount, i-1, dp);
    }
    int change(int amount, vector<int>& coins) {
        vector<vector<int>> dp(coins.size(), vector<int>(amount+1, -1));
        return recur(coins, amount, coins.size()-1, dp);
    }
};