class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int left = INT_MAX;
        int mid = INT_MAX;
        if(nums.size() < 3) return false;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] > mid) return true;
            else if(nums[i] > left && nums[i] <= mid) mid = nums[i];
            else left = nums[i];
        }
        return false;
    }
};