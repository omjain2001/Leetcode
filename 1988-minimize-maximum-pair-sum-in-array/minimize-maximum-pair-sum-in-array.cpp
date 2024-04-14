class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int mini = INT_MIN;
        int n = nums.size();
        int i=0, j=n-1;
        while(i < j){
            mini = max(mini, nums[i] + nums[j]);
            i++;
            j--;
        }
        return mini;
    }
};