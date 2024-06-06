class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        for(int i=0; i<grid.size(); i++){
            if(grid[i][0] == 0){
                for(int j=0; j<grid[0].size(); j++){
                    grid[i][j] ^= 1;
                }
            }
        }

        int ans = 0;

        for(int i=0; i<grid[0].size(); i++){
            int count = 0;
            for(int j=0; j<grid.size(); j++){
                if(grid[j][i] == 0) count++;
            }

            if(count > grid.size()/2){
                for(int j=0; j<grid.size(); j++){
                    grid[j][i] ^= 1;
                }
            }
        }

        for(int i=0; i<grid.size(); i++){
            long long pow = 1;
            for(int j=grid[0].size()-1; j>=0; j--){
                ans += pow * grid[i][j];
                pow *= 2;
            }
        }

        return ans;
    }
};