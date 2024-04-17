class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        int mod = 1e9 + 7;
        long count = 0;
        map<int,long> m;
        // for(int i=0; i<nums.size(); i++){
        //     for(int j=i+1; j<nums.size(); j++){
        //         string num = to_string(nums[i]);
        //         reverse(num.begin(),num.end());
        //         int rev_num = stoi(num);

        //         string num2 = to_string(nums[j]);
        //         reverse(num2.begin(),num2.end());
        //         int rev_num2 = stoi(num2);

        //         if((nums[i] + rev_num2) % mod == (nums[j] + rev_num) % mod) count++;
        //     }
        // }
        for(int i=0; i<nums.size(); i++){
                string num = to_string(nums[i]);
                reverse(num.begin(),num.end());
                int rev_num = stoi(num);   
                m[nums[i] - rev_num]++;
        }
        for(auto ele: m){
            count = (count + (ele.second * (ele.second - 1) / 2)) % mod;
        }
        return count;
    }
};