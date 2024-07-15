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
        vector<vector<int>> dp(coins.size()+1, vector<int>(amount+1, 0));
        // return recur(coins, amount, coins.size()-1, dp);
        for(int i=0; i<=coins.size(); i++) dp[i][0] = 1;
        for(int i=0; i<=amount; i++) dp[0][i] = 0;
        for(int i=1; i<=coins.size(); i++){
            for(int j=1; j<=amount; j++){
                dp[i][j] = dp[i-1][j];
                if(coins[i-1] <= j){
                    dp[i][j] += dp[i][j-coins[i-1]];
                }
            }
        }
        return dp[coins.size()][amount];
    }
};