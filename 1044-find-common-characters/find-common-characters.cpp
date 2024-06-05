class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<map<char,int>> v;
        for(auto word: words){
            map<char,int> m;
            for(auto ele: word) m[ele]++;
            v.push_back(m);
        }
        vector<string> ans;
        for(auto ele: v[0]){
            int mini = ele.second;
            for(int i=1; i<v.size(); i++){
                if(v[i].find(ele.first) == v[i].end()){
                    mini = INT_MAX;
                    break;
                }
                mini = min(mini, v[i][ele.first]);
            }
            if(mini != INT_MAX){
                while(mini){
                    ans.push_back(string(1,ele.first));
                    mini--;
                }
            }
        }

        return ans;
    }
};