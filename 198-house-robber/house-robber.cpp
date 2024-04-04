class Solution {
public:
    int recur(vector<int> &nums, int i, vector<int> &arr){
        if(i < 0 || i >= nums.size()) return 0;
        if(arr[i] != -1) return arr[i];
        return arr[i] = max(nums[i] + recur(nums,i-2,arr), recur(nums,i-1,arr));
    }
    int rob(vector<int>& nums) {
        vector<int> arr(nums.size(),-1);
        return recur(nums,nums.size()-1, arr);
    }
};