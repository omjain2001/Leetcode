class Solution {
public:
    long long recur(vector<int> &power, map<int,int> &freq, vector<long long> &dp, int i){
        if(i >= power.size()) return 0;
        if(dp[i] != -1) return dp[i];
        long long take = 0;
        int nextIndex = i+1;
        while(nextIndex < power.size() && power[nextIndex] - power[i] <= 2) nextIndex++;
        take = (long long) power[i] * freq[power[i]] + recur(power, freq, dp, nextIndex);
        long long notTake = recur(power, freq, dp, i+1);
        return dp[i] = max(take, notTake);
    }
    long long maximumTotalDamage(vector<int>& power) {
        map<int,int> m;
        vector<int> unique;
        for(auto ele: power) m[ele]++;
        for(auto ele: m) unique.push_back(ele.first);
        vector<long long> dp(power.size(), -1);
        return recur(unique, m, dp, 0);
    }
};