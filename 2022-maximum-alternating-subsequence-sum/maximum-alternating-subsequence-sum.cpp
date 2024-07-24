class Solution {
public:
    long long recur(vector<int> &nums, vector<vector<long long>> &dp, int i, int j){
        if(i >= nums.size()) return 0;
        if(dp[i][j] != -1) return dp[i][j];
        long long take = 0;
        if(j == 0) take = nums[i] + recur(nums, dp, i+1, 1);
        else take = -nums[i] + recur(nums, dp, i+1, 0);
        long long notTake = recur(nums, dp, i+1, j);
        return dp[i][j] = max(take, notTake);
    }
    long long maxAlternatingSum(vector<int>& nums) {
        vector<vector<long long>> dp(nums.size(), vector<long long>(2, -1));
        return recur(nums, dp, 0, 0);
    }
};