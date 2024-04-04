class Solution {
public:
    int findPeakElement(vector<int>& nums) {

        // // O(n) approach
        // if(nums.size() == 1) return 0;
        // if(nums[0] > nums[1]) return 0;
        // if(nums[nums.size()-1] > nums[nums.size()-2]) return nums.size()-1;
        // for(int i=1; i<nums.size()-1; i++){
        //     if(nums[i] > nums[i-1] && nums[i] > nums[i+1]) return i;
        // }
        // return -1;

        // O(lgn) approach
        int n = nums.size();
        if(n == 1) return 0;
        if(nums[0] > nums[1]) return 0;
        if(nums[n-1] > nums[n-2]) return n-1;

        int left = 1;
        int right = n-2;
        while(left <= right){
            int mid = (left+right)/2;
            if(nums[mid] > nums[mid+1] && nums[mid] > nums[mid-1]) return mid;\
            else if(nums[mid] < nums[mid-1]) right = mid-1;
            else if(nums[mid] < nums[mid+1]) left = mid+1;
        }
        return -1;
    }
};