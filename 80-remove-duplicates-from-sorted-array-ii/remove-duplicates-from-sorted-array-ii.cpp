class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = -1;
        int count = 0;
        int curr = 0;
        for(int i=0; i<nums.size(); i++){
            if(i > 0 && nums[i-1] != nums[i]) count = 0;
            count++;
            if(count < 3){
                nums[++k] = nums[i];
            }
        }
        return k+1;
    }
};