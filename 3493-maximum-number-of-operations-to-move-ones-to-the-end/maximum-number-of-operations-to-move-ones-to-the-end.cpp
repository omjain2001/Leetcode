class Solution {
public:
    int maxOperations(string s) {
        int count = 0;
        int ans = 0;
        for(int i=0; i<s.length(); i++){
            if(s[i] == '0'){
                ans += count;
                while(i < s.length() && s[i] == '0') i++;
            }
            count++;
        }
        return ans;
    }
};