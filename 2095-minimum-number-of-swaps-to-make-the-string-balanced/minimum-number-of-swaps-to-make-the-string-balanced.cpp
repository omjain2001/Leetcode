class Solution {
public:
    int minSwaps(string s) {
        stack<char> st;
        int mismatch = 0;
        for(int i=0; i<s.length(); i++){
            if(s[i] == '[') st.push(s[i]);
            else {
                if(!st.empty()) st.pop();
                else mismatch++;
            }
        }

        return (mismatch + 1) / 2;
    }
};