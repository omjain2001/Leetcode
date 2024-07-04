class Solution {
public:
    long long mod = 1e9+7;
    long long recur(int len, int low, int high, int z, int o, vector<long long> &dp){
        if(len > high) return 0;
        if(dp[len] != -1) return dp[len];
        dp[len] = len >= low ? 1 : 0;
        dp[len] += recur(len + z, low, high, z, o, dp) + recur(len + o, low, high, z, o, dp);
        return dp[len] % mod;
    }
    int countGoodStrings(int low, int high, int zero, int one) {
        vector<long long> dp(high+1, -1);
        return recur(0, low, high, zero, one, dp);
    }
};