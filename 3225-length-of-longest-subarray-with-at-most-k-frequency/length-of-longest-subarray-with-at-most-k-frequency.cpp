class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        int n = nums.size();
        int l=0, r=0;
        int maxi = INT_MIN;
        while(r < n){
            m[nums[r]]++;
            while(l <= r && m[nums[r]] > k) m[nums[l++]]--;
            maxi = max(maxi, r-l+1);
            r++;
        }
        return maxi;
    }
};