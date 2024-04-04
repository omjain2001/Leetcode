class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int mini = INT_MAX;
        int i = 0;
        int n = nums.size();
        int sum = 0;
        int start = 0;
        while(i < n){
            sum += nums[i];
            if(sum >= target){
                mini = min(mini, i-start+1);
                while(start <= i && sum >= target){
                    mini = min(mini, i-start+1);
                    sum -= nums[start];
                    start++;
                }
            }
            i++;
        }
        if(mini == INT_MAX) return 0; 
        return mini;
    }
};