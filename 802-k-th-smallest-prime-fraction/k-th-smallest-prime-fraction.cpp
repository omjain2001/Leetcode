class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        set<pair<double,pair<int,int>>> s;
        for(int i=0; i<arr.size(); i++){
            for(int j=i+1; j<arr.size(); j++){
                s.insert({double(arr[i])/arr[j],{i,j}});
            }
        }
        int i = 0;
        vector<int> ans;
        for(auto ele: s){
            if(i == (k-1)){
                ans.push_back(arr[ele.second.first]);
                ans.push_back(arr[ele.second.second]);
                break;
            }
            i++;
        }
        return ans;   
    }
};