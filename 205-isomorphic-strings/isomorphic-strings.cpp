class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.length() != t.length()) return false;
        map<char,char> m;
        map<char,char> m2;
        for(int i=0; i<s.length(); i++){
            if(m.find(s[i]) != m.end() && m[s[i]] != t[i]) return false;
            else if(m2.find(t[i]) != m2.end() && m2[t[i]] != s[i]) return false;
            m[s[i]] = t[i];
            m2[t[i]] = s[i];
        }
        return true;
    }
};