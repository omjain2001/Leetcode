class Solution {
public:
    int minDistance(string word1, string word2) {
        int n1 = word1.length();
        int n2 = word2.length();
        int mat[n1+1][n2+1];
        for(int i=0; i<n2+1; i++){
            mat[0][i] = i;
        }
        for(int i=0; i<n1+1; i++){
            mat[i][0] = i;
        }
        for(int i=1; i<n1+1; i++){
            for(int j=1; j<n2+1; j++){
                if(word1[i-1] == word2[j-1]) mat[i][j] = mat[i-1][j-1];
                else mat[i][j] = min(1 + mat[i-1][j-1], min(mat[i][j-1] + 1, mat[i-1][j] + 1));
            }
        }

        return mat[n1][n2];
    }
};