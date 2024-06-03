class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());
        int n = meetings.size();
        int end = INT_MIN;
        int ans = (meetings[0][0] - 1);
        for(int i=0; i<meetings.size()-1; i++){
            end = max(end, meetings[i][1]);
            if(meetings[i+1][0] > end){
                ans += (meetings[i+1][0] - end - 1);
                end = meetings[i+1][1];
            }
        }
        ans += days - max(end, meetings[n-1][1]);
        return ans;
    }
};