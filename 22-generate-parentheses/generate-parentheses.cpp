class Solution {
public:
    void recur(string s, int i, string temp, vector<string> &ans){
        if(temp.length() == (2*s.length())){
            ans.push_back(temp);
            return;
        }
        if(i == s.length()) return recur(s, i, temp + ')', ans);
        if(temp.length() == 0) return recur(s, i+1, temp+'(', ans);
        recur(s, i+1, temp+'(', ans);
        recur(s, i, temp+')', ans);
        return;
    }
    void recur_2(int open, int close, string temp, int n, vector<string> &ans){
        if(open == n && close == n){
            ans.push_back(temp);
            return;
        }
        if(open < n) recur_2(open+1, close, temp+'(', n, ans);
        if(close < open) recur_2(open, close+1, temp+')', n, ans);
        // recur_2(open+1, close, temp+'(', n, ans);
        // recur_2(open, close+1, temp+')', n, ans);
        return;
    }
    vector<string> generateParenthesis(int n) {
        string s = "";
        for(int i=0; i<n; i++) s+='(';
        vector<string> ans;
        // recur(s, 0, "", ans);
        recur_2(0,0,"",n,ans);
        return ans;
    }
};