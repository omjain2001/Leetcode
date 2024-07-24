class Solution {
public:
    int minChanges(vector<int>& nums, int k) {
        unordered_map<int,int> zero_ops;
        int n = nums.size();
        for(int i=0; i<n/2; i++){
            zero_ops[abs(nums[i]-nums[n-i-1])]++;
        }

        vector<int> one_ops(k+1, 0);
        for(int i=0; i<n/2; i++){
            int max_diff = max(max(nums[i], nums[n-i-1]), k-min(nums[i], nums[n-i-1]));
            one_ops[max_diff]++;
        }

        for(int i=k-1; i>=0; i--){
            one_ops[i] += one_ops[i+1];
        }
        int mini = INT_MAX;
        for(int i=0; i<=k; i++){
            int actual_one = one_ops[i] - zero_ops[i];
            mini = min(mini, actual_one + 2 * (n/2-one_ops[i]));
        }
        return mini;
    }
};