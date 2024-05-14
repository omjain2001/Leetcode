class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int num = 1;
        int prod = 9;
        if(n == 0) return 1;
        if(n == 1) return 10;
        vector<int> dp(n,0);
        dp[0] = 10;
        for(int i=1; i<n; i++){
            dp[i] = prod * (10 - num) + dp[i-1];
            prod = prod * (10 - num);
            num++;
        }
        return dp[n-1];
    }
};