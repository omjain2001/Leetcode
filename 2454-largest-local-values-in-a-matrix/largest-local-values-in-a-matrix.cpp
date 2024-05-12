class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int c1 = INT_MIN, c2 = INT_MIN, c3 = INT_MIN;
        int n = grid.size();
        vector<vector<int>> ans;
        for(int i=0; i<n-2; i++){
            vector<int> temp;
            for(int j=0; j<3; j++){
                for(int k=i; k<i+3; k++){
                    if(j == 0) c1 = max(c1,grid[k][j]);
                    if(j == 1) c2 = max(c2,grid[k][j]);
                    if(j == 2) c3 = max(c3, grid[k][j]);
                }
            }
            temp.push_back(max({c1,c2,c3}));
            for(int j=3; j<n; j++){
                c1 = c2;
                c2 = c3;
                c3 = INT_MIN;
                for(int k=i; k<i+3; k++) c3 = max(c3,grid[k][j]);
                temp.push_back(max({c1,c2,c3}));
            } 
            ans.push_back(temp);
            c1 = INT_MIN;
            c2 = INT_MIN;
            c3 = INT_MIN;
        }
        return ans;
    }
};