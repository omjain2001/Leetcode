class Solution {
public:
    int maxVowels(string s, int k) {
        unordered_set<char> st = {'a', 'e', 'i', 'o', 'u'};
        int count = 0;
        int l = 0, r = 0;
        int ans = 0;
        while(r < s.length()){
            if(st.find(s[r]) != st.end()){
                count++;
            }
            if(r >= k-1){
                ans = max(ans, count);
                if(st.find(s[l]) != st.end()) count--;
                l++;
            }
            r++;
        }
        return ans;
    }
};