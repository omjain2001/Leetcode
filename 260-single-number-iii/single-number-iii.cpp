class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long long diff = 0;
        for(auto ele: nums) diff ^= ele;
        diff &= -diff;

        vector<int> res = {0,0};
        for(auto ele: nums){
            if((diff & ele) == 0) res[0] ^= ele;
            else res[1] ^= ele;
        }

        return res;
    }
};