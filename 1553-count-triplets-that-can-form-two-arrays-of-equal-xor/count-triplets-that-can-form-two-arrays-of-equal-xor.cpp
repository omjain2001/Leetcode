class Solution {
public:
    int countTriplets(vector<int>& arr) {
        int ans = 0;
        for(int i=0; i<arr.size(); i++){
            int temp = arr[i];
            for(int k=i+1; k<arr.size(); k++){
                temp ^= arr[k];
                if(temp == 0){
                    ans += (k-i);
                }
            }
        }
        return ans;
    }
};