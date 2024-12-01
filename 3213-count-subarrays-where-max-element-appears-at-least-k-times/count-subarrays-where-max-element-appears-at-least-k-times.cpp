class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        long long count = 0;
        int n = nums.size();
        int l = 0, r = 0;
        int maxElement = INT_MIN;
        int countK = 0;
        for(auto ele: nums) maxElement = max(maxElement, ele);
        while(r < n){
            if(nums[r] == maxElement) countK++;
            while(l <= r && countK >= k){
                count += (n-r);
                if(nums[l++] == maxElement) countK--;
            }
            r++; 
        }
        return count;
    }
};