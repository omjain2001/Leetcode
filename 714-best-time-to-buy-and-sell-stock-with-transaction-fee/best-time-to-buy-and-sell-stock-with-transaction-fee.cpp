class Solution {
public:
    int recur(vector<int> &prices, int idx, int buy, int fee, vector<vector<int>> &dp){
        if(idx == prices.size()) return 0;
        if(dp[idx][buy] != -1) return dp[idx][buy];
        if(buy == 1){
            return dp[idx][buy] = max(-prices[idx]-fee+recur(prices,idx+1,0,fee,dp), recur(prices,idx+1,buy,fee,dp));
        } else {
            return dp[idx][buy] = max(prices[idx]+recur(prices,idx+1,1,fee,dp), recur(prices,idx+1,buy,fee,dp));
        }
    }
    int maxProfit(vector<int>& prices, int fee) {
        vector<vector<int>> dp(prices.size(), vector<int>(2,-1));
        return recur(prices,0,1,fee,dp);
    }
};