class Solution {
public:
    int longestIdealString(string s, int k) {
        vector<int> dp(27, 0);
        int n = s.length();
        for(int i=s.length()-1; i>=0; i--){
            int idx = s[i]-'a';
            int left = max(idx-k, 0);
            int right = min(idx+k, 26);
            int maxi = INT_MIN;
            for(int j=left; j<=right; j++){
                maxi = max(maxi, dp[j]);
            }
            dp[idx] = maxi + 1;
        }
        int ans = INT_MIN;
        for(int i=0; i<27; i++){
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};