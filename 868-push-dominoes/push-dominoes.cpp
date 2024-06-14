class Solution {
public:
    string pushDominoes(string dominoes) {
        int right = -1;
        int n = dominoes.length();
        string ans = dominoes;
        for(int i=0; i<n; i++){
            if(ans[i] == '.') continue;
            else if(ans[i] == 'L'){
                if(right == -1){
                    for(int j=i-1; j >= 0 && ans[j] != 'L'; j--) ans[j] = 'L';
                } else {
                    for(int j=right+1, k=i-1; j < k; j++, k--){
                        ans[j] = 'R';
                        ans[k] = 'L';
                    }
                    right = -1;
                }
            } else {
                if(right != -1){
                    for(int j=right+1; j<i; j++) ans[j] = 'R';
                }
                right = i;
            }
        }

        if(right != -1){
            for(int j=right+1; j<n; j++) ans[j] = 'R';
        }

        return ans;
    }
};