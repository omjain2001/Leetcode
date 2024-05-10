class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(1,0);
        if(n >= 1) ans.push_back(1);
        for(int i=2; i<=n; i++){
            if(i % 2 == 0) ans.push_back(ans[i/2]);
            else ans.push_back(ans[i/2]+1);
        }
        return ans;
    }
};