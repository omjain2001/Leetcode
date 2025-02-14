class Solution {
public:
    void recur(int open, int close, string temp, int n, vector<string> &ans){
        if(open == n && close == n){
            ans.push_back(temp);
            return;
        }
        if(open < n) recur(open+1, close, temp+'(', n, ans);
        if(close < open) recur(open, close+1, temp+')', n, ans);
        return;
    }
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        recur(0,0,"",n,ans);
        return ans;
    }
};