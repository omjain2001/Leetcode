class Solution {
public:
    int recur(vector<int> &nums, int index, int k, unordered_map<int,int> &m){
        // if(index >= nums.size()){
        //     return 0;
        //     bool found = false;
        //     for(auto x: m){
        //         if(x.second > 0){
        //             found = true;
        //             break;
        //         }
        //     }
        //     if(found) return 1;
        //     return 0;
        // }

        if(index >= nums.size()) return 0;

        int include = 0;
        if(!m[nums[index]-k]){
            m[nums[index]]++;
            include = 1 + recur(nums,index+1,k,m);
            m[nums[index]]--;
        }

        return include + recur(nums,index+1,k,m);
    }
    int beautifulSubsets(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        unordered_map<int,int> m;
        return recur(nums,0,k,m);
    }
};