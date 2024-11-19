class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.length();
        int ans = INT_MIN;
        for(int i=0; i<26; i++){
            int repl = 0;
            int count = 0;
            int l = 0, r = 0;
            int maxi = INT_MIN;
            while(r < n){
                if(s[r] == (char)('A'+i)) count++;
                else repl++;
                if(repl > k){
                    while(l < r && repl > k){
                        if(s[l] == (char)('A'+i)) count--;
                        else repl--;
                        l++;
                    }
                }
                maxi = max(maxi, repl+count);
                r++;
            }
            ans = max(ans, maxi);
        }
        return ans;
    }
};