class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        vector<int> ans;
        int n = nums.size();
        int total_sum = 0;
        for(auto i: nums) total_sum += i;
        int curr = 0;
        for(int i=0; i<n; i++){
            curr += nums[i];
            int lsum = curr - nums[i];
            int rsum = total_sum - curr;
            lsum = nums[i] * (i) - lsum;
            rsum = rsum - (nums[i] * (n - (i+1)));
            ans.push_back(lsum+rsum);
        }
        return ans;
    }
};