class Solution {
public:
    bool isValid(vector<int> &nums, int p, int mid){
        int count = 0;
        for(int i=0; i<nums.size()-1; i++){
            if(abs(nums[i]-nums[i+1]) <= mid){
                count += 1;
                i++;
            }
            if(count == p) return true;
        }
        return false;
    }
    int minimizeMax(vector<int>& nums, int p) {
        if (p == 0) return 0;
        int l = 0, r = 1e9;
        sort(nums.begin(), nums.end());
        while(l <= r){
            int mid = (l+r)/2;
            if(isValid(nums, p, mid)){
                r = mid-1;
            } else l = mid+1;
        }
        return l;
    }
};