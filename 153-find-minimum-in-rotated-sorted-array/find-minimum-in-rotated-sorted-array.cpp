class Solution {
public:
    int findMin(vector<int>& nums) {
       int left = 0;
       int right = nums.size()-1;
       if(nums.size()==1) return nums[0];
       if(nums.size()==2) return min(nums[0],nums[1]);
       while(left < right){
        int mid = (left+right)/2;
        if(mid > 0 && nums[mid] < nums[mid-1]) return nums[mid];
        else if(mid < nums.size()-1 && nums[mid] > nums[mid+1]) return nums[mid+1];
        else if(nums[mid] >= nums[left]) left = mid+1;
        else right = mid-1;
       }
       if(left == nums.size()-1) return nums[0];
       return -1; 
    }
};