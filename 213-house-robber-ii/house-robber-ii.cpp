class Solution {
public:
    int recur(vector<int> &nums, int index, vector<int> &dp){
        int n = nums.size() - 1;

        if (index == n)
            return nums[n];
        if (index > n)
            return 0;
        if (dp[index] != -1)
            return dp[index];

        int incl = nums[index] + recur(nums, index + 2, dp);
        int excl = 0 + recur(nums, index + 1, dp);
        dp[index] = max(incl, excl);
        return dp[index];
    }
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        int ans;
        vector<int> dp1(n, -1);
        vector<int> dp2(n, -1);
        vector<int> first, second;

        for (int i = 0; i < n; i++) {
            if (i != n - 1)
                first.push_back(nums[i]);
            if (i != 0)
                second.push_back(nums[i]);
        }

        ans = max(recur(first, 0, dp1), recur(second, 0, dp2));
        return ans;
    }
};