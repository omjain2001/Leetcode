class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        int i = 0;
        int n = s.length();
        for (auto i: s){
            if(i == '(' || i == '{' || i == '[') st.push(i);
            else if(st.empty()) return false;
            else{
                char ch = st.top();
                st.pop();
                if((i == ')' && ch != '(') || (i == '}' && ch != '{') || (i == ']' && ch != '[')) return false;
            }
        }

        if(!st.empty()) return false;

        return true;
    }
};