class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int> ans;
        int i=0;
        while(i < arr.size() && arr[i] < x) i++;
        int l = i-1, r = i;
        while(ans.size() < k){
            if(l >= 0 && r < arr.size()){
                if(abs(arr[l]-x) > abs(arr[r]-x)){
                    ans.push_back(arr[r]);
                    r++;
                } else {
                    ans.push_back(arr[l]);
                    l--;
                }
            } else if(l >= 0) {
                ans.push_back(arr[l]);
                l--;
            } else {
                ans.push_back(arr[r]);
                r++;
            }
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};