class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<int> dp(n, 1);
        vector<int> idx(n, -1);
        for(int i=0; i<n; i++){
            for(int j=0; j<i; j++){
                if(nums[j] % nums[i] == 0 || nums[i] % nums[j] == 0){
                    if(dp[i] < dp[j] + 1){
                        dp[i] = dp[j] + 1;
                        idx[i] = j;
                    }
                }
            }
        }
        int max_idx = -1;
        int maxi = INT_MIN;
        for(int i=0; i<n; i++){
            if(maxi < dp[i]){
                maxi = dp[i];
                max_idx = i;
            }
        }
        // for(auto ele: idx) cout<<ele<<" ";
        // cout<<endl;
        vector<int> ans;
        while(max_idx != -1){
            ans.insert(ans.begin(), nums[max_idx]);
            max_idx = idx[max_idx];
        }
        return ans;
    }
};