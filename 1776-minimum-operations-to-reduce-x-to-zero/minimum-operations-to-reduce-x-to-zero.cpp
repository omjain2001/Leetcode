class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int l=0, r=0;
        int n = nums.size();
        int currsum = 0;
        int sum = 0;
        for(auto ele: nums) sum+=ele;
        int maxi = INT_MIN;
        while(r < n){
            currsum += nums[r];
            while(l <= r && currsum > (sum-x)) currsum -= nums[l++];
            if(currsum == sum-x) maxi = max(maxi, r-l+1);
            r++;
        }
        if(maxi == INT_MIN) return -1;
        return (n-maxi);
    }
};