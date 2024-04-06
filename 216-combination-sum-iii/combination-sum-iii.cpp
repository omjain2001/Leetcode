class Solution {
public:
    void recur(int k, int n, int i, vector<int> &temp, vector<vector<int>> &ans){
        if(n == 0){
            if(temp.size() == k){
                ans.push_back(temp);
            }
            return;
        }
        if(i == 10 || n < 0) return;
        if(n >= i){
            temp.push_back(i);
            recur(k,n-i,i+1,temp,ans);
            temp.pop_back();
        }
        recur(k,n,i+1,temp,ans);
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ans;
        vector<int> temp;
        recur(k,n,1,temp,ans);
        return ans;
    }
};