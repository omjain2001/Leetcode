class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int n = nums.size();
        if(n == 1) return (nums[0] == target); 
        if(nums[0] == target || nums[n-1] == target) return true;
        int l=1, r=n-2;
        while(l <= r){
            // while(l <= r && nums[l+1] == nums[l]) l++;
            // while(r >= l && nums[r-1] == nums[r]) r--;
            // if(l > r) return (nums[l] == target);
            int mid = (l+r)/2;
            if(nums[mid] == target) return true;
            if((nums[l] == nums[mid]) && (nums[r] == nums[mid])) {
                l++;
                r--;
            }
            else if(nums[mid] >= nums[l]){
                if((target >= nums[l]) && (target < nums[mid])) r = mid-1; 
                else l = mid+1;
            } else {
                if((target > nums[mid]) && (target <= nums[r])) l=mid+1; 
                else r = mid-1;
            }
        }
        return false;
    }
};