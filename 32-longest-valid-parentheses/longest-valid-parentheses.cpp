class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
        st.push(-1);
        int maxL = INT_MIN;
        for(int i=0; i<s.length(); i++){
            if(s[i] == '(') st.push(i);
            else {
                st.pop();
                if(st.empty()) st.push(i);
                else maxL = max(maxL, i-st.top());
            }
        }
        if(maxL == INT_MIN) return 0;
        return maxL;
    }
};