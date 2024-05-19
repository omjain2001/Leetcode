class Solution {
public:
    string frequencySort(string s) {
        sort(s.begin(),s.end());
        set<pair<int,char>> fre;
        for(int i=0; i<s.length(); i++){
            int count = 1;
            while(s[i+1] == s[i]){
                count++;
                i++;
            }
            fre.insert({count, s[i]});
        }
        string ans = "";
        for(auto ele = fre.rbegin(); ele != fre.rend(); ele++){
            int n = ele->first;
            while(n--) ans += ele->second;
        }
        return ans;
    }
};