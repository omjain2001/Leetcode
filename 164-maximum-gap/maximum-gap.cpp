class Solution {
public:
    int maximumGap(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        set<int>::iterator itr = s.begin();
        int maxi = 0;
        int prev = *itr;
        while(++itr != s.end()){
            maxi = max(maxi, *itr - prev);
            prev = *itr;
        }
        return maxi;
    }
};