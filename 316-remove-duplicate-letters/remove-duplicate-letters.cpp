class Solution {
public:
    string removeDuplicateLetters(string s) {
        stack<char> st;
        vector<bool> included(26,false);
        vector<int> index(26,-1);
        for(int i=0; i<s.length(); i++){
            index[s[i]-'a'] = i;
        }
        for(int i=0; i<s.length(); i++){
            if(!included[s[i]-'a']){
                while(!st.empty() && st.top() > s[i] && index[st.top()-'a'] > i){
                    included[st.top()-'a'] = false;
                    st.pop();
                }
                st.push(s[i]);
                included[s[i]-'a'] = true;
            }
        }

        string ans = "";
        while(!st.empty()){
            ans += st.top();
            st.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};