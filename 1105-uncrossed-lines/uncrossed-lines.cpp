class Solution {
public:
    int recur(vector<int> &nums1, vector<int> &nums2, int i, int j){
        if(i >= nums1.size() || j >= nums2.size()) return 0;
        if(nums1[i] == nums2[j]) return 1 + recur(nums1, nums2, i+1, j+1);
        else return max(recur(nums1, nums2, i+1, j), recur(nums1, nums2, i, j+1));
    }
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        // return recur(nums1, nums2, 0, 0);

        vector<vector<int>> dp(nums1.size()+1, vector<int>(nums2.size()+1, 0));
        for(int i=1; i<=nums1.size(); i++){
            for(int j=1; j<=nums2.size(); j++){
                if(nums1[i-1] == nums2[j-1]){
                    dp[i][j] = 1 + dp[i-1][j-1];
                } else {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }

        return dp[nums1.size()][nums2.size()];
    }
};