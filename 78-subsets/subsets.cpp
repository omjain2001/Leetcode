class Solution {
public:
    void recur(vector<int>& nums, vector<vector<int>> &ans, vector<int> &temp, int i){
        int n = nums.size();
        if(i >= n){
            ans.push_back(temp);
            return;
        } else {
            temp.push_back(nums[i]);
            recur(nums, ans, temp, i+1);
            temp.pop_back();
            recur(nums, ans, temp, i+1);
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> temp;
        recur(nums, ans, temp, 0);
        return ans;
    }
};