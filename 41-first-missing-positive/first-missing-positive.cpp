class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        set<int> s;
        int maxi = INT_MIN;
        for(int i=0; i<nums.size(); i++) {
            s.insert(nums[i]);
            maxi = max(maxi, nums[i]);
        }
        for(int i=1; i<maxi; i++){
            if(s.find(i) == s.end()) return i;
        }
        if(maxi < 0) return 1;
        return maxi + 1;
    }
};