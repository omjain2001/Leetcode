class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        map<char,int> sm, pm;
        for(auto ele: p) pm[ele]++;
        int start = 0, end = 0;
        vector<int> ans;
        while(end < s.length()){
            // cout<<start<<" "<<end<<endl;
            if(pm.find(s[end]) == pm.end()){
                sm.clear();
                end++;
                start = end;
            } else {
                sm[s[end]]++;
                if(sm[s[end]] > pm[s[end]]){
                    while(start < end && s[start] != s[end]){
                        sm[s[start]]--;
                        if(sm[s[start]] == 0) sm.erase(s[start]);
                        start++;
                    }
                    sm[s[start]]--;
                    start++;
                    // cout<<start<<" "<<end<<endl;
                }
                if(end-start+1 == p.length()){
                    ans.push_back(start);
                    sm[s[start]]--;
                    if(sm[s[start]] == 0) sm.erase(s[start]);
                    start++;
                }
                end++;
            }
        }
        return ans;
    }
};