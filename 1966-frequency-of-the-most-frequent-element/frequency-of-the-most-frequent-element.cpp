class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        long long i=0, j=0, sum=0, ans=1;
        sort(nums.begin(), nums.end());
        while(j < nums.size()){
            sum += nums[j];
            while(i < j && ((j-i+1)*nums[j] - sum) > k) sum -= nums[i++];
            ans = max(ans, (j-i+1));
            j++;
        }
        return ans;
    }
};