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
    long long tabular(vector<int> &nums){
        int n = nums.size();
        vector<long long> endEven(n, 0);
        vector<long long> endOdd(n, 0);
        endEven[0] = nums[0];
        for(int i=1; i<n; i++){
            endEven[i] = max(endEven[i-1], endOdd[i-1]+nums[i]);
            endOdd[i] = max(endOdd[i-1], endEven[i-1]-nums[i]);
        }
        return max(endEven[n-1], endOdd[n-1]);
    }
    long long maxAlternatingSum(vector<int>& nums) {

        // Memoization
        // vector<vector<long long>> dp(nums.size(), vector<long long>(2, -1));
        // return recur(nums, dp, 0, 0);

        // Tabulation
        return tabular(nums);
    }
};