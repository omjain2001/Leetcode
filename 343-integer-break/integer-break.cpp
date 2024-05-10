class Solution {
public:
    int recur(vector<int> &arr, int i, int n,vector<int> &dp){
        if(n < 0) return 0;
        if(n == 0 || i == 0) return 1;
        if(dp[n] != -1) return dp[n];
        return dp[n] = max(arr[i] * recur(arr,i,n-arr[i],dp), recur(arr,i-1,n,dp));
    }
    int integerBreak(int n) {
        vector<int> arr;
        vector<int> dp(n+1,-1);
        for(int i=1; i<n; i++) arr.push_back(i);
        return recur(arr,arr.size()-1,n,dp);
    }
};