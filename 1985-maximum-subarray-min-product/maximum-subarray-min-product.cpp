class Solution {
public:
    vector<int> smallestLeftElement(vector<int> nums){
        vector<int> res(nums.size());
        stack<int> s;
        for(int i=0; i<nums.size(); i++){
            while(!s.empty() && nums[s.top()] >= nums[i]) s.pop();
            if(s.empty()) res[i] = -1;
            else res[i] = s.top();
            s.push(i);
        }
        return res;
    }
    vector<int> smallestRightElement(vector<int> nums){
        vector<int> res(nums.size());
        stack<int> s;
        for(int i=nums.size()-1; i>=0; i--){
            while(!s.empty() && nums[s.top()] >= nums[i]) s.pop();
            if(s.empty()) res[i] = nums.size();
            else res[i] = s.top();
            s.push(i);
        }
        return res;
    }
    int maxSumMinProduct(vector<int>& nums) {
        vector<long long> prefix(nums.size()+1, 0);
        for(int i=0; i<nums.size(); i++){
            prefix[i+1] = prefix[i] + nums[i];
        }
        vector<int> smallestLeft = smallestLeftElement(nums);
        vector<int> smallestRight = smallestRightElement(nums);

        long long maxi = INT_MIN;
        for(int i=0; i<nums.size(); i++){
            long long total = prefix[smallestRight[i]] - prefix[smallestLeft[i] + 1];
            maxi = max(maxi, total * nums[i]);
        }
        long long mod = 1e9 + 7;
        return (int)(maxi % mod);
    }
};