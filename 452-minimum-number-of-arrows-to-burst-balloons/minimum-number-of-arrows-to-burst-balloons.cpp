class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](vector<int> &a, vector<int> &b) -> bool {
            return a[1] < b[1];
        });

        int count = 1;
        int end = points[0][1];
        for(int i=0; i<points.size(); i++){
            if(points[i][0] > end){
                count++;
                end = points[i][1];
            }
        }
        return count;
    }
};