class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        if(s.size() < 3) return *s.rbegin();
        else {
            int count = 0;
            for(auto itr = s.rbegin(); itr != s.rend(); itr++){
                if(count == 2) return *itr;
                count++;
            }
        }
        return 0;
    }
};