class Solution {
public:
    void recur(string s, string ans, unordered_map<string,int> &m, int i, int mini, int maxi, vector<string> &result){
        if(i < 0){
            result.push_back(ans.substr(1, ans.length()-1));
            return;
        }
        int right = max(i-mini+1,0);
        int left = max(i-maxi+1,0);
        for(int j=right; j>=left; j--){
            string sub = s.substr(j, i-j+1);
            if(m.find(sub) != m.end()){
                recur(s, " " + sub + ans, m, j-1, mini, maxi, result);
            }
        }
    }
    vector<string> wordBreak(string s, vector<string>& wordDict) {
       unordered_map<string, int> m;
       int mini = INT_MAX;
       int maxi = INT_MIN;
       for(auto ele: wordDict){
        m[ele]++;
        mini = min(mini, (int)ele.length());
        maxi = max(maxi, (int)ele.length());
       }
       vector<string> result;
       recur(s,"",m,s.length()-1,mini,maxi,result);
       return result;
    }
};