class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char,char> m;
        m[')'] = '(';
        m[']'] = '[';
        m['}'] = '{';
        for(auto ele: s){
            if(ele == '(' || ele == '{' || ele == '[') st.push(ele);
            else {
                if(st.empty() || m[ele] != st.top()) return false;
                st.pop();
            }
        }
        if(!st.empty()) return false;
        return true;
    }
};