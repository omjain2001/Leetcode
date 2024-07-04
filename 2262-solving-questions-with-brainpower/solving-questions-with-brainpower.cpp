class Solution {
public:
    long long recur(vector<vector<int>> &ques, int i, vector<long long> &dp){
        if(i >= ques.size()) return 0;
        if(dp[i] != -1) return dp[i];
        return dp[i] = max(ques[i][0] + recur(ques, i+ques[i][1]+1, dp), recur(ques, i+1, dp));
    }
    long long mostPoints(vector<vector<int>>& questions) {
        vector<long long> dp(questions.size(), -1);
        return recur(questions, 0, dp);
    }
};