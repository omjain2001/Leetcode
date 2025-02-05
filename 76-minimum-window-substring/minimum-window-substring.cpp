class Solution {
public:
    bool checkEqual(int sc[123], int tc[123]){
        for(int i=0; i<123; i++){
            if(sc[i] < tc[i]) return false;
        }
        return true;
    }
    string minWindow(string s, string t) {
        int sc[123] = {0}, tc[123] = {0};
        for(auto i: t) {
            if(isupper(i)) tc[i]++;
            else tc[i]++;
        }
        int i=0;
        while(i < s.length() && i < t.length()){
            if(isupper(s[i])) sc[s[i]]++;
            else sc[s[i]]++;
            i++;
        }
        if(checkEqual(sc,tc)) return s.substr(0, t.length());

        int f = 0;
        int mini = INT_MAX;
        int start = -1, end = -1;
        while(i < s.length()){
            if(isupper(s[i])) sc[s[i]]++;
            else sc[s[i]]++;
            
            while(checkEqual(sc,tc)){
                if((i-f+1) < mini){
                    mini = i-f+1;
                    start = f;
                    end = i;
                }
                if(isupper(s[f])) sc[s[f]]--;
                else sc[s[f]]--;
                f++;
            }
            i++;
        }
        if(start == -1) return "";
        return s.substr(start, end-start+1);
    }
};