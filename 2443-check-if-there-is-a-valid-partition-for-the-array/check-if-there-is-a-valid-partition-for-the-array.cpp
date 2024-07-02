class Solution {
public:
    bool recur(vector<int> &nums, int i, vector<int> &dp){
        if(i == nums.size()) return true;
        if(i == nums.size()-1) return dp[i] = false;
        if(dp[i] != -1) return dp[i];
        bool result = false;
        if(nums[i+1] == nums[i]){
            result = result || recur(nums, i+2, dp);
            if(i+2 < nums.size() && nums[i+2] == nums[i+1]){
                result = result || recur(nums, i+3, dp);
            }
            return dp[i] = result;
        } else if((nums.size() - i) >= 3 && nums[i+1] == nums[i] + 1 && nums[i+2] == nums[i] + 2) {
            return dp[i] = (result || recur(nums, i+3, dp));            
        }
        return dp[i] = false;
    }
    bool validPartition(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        return recur(nums, 0, dp);
    }
};