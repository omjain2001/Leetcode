class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> s;
        int n = pushed.size();
        int i=0, j=0;
        for(int i=0; i<n; i++){
            s.push(pushed[i]);
            while(!s.empty() && s.top() == popped[j]){
                s.pop();
                j++;
            }
        }
        if(j < n) return false;
        return true;
    }
};