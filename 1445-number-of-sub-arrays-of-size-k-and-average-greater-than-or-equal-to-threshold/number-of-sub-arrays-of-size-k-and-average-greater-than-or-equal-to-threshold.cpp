class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int n = arr.size();
        int total = threshold * k;
        int sum = 0;
        int ans = 0;
        for(int i=0; i<n; i++){
            sum += arr[i];
            if(i >= k-1){
                cout<<sum<<endl;
                if(sum >= total) ans++;
                sum -= arr[i-k+1];
            }
        }
        return ans;
    }
};