class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string,string> m;
        for(int i=0; i<paths.size(); i++){
            m[paths[i][0]] = paths[i][1];
        }
        string dest = "";
        for(auto ele: m){
            if(m.find(ele.second) == m.end()){
                dest = ele.second;
                break;
            }
        }
        return dest;
    }
};