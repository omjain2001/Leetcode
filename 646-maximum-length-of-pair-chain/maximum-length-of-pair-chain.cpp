class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(), pairs.end(), [](vector<int> &a, vector<int> &b) -> bool {
            if(a[1] == b[1]) return a[0] > b[0];
            else return a[1] < b[1];
        });
        vector<int> temp(pairs.size(), 1);
        for(int i=1; i<pairs.size(); i++){
            int maxi = 0;
            for(int j=i-1; j>=0; j--){
                if(pairs[i][0] > pairs[j][1]){
                    maxi = max(maxi, temp[j]);
                }
            }
            temp[i] = 1 + maxi;
        }

        int maxi = INT_MIN;
        for(int i=0; i<temp.size(); i++){
            maxi = max(maxi, temp[i]);
        }

        return maxi;
    }
};