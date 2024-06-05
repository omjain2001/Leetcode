class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        vector<int> cols(grid[0].size(),INT_MIN);
        vector<int> rows(grid.size(),INT_MIN);
        for(int i=0; i<rows.size(); i++){
            for(int j=0; j<cols.size(); j++){
                rows[i] = max(rows[i], grid[i][j]);
            }
        }

        for(int i=0; i<cols.size(); i++){
            for(int j=0; j<rows.size(); j++){
                cols[i] = max(cols[i], grid[j][i]);
            }
        }

        int ans = 0;
        for(int i=0; i<rows.size(); i++){
            for(int j=0; j<cols.size(); j++){
                ans += min(rows[i],cols[j]) - grid[i][j];
            }
        }

        return ans;
    }
};