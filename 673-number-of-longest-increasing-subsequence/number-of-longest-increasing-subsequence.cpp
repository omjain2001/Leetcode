class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        vector<int> count(nums.size(), 1);
        int maxi = INT_MIN;
        int ans = 0;
        for(int i=0; i<nums.size(); i++){
            for(int j=0; j<i; j++){
                if(nums[j] < nums[i]){
                    if(dp[i] < dp[j] + 1){
                        dp[i] = dp[j] + 1;
                        count[i] = count[j];
                    } else if(dp[i] == dp[j] + 1){
                        count[i] += count[j];
                    }
                }
            }
            if(maxi < dp[i]){
                maxi = dp[i];
                ans = count[i];
            } else if(maxi == dp[i]){
                ans += count[i];
            }
        }
        return ans;
    }
};