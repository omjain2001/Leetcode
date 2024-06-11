class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int,int> m;
        for(auto vec: wall){
            if(vec.size() > 1){
                int sum = vec[0];
                m[sum]++;
                for(int i=1; i<vec.size()-1; i++){
                    sum += vec[i];
                    m[sum]++;
                }
            }
        }
        int maxi = 0;
        for(auto ele: m){
            if(ele.second > maxi){
                maxi = ele.second;
            }
        }
        // if(maxi == wall.size()) return wall.size();
        return wall.size() - maxi;
    }
};