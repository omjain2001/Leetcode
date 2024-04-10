class Solution {
public:
    int recur(vector<int> &nums, int i, vector<int> &arr){
        if(i < 0 || i >= nums.size()) return 0;
        if(arr[i] != -1) return arr[i];
        return arr[i] = max(nums[i] + recur(nums,i-2,arr), recur(nums,i-1,arr));
    }
    int rob(vector<int>& nums) {
        vector<int> arr(nums.size()+1,-1);
        // return recur(nums,nums.size()-1, arr);
        int n = nums.size();
        if(n == 1) return nums[0];
        if(n == 2) return max(nums[0], nums[1]);
        arr[0] = 0;
        arr[1] = nums[0];
        for(int i=2; i<=nums.size(); i++){
            arr[i] = max(nums[i-1] + arr[i-2], arr[i-1]);
        }
        return arr[nums.size()];
    }
};