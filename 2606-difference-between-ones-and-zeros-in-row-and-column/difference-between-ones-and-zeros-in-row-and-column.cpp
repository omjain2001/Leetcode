class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> rows(m,0);
        vector<int> cols(n,0);
        for(int i=0; i<m; i++){
            int cnt_one = 0, cnt_zero = 0;
            for(int j=0; j<n; j++){
                if(grid[i][j] == 1) cnt_one++;
                else cnt_zero++;
            }
            rows[i] = cnt_one - cnt_zero;
        }

        for(int i=0; i<n; i++){
            int cnt_one = 0, cnt_zero = 0;
            for(int j=0; j<m; j++){
                if(grid[j][i] == 1) cnt_one++;
                else cnt_zero++;
            }
            cols[i] = cnt_one - cnt_zero;
        }

        vector<vector<int>> diff(m,vector<int>(n));
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                diff[i][j] = rows[i]+cols[j];
            }
        }       
        return diff; 
    }
};