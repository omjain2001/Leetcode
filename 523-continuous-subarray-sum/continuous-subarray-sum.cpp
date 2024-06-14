class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        m[0] = -1;
        int cum_sum = 0;
        for(int i=0; i<nums.size(); i++){
            cum_sum += nums[i];
            int remainder = (k == 0) ? remainder : (cum_sum % k);
            if(m.count(remainder)){
                if((i - m[remainder]) > 1) return true;
            } else {
                m[remainder] = i;
            }
        }

        return false;
    }
};