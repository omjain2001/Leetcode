class Solution {
public:
    bool isPalindrome(string s) {
        string alpha = "";
        for (auto ele: s){
            if(isalnum(ele)){
                alpha += tolower(ele);
            }
        }
        cout<<alpha<<endl;
        string rev = alpha;
        reverse(rev.begin(), rev.end());
        if(alpha == rev) return true;
        return false;
    }
};