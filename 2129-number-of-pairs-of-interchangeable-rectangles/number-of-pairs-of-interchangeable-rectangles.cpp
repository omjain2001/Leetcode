class Solution {
public:
    long long interchangeableRectangles(vector<vector<int>>& rectangles) {
        unordered_map<double,long long> m;
        for(int i=0; i<rectangles.size(); i++){
            m[(double)rectangles[i][0] / (double)rectangles[i][1]]++;
        }
        long long count = 0;
        for(auto ele: m){
            if(ele.second > 1) count += (ele.second * (ele.second - 1)) / 2;
        }
        return count;
    }
};