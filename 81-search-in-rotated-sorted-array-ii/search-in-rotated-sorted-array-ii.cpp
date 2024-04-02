class Solution {
public:
    int find_pivot(vector<int>&nums, int s, int e){
        while(e > s && nums[e] == nums[e-1]) e--;
        while(s < e && nums[s] == nums[s+1]) s++;
        if(s > e) return nums.size()-1;
        else if(s == e) return s;
        else if(s+1 == e) return nums[e] >= nums[s] ? e : s;
        int mid = (s+e)/2;
        if(nums[mid] < nums[mid-1]) return mid-1;
        else if(nums[mid] > nums[mid+1]) return mid;
        else if(nums[mid] > nums[s]) return find_pivot(nums,mid+1,e);
        else return find_pivot(nums,s,mid-1);
    }
    bool bin_search(vector<int> &nums, int s, int e, int target){
        if(s > e) return false;
        int mid = (s+e)/2;
        if(nums[mid] == target) return true;
        else if(target > nums[mid]) return bin_search(nums,mid+1,e,target);
        else return bin_search(nums,s,mid-1,target);
    }
    bool search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size()-1;
        int mid = find_pivot(nums, start, end);
        if(target >= nums[start] && target <= nums[mid]) return bin_search(nums, start, mid, target);
        else return bin_search(nums, mid+1, end, target);
    }
};