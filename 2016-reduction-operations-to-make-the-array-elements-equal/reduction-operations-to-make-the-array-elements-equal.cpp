class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        int ops = 0;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int i = n-1;
        while(i >= 0){
            int j = i;
            while(i > 0 && nums[i] == nums[i-1]) i--;
            if(i == 0) break;
            ops += (n-i);
            i--;
        }
        return ops;
    }
};