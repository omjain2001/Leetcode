class Solution {
public:
    int recur(vector<int> &days, vector<int> &costs, int i, vector<int> &dp){
        if(i >= days.size()) return 0;
        if(dp[i] != -1) return dp[i];
        int day = costs[0] + recur(days, costs, i+1, dp);
        int j = i;
        while(j < days.size() && days[i] + 7 > days[j]) j++;
        int week = costs[1] + recur(days, costs, j, dp);

        j = i;
        while(j < days.size() && days[i] + 30 > days[j]) j++;
        int month = costs[2] + recur(days, costs, j, dp);

        return dp[i] = min({day, week, month});

    }
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        vector<int> dp(days.size(), -1);
        return recur(days, costs, 0, dp);
    }
};