class Solution {
public:
    int minFlips(vector<vector<int>>& grid) {
        int ans = 0;
        int totalOnes = 0;
        int m = grid.size();
        int n = grid[0].size();
        for(int i=0; i<m/2; i++){
            for(int j=0; j<n/2; j++){
                int ones = 0;
                if(grid[i][j] == 1) ones++;
                if(grid[i][n-j-1] == 1) ones++;
                if(grid[m-i-1][j] == 1) ones++;
                if(grid[m-i-1][n-j-1] == 1) ones++;

                if(ones == 4 || ones == 0){
                    totalOnes += ones;
                } else if(ones >= 2){
                    ans += (4-ones);
                    totalOnes += 4;
                } else {
                    ans += ones;
                }
            }
        }

        if(m % 2 == 0 && n % 2 == 0) return ans;
        int palidOnes = 0, oneChange = 0;
        if(m % 2 == 1){
            for(int i=0; i<n/2; i++){
                if(grid[m/2][i] == 1 && grid[m/2][n-i-1] == 1) palidOnes++;
                if(grid[m/2][i] != grid[m/2][n-i-1]){
                    oneChange++;
                    ans++;
                }
            }
        }

        if(n % 2 == 1){
            for(int i=0; i<m/2; i++){
                if(grid[i][n/2] == 1 && grid[m-i-1][n/2] == 1) palidOnes++;
                if(grid[i][n/2] != grid[m-i-1][n/2]){
                    oneChange++;
                    ans++;
                }
            }
        }

        if(palidOnes % 2 == 1){
            if(oneChange == 0) ans += 2;
        }

        if(m%2 == 1 && n%2 == 1 && grid[m/2][n/2] == 1) ans++;

        return ans;
    }
};