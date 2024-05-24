class Solution {
public:
    int longestPalindrome(string s) {
        map<char,int> m;
        for(int i=0; i<s.length(); i++){
            m[s[i]]++;
        }

        int ans = 0;
        int max_odd = 0;
        int odd_count = 0;
        for(auto ele: m){
            if(ele.second % 2 == 0) ans += ele.second;
            else odd_count++;
        }
        if(odd_count > 1) return s.length() - odd_count + 1;
        return s.length();
    }
};