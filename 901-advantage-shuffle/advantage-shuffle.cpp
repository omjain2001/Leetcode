class Solution {
public:
    vector<int> advantageCount(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        vector<pair<int,int>> temp;
        for(int i=0; i<nums2.size(); i++){
            temp.push_back({nums2[i],i});
        }
        sort(temp.begin(), temp.end());
        int front = 0, last = nums1.size()-1;
        vector<int> ans(nums1.size());
        for(auto ele: nums1){
            if(temp[front].first < ele){
                ans[temp[front++].second] = ele;
            } else {
                ans[temp[last--].second] = ele;
            }
        }

        return ans;
    }
};