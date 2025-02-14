class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> s;
        vector<int> v(temperatures.size());
        int n = temperatures.size();
        for(int i=0; i<n; i++){
            while(!s.empty() && temperatures[s.top()] < temperatures[i]){
                v[s.top()] = i-s.top();
                s.pop();
            }
            s.push(i);
        }
        return v;
    }
};