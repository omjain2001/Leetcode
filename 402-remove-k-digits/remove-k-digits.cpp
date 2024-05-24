class Solution {
public:
    string removeKdigits(string num, int k) {
        if(num.length() == k) return "0";
        stack<char> s;
        for(int i=0; i<num.length(); i++){
            while(!s.empty() && k > 0 && num[i] < s.top()){
                s.pop();
                k--;
            }
            s.push(num[i]);
        }
        while(!s.empty() && k > 0){
            s.pop();
            k--;
        }
        string ans = "";
        while(!s.empty()){
            ans += s.top();
            s.pop();
        }
        reverse(ans.begin(),ans.end());
        int i = 0;
        while(i < ans.length() && ans[i] == '0') i++;
        ans = ans.substr(i, ans.length()-i);
        if(ans.length() == 0) return "0";
        return ans;
    }
};