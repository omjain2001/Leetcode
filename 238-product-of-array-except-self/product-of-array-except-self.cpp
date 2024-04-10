class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        vector<int> pre(n);
        vector<int> suf(n);
        int pro = 1;
        pre[0] = 1;
        suf[n-1] = 1;
        pro = nums[0];
        for(int i=1; i<n; i++){
            pre[i] = pro;
            pro *= nums[i];
        }
        pro = nums[n-1];
        for(int i=n-2; i>=0; i--){
            suf[i] = pro;
            pro *= nums[i];
        }

        for(int i=0; i<n; i++){
            ans[i] = pre[i] * suf[i];
        }
        return ans;
    }
};