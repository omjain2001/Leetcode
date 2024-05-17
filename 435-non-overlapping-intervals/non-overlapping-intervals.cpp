class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int> &a, vector<int> &b) -> bool {
            if(a[1] != b[1]) return a[1] < b[1];
            else return a[0] > b[0];
        });
        int end = intervals[0][1];
        int count = 0;
        for(int i=1; i<intervals.size(); i++){
            if(intervals[i][0] >= end){
                end = intervals[i][1];
            } else count++;
        }
        return count;
    }
};