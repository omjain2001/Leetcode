class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        vector<vector<int>> ans;
        sort(people.begin(), people.end(), [](vector<int> &a, vector<int> &b) -> bool {
            if(a[0] != b[0]){
                return a[0] > b[0];
            } else {
                return a[1] < b[1];
            }
        });

        for(int i=0; i<people.size(); i++){
            ans.insert(ans.begin() + people[i][1], people[i]);
        }
        return ans;
    }
};