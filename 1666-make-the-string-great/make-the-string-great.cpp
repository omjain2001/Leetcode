class Solution {
public:
    string makeGood(string s) {
        stack<char> st;
        for(auto ele: s){
            if(!st.empty() && abs((int)ele - (int)st.top()) == 32) st.pop();
            else st.push(ele);
        }
        string ans = "";
        while(!st.empty()){
            ans = st.top() + ans;
            st.pop();
        }
        return ans;
    }
};