class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        vector<pair<int,int>> prof;
        for(int i=0; i<profit.size(); i++){
            prof.push_back({profit[i],i});
        }
        sort(prof.begin(),prof.end());
        sort(worker.begin(), worker.end());

        int i=prof.size()-1;
        int j=worker.size()-1;
        int ans = 0;
        while(i >= 0 && j >= 0){
            if(worker[j] >= difficulty[prof[i].second]){
                ans += prof[i].first;
                j--;
            } else i--;
        }

        return ans;
    }
};