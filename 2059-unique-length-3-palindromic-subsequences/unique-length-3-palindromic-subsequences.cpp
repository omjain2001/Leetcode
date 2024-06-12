class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_set<char> left;
        unordered_map<char,int> right;
        for(int i=1; i<s.length(); i++) right[s[i]]++;
        left.insert(s[0]);
        int count = 0;
        unordered_set<string> ans;
        for(int i=1; i<s.length()-1; i++){
            right[s[i]]--;
            if(right[s[i]] == 0){
                right.erase(s[i]);
            }
            for(int j=0; j<26; j++){
                char c = 'a' + j;
                if(left.find(c) != left.end() && right.find(c) != right.end()){
                    string temp = "";
                    temp += c;
                    temp += s[i];
                    temp += c;
                    ans.insert(temp);
                }
            }
            left.insert(s[i]);
        }

        return ans.size();
    }
};