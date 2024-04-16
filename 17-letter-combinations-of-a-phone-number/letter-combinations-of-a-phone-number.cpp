class Solution {
public:
    void recur(vector<string> &arr, vector<string> &ans, string temp, int i){
        if(i == arr.size()){
            if(temp != "") ans.push_back(temp);
            return;
        }
        for(int j=0; j<arr[i].length(); j++){
            recur(arr,ans,temp+arr[i][j],i+1);
        }
    }
    vector<string> letterCombinations(string digits) {
        map<int,string> m;
        m[2] = "abc";
        m[3] = "def";
        m[4] = "ghi";
        m[5] = "jkl";
        m[6] = "mno";
        m[7] = "pqrs";
        m[8] = "tuv";
        m[9] = "wxyz";

        vector<string> ans;
        vector<string> temp;
        for(int i=0; i<digits.size(); i++){
            string s = "";
            s += digits[i];
            int num = stoi(s);
            temp.push_back(m[num]);
        }
        recur(temp,ans,"",0);
        return ans;
    }
};