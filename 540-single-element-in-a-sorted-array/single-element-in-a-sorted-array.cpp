class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        // Solution 1

        // int ans = 0;
        // for(auto ele: nums) ans ^= ele;
        // return ans;
        

        // Solution 2

        int l = 0, r = nums.size()-1;
        while(l < r){
            int mid = (l+r)/2;
            if(mid%2 == 1) mid--;
            if(nums[mid+1] == nums[mid]) l = mid+2;
            else r = mid;
        }
        return nums[l];
    }
};