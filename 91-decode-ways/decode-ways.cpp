class Solution {
public:
    int recur(string s, int i, int dp[]){
        if(i == 0 && s[i] == '0') return 0;
        if(i == 0 || i < 0) return 1;
        if(dp[i] != -1) return dp[i];
        int sum1 = 0;
        if(s[i] != '0'){
            sum1 = recur(s,i-1,dp);
        }
        int sum2 = 0;
        if(s[i-1] != '0' && stoi(s.substr(i-1,2)) > 9 && stoi(s.substr(i-1,2)) <= 26){
            sum2 = recur(s,i-2,dp);
        }

        return dp[i] = sum1 + sum2;
        
    }
    int numDecodings(string s) {
        int dp[s.length()];
        memset(dp,-1,s.length() * sizeof(int));
        // return recur(s,0,t);
        int n = s.length();
        return recur(s,n-1,dp);
    }
};