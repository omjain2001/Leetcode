class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        int j = -1;
        int i = 0;
        while(i < nums.size()){
            if(nums[i] != val){
                int temp = nums[++j];
                nums[j] = nums[i];
                nums[i] = temp;
                count++;
            }
            i++;
        }
        return count;
        
    }
};