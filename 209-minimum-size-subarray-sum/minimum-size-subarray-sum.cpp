class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, r = 0;
        int n = nums.size();
        int sum = 0;
        int mini = INT_MAX;
        while(r < n){
            sum += nums[r];
            while(l <= r && sum >= target){
                mini = min(mini, (r-l+1));
                sum -= nums[l];
                l++;
            }
            r++;
        }
        while(l < r && sum >= target){
            mini = min(mini, (r-l));
            sum -= nums[l];
            l++;
        }
        if(mini == INT_MAX) return 0;
        return mini;
    }
};