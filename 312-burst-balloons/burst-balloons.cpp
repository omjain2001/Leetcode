class Solution {
public:
    int solve(vector<int> &nums, int i, int j, vector<vector<int>> &dp){
        if(i > j) return 0;
        if(dp[i][j] != -1) return dp[i][j];
        if(i == j){
            int temp = nums[i];
            if(i-1 >= 0) temp *= nums[i-1];
            if(j+1 < nums.size()) temp *= nums[j+1];
            return dp[i][j] = temp;
        } else {
            int ans = INT_MIN;
            for(int k=i; k<=j; k++){
                int temp = nums[k];
                if(i-1 >= 0) temp *= nums[i-1];
                if(j+1 < nums.size()) temp *= nums[j+1];

                ans = max(ans, temp + solve(nums,i,k-1,dp) + solve(nums,k+1,j,dp));
            }
            return dp[i][j] = ans;
        }
    }

    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n, -1));
        return solve(nums,0,n-1,dp);
    }
};