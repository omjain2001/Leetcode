class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int mini = INT_MAX;
        int maxi = INT_MIN;
        int st = 0;
        int ed = -1;
        int n = nums.size();
        for(int i=n-1; i >= 0; i--){
            if(nums[i] <= mini) mini = nums[i];
            else st = i;
        }
        for(int i=0; i<n; i++){
            if(nums[i] >= maxi) maxi = nums[i];
            else ed = i;
        }

        return ed-st+1;
    }
};