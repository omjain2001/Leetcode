class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0) return 0;
        vector<int> dp(256, 0);
        int maxi = 1;
        int f = 0;
        for(int i=0; i<s.length(); i++){
            dp[s[i]]++;
            while(dp[s[i]] > 1){
                dp[s[f]]--;
                f++;
            }
            maxi = max(maxi, i-f+1);
        }
        return maxi;
    }
};