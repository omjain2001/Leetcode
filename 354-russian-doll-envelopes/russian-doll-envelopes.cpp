class Solution {
public:
    int solve(vector<vector<int>> &envelopes, int i, int prev, vector<vector<int>> &dp){
        if(i < 0) return 0;
        int sum1 = 0;
        if(dp[i][prev] != -1) return dp[i][prev];
        if(envelopes[i][0] < envelopes[prev][0] && envelopes[i][1] < envelopes[prev][1]){
            sum1 = 1 + solve(envelopes, i-1, i, dp);
        }
        return dp[i][prev] = max(sum1, solve(envelopes, i-1, prev, dp));
    }
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        // vector<vector<int>> arr(envelopes.begin(), envelopes.end());
        // arr.push_back({INT_MAX, INT_MAX});
        // sort(arr.begin(), arr.end());
        // int n = envelopes.size();
        // vector<vector<int>> dp(n+1, vector<int>(n+1, -1));
        // return solve(arr, n-1, n, dp);
        sort(envelopes.begin(), envelopes.end(), [](vector<int> &a, vector<int> &b) -> bool {return a[0] == b[0] ? b[1] < a[1] : a[0] < b[0];});
        vector<int> dp;
        for(auto ele: envelopes){
            int height = ele[1];
            int left = lower_bound(dp.begin(), dp.end(), height) - dp.begin();
            if(left == dp.size()) dp.push_back(height);
            else dp[left] = height;
        }
        return dp.size();
    }
};