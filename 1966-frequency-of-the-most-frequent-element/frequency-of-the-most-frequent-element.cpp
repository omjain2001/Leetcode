class Solution {
public:
    int recur(vector<int> &nums, int i, int k, int target, vector<vector<int>> &dp){
        if(k == 0 || target-nums[i] > k) return 0;
        if(i == 0){
            if(target-nums[i] <= k) return 1;
            return 0;
        }
        if(dp[i][k-1] != -1) return dp[i][k-1];
        return dp[i][k-1] = 1 + recur(nums,i-1,k-(target-nums[i]),target,dp);
    }
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        long long left = 0, right = 0, res = 0, total = 0;
        while(right < n){
            total += nums[right];
            while(nums[right] * (right-left+1) > total+k){
                total-=nums[left];
                left++;
            }
            res = max(res, (right-left+1));
            right++;
        }
        return res;
    }
};