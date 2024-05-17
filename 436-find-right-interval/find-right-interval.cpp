class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        map<int,int> m {{INT_MAX, -1}};
        for(int i=0; i<intervals.size(); i++){
            m[intervals[i][0]] = i;
        }
        vector<int> ans;
        for(int i=0; i<intervals.size(); i++){
            auto itr = m.lower_bound(intervals[i][1]);
            ans.push_back(itr -> second);
        }
        return ans;
    }
};