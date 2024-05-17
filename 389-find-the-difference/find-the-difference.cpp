class Solution {
public:
    char findTheDifference(string s, string t) {
        int count = 0;
        for(int i=0; i<s.size(); i++){
            count ^= ((int)s[i] ^ (int)t[i]);
        }
        count ^= (int)t[s.size()];
        return (char)count;
    }
};