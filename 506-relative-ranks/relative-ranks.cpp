class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<string> ans(score.size());
        set<pair<int,int>> s;
        for(int i=0; i<score.size(); i++){
            s.insert({score[i],i});
        }
        int count = 0;
        for(auto ele = s.rbegin(); ele != s.rend(); ele++){
            if(count < 3){
                if(count == 0) ans[ele->second] = "Gold Medal";
                else if(count == 1) ans[ele->second] = "Silver Medal";
                else ans[ele->second] = "Bronze Medal";
            } else ans[ele->second] = to_string(count+1);

            count++;
        }
        return ans;
    }
};