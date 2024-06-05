class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<pair<int,int>> v(26, {INT_MAX,INT_MAX});
        for(int i=0; i<s.length(); i++){
            if(v[s[i]-'a'].first == INT_MAX){
                v[s[i]-'a'].first = i;
            }
            v[s[i]-'a'].second = i;
        }

        // sort(v.begin(), v.end());
        // for(int i=0; i<v.size(); i++) cout<<v[i].first<<" "<<v[i].second<<endl;
        vector<int> ans;
        int start = v[s[0]-'a'].first;
        int end = v[s[0]-'a'].second;

        for(int i=0; i<s.length(); i++){
            if(v[s[i]-'a'].first > end){
                ans.push_back(end-start+1);
                start = v[s[i]-'a'].first;
                end = v[s[i]-'a'].second;
            } else {
                end = max(v[s[i]-'a'].second, end);
            }
        }
        ans.push_back(end-start+1);
        return ans;
    }
};