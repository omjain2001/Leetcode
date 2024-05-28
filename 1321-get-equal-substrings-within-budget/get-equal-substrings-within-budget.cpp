class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {

        // Brute force
        // int n = s.length();
        // vector<int> cum(n+1,0);
        // for(int i=1; i<n+1; i++){
        //     cum[i] = cum[i-1] + (abs((int)s[i-1] - (int)t[i-1]));
        // }
        // for(int i=n; i>0; i--){
        //     int right = n;
        //     int left = right - i;
        //     bool isValid = false;
        //     while(left >= 0){
        //         if(cum[right] - cum[left] <= maxCost){
        //             isValid = true;
        //             break;
        //         }
        //         right--;
        //         left = right - i;
        //     }
        //     if(isValid) return i;
        // }
        // return 0;

        // Sliding window
        int n = s.length();
        vector<int> diff(n);
        for(int i=0; i<n; i++){
            diff[i] = abs((int)s[i] - (int)t[i]);
        }
        int maxi = INT_MIN;
        int sum = 0;
        int right = 0, left = 0;
        while(right < n){
            sum = sum + diff[right];
            if(sum <= maxCost){
                maxi = max(maxi, right-left+1);
            } else {
                while(left <= right && sum > maxCost){
                    sum -= diff[left];
                    left++;
                }
            }
            right++;
        }

        return max(maxi,0);
    }
};