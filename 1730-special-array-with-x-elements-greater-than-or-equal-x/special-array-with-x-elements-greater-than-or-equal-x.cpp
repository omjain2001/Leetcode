class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int count = 0;
        int n = nums.size();
        for(int i=0; i<n; i++){
            if(nums[i] == (n-i)) return nums[i];
            else if(nums[i] > (n-i)){
                if(i > 0 && (n-i) > nums[i-1]) return (n-i);
                else if(i == 0 && (n-i) >= 0) return (n-i);
            }
            while(i < n-1 && nums[i] == nums[i+1]) i++;     
        }
        return -1;
    }
};