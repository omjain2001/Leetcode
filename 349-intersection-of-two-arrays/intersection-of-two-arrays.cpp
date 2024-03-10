class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> m1,m2;
        for(int i=0; i<nums1.size(); i++){
            m1[nums1[i]]++;
        }
        
        for(int j=0; j<nums2.size(); j++){
            m2[nums2[j]]++;
        }
        
        vector<int> ans;
        for(auto itr = m1.begin(); itr != m1.end(); itr++){
            if(m2.find(itr->first) != m2.end()){
                ans.push_back(itr->first);
            }
        }
        return ans;
    }
};