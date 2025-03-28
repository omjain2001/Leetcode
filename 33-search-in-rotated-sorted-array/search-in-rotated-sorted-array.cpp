class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        // if(nums[0] == target) return 0;
        int l=0, r=n-1;
        while(l <= r){
            int mid = (l+r)/2;
            if(nums[mid] == target) return mid;
            if(nums[0] <= nums[mid]){
                if(target >= nums[0] && target <= nums[mid]) r = mid-1;
                else l = mid+1;
            } else {
                if(target >= nums[mid] && target <= nums[n-1]) l = mid+1;
                else r = mid-1;
            }
        }
        return -1;
    }
};