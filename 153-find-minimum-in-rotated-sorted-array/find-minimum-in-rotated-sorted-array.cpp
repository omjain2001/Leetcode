class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        int l=1, r=n-1;
        if(n == 1) return nums[0];
        if(n == 2) return min(nums[0], nums[1]);
        if(nums[0] < nums[n-1]) return nums[0];
        while(l <= r){
            int mid = (l+r)/2;
            if(nums[mid]>nums[mid-1]){
                if(nums[mid] > nums[0]) l = mid+1;
                else r = mid-1;
            } else return nums[mid];
        }
        return nums[l];
    }
};