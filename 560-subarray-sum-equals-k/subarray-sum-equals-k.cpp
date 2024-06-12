class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        m[0]++;
        int sum = 0;
        int count = 0;
        for(int i=0; i<nums.size(); i++){
            sum += nums[i];
            if(m.find(sum - k) != m.end()) count += m[sum-k];
            m[sum]++;
        }
        return count;
    }
};