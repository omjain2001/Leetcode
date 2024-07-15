class Solution {
public:
    bool recur(vector<int> &piles, int i, int j, int sum, int total, vector<vector<int>> &dp){
        if((j-i+1) == piles.size()/2) return sum > (total / 2);
        if(dp[i][j] != -1) return dp[i][j];
        return dp[i][j] = recur(piles, i+1, j, sum + piles[i], total, dp) || recur(piles, i, j-1, sum+piles[j], total, dp);
    }
    bool stoneGame(vector<int>& piles) {
        int total = 0;
        vector<vector<int>> dp(piles.size(), vector<int>(piles.size(), -1));
        for(auto ele: piles) total += ele;
        return recur(piles, 0, piles.size()-1, 0, total, dp);
    }
};