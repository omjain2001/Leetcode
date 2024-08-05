class Solution {
public:
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        set<int> s;
        for(int i=0; i<n; i++) s.insert(i);
        vector<int> ans;
        for(auto ele: queries){
            int st = ele[0];
            int dt = ele[1];
            auto lower = s.lower_bound(st+1);
            auto upper = s.upper_bound(dt-1);
            s.erase(lower, upper);
            ans.push_back(s.size()-1);
        }
        return ans;
    }
};